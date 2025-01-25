from pipetee.core import example_function


def test_example_function_no_input() -> None:
    """Test example_function with no input."""
    result = example_function()
    assert result["message"] == "Hello from my_package!"
    assert result["data"] == {}


def test_example_function_with_input() -> None:
    """Test example_function with input data."""
    test_data = {"key": "value"}
    result = example_function(test_data)
    assert result["message"] == "Hello from my_package!"
    assert result["data"] == test_data
