import pytest
from n_queens_puzzle import NQueensPuzzle

reference_solutions = [
        { 'n': 4, 'solution': 2 },
        { 'n': 5, 'solution': 10 },
        { 'n': 6, 'solution': 4 },
        { 'n': 7, 'solution': 40 },
        { 'n': 8, 'solution': 92 },
        { 'n': 9, 'solution': 352 },
        { 'n': 10, 'solution': 724 },
        { 'n': 11, 'solution': 2680 },
        { 'n': 12, 'solution': 14200 },
    ]

"""
More Test Cases, with much more execution time
        { 'n': 13, 'solution': 73712 },
        { 'n': 14, 'solution': 365596 },
        { 'n': 15, 'solution': 2279184 },
        { 'n': 16, 'solution': 14772512 },
        { 'n': 17, 'solution': 95815104 },
        { 'n': 18, 'solution': 666090624 },
        { 'n': 19, 'solution': 4968057848 },
        { 'n': 20, 'solution': 39029188884 },
        { 'n': 21, 'solution': 314666222712 },
        { 'n': 22, 'solution': 2691008701644 },
"""

limit_time = 1000 * 60 * 10

def test_n_queen_puzzle():
    for test_case in reference_solutions:
        _solution = NQueensPuzzle(test_case['n'], False, False)
        assert test_case['solution'] == len(_solution.solutions), "test failed, bad solutions number"
        assert _solution.time_elapsed < limit_time, "test failed, over time limit"
