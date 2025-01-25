import json

import pandas as pd
import pytest

from shining_brain.tree import create_tree


@pytest.mark.parametrize("csv, json_file", [
    ('data/tree/input_1.csv', 'data/tree/output_1.json'),
    ('data/tree/input_2.csv', 'data/tree/output_2.json'),
    ('data/tree/input_3.csv', 'data/tree/output_3.json'),
    ('data/tree/input_4.csv', 'data/tree/output_4.json'),
    ('data/tree/input_5.csv', 'data/tree/output_5.json')
])
def test_to_snake_case(csv, json_file):
    df = pd.read_csv(csv, dtype={"Level": str})
    tree = create_tree(df)
    with open(json_file, 'r') as file:
        expected = json.load(file)
    assert tree == expected
