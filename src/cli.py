import sys
from src.logic import add_numbers


def main() -> None:
    print("--- Prosty Program CLI ---")
    res = add_numbers(5, 7)
    print(f"Wynik dodawania 5 + 7 to: {res}")


if __name__ == "__main__":
    main()
