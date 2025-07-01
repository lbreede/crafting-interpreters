from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Self
from dataclasses import dataclass


class Node(ABC):
    def __init__(self, left: Self | None, right: Self | None) -> None:
        self.left = left
        self.right = right

    @abstractmethod
    def eval(self) -> Self: ...


class Add(Node):
    def eval(self) -> Number:
        return self.left.eval() + self.right.eval()

    def __str__(self) -> str:
        return f"(+ {self.left} {self.right})"


class Subtract(Node):
    def eval(self) -> Number:
        return self.left.eval() - self.right.eval()

    def __str__(self) -> str:
        return f"(- {self.left} {self.right})"


class Multiply(Node):
    def eval(self) -> Number:
        return self.left.eval() * self.right.eval()

    def __str__(self) -> str:
        return f"(* {self.left} {self.right})"


class Divide(Node):
    def eval(self) -> Number:
        return self.left.eval() // self.right.eval()

    def __str__(self) -> str:
        return f"(/ {self.left} {self.right})"


class Number(Node):
    def __init__(self, number: int) -> None:
        super().__init__(None, None)
        self.number = number

    def eval(self) -> int:
        return self.number

    def __repr__(self) -> str:
        return f"Number({self.number!r})"

    def __str__(self) -> str:
        return f"{self.number}"


def main():
    result = Divide(
        Subtract(Add(Number(1), Multiply(Number(2), Number(3))), Number(4)),
        Number(3),
    )
    print(f"{result} = {result.eval()}")


if __name__ == "__main__":
    main()
