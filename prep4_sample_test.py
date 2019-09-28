"""CSC148 Prep 4: Abstract Data Types

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Prep 4. You may use these to test your
code.

You are to implement AT LEAST 1 test case that will fail on a flawed
implementation of the function reverse_top_two() but pass on a correct
implementation. You may write as many test cases as you would like, so long
as at least 1 fails.

For the flawed implementation of reverse_top_two() that we will run your test
on, you may assume that it passes the doctest test case.

---

WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<https://www.teach.cs.toronto.edu/~csc148h/fall/notes/testing/hypothesis.html>.
"""
from typing import List

from hypothesis import given
from hypothesis.strategies import integers, lists

from preps.prep4.adts import Stack, Queue
from prep4git.prep4 import peek, reverse_top_two, remove_all, remove_all_but_one

#testing


def test_peek_doctest() -> None:
    """This is the doctest given in peek."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert peek(stack) == 2
    assert stack.pop() == 2

@given(lists(integers(), min_size=1, max_size=100))
def test_peek_general(items: List[int]) -> None:
    """Test that peek works for a large range of stack sizes."""
    stack = Stack()
    for item in items:
        stack.push(item)
    assert peek(stack) == items[-1]
    assert stack.pop() == items[-1]


def test_peek_empty() -> None:
    """Test that peek return None for an empty stack."""
    stack = Stack()
    result = peek(stack)
    assert result is None


def test_peek_single_item() -> None:
    """ Test that peek works for a Stack with only one item."""
    stack = Stack()
    stack.push(1)
    result = peek(stack)
    assert result == 1


def test_reverse_top_two_doctest() -> None:
    """This is the doctest given in reverse_top_two."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    reverse_top_two(stack)
    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.is_empty()


def test_reverse_top_two_multiple() -> None:
    """Test that reverse_top_two works when the
     Stack has more than 2 items in it"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    reverse_top_two(stack)
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.is_empty()


def test_remove_all_doctest() -> None:
    """This is the doctest given in remove_all."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    remove_all(queue)
    assert queue.is_empty()

def test_remove_all_empty() -> None:
    """Test what queue_all if passed an empty queue."""
    queue = Queue()
    assert queue.is_empty()
    remove_all(queue)
    assert queue.is_empty()


def test_remove_all_but_one_doctest() -> None:
    """Test is the doctest given in remove_all_but_one."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    remove_all_but_one(queue)
    assert queue.is_empty() is False
    assert queue.dequeue() == 3
    assert queue.is_empty()

def test_remove_all_but_one_single_item() -> None:
    """Test remove_all_but_one when there is only one item in the list"""
    queue = Queue()
    queue.enqueue(1)
    remove_all_but_one(queue)
    assert queue.is_empty() is False
    assert queue.dequeue() == 1
    assert queue.is_empty()

if __name__ == '__main__':
    import pytest
    pytest.main(['prep4_sample_test.py'])
