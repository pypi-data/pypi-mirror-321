import contextlib
import os
import pathlib
import pickle
import re
import textwrap
from collections.abc import AsyncIterable, Sequence
from copy import deepcopy
from datetime import datetime, timedelta
from io import BytesIO
from pathlib import Path
from typing import cast

import httpx
import numpy as np
import pytest
from llmclient import (
    CommonLLMNames,
    Embeddable,
    EmbeddingModel,
    HybridEmbeddingModel,
    LiteLLMEmbeddingModel,
    LLMModel,
    LLMResult,
    SparseEmbeddingModel,
)
from pytest_subtests import SubTests

from paperqa import (
    Answer,
    Doc,
    DocDetails,
    Docs,
    NumpyVectorStore,
    PQASession,
    QdrantVectorStore,
    Settings,
    Text,
    VectorStore,
    print_callback,
)
from paperqa.clients import CrossrefProvider
from paperqa.clients.journal_quality import JournalQualityPostProcessor
from paperqa.core import llm_parse_json
from paperqa.prompts import CANNOT_ANSWER_PHRASE
from paperqa.prompts import qa_prompt as default_qa_prompt
from paperqa.readers import read_doc
from paperqa.utils import (
    extract_score,
    get_citenames,
    maybe_is_html,
    maybe_is_text,
    name_in_text,
    strings_similarity,
    strip_citations,
)
from tests.conftest import VCR_DEFAULT_MATCH_ON

THIS_MODULE = pathlib.Path(__file__)


@pytest.fixture
def docs_fixture(stub_data_dir: Path) -> Docs:
    docs = Docs()
    with (stub_data_dir / "paper.pdf").open("rb") as f:
        docs.add_file(f, "Wellawatte et al, XAI Review, 2023")
    return docs


def test_get_citations() -> None:
    text = (
        "Yes, COVID-19 vaccines are effective. Various studies have documented the"
        " effectiveness of COVID-19 vaccines in preventing severe disease,"
        " hospitalization, and death. The BNT162b2 vaccine has shown effectiveness"
        " ranging from 65% to -41% for the 5-11 years age group and 76% to 46% for the"
        " 12-17 years age group, after the emergence of the Omicron variant in New York"
        " (Dorabawila2022EffectivenessOT). Against the Delta variant, the effectiveness"
        " of the BNT162b2 vaccine was approximately 88% after two doses"
        " (Bernal2021EffectivenessOC pg. 1-3).\n\nVaccine effectiveness was also found"
        " to be 89% against hospitalization and 91% against emergency department or"
        " urgent care clinic visits (Thompson2021EffectivenessOC pg. 3-5, Goo2031Foo"
        " pg. 3-4). In the UK vaccination program, vaccine effectiveness was"
        " approximately 56% in individuals aged ≥70 years between 28-34 days"
        " post-vaccination, increasing to approximately 58% from day 35 onwards"
        " (Marfé2021EffectivenessOC).\n\nHowever, it is important to note that vaccine"
        " effectiveness can decrease over time. For instance, the effectiveness of"
        " COVID-19 vaccines against severe COVID-19 declined to 64% after 121 days,"
        " compared to around 90% initially (Chemaitelly2022WaningEO, Foo2019Bar)."
        " Despite this, vaccines still provide significant protection against severe"
        " outcomes (Bar2000Foo pg 1-3; Far2000 pg 2-5)."
    )
    ref = {
        "Dorabawila2022EffectivenessOT",
        "Bernal2021EffectivenessOC pg. 1-3",
        "Thompson2021EffectivenessOC pg. 3-5",
        "Goo2031Foo pg. 3-4",
        "Marfé2021EffectivenessOC",
        "Chemaitelly2022WaningEO",
        "Foo2019Bar",
        "Bar2000Foo pg 1-3",
        "Far2000 pg 2-5",
    }
    assert get_citenames(text) == ref


def test_single_author() -> None:
    text = "This was first proposed by (Smith 1999)."
    assert strip_citations(text) == "This was first proposed by ."


def test_multiple_authors() -> None:
    text = "Recent studies (Smith et al. 1999) show that this is true."
    assert strip_citations(text) == "Recent studies  show that this is true."


def test_multiple_citations() -> None:
    text = (
        "As discussed by several authors (Smith et al. 1999; Johnson 2001; Lee et al."
        " 2003)."
    )
    assert strip_citations(text) == "As discussed by several authors ."


def test_citations_with_pages() -> None:
    text = "This is shown in (Smith et al. 1999, p. 150)."
    assert strip_citations(text) == "This is shown in ."


def test_citations_without_space() -> None:
    text = "Findings by(Smith et al. 1999)were significant."
    assert strip_citations(text) == "Findings bywere significant."


def test_citations_with_commas() -> None:
    text = "The method was adopted by (Smith, 1999, 2001; Johnson, 2002)."
    assert strip_citations(text) == "The method was adopted by ."


def test_citations_with_text() -> None:
    text = "This was noted (see Smith, 1999, for a review)."
    assert strip_citations(text) == "This was noted ."


def test_no_citations() -> None:
    text = "There are no references in this text."
    assert strip_citations(text) == "There are no references in this text."


def test_malformed_citations() -> None:
    text = "This is a malformed citation (Smith 199)."
    assert strip_citations(text) == "This is a malformed citation (Smith 199)."


def test_edge_case_citations() -> None:
    text = "Edge cases like (Smith et al.1999) should be handled."
    assert strip_citations(text) == "Edge cases like  should be handled."


def test_citations_with_special_characters() -> None:
    text = "Some names have dashes (O'Neil et al. 2000; Smith-Jones 1998)."
    assert strip_citations(text) == "Some names have dashes ."


def test_citations_with_nonstandard_chars() -> None:
    text = (
        "In non-English languages, citations might look different (Müller et al. 1999)."
    )
    assert (
        strip_citations(text)
        == "In non-English languages, citations might look different ."
    )


def test_maybe_is_text() -> None:
    assert maybe_is_text("This is a test. The sample conc. was 1.0 mM (at 245 ^F)")
    assert not maybe_is_text("\\C0\\C0\\B1\x00")
    # get front page of wikipedia
    r = httpx.get("https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day")
    assert maybe_is_text(r.text)

    assert maybe_is_html(BytesIO(r.text.encode()))

    # now force it to contain lots of weird encoding
    bad_text = r.text.encode("latin1", "ignore").decode("utf-16", "ignore")
    assert not maybe_is_text(bad_text)

    # account for possible spaces in the text due to tables or title pages
    assert maybe_is_text("entry1                    entry2                    entry3")


def test_name_in_text() -> None:
    name1 = "FooBar2022"
    name2 = "FooBar2022a"
    name3 = "FooBar20"

    text1 = "As mentioned by FooBar2022, this is a great paper"
    assert name_in_text(name1, text1)
    assert not name_in_text(name2, text1)
    assert not name_in_text(name3, text1)

    text2 = "This is great, as found by FooBar20"
    assert name_in_text(name3, text2)
    assert not name_in_text(name1, text2)
    assert not name_in_text(name2, text2)

    text3 = "Per previous work (FooBar2022, FooBar2022a), this is great"
    assert name_in_text(name1, text3)
    assert name_in_text(name2, text3)
    assert not name_in_text(name3, text3)

    text4 = "Per previous work (Foo2022, Bar2023), this is great"
    assert not name_in_text(name1, text4)
    assert not name_in_text(name2, text4)
    assert not name_in_text(name3, text4)

    text5 = "Per previous work (FooBar2022; FooBar2022a), this is great"
    assert name_in_text(name1, text5)
    assert name_in_text(name2, text5)
    assert not name_in_text(name3, text5)

    text6 = "According to FooBar2022 and Foobars, this is great"
    assert name_in_text(name1, text6)
    assert not name_in_text(name2, text6)
    assert not name_in_text(name3, text6)

    text7 = "As stated by FooBar2022.\n\nThis is great"
    assert name_in_text(name1, text7)
    assert not name_in_text(name2, text7)
    assert not name_in_text(name3, text7)


def test_extract_score() -> None:
    sample = """
    The text describes an experiment where different cell subtypes,
    including colorectal cancer-associated fibroblasts, were treated with
    oxaliplatin for 12 days. The concentration of oxaliplatin used was the
    EC50 for each cell subtype, which was determined individually.
    The media were changed every 3 days to avoid complete cell death.
    The text does not provide information about the percentage of colorectal
    cancer-associated fibroblasts that typically survive at 2 weeks when cultured
    with oxaliplatin. (0/10)
    """
    assert extract_score(sample) == 0

    sample = """
    COVID-19 vaccinations have been shown to be effective against hospitalization
    from the Omicron and Delta variants, though effectiveness may decrease over
    time. A study found that vaccine effectiveness against hospitalization peaked
    around 82-92% after a third dose but declined to 53-77% 15+ weeks after the third
    dose, depending on age group and hospitalization definition. Stricter
    definitions of hospitalization, like requiring oxygen use or ICU admission,
    showed higher and more sustained vaccine effectiveness. 8
    """

    assert extract_score(sample) == 8

    sample = """
    Here is a 100-word summary of the text:
    The text discusses a phase 3 trial of a combined
    vector vaccine based on rAd26 and rAd5 vectors carrying the
    SARS-CoV-2 spike protein gene. The trial aimed to assess the efficacy,
    immunogenicity and safety of the vaccine against COVID-19 in adults.
    The study design was a randomized, double-blind, placebo-controlled trial
    done at 25 hospitals in Moscow, Russia. Eligible participants were 18 years
    or older with no history of COVID-19. The exclusion criteria ensured
    participants were healthy and had no contraindications for vaccination.
    The trial aimed to determine if the vaccine could safely and effectively
    provide protection against COVID-19. Relevance score: 8
    """

    assert extract_score(sample) == 8

    sample = """
    Here is a 100-word summary of the provided text: The text details
    trial procedures for a COVID-19 vaccine, including screening
    visits, observation visits to assess vital signs, PCR testing, and
    telemedicine consultations. Participants who tested positive for
    COVID-19 during screening were excluded from the trial. During the trial
    , additional PCR tests were only done when COVID-19 symptoms were reported
    . An electronic health record platform was in place to record data from
    telemedicine consultations. The text details the screening and trial
    procedures but does not provide direct evidence regarding the
    effectiveness of COVID-19 vaccinations. Score: 3/10
    """

    assert extract_score(sample) == 3

    sample = """
    Here is a 100-word summary of the text: The text discusses a
    phase 3 trial of a COVID-19 vaccine in Russia. The vaccine
    uses a heterologous prime-boost regimen, providing robust
    immune responses. The vaccine can be stored at -18°C and
    2-8°C. The study reports 91.6% efficacy against COVID-19 based on
    interim analysis of over 21,000 participants. The authors
    compare their results to other published COVID-19 vaccine
    efficacy data. They previously published safety and immunogenicity
    results from phase 1/2 trials of the same vaccine. Relevance score:
    8/10. The text provides details on the efficacy and immune response
    generated by one COVID-19 vaccine in a large phase 3 trial, which is
    relevant evidence to help answer the question regarding effectiveness
    of COVID-19 vaccinations.
    """

    assert extract_score(sample) == 8

    sample = """
    Here is a 100-word summary of the text: The text discusses the safety and
    efficacy of the BNT162b2 mRNA Covid-19 vaccine. The study found that
    the vaccine was well tolerated with mostly mild to moderate side
    effects. The vaccine was found to be highly effective against Covid-19,
    with an observed vaccine efficacy of 90.5% after the second dose.
    Severe Covid-19 cases were also reduced among vaccine recipients.
    The vaccine showed an early protective effect after the first dose
    and reached full efficacy 7 days after the second dose. The favorable
    safety and efficacy results provide evidence that the BNT162b2 vaccine
    is effective against Covid-19. The text provides data on the efficacy
    and safety results from a clinical trial of the BNT162b2 Covid-19 vaccine,
    which is highly relevant to answering the question about the effectiveness
    of Covid-19 vaccinations.
    """

    assert extract_score(sample) == 5

    sample = """
    Introduce dynamic elements such as moving nodes or edges to create a sense of activity within
    the network. 2. Add more nodes and connections to make the network
    appear more complex and interconnected. 3. Incorporate both red and
    green colors into the network, as the current screenshot only shows
    green lines. 4. Vary the thickness of the lines to add depth and
    visual interest. 5. Implement different shades of red and green to
    create a gradient effect for a more visually appealing experience.
    6. Consider adding a background color or pattern to enhance the
    contrast and make the network stand out. 7. Introduce interactive
    elements that allow users to manipulate the network, such as
    dragging nodes or zooming in/out. 8. Use animation effects like
    pulsing or changing colors to highlight certain parts of the network
    or to show activity. 9. Add labels or markers to provide information
      about the nodes or connections, if relevant to the purpose of the
        network visualization. 10. Consider the use of algorithms that
        organize the network in a visually appealing manner, such as
        force-directed placement or hierarchical layouts. 3/10 """

    assert extract_score(sample) == 3

    sample = (
        "The text mentions a work by Shozo Yokoyama titled "
        '"Evolution of Dim-Light and Color Vision Pigments". '
        "This work, published in the Annual Review of Genomics and "
        "Human Genetics, discusses the evolution of human color vision. "
        "However, the text does not provide specific details or findings "
        "from Yokoyama's work. \n"
        "Relevance Score: 7"
    )

    assert extract_score(sample) == 7

    sample = (
        "The evolution of human color vision is "
        "closely tied to theories about the nature "
        "of light, dating back to the 17th to 19th "
        "centuries. Initially, there was no clear distinction "
        "between the properties of light, the eye and retina, "
        "and color percepts. Major figures in science attempted "
        "to resolve these issues, with physicists leading most "
        "advances in color science into the 20th century. Prior "
        "to Newton, colors were viewed as stages between black "
        "and white. Newton was the first to describe colors in "
        "a modern sense, using prisms to disperse light into "
        "a spectrum of colors. He demonstrated that each color "
        "band could not be further divided and that different "
        "colors had different refrangibility. \n"
        "Relevance Score: 9.5"
    )

    assert extract_score(sample) == 9


@pytest.mark.parametrize(
    "example",
    [
        """Sure here is the json you asked for!

    {
    "example": "json"
    }

    Did you like it?""",
        '{"example": "json"}',
        """
```json
{
    "example": "json"
}
```

I have written the json you asked for.""",
        """

{
    "example": "json"
}

""",
    ],
)
def test_llm_parse_json(example: str) -> None:
    assert llm_parse_json(example) == {"example": "json"}


def test_llm_parse_json_newlines() -> None:
    """Make sure that newlines in json are preserved and escaped."""
    example = textwrap.dedent(
        """
        {
        "summary": "A line

        Another line",
        "relevance_score": 7
        }"""
    )
    assert llm_parse_json(example) == {
        "summary": "A line\n\nAnother line",
        "relevance_score": 7,
    }


@pytest.mark.asyncio
async def test_chain_completion() -> None:
    s = Settings(llm="babbage-002", temperature=0.2)
    outputs = []

    def accum(x) -> None:
        outputs.append(x)

    llm = s.get_llm()
    completion = await llm.run_prompt(
        prompt="The {animal} says",
        data={"animal": "duck"},
        system_prompt=None,
        callbacks=[accum],
    )
    assert completion.seconds_to_first_token > 0
    assert completion.prompt_count > 0
    assert completion.completion_count > 0
    assert str(completion) == "".join(outputs)

    completion = await llm.run_prompt(
        prompt="The {animal} says", data={"animal": "duck"}, system_prompt=None
    )
    assert completion.seconds_to_first_token == 0
    assert completion.seconds_to_last_token > 0

    assert completion.cost > 0


@pytest.mark.skipif(os.environ.get("ANTHROPIC_API_KEY") is None, reason="No API key")
@pytest.mark.asyncio
async def test_anthropic_chain(stub_data_dir: Path) -> None:
    anthropic_settings = Settings(llm=CommonLLMNames.ANTHROPIC_TEST.value)
    outputs: list[str] = []

    def accum(x) -> None:
        outputs.append(x)

    llm = anthropic_settings.get_llm()
    completion = await llm.run_prompt(
        prompt="The {animal} says",
        data={"animal": "duck"},
        system_prompt=None,
        callbacks=[accum],
    )
    assert completion.seconds_to_first_token > 0
    assert completion.prompt_count > 0
    assert completion.completion_count > 0
    assert str(completion) == "".join(outputs)
    assert isinstance(completion.text, str)
    assert completion.cost > 0

    completion = await llm.run_prompt(
        prompt="The {animal} says", data={"animal": "duck"}, system_prompt=None
    )
    assert completion.seconds_to_first_token == 0
    assert completion.seconds_to_last_token > 0
    assert isinstance(completion.text, str)
    assert completion.cost > 0

    docs = Docs()
    await docs.aadd(
        stub_data_dir / "flag_day.html",
        "National Flag of Canada Day",
        settings=anthropic_settings,
    )
    result = await docs.aget_evidence(
        "What is the national flag of Canada?", settings=anthropic_settings
    )
    assert result.cost > 0


@pytest.mark.vcr
@pytest.mark.asyncio
async def test_docs_lifecycle(subtests: SubTests, stub_data_dir: Path) -> None:
    docs = Docs()
    await docs.aadd(
        stub_data_dir / "flag_day.html",
        "WikiMedia Foundation, 2023, Accessed now",
        dockey="test",
    )
    with subtests.test(msg="citation-creation"):
        assert docs.docs["test"].docname == "Wiki2023"

    with subtests.test(msg="text-contains"):
        await docs.aget_evidence("What is the national flag of Canada?")
        assert docs.texts_index.texts_hashes
        assert docs.texts
        assert all(t in docs.texts_index for t in docs.texts)

        docs.texts_index.clear()
        assert docs.texts
        assert all(t not in docs.texts_index for t in docs.texts)


def test_evidence(docs_fixture) -> None:
    debug_settings = Settings.from_name("debug")
    evidence = docs_fixture.get_evidence(
        PQASession(question="What does XAI stand for?"),
        settings=debug_settings,
    ).contexts
    assert len(evidence) >= debug_settings.answer.evidence_k


def test_json_evidence(docs_fixture) -> None:
    settings = Settings.from_name("fast")
    settings.prompts.use_json = True
    settings.prompts.summary_json_system = (
        "Provide a summary of the excerpt that could help answer the question based on"
        " the excerpt. The excerpt may be irrelevant. Do not directly answer the"
        " question - only summarize relevant information.  Respond with the following"
        ' JSON format:\n\n {{\n"summary": "...",\n"author_name":'
        ' "...",\n"relevance_score": "..."}}\n\n where `summary` is relevant'
        " information from text -  about 100 words words, `author_name` specifies the"
        " author , and `relevance_score` is  the relevance of `summary` to answer the"
        " question (integer out of 10)."
    )
    evidence = docs_fixture.get_evidence(
        PQASession(question="Who wrote this article?"),
        settings=settings,
    ).contexts
    assert evidence[0].author_name


def test_ablations(docs_fixture) -> None:
    settings = Settings()
    settings.answer.evidence_skip_summary = True
    settings.answer.evidence_retrieval = False
    contexts = docs_fixture.get_evidence(
        "Which page is the statement 'Deep learning (DL) is advancing the boundaries of"
        " computational chemistry because it can accurately model non-linear"
        " structure-function relationships.' on?",
        settings=settings,
    ).contexts
    assert contexts[0].text.text == contexts[0].context, "summarization not ablated"

    assert len(contexts) == len(docs_fixture.texts), "evidence retrieval not ablated"


def test_location_awareness(docs_fixture) -> None:
    settings = Settings()
    settings.answer.evidence_k = 3
    settings.prompts.use_json = False
    settings.prompts.system = "Answer either N/A or a page number."
    settings.prompts.summary = "{citation}\n\n{text}\n\n{question}{summary_length}"
    settings.answer.evidence_summary_length = ""

    contexts = docs_fixture.get_evidence(
        "Which page is the statement 'Deep learning (DL) is advancing the boundaries of"
        " computational chemistry because it can accurately model non-linear"
        " structure-function relationships.' on?",
        settings=settings,
    ).contexts
    assert "1" in "\n".join(
        [c.context for c in contexts]
    ), "location not found in evidence"


def test_query(docs_fixture) -> None:
    docs_fixture.query("Is XAI usable in chemistry?")


def test_llmresult_callback(docs_fixture: Docs) -> None:
    my_results: list[LLMResult] = []

    settings = Settings.from_name("fast")
    summary_llm = settings.get_summary_llm()
    summary_llm.llm_result_callback = my_results.append
    docs_fixture.get_evidence(
        "What is XAI?", settings=settings, summary_llm_model=summary_llm
    )
    assert my_results
    assert len(my_results) >= 1, "Expected the callback to append results"
    assert my_results[0].name
    assert my_results[0].session_id


def test_duplicate(stub_data_dir: Path) -> None:
    """Check Docs doesn't store duplicates, while checking nonduplicate docs are stored."""
    docs = Docs()
    assert docs.add(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        dockey="test1",
    )
    assert (
        docs.add(
            stub_data_dir / "bates.txt",
            citation="WikiMedia Foundation, 2023, Accessed now",
            dockey="test1",
        )
        is None
    )
    assert len(docs.docs) == 1, "Should have added only one document"
    assert docs.add(
        stub_data_dir / "flag_day.html",
        citation="WikiMedia Foundation, 2023, Accessed now",
        dockey="test2",
    )
    assert (
        len(set(docs.docs.values())) == 2
    ), "Unique documents should be hashed as unique"


@pytest.mark.asyncio
@pytest.mark.parametrize("vector_store", [NumpyVectorStore, QdrantVectorStore])
async def test_docs_with_custom_embedding(
    subtests: SubTests, stub_data_dir: Path, vector_store: type[VectorStore]
) -> None:
    class MyEmbeds(EmbeddingModel):
        name: str = "my_embed"

        async def embed_documents(self, texts):
            return [[0.0, 0.28, 0.95] for _ in texts]

    docs = Docs(texts_index=vector_store())
    await docs.aadd(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        embedding_model=MyEmbeds(),
    )

    with subtests.test(msg="confirm-embedding"):
        assert docs.texts[0].embedding == [0.0, 0.28, 0.95]

    with subtests.test(msg="copying-before-get-evidence"):
        # Before getting evidence, shallow and deep copies are the same
        docs_shallow_copy = Docs(
            texts_index=type(docs.texts_index)(**docs.texts_index.model_dump()),
            **docs.model_dump(exclude={"texts_index"}),
        )
        docs_deep_copy = deepcopy(docs)

        assert (
            docs.texts_index
            == docs_shallow_copy.texts_index
            == docs_deep_copy.texts_index
        )

    with subtests.test(msg="copying-after-get-evidence"):
        # After getting evidence, a shallow copy of Docs is not the same because its
        # texts index gets lazily populated, while a deep copy should preserve it
        _ = await docs.aget_evidence(
            "What country is Frederick Bates from?", embedding_model=MyEmbeds()
        )
        docs_shallow_copy = Docs(
            texts_index=type(docs.texts_index)(**docs.texts_index.model_dump()),
            **docs.model_dump(exclude={"texts_index"}),
        )
        docs_deep_copy = deepcopy(docs)

        assert docs.texts_index != docs_shallow_copy.texts_index
        assert docs.texts_index == docs_deep_copy.texts_index

    with subtests.test(msg="clear-vector-store"):
        # Test that the vector store has content before clearing
        if isinstance(docs.texts_index, QdrantVectorStore):
            # For QdrantVectorStore, we need to check if collection exists and has points
            assert await docs.texts_index._collection_exists()
            collection_info = await docs.texts_index.client.get_collection(
                docs.texts_index.collection_name
            )
            assert collection_info.points_count > 0
        assert len(docs.texts_index) > 0
        assert len(docs.texts_index.texts_hashes) > 0

        # Clear the vector store via Docs
        docs.clear_docs()

        # Verify the vector store is empty
        if isinstance(docs.texts_index, QdrantVectorStore):
            assert not await docs.texts_index._collection_exists()
            assert docs.texts_index._point_ids is None
        assert len(docs.texts_index) == 0
        assert len(docs.texts_index.texts_hashes) == 0


@pytest.mark.parametrize("vector_store", [NumpyVectorStore, QdrantVectorStore])
def test_sparse_embedding(stub_data_dir: Path, vector_store: type[VectorStore]) -> None:
    docs = Docs(texts_index=vector_store())
    docs.add(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        embedding_model=SparseEmbeddingModel(),
    )
    assert any(cast(list[float], docs.texts[0].embedding))
    assert all(
        len(np.array(x.embedding).shape) == 1 for x in docs.texts
    ), "Embeddings should be 1D"

    # check the embeddings are the same size
    assert docs.texts[0].embedding is not None
    assert docs.texts[1].embedding is not None
    assert np.shape(docs.texts[0].embedding) == np.shape(docs.texts[1].embedding)


@pytest.mark.parametrize("vector_store", [NumpyVectorStore, QdrantVectorStore])
def test_hybrid_embedding(stub_data_dir: Path, vector_store: type[VectorStore]) -> None:
    emb_model = HybridEmbeddingModel(
        models=[LiteLLMEmbeddingModel(), SparseEmbeddingModel()]
    )
    docs = Docs(texts_index=vector_store())
    docs.add(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        embedding_model=emb_model,
    )
    assert any(cast(list[float], docs.texts[0].embedding))

    # check the embeddings are the same size
    assert docs.texts[0].embedding is not None
    assert docs.texts[1].embedding is not None
    assert np.shape(docs.texts[0].embedding) == np.shape(docs.texts[1].embedding)

    # now try via alias
    emb_settings = Settings(
        embedding="hybrid-text-embedding-3-small",
    )
    docs.add(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        embedding_model=emb_settings.get_embedding_model(),
    )
    assert any(docs.texts[0].embedding)


def test_custom_llm(stub_data_dir: Path) -> None:
    from llmclient import Chunk

    class StubLLMModel(LLMModel):
        name: str = "myllm"

        async def acomplete(self, prompt: str) -> Chunk:  # noqa: ARG002
            return Chunk(text="Echo", prompt_tokens=1, completion_tokens=1)

        async def acomplete_iter(
            self, prompt: str  # noqa: ARG002
        ) -> AsyncIterable[Chunk]:
            yield Chunk(text="Echo", prompt_tokens=1, completion_tokens=1)

    docs = Docs()
    docs.add(
        stub_data_dir / "bates.txt",
        citation="WikiMedia Foundation, 2023, Accessed now",
        dockey="test",
        llm_model=StubLLMModel(),
    )
    # ensure JSON summaries are not used
    no_json_settings = Settings(prompts={"use_json": False})
    evidence = docs.get_evidence(
        "Echo", summary_llm_model=StubLLMModel(), settings=no_json_settings
    ).contexts
    assert "Echo" in evidence[0].context

    evidence = docs.get_evidence(
        "Echo",
        callbacks=[print_callback],
        summary_llm_model=StubLLMModel(),
        settings=no_json_settings,
    ).contexts
    assert "Echo" in evidence[0].context


def test_docs_pickle(stub_data_dir) -> None:
    """Ensure that Docs object can be pickled and unpickled correctly."""
    docs = Docs()
    docs.add(
        stub_data_dir / "flag_day.html",
        "WikiMedia Foundation, 2023, Accessed now",
        dockey="test",
    )

    # Pickle the Docs object
    docs_pickle = pickle.dumps(docs)
    unpickled_docs = pickle.loads(docs_pickle)

    assert unpickled_docs.docs["test"].docname == "Wiki2023"
    assert len(unpickled_docs.docs) == 1


@pytest.mark.parametrize(
    ("qa_prompt", "unsure_sentinel"),
    [
        pytest.param(default_qa_prompt, CANNOT_ANSWER_PHRASE, id="default-unsure"),
        pytest.param(
            default_qa_prompt.replace(CANNOT_ANSWER_PHRASE, "I am unsure"),
            "I am unsure",
            id="custom-unsure",
        ),
    ],
)
def test_unrelated_context(
    agent_test_settings: Settings,
    stub_data_dir: Path,
    qa_prompt: str,
    unsure_sentinel: str,
) -> None:
    agent_test_settings.prompts.qa = qa_prompt
    assert unsure_sentinel in qa_prompt, "Test relies on unsure sentinel in qa prompt"

    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    session = docs.query(
        "What do scientist estimate as the planetary composition of Jupyter?",
        settings=agent_test_settings,
    )
    assert unsure_sentinel in session.answer


def test_repeat_keys(stub_data_dir) -> None:
    docs = Docs()
    result = docs.add(
        stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now"
    )
    assert result
    result = docs.add(
        stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now"
    )
    assert not result
    assert len(docs.docs) == 1

    docs.add(
        stub_data_dir / "flag_day.html", "WikiMedia Foundation, 2023, Accessed now"
    )
    assert len(docs.docs) == 2

    # check keys
    ds = list(docs.docs.values())
    assert ds[0].docname == "Wiki2023"
    assert ds[1].docname == "Wiki2023a"


def test_can_read_normal_pdf_reader(docs_fixture) -> None:
    answer = docs_fixture.query("Are counterfactuals actionable? [yes/no]")
    assert "yes" in answer.answer or "Yes" in answer.answer


def test_pdf_reader_w_no_match_doc_details(stub_data_dir: Path) -> None:
    docs = Docs()
    docs.add(stub_data_dir / "paper.pdf", "Wellawatte et al, XAI Review, 2023")
    # doc will be a DocDetails object, but nothing can be found
    # thus, we retain the prior citation data
    assert (
        next(iter(docs.docs.values())).citation == "Wellawatte et al, XAI Review, 2023"
    )
    assert (
        next(iter(docs.docs.values())).formatted_citation
        == "Wellawatte et al, XAI Review, 2023"
    ), "Formatted citation should be the same when no metadata is found."


def test_pdf_reader_w_no_chunks(stub_data_dir: Path) -> None:
    settings = Settings.from_name("debug")
    assert settings.parsing.defer_embedding, "Test relies on deferred embedding"
    settings.parsing.chunk_size = 0  # Leads to one chunk = entire text
    # don't want to shove whole document into llm to get citation or embedding
    settings.parsing.use_doc_details = False
    settings.summary_llm = "gpt-4o-mini"  # context window needs to fit our one chunk

    docs = Docs()
    docs.add(
        stub_data_dir / "paper.pdf",
        "Wellawatte et al, XAI Review, 2023",
        settings=settings,
    )
    assert len(docs.texts) == 1, "Should have been one chunk"
    assert docs.texts[0].embedding is None, "Should have deferred the embedding"


@pytest.mark.vcr
@pytest.mark.parametrize("defer_embeddings", [True, False])
@pytest.mark.asyncio
async def test_partly_embedded_texts(defer_embeddings: bool) -> None:
    settings = Settings.from_name("fast")
    settings.parsing.defer_embedding = defer_embeddings
    docs = Docs()
    assert isinstance(
        docs.texts_index, NumpyVectorStore
    ), "We want this test to cover NumpyVectorStore"

    stub_doc = Doc(docname="stub", citation="stub", dockey="stub")
    pre_embedded_text = Text(text="I like turtles.", name="sentence1", doc=stub_doc)
    pre_embedded_text.embedding = (
        await settings.get_embedding_model().embed_documents([pre_embedded_text.text])
    )[0]
    texts_to_add = [
        pre_embedded_text,
        Text(text="I like cats.", name="sentence2", doc=stub_doc),
    ]

    # 1. Add texts (and some are partly embedded)
    await docs.aadd_texts(texts=texts_to_add, doc=stub_doc)
    assert docs.texts == texts_to_add
    assert not docs.texts_index.texts
    assert not docs.texts_index.texts_hashes

    # 2. Gather evidence should work
    await docs.aget_evidence("What do I like?")
    assert docs.texts_index.texts == docs.texts == texts_to_add
    assert len(docs.texts_index.texts_hashes) == len(texts_to_add)

    # 3. Gathering evidence again should not change shapes
    await docs.aget_evidence("What was it that I liked?")
    assert docs.texts_index.texts == docs.texts == texts_to_add
    assert len(docs.texts_index.texts_hashes) == len(texts_to_add)


# some of the stored requests will be identical on method, scheme, host, port, path, and query (if defined)
# body will always be different between requests
# adding body so that vcr correctly match the right request with its response.
@pytest.mark.vcr(match_on=[*VCR_DEFAULT_MATCH_ON, "body"])
def test_pdf_reader_match_doc_details(stub_data_dir: Path) -> None:
    docs = Docs()
    docs.add(
        stub_data_dir / "paper.pdf",
        "Wellawatte et al, A Perspective on Explanations of Molecular Prediction"
        " Models, XAI Review, 2023",
        use_doc_details=True,
        clients={
            CrossrefProvider,
            JournalQualityPostProcessor,
        },  # Limit to only crossref since s2 is too flaky
        fields=["author", "journal", "citation_count"],
    )
    doc_details = next(iter(docs.docs.values()))
    # Crossref is non-deterministic in its ordering for results
    # thus we need to capture both possible dockeys
    assert doc_details.dockey in {"d7763485f06aabde", "5300ef1d5fb960d7"}
    assert isinstance(doc_details, DocDetails)
    # note year is unknown because citation string is only parsed for authors/title/doi
    # AND we do not request it back from the metadata sources
    assert doc_details.docname == "wellawatteUnknownyearaperspectiveon"
    assert doc_details.authors
    assert set(doc_details.authors) == {
        "Geemi P. Wellawatte",
        "Heta A. Gandhi",
        "Aditi Seshadri",
        "Andrew D. White",
    }
    assert doc_details.doi in {
        "10.1021/acs.jctc.2c01235",
        "10.26434/chemrxiv-2022-qfv02",
    }
    match = re.search(
        r"This article has (\d+) citations", doc_details.formatted_citation
    )
    assert match
    num_citations = int(match.group(1))
    assert num_citations >= 1, "Expected at least one citation"
    assert (
        "Journal of Chemical Theory and Computation" in doc_details.formatted_citation
    )

    num_retries = 3
    for _ in range(num_retries):
        answer = docs.query("Are counterfactuals actionable? [yes/no]")
        if any(w in answer.answer for w in ("yes", "Yes")):
            assert f"This article has {num_citations} citations" in answer.context
            return
    raise AssertionError(f"Query was incorrect across {num_retries} retries.")


def test_fileio_reader_pdf(stub_data_dir: Path) -> None:
    with (stub_data_dir / "paper.pdf").open("rb") as f:
        docs = Docs()
        docs.add_file(f, "Wellawatte et al, XAI Review, 2023")
    num_retries = 3
    for _ in range(num_retries):
        answer = docs.query("Are counterfactuals actionable? [yes/no]")
        if any(w in answer.answer for w in ("yes", "Yes")):
            return
    raise AssertionError(f"Query was incorrect across {num_retries} retries.")


def test_fileio_reader_txt(stub_data_dir: Path) -> None:
    # can't use curie, because it has trouble with parsed HTML
    docs = Docs()
    with (stub_data_dir / "bates.txt").open("rb") as file:
        file_content = file.read()

    docs.add_file(
        BytesIO(file_content),
        "WikiMedia Foundation, 2023, Accessed now",
    )
    answer = docs.query("What country was Frederick Bates born in?")
    assert "United States" in answer.answer


def test_parser_only_reader(stub_data_dir: Path):
    doc_path = stub_data_dir / "paper.pdf"
    parsed_text = read_doc(
        Path(doc_path),
        Doc(docname="foo", citation="Foo et al, 2002", dockey="1"),
        parsed_text_only=True,
    )
    assert parsed_text.metadata.parse_type == "pdf"
    assert parsed_text.metadata.chunk_metadata is None
    assert parsed_text.metadata.total_parsed_text_length == sum(
        len(t) for t in parsed_text.content.values()  # type: ignore[misc,union-attr]
    )


def test_chunk_metadata_reader(stub_data_dir: Path) -> None:
    doc_path = stub_data_dir / "paper.pdf"
    chunk_text, metadata = read_doc(
        Path(doc_path),
        Doc(docname="foo", citation="Foo et al, 2002", dockey="1"),
        parsed_text_only=False,  # noqa: FURB120
        include_metadata=True,
    )
    assert metadata.parse_type == "pdf"
    assert metadata.chunk_metadata.chunk_type == "overlap_pdf_by_page"  # type: ignore[union-attr]
    assert metadata.chunk_metadata.overlap == 100  # type: ignore[union-attr]
    assert metadata.chunk_metadata.chunk_chars == 3000  # type: ignore[union-attr]
    assert all(len(chunk.text) <= 3000 for chunk in chunk_text)
    assert metadata.total_parsed_text_length // 3000 <= len(chunk_text)
    assert all(
        chunk_text[i].text[-100:] == chunk_text[i + 1].text[:100]
        for i in range(len(chunk_text) - 1)
    )

    doc_path = stub_data_dir / "flag_day.html"

    chunk_text, metadata = read_doc(
        Path(doc_path),
        Doc(docname="foo", citation="Foo et al, 2002", dockey="1"),
        parsed_text_only=False,  # noqa: FURB120
        include_metadata=True,
    )
    # NOTE the use of tiktoken changes the actual char and overlap counts
    assert metadata.parse_type == "html"
    assert metadata.chunk_metadata.chunk_type == "overlap"  # type: ignore[union-attr]
    assert metadata.chunk_metadata.overlap == 100  # type: ignore[union-attr]
    assert metadata.chunk_metadata.chunk_chars == 3000  # type: ignore[union-attr]
    assert all(len(chunk.text) <= 3000 * 1.25 for chunk in chunk_text)
    assert metadata.total_parsed_text_length // 3000 <= len(chunk_text)

    doc_path = Path(os.path.abspath(__file__))

    chunk_text, metadata = read_doc(
        doc_path,
        Doc(docname="foo", citation="Foo et al, 2002", dockey="1"),
        parsed_text_only=False,  # noqa: FURB120
        include_metadata=True,
    )
    assert metadata.parse_type == "txt"
    assert metadata.chunk_metadata.chunk_type == "overlap_code_by_line"  # type: ignore[union-attr]
    assert metadata.chunk_metadata.overlap == 100  # type: ignore[union-attr]
    assert metadata.chunk_metadata.chunk_chars == 3000  # type: ignore[union-attr]
    assert all(len(chunk.text) <= 3000 * 1.25 for chunk in chunk_text)
    assert metadata.total_parsed_text_length // 3000 <= len(chunk_text)


def test_code() -> None:
    settings = Settings.from_name("fast")
    docs = Docs()
    # load this script
    docs.add(
        THIS_MODULE, "test_paperqa.py", docname="test_paperqa.py", disable_check=True
    )
    assert len(docs.docs) == 1
    session = docs.query("What file is read in by test_code?", settings=settings)
    assert "test_paperqa.py" in session.answer


def test_zotero() -> None:
    from paperqa.contrib import ZoteroDB

    Docs()
    with contextlib.suppress(ValueError):  # Close enough
        ZoteroDB()  # "group" if group library


def test_too_much_evidence(
    stub_data_dir: Path, stub_data_dir_w_near_dupes: Path
) -> None:
    doc_path = stub_data_dir / "obama.txt"
    mini_settings = Settings(llm="gpt-4o-mini", summary_llm="gpt-4o-mini")
    docs = Docs()
    docs.add(
        doc_path, "WikiMedia Foundation, 2023, Accessed now", settings=mini_settings
    )
    # add with new dockey
    docs.add(
        stub_data_dir_w_near_dupes / "obama_modified.txt",
        "WikiMedia Foundation, 2023, Accessed now",
        settings=mini_settings,
    )
    settings = Settings.from_name("fast")
    settings.answer.evidence_k = 10
    settings.answer.answer_max_sources = 10
    docs.query("What is Barrack's greatest accomplishment?", settings=settings)


def test_custom_prompts(stub_data_dir: Path) -> None:
    my_qaprompt = (
        "Answer the question '{question}' using the country name alone. For example: A:"
        " United States\nA: Canada\nA: Mexico\n\n Using the"
        " context:\n\n{context}\n\nA: "
    )
    settings = Settings.from_name("fast")
    settings.prompts.qa = my_qaprompt
    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    answer = docs.query("What country is Frederick Bates from?", settings=settings)
    assert "United States" in answer.answer


def test_pre_prompt(stub_data_dir: Path) -> None:
    pre = (
        "What is water's boiling point in Fahrenheit? Please respond with a complete"
        " sentence."
    )

    settings = Settings.from_name("fast")
    settings.prompts.pre = pre
    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    assert "212" not in docs.query("What is the boiling point of water?").answer
    assert (
        "212"
        in docs.query("What is the boiling point of water?", settings=settings).answer
    )


def test_post_prompt(stub_data_dir: Path) -> None:
    post = "The opposite of down is"
    settings = Settings.from_name("fast")
    settings.prompts.post = post
    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    response = docs.query("What country is Bates from?", settings=settings)
    assert "up" in response.answer.lower()


def test_external_doc_index(stub_data_dir: Path) -> None:
    docs = Docs()
    docs.add(
        stub_data_dir / "flag_day.html", "WikiMedia Foundation, 2023, Accessed now"
    )
    # force embedding
    _ = docs.get_evidence(query="What is the date of flag day?")
    docs2 = Docs(texts_index=docs.texts_index)
    assert not docs2.docs
    assert docs2.get_evidence("What is the date of flag day?").contexts


def test_context_inner_outer_prompt(stub_data_dir: Path) -> None:

    prompt_settings = Settings()

    # try bogus prompt
    with pytest.raises(ValueError, match="Context inner prompt must"):
        prompt_settings.prompts.context_inner = "A:"

    prompt_settings = Settings()
    with pytest.raises(ValueError, match="Context outer prompt can only"):
        prompt_settings.prompts.context_outer = "{foo}"

    # make sure prompt gets used
    settings = Settings.from_name("fast")
    settings.prompts.context_inner = "{name} @@@@@ {text}\nFrom: {citation}"
    settings.prompts.context_outer = "{context_str}"
    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    response = docs.query("What country is Bates from?", settings=settings)
    assert "@@@@@" in response.context
    assert "WikiMedia Foundation, 2023" in response.context
    assert "Valid Keys" not in response.context


def test_evidence_detailed_citations_shim(stub_data_dir: Path) -> None:
    # TODO: delete this test in v6
    settings = Settings.from_name("fast")
    # NOTE: this bypasses DeprecationWarning, as the warning is done on construction
    settings.answer.evidence_detailed_citations = False
    docs = Docs()
    docs.add(stub_data_dir / "bates.txt", "WikiMedia Foundation, 2023, Accessed now")
    response = docs.query("What country is Bates from?", settings=settings)
    assert "WikiMedia Foundation, 2023, Accessed now" not in response.context


def test_case_insensitive_matching():
    assert strings_similarity("my test sentence", "My test sentence") == 1.0
    assert strings_similarity("a b c d e", "a b c f") == 0.5
    assert strings_similarity("A B c d e", "a b c f") == 0.5


def test_answer_rename(recwarn) -> None:
    # TODO: delete this test in v6
    answer = Answer(question="")
    assert isinstance(answer, PQASession)
    assert len(recwarn) == 1
    warning_msg = recwarn.pop(DeprecationWarning)
    assert "'Answer' class is deprecated" in str(warning_msg.message)


@pytest.mark.parametrize(
    "doi_journals",
    [
        {"doi": "https://doi.org/10.31224/4087", "journal": "EngRxiv"},
        {"doi": "10.26434/chemrxiv-2021-hz0qp", "journal": "ChemRxiv"},
        {"doi": "https://doi.org/10.1101/2024.11.04.621790", "journal": "BioRxiv"},
        {"doi": "10.1101/2024.11.02.24316629", "journal": "MedRxiv"},
        # ensure we don't crash when externalIds key is included, but it's None
        {
            "doi": "https://doi.org/10.48550/arXiv.2407.10362",
            "journal": "ArXiv",
            "other": {"externalIds": None},
        },
    ],
)
def test_dois_resolve_to_correct_journals(doi_journals):
    details = DocDetails(doi=doi_journals["doi"])  # type: ignore[call-arg]
    assert details.journal == doi_journals["journal"]


def test_docdetails_merge_with_non_list_fields() -> None:
    """Check republication where the source metadata has different shapes."""
    initial_date = datetime(2023, 1, 1)
    doc1 = DocDetails(
        citation="Citation 1",
        publication_date=initial_date,
        docname="Document 1",
        dockey="key1",
        # NOTE: doc1 has non-list bibtex_source and list client_source
        other={"bibtex_source": "source1", "client_source": ["client1"]},
    )

    later_publication_date = initial_date + timedelta(weeks=13)
    doc2 = DocDetails(
        citation=doc1.citation,
        publication_date=later_publication_date,
        docname=doc1.docname,
        dockey=doc1.dockey,
        # NOTE: doc2 has list bibtex_source and non-list client_source
        other={"bibtex_source": ["source2"], "client_source": "client2"},
    )

    # Merge the two DocDetails instances
    merged_doc = doc1 + doc2

    assert {"source1", "source2"}.issubset(
        merged_doc.other["bibtex_source"]
    ), "Expected merge to keep both bibtex sources"
    assert {"client1", "client2"}.issubset(
        merged_doc.other["client_source"]
    ), "Expected merge to keep both client sources"
    assert isinstance(merged_doc, DocDetails), "Merged doc should also be DocDetails"


def test_docdetails_merge_with_list_fields() -> None:
    """Check republication where the source metadata is the same shape."""
    initial_date = datetime(2023, 1, 1)
    doc1 = DocDetails(
        citation="Citation 1",
        publication_date=initial_date,
        docname="Document 1",
        dockey="key1",
        # NOTE: doc1 has list bibtex_source and list client_source
        other={"bibtex_source": ["source1"], "client_source": ["client1"]},
    )

    later_publication_date = initial_date + timedelta(weeks=13)
    doc2 = DocDetails(
        citation=doc1.citation,
        publication_date=later_publication_date,
        docname=doc1.docname,
        dockey=doc1.dockey,
        # NOTE: doc2 has list bibtex_source and list client_source
        other={"bibtex_source": ["source2"], "client_source": ["client2"]},
    )

    # Merge the two DocDetails instances
    merged_doc = doc1 + doc2

    assert {"source1", "source2"}.issubset(
        merged_doc.other["bibtex_source"]
    ), "Expected merge to keep both bibtex sources"
    assert {"client1", "client2"}.issubset(
        merged_doc.other["client_source"]
    ), "Expected merge to keep both client sources"
    assert isinstance(merged_doc, DocDetails), "Merged doc should also be DocDetails"


@pytest.mark.vcr
@pytest.mark.parametrize("use_partition", [True, False])
@pytest.mark.asyncio
async def test_partitioning_fn_docs(use_partition: bool) -> None:
    settings = Settings.from_name("fast")
    settings.answer.evidence_k = 2  # limit to only 2

    # imagine we have some special selection we want to
    # embedding rank by itself
    def partition_by_citation(t: Embeddable) -> int:
        if isinstance(t, Text) and "special" in t.doc.citation:
            return 1
        return 0

    partitioning_fn = partition_by_citation if use_partition else None

    docs = Docs()

    assert isinstance(
        docs.texts_index, NumpyVectorStore
    ), "We want this test to cover NumpyVectorStore"

    # add docs that we can use our partitioning function on
    positive_statements_doc = Doc(docname="stub", citation="stub", dockey="stub")
    negative_statements_doc = Doc(
        docname="special", citation="special", dockey="special"
    )
    texts = []
    for i, (statement, doc) in enumerate(
        [
            ("I like turtles", positive_statements_doc),
            ("I like cats", positive_statements_doc),
            ("I don't like turtles", negative_statements_doc),
            ("I don't like cats", negative_statements_doc),
        ]
    ):
        texts.append(Text(text=statement, name=f"statement_{i}", doc=doc))
        texts[-1].embedding = (
            await settings.get_embedding_model().embed_documents([texts[-1].text])
        )[0]
    await docs.aadd_texts(
        texts=[t for t in texts if t.doc.docname == "stub"], doc=positive_statements_doc
    )
    await docs.aadd_texts(
        texts=[t for t in texts if t.doc.docname == "special"],
        doc=negative_statements_doc,
    )

    # look at the raw rankings first, compare them with and without partitioning
    await docs._build_texts_index(settings.get_embedding_model())

    partitioned_texts, _ = cast(
        tuple[Sequence[Text], list[float]],
        await docs.texts_index.partitioned_similarity_search(
            "What do I like?",
            k=4,
            embedding_model=settings.get_embedding_model(),
            partitioning_fn=partition_by_citation,
        ),
    )

    default_texts, _ = cast(
        tuple[Sequence[Text], list[float]],
        await docs.texts_index.similarity_search(
            "What do I like?", k=4, embedding_model=settings.get_embedding_model()
        ),
    )

    assert partitioned_texts != default_texts, "Should have different rankings"

    # the "like" statements should be before the "don't" like by default
    assert all(
        "don't" not in c.text for c in default_texts[:2]
    ), "None of the 'don't like X' should be first"
    assert all(
        "don't" in c.text for c in default_texts[2:]
    ), "'don't like X' should be second"

    # Otherwise they should be interleaved
    assert (
        sum(int("don't" in c.text) for c in default_texts[:2])
        + sum(int("don't" not in c.text) for c in default_texts[:2])
        == 2
    ), "Should have 1 'like' and 1 'don't like'"

    assert (
        sum(int("don't" in c.text) for c in default_texts[2:])
        + sum(int("don't" not in c.text) for c in default_texts[2:])
        == 2
    ), "Should have 1 'like' and 1 'don't like'"

    # Get the contexts -- ranked via partitioning
    # without partitioning, the "I like X" statements would be ranked first
    # with partitioning, we are forcing them to be interleaved, thus
    # at least one "I don't like X" statements will be in the top 2
    session = await docs.aget_evidence(
        "What do I like?", settings=settings, partitioning_fn=partitioning_fn
    )
    assert docs.texts_index.texts == docs.texts == texts

    if use_partition:
        assert any(
            "don't" in c.text.text for c in session.contexts
        ), 'Should have at least one "I don\'t like X" statement'
    else:
        assert all(
            "don't" not in c.text.text for c in session.contexts
        ), "None of the 'don't like X' statements should be included"
