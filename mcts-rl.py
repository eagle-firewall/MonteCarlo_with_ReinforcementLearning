

import random
import pickle

def save_qtable(qtable, filename):
    with open(filename, 'wb') as f:
        pickle.dump(qtable, f)

def load_qtable(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        return {}

def print_board(board):
    a = f'''
{board[0]} {board[1]} {board[2]} 
{board[3]} {board[4]} {board[5]} 
{board[6]} {board[7]} {board[8]} 

    '''
    print(a)
def print_qtable(qtable, state):
  if state in qtable: 
      print("Q-table for current state:")
      print("+-----------+------------------------------------+")
      print("  Action    |              Q-value               ")
      print("+-----------+------------------------------------+")
      for action, q_value in qtable[state].items():
        print(f"    {action}      |   {q_value}              ")
      print("+-----------+------------------------------------+")
  else:
      print(f'qtable for this {state} is currently not updated')


def is_won(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if all(board[i + j] == player for j in range(3)):
            return True

    for i in range(3):
        if all(board[i + j] == player for j in range(0, 9, 3)):
            return True

    if all(board[i] == player for i in range(0, 9, 4)) or all(board[i] == player for i in range(2, 7, 2)):
        return True

    return False

def is_draw(board):
    return '-' not in board and not any(is_won(board, player) for player in ['X', 'O'])

def possible_moves(board):
    return [i for i in range(9) if board[i] == '-']

def play_random_move(board, player):
    empty_cells = possible_moves(board)
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = player
        return move

def play_greedy_move(board, player, possible_moves,qtable):
    state = ''.join(board)
    action_moves = possible_moves
    if state in qtable and action_moves:
        # Choose the move with the highest Q-value
        max_value=max([qtable[state][d] for d in action_moves ])
        best_actions = [ d for d in action_moves if qtable[state][d]==max_value ]
        best_move = random.choice(best_actions)
        board[best_move] = player
        return best_move
    else:
        simulations = 1500  # Adjust the number of simulations as needed

        # Perform Monte Carlo simulations
        results = {}
        for move in action_moves:
            total_reward = 0
            for _ in range(simulations):
                temp_board = board.copy()
                temp_board[move] = player
                total_reward += simulate_game(temp_board, player)
            average_reward = total_reward / simulations
            results[move] = average_reward

        # Choose the move with the highest average reward from simulations
        best_move = max(results, key=results.get)
        board[best_move] = player
        return best_move
def simulate_game(board, player):
    # Simulate a game by playing random moves until it ends
    while True:
        empty_cells = possible_moves(board)
        if is_won(board, 'X' if player == 'O' else 'O'):
            return -50  # Opponent won
        elif is_draw(board):
            return -3  # It's a draw
        elif not empty_cells:
            return 0  # Game is still ongoing
        move = random.choice(empty_cells)
        board[move] = 'X' if player == 'O' else 'O'
        if is_won(board, player):
            return 50  # Player won
def q_record(game_record, reward, qtable,learning_rate=0.1):
    games = game_record[::-1]
    for j, i in enumerate(games):
        state, action, possible_action = i
        if state not in qtable:
            qtable[state] = {k: 0 for k in possible_action}
        if action not in qtable[state]:
            qtable[state][action] = 0 

        if qtable[state][action] == 0:
            if j == 0:
                qtable[state][action] = reward
            else:
                reward -= 1
                qtable[state][action] = reward
        else:
            if j == 0:
                qtable[state][action] += learning_rate * (reward - qtable[state][action]) 
            else:
                reward -= 1
                qtable[state][action] += learning_rate * (reward - qtable[state][action])

# Load Q-table using Pickle
qtable = load_qtable('qtablex.pkl')

# Initialize the game
board = ['-'] * 9
current_player = 'X'
game_record = []

while True:
    # AI's turn
    print_qtable(qtable, ''.join(board))
    state = ''.join(board)
    action_moves = possible_moves(board)
    ai_move = play_greedy_move(board, current_player,action_moves ,qtable) 
    state_action = (state, ai_move, action_moves)
    game_record.append(state_action)

    if is_won(board, 'X'):
        q_record(game_record, 50, qtable)
        print("AI won!")
        break
    elif is_draw(board):
        q_record(game_record, -3, qtable)
        print("It's a draw!")
        break
    print_board(board)

    user_move = int(input("Enter your move (0-8): "))
    if user_move not in possible_moves(board):
        print("Illegal move, you lost.")
        break
    board[user_move] = 'O' 
    if is_won(board, 'O'):
        q_record(game_record, -50, qtable)
        print("You won!")
        break
    elif is_draw(board):
        q_record(game_record, -3, qtable)
        print("It's a draw!")
        break
    print_board(board)
   
    
    
print_board(board)
save_qtable(qtable, 'qtablex.pkl')
