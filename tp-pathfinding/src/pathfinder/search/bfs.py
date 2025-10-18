from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search
        Args:
            grid (Grid): Grid of points
        Returns:
            Solution: Solution found
        """

        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}  # dicc expandidos, estados alcanzados
        reached[root.state] = True

        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontera = QueueFrontier()
        frontera.add(root)

        while True:
            if frontera.is_empty():
                return NoSolution(reached)

            nodo = frontera.remove()  # guardamos el nodo en n y lo sacamos de la cola

            for accion in grid.actions(nodo.state):
                sucesor = grid.result(nodo.state, accion)
                if sucesor not in reached:
                    hijo = Node("",sucesor,nodo.cost + grid.individual_cost(nodo.state, accion),nodo,accion,)

                    if grid.objective_test(sucesor):
                        return Solution(hijo, reached)

                    reached[sucesor] = True
                    frontera.add(hijo)
