import pytest
from typing import Dict, List, Union

def convert_keys(d: Dict[str, Union[int, float, str]], var_type: List[str]) -> Dict[str, Union[int, float]]:
    """Convert values in a dictionary to integers or floats based on a list of variable types."""
    keys = list(d.keys())
    
    for i in range(len(keys)):
        try:
            if var_type[i] not in ["num", "float"]:
                value = float(d[keys[i]])
                if value.is_integer():
                    d[keys[i]] = int(value)
                else:
                    raise ValueError(f"Value for {keys[i]} is not an integer: {d[keys[i]]}")
            elif var_type[i] == "float":
                d[keys[i]] = float(d[keys[i]])
            elif var_type[i] == "num":
                value = float(d[keys[i]])
                d[keys[i]] = int(value) if value.is_integer() else value
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid value for conversion at {keys[i]}: {d[keys[i]]}")

    return d

def test_convert_keys():
    # Test case 1: Basic conversion to int and float should succeed
    d = {'a': '1', 'b': '2.0', 'c': '3.5'}
    var_type = ["int", "num", "float"]
    result = convert_keys(d, var_type)
    expected = {'a': 1, 'b': 2, 'c': 3.5}
    assert result == expected
    
    # Test case 2: Conversion to int should raise an error for non-integer strings
    d = {'a': '1.5', 'b': '2', 'c': '3'}
    var_type = ["int", "int", "int"]
    with pytest.raises(ValueError, match="Value for a is not an integer"):
        convert_keys(d, var_type)

    # Test case 3: Conversion with all "num" type should succeed
    d = {'a': '1', 'b': '2.2', 'c': '3'}
    var_type = ["num", "num", "num"]
    result = convert_keys(d, var_type)
    expected = {'a': 1, 'b': 2.2, 'c': 3}
    assert result == expected

    # Test case 4: Check for correct float conversion with "float" type
    d = {'a': '1.0', 'b': '2.5', 'c': '3.1'}
    var_type = ["float", "float", "float"]
    result = convert_keys(d, var_type)
    expected = {'a': 1.0, 'b': 2.5, 'c': 3.1}
    assert result == expected

    # Test case 5: Handling strings that cannot be converted to numbers
    d = {'a': 'hello', 'b': '2', 'c': '3'}
    var_type = ["int", "float", "num"]
    with pytest.raises(ValueError, match="Invalid value for conversion at a"):
        convert_keys(d, var_type)

if __name__ == "__main__":
    pytest.main()