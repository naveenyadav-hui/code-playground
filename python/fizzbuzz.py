"""Classic FizzBuzz with a tiny twist: pick your own range from the command line."""
import sys


def fizzbuzz(n: int) -> str:
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz"
    return out or str(n)


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    for i in range(1, limit + 1):
        print(fizzbuzz(i))
