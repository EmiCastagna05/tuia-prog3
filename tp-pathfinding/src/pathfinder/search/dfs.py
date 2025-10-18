from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search
        Args:
            grid (Grid): Grid of points
        Returns:
            Solution: Solution found
        """

        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize explored with the initial state
        explored = {}
        # explored[root.state] = True

        frontera = StackFrontier()
        frontera.add(root)

        # Initialize frontier with the root node
        if grid.objective_test(root.state):
            return Solution(root, explored)

        while True:
            if frontera.is_empty():
                return NoSolution(explored)

            n1 = frontera.remove()

            if n1.state in explored:
                continue

            explored[n1.state] = True

            for accion in grid.actions(n1.state):
                s = grid.result(n1.state, accion)

                if s not in explored:
                    n2 = Node("",s,n1.cost + grid.individual_cost(n1.state, accion),n1,accion)
                    if grid.objective_test(s):
                        return Solution(n2, explored)
                    frontera.add(n2)
