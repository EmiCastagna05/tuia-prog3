from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search
        Args:
            grid (Grid): Grid of points
        Returns:
            Solution: Solution found
        """

        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        def heuristica(nodo: Node) -> int:
            xa, ya = nodo.state
            xg, yg = grid.end
            return abs(xa - xg) + abs(ya - yg)

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost + heuristica(root))

        while True:
            if frontera.is_empty():
                return NoSolution(reached)

            nodo = frontera.pop()

            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)

            for accion in grid.actions(nodo.state):
                sucesor = grid.result(nodo.state, accion)
                costo = nodo.cost + grid.individual_cost(nodo.state, accion)

                if sucesor not in reached or costo < reached[sucesor]:
                    nodoSig = Node("", sucesor, costo, nodo, accion)
                    reached[sucesor] = costo
                    frontera.add(nodoSig, nodoSig.cost + heuristica(nodoSig))
