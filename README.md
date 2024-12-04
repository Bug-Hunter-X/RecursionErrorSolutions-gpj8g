# Python RecursionError Example

This repository demonstrates a common error in Python involving recursive functions and how to fix it. The `bug.py` file contains code that leads to a `RecursionError`. The `bugSolution.py` file shows the corrected code.

The error occurs because the recursive function `factorial` doesn't handle the case where the input `n` is negative. This leads to an infinite recursion, exceeding Python's maximum recursion depth.

The solution involves adding a check for negative inputs and handling them appropriately (e.g., raising an exception or returning a specific value).