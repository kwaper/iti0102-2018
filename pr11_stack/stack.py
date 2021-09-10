"""Classes practice."""
from typing import Any


class StackUnderflowException(Exception):
    """If stack is empty exception."""

    print("Sorry, stack is empty.")


class StackOverflowException(Exception):
    """If stack is full exception."""

    print("Sorry, stack is full.")


class Stack:
    """Simple stack implementation."""

    def __init__(self, capacity: int) -> None:
        """
        Initialise the stack.

        :param capacity: the maximum number of objects that stack can hold.
        """
        self.listing = []
        self.capacity = capacity
        pass

    def push(self, item: Any) -> None:
        """
        Add the element to the collection.

        If stack has no more room, raises StackOverflowException.
        """
        if self.is_full() is False:
            self.listing.append(item)
        else:
            raise StackOverflowException
        pass

    def pop(self) -> Any:
        """
        Remove the most recently added element that was not yet removed.

        If stack is empty, raises StackUnderflowException.
        """
        if self.is_empty() is False:
            return self.listing.pop()
        else:
            raise StackUnderflowException

    def peek(self) -> Any:
        """
        Show the most recently added element without removing it from the stack.

        If stack is empty returns None.
        """
        return self.listing[-1] if self.is_empty() is False else None
        pass

    def is_empty(self) -> bool:
        """Checking stack for emptiness."""
        return len(self.listing) == 0
        pass

    def is_full(self) -> bool:
        """Checking stack for fullness."""
        return len(self.listing) == self.capacity
        pass

    def __str__(self) -> str:
        """
        Get string representation of stack.

        If top element is present should return:
            "Stack(capacity={capacity}, top_element={top_element})"
        Else
            "Stack(capacity={capacity})"
        """
        if len(self.listing) > 0:
            return f"Stack(capacity={self.capacity}, top_element={self.listing[-1]})"
        else:
            return f"Stack(capacity={self.capacity})"

        pass
