from pathlib import Path

import pytest
import yaml

from ..algorithm import get_longest_common_sequence


def yaml_fixtures():
    for file in (Path(__file__).parent / "fixtures").glob("*yaml"):
        data = yaml.safe_load(file.open())
        for item in data.get("testcases", []):
            yield item["positives"], item["negatives"], item["result"]


@pytest.mark.parametrize("positives,negatives,expected", yaml_fixtures())
def test_fixtures(positives, negatives, expected):
    assert get_longest_common_sequence(positives, negatives) == set(expected)
