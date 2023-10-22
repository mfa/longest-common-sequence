from ..algorithm import get_longest_common_substrings


def test_readme_example():
    assert get_longest_common_substrings(
        [
            "this dummy example.",
            "example this",
            "this example",
        ],
        [
            "this foo",
            "another not relevant string",
        ],
    ) == {"example"}
