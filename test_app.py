from unittest.mock import patch
from app import take_order


def test_order():
    fake_inputs = ["1", "2", "5", "1", "0"]

    with patch("builtins.input", side_effect=fake_inputs):
        take_order()

    print("\n--- TEST PASSED ---")


if __name__ == "__main__":
    test_order()