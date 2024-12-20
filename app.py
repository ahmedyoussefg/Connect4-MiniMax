from flask import Flask, request, jsonify
from flask_cors import CORS
from MiniMax.MiniMax import MiniMax
from Heuristic.heuristics_factory import HeuristicsFactory
from MiniMax.algorithms_factory import AlgorithmsFactory

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

score_calculator = HeuristicsFactory().get_heuristic("NormalScore")
heuristic = HeuristicsFactory().get_heuristic("ConsecutiveCounts")

@app.route('/api/game/move', methods=['POST'])
def make_move():
    try:
        # Extract the board and current player from the request
        data = request.json
        board = data.get("board")
        algorithm = data.get("algorithm", 1)
        turn = data.get("aiTurn", 1)
        max_depth = data.get("depth", 3)
        
        # Set up MiniMax
        heuristic = HeuristicsFactory().get_heuristic("ConsecutiveCounts")
        algorithm = AlgorithmsFactory().get_algorithm(algorithm, heuristic, board, turn, max_depth)
        best_move = algorithm.minimax(board, max_depth)
        nodes_expanded = algorithm.nodes_expanded
        board = algorithm.make_move(board, best_move, turn)
        player1_score = score_calculator.count_fours(board, 1)
        player2_score = score_calculator.count_fours(board, 2)
        tree = algorithm.tree_to_graph(algorithm.root)
        print("done processing")
        return jsonify({
            "board": board,
            "player1_score": player1_score,
            "player2_score": player2_score,
            "nodes_expanded": nodes_expanded,
            "tree": tree
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
