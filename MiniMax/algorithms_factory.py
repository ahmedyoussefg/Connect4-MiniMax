from MiniMax.MiniMaxWoPruning import MiniMaxWoPruning
from MiniMax.MiniMax import MiniMax
from Heuristic.heuristic import Heuristic


class AlgorithmsFactory:
    # Factory class for creating search algorithms
    def get_algorithm(self, algorithm_name, heuristic, board, player, max_depth):
        if algorithm_name == "MiniMax":
            return MiniMaxWoPruning(heuristic, board, player, max_depth)
        

