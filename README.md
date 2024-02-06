# Monte Carlo with Reinforcement Learning

This project implements the game of Tic-Tac-Toe using both Monte Carlo simulation and Minimax algorithms for reinforcement learning. It explores two different strategies for an AI player: one that utilizes Monte Carlo simulation and another that utilizes the Minimax algorithm. Additionally, there's an interactive mode where a human player can play against the AI player using the trained models.

## Description

The project consists of three Python files:

1. `train-with-random-montecarlo.py`: This script trains an AI player using Monte Carlo simulation. It generates training data by simulating games against random moves. After each game, the Q-values are updated using the rewards obtained from the simulations.

2. `train-with-minimax.py`: This script trains an AI player using the Minimax algorithm. It searches through the game tree using the Minimax algorithm to find the best move for the AI player. Similar to the Monte Carlo approach, it updates the Q-values after each game.

3. `mcts-rl.py`: This script allows the user to play against the trained AI player. It loads the trained Q-table and prompts the user to make a move. The AI player then selects its move based on the learned Q-values.

## Algorithms Used

1. **Monte Carlo Simulation**: Monte Carlo simulation is used to estimate the value of a move by running multiple simulations of random moves and averaging the results. This allows the AI player to explore different paths in the game tree and make informed decisions.

2. **Minimax Algorithm**: The Minimax algorithm is a decision-making algorithm used in two-player games. It searches through the game tree to find the optimal move for the AI player, assuming that the opponent plays optimally as well. It minimizes the potential loss (hence the name Minimax) in the worst-case scenario.

3. **Q-learning Algorithm with Greedy Policy**: Q-learning is a model-free reinforcement learning algorithm used for learning optimal actions. In this project, the AI player uses Q-learning with a greedy policy to select actions. Q-learning updates the Q-values of state-action pairs based on the rewards obtained and learns to choose actions that maximize the expected future rewards.

## Python Object Serialization with Pickle

Python object serialization is used in this project to save and load the trained Q-tables. The Pickle module in Python is employed for this purpose, allowing objects to be converted into a byte stream for storage or transmission.

## Project Process

1. **Training with Monte Carlo Simulation**: The `train-with-random-montecarlo.py` script trains the AI player by simulating games against random moves. It updates the Q-values after each game based on the rewards obtained from the simulations.

2. **Training with Minimax Algorithm**: The `train-with-minimax.py` script trains the AI player using the Minimax algorithm. It searches through the game tree to find the best move for the AI player, updating the Q-values similarly to the Monte Carlo approach.

3. **AI Player Interaction**: The `mcts-rl.py` script allows the user to play against the trained AI player. It loads the trained Q-table and prompts the user to make a move. The AI player then selects its move based on the learned Q-values.

## Usage

To train the AI player using Monte Carlo simulation:
```bash
$ python train-with-random-montecarlo.py
```

To train the AI player using the Minimax algorithm:
```bash
$ python train-with-minimax.py
```

To play against the trained AI player:
```bash
$ python mcts-rl.py
```

---

This README provides an overview of your project, explains the algorithms used, outlines the process involved in training and using the AI player, and highlights the use of Python object serialization with Pickle.
