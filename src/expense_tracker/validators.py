def get_string_input(prompt: str) -> str:
    while True:
        try:
            return input(prompt).strip()
        except ValueError:
            print("Invalid input")


def get_float_input(prompt: str, min_value: float = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Value must be greater than {min_value}")
                continue
            return value
        except ValueError:
            print("Invalid input")


def get_int_input(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Value must be greater than {min_value}")
                continue
            return value
        except ValueError:
            print("Invalid input")
