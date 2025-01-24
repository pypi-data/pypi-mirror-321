from canproc.pipelines.utils import merge_lists


def test_merge_lists_same():

    # full overlap, output = a = b
    a = ["a", "b", "c"]
    b = ["a", "b", "c"]
    assert merge_lists(a, b) == ["a", "b", "c"]


def test_merge_lists_no_overlap():
    # no strict order between a and b list, but order must be preserved of individual elements
    a = ["a", "b", "c"]
    b = ["d", "e", "f"]
    out = merge_lists(a, b)
    assert out.index("a") < out.index("b")
    assert out.index("b") < out.index("c")
    assert out.index("d") < out.index("e")
    assert out.index("e") < out.index("f")


def test_merge_lists_partial_overlap():
    # c must come after b
    a = ["a", "b", "d", "e"]
    b = ["b", "c"]
    out = merge_lists(a, b)
    assert out.index("a") < out.index("b")
    assert out.index("b") < out.index("c")
    assert out.index("b") < out.index("d")
    assert out.index("d") < out.index("e")
