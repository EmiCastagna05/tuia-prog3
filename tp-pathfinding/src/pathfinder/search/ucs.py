from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search
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

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost)

        while True:
            if frontera.is_empty():

                return NoSolution(reached)

            nodo_padre = frontera.pop()

            if grid.objective_test(nodo_padre.state):
                return Solution(nodo_padre, reached)

            for accion in grid.actions(nodo_padre.state):
                estado_sucesor = grid.result(nodo_padre.state, accion)
                costo_sucesor = nodo_padre.cost + grid.individual_cost(
                    nodo_padre.state, accion
                )

                if (estado_sucesor not in reached or costo_sucesor < reached[estado_sucesor]):
                    nuevo_nodo = Node("", estado_sucesor, costo_sucesor, nodo_padre, accion)
                    reached[estado_sucesor] = costo_sucesor
                    frontera.add(nuevo_nodo, costo_sucesor)