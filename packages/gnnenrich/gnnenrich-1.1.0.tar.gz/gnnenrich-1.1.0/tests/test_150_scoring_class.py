import collections
import gnnenrich
import numpy
import pytest

def test_initializer() -> None:

    emb = collections.OrderedDict()

    for v in (0.0, 0.1, 0.9999999999999999, -1):
        with pytest.raises(ValueError):
            gnnenrich.Scoring(emb, overlap_score = v)

    _ = gnnenrich.Scoring(emb, overlap_score = 1.0)

def test_set_pathways() -> None:

    # Create Scoring object
    emb = collections.OrderedDict()
    scoring = gnnenrich.Scoring(emb)

    # Try to get pathway keys
    with pytest.raises(RuntimeError):
        _ = scoring.get_pathway_keys()

    # Set pathways
    pw: gnnenrich.PathwaysDict = {"pw1": ["a", "b"]}
    scoring.set_pathways(pw)

    # Get pathway keys
    assert scoring.get_pathway_keys() == ["pw1"]

def test_get_pathway_embedding() -> None:

    # Create Scoring object
    emb: gnnenrich.Embeddings = collections.OrderedDict([
            ("a", [0.1, 0.4]),
            ("b", [0.3, 1.0]),
            ])
    scoring = gnnenrich.Scoring(emb)

    # Try to get embeddings
    with pytest.raises(RuntimeError):
        _ = scoring.get_pathway_embeddings()

    # Set pathways
    pw: gnnenrich.PathwaysDict = {"pw1": ["a", "b"]}
    scoring.set_pathways(pw)

    # Get embeddings
    emb = scoring.get_pathway_embeddings() 
    assert isinstance(emb, dict)
    assert len(emb) == 1
    assert "pw1" in emb

    # Get pathway embedding by key
    assert (numpy.array(scoring.get_pathway_embedding("pw1")) ==
            emb["pw1"]).all()
    with pytest.raises(KeyError):
        _ = scoring.get_pathway_embedding("pw2")

def test_compute_pathway_score() -> None:

    # Create Scoring object
    emb: gnnenrich.Embeddings = collections.OrderedDict([
            ("a", [0.1, 0.4]),
            ("b", [0.3, 1.0]),
            ])
    scoring = gnnenrich.Scoring(emb)

    # Set pathways
    pw: gnnenrich.PathwaysDict = {"pw1": ["a", "b"]}
    scoring.set_pathways(pw)

    # Test compute_pathway_score()
    e: EmbArr = numpy.array([[1.0, 2.0], [0.4, 0.7]])
    score = scoring.compute_pathway_score("pw1", e)
    assert isinstance(score, float)
    assert score == 3.0
    with pytest.raises(KeyError):
        _ = scoring.compute_pathway_score("pw2", e)

def test_compute_pathway_scores() -> None:

    # Create Scoring object
    emb: gnnenrich.Embeddings = collections.OrderedDict([
            ("a", [0.1, 0.4]),
            ("b", [0.3, 1.0]),
            ])
    scoring = gnnenrich.Scoring(emb)

    # Set pathways
    pw: gnnenrich.PathwaysDict = {"pw1": ["a", "b"]}
    scoring.set_pathways(pw)

    # Test compute_pathway_scores()
    e: EmbArr = numpy.array([[1.0, 2.0], [0.4, 0.7]])
    scoring.compute_pathway_scores(e)
    assert {"pw1": 3.0} == scoring.get_computed_pathway_scores()
