"""Tests for pykp.solvers module."""

import json

import numpy as np
import pytest

from pykp import Item, Sampler, solvers

HEURISTIC_SOLVERS = ["greedy"]
OPTIMAL_SOLVERS = [
    "branch_and_bound",
    # "mzn_geocode",
]
ALL_SOLVERS = HEURISTIC_SOLVERS + OPTIMAL_SOLVERS

with open("tests/test_cases.json") as f:
    TEST_CASES = json.load(f)


@pytest.fixture
def solver(request):
    """Define the solver to be used in the test."""
    if request.param == "greedy":
        solver = solvers.greedy
    elif request.param == "branch_and_bound":
        solver = solvers.branch_and_bound
    elif request.param == "mzn_geocode":
        solver = solvers.mzn_gecode

    return solver


@pytest.mark.parametrize("solver", ALL_SOLVERS, indirect=True)
def test_empty_items(solver):
    """Test the case where there are no items."""
    items = np.array([])
    solutions = solver(items, 0)

    if not isinstance(solutions, np.ndarray):
        solutions = [solutions]

    assert len(solutions) == 1
    assert solutions[0].value == 0
    assert solutions[0].weight == 0


@pytest.mark.parametrize("solver", ALL_SOLVERS, indirect=True)
def test_single_item_fits(solver):
    """Test a single item that fits in the knapsack."""
    items = np.array([Item(value=10, weight=5)])
    capacity = 10
    solutions = solver(items, capacity)

    if not isinstance(solutions, list):
        solutions = [solutions]

    assert len(solutions) == 1
    assert solutions[0].value == 10
    assert solutions[0].weight == 5


@pytest.mark.parametrize("solver", ALL_SOLVERS, indirect=True)
def test_single_item_does_not_fit(solver):
    """Test a single item that does not fit in the knapsack."""
    items = np.array([Item(value=10, weight=15)])
    capacity = 10
    solutions = solver(items, capacity)

    if not isinstance(solutions, list):
        solutions = [solutions]

    assert len(solutions) == 1
    assert solutions[0].value == 0
    assert solutions[0].weight == 0


@pytest.mark.parametrize("solver", ALL_SOLVERS, indirect=True)
def test_all_items_fit(solver):
    """Test scenario where all items fit in the knapsack."""
    items = np.array(
        [
            Item(value=10, weight=5),
            Item(value=20, weight=5),
            Item(value=30, weight=5),
        ]
    )
    capacity = 15
    solutions = solver(items, capacity)

    if not isinstance(solutions, list):
        solutions = [solutions]

    assert len(solutions) == 1
    assert solutions[0].value == 60
    assert solutions[0].weight == 15


@pytest.mark.parametrize("solver", ALL_SOLVERS, indirect=True)
def test_all_items_do_not_fit(solver):
    """Test scenario where no items fit in the knapsack."""
    items = np.array(
        [
            Item(value=10, weight=15),
            Item(value=20, weight=15),
            Item(value=30, weight=15),
        ]
    )
    capacity = 10
    solutions = solver(items, capacity)

    if not isinstance(solutions, list):
        solutions = [solutions]

    assert len(solutions) == 1
    assert solutions[0].value == 0
    assert solutions[0].weight == 0
    assert np.array_equal(solutions[0].state, np.zeros(len(items)))


@pytest.mark.parametrize("solver", OPTIMAL_SOLVERS, indirect=True)
@pytest.mark.parametrize("case", TEST_CASES)
def test_correct_optimal_found(solver, case):
    """Test that the correct optimal solution is found."""
    items = np.array(
        [
            Item(value=case["values"][i], weight=case["weights"][i])
            for i in range(len(case["values"]))
        ]
    )
    solution = solver(np.array(items), case["capacity"])
    if isinstance(solution, list):
        solution = solution[0]

    assert np.isclose(solution.value, case["optimal_value"])


@pytest.mark.parametrize("num_items", [5, 10, 15, 20])
@pytest.mark.parametrize("seed", [1, 2, 3, 4])
def test_branch_and_bound_decision_variant(num_items, seed):
    """Test that the branch-and-bound (decision) algorithm is correct."""
    sampler = Sampler(num_items=num_items, normalised_capacity=0.5)
    instance = sampler.sample(seed=seed)
    instance.solve()
    optimal = instance.optimal_nodes[0].value

    assert solvers._branch_and_bound_decision_variant(
        instance.items, instance.capacity, optimal
    )
    assert not solvers._branch_and_bound_decision_variant(
        instance.items, instance.capacity, optimal + 0.001
    )
