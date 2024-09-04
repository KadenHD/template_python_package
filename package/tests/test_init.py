import pytest
from insightsapi import get_asset_path


@pytest.mark.parametrize("input_name, expected_output", [
    ("", "/package/assets/"),  # Valid path case
    ("not_existing_path", ""),  # Invalid path case
])  # type: ignore
def test_get_asset_path(input_name: str, expected_output: str) -> None:
    """
    Test the `get_asset_path` function with various inputs.

    This test verifies the behavior of the `get_asset_path` function by testing
    both valid and invalid input cases:

    1. Valid path case:
       Checks if the returned path ends with the expected
       output when a valid `input_name` is provided.
    2. Invalid path case:
       Ensures that an `AssertionError` is raised when
       `get_asset_path` is called with an invalid `input_name` that results in
       an empty or non-existent path.

    Parameters:
        input_name (str): The name of the asset or path segment to be appended.
        expected_output (str): The expected ending of the full asset path. If this is an empty string, the test checks for an `AssertionError`.

    Raises:
        AssertionError: If the path does not exist or the output does not match the expected result.
    """  # noqa: E501
    if expected_output:
        assert get_asset_path(input_name).endswith(expected_output)
    else:
        with pytest.raises(AssertionError):
            assert get_asset_path(input_name)
