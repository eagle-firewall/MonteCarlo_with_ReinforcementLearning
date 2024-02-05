# MonteCarlo with ReinforcementLearning

This repository contains two Python scripts for playing Tic-Tac-Toe using a combination of Monte Carlo simulations and Reinforcement Learning.

## Reinforcement Learning (mcts-rl.py)

### Overview
- `mcts-rl.py` implements a Tic-Tac-Toe game where the AI player uses a combination of Q-learning and Monte Carlo simulations to make intelligent moves.
- The Q-learning algorithm updates the Q-table based on game outcomes, and the AI player makes decisions based on the Q-values.

### Usage
1. Run the script: `python mcts-rl.py`
2. Follow the on-screen instructions to play the game against the reinforcement learning AI.

## Automated Training with Minimax (trainwith minimax.py)

### Overview
- `trainwith minimax.py` automates the training process by using the Minimax algorithm to train the AI player against itself.
- The script simulates games and updates the Q-table with the results.

### Usage
1. Run the script: `python trainwith minimax.py`
2. Adjust the number of training episodes and other parameters in the script as needed.

## Files

- `mcts-rl.py`: Main script for playing Tic-Tac-Toe against the reinforcement learning AI.
- `trainwith minimax.py`: Script to automate the training process using the Minimax algorithm.
- `qtablex.pkl`: Pickle file storing the Q-table for the reinforcement learning AI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Statistics

- Total games played: [Replace with the total number of games played]
- AI wins: [Replace with the number of AI wins]
- AI losses: [Replace with the number of AI losses]
- Draws: [Replace with the number of draws]

Feel free to customize this README based on your specific project details and requirements.

