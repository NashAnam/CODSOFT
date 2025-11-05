import random

def print_board(board):
    print()
    for i in range(3):
        a = board[i*3]
        b = board[i*3 + 1]
        c = board[i*3 + 2]
        if a == " ":
            a = "_"
        if b == " ":
            b = "_"
        if c == " ":
            c = "_"
        print(a, "|", b, "|", c)
    print()

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] and board[w[0]] != " ":
            return board[w[0]]
    if " " not in board:
        return "Tie"
    return None

def minimax(board, depth, alpha, beta, is_max):
    result = check_winner(board)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Tie":
        return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = " "
                if score > best:
                    best = score
                if best > alpha:
                    alpha = best
                if beta <= alpha:
                    break
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = " "
                if score < best:
                    best = score
                if best < beta:
                    beta = best
                if beta <= alpha:
                    break
        return best

def ai_move(board, level):
    if level == "easy":
        empty = [i for i in range(9) if board[i] == " "]
        return random.choice(empty)

    if level == "medium":
        # 50% random, 50% smart
        if random.random() < 0.5:
            empty = [i for i in range(9) if board[i] == " "]
            return random.choice(empty)

    best_score = -999
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, -999, 999, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    print("Welcome to Tic Tac Toe!")
    print("You are X and AI is O")
    print("Choose positions from 1 to 9")

    print("\nChoose difficulty:")
    print("1. Easy\n2. Medium\n3. Hard")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        level = "easy"
    elif choice == "2":
        level = "medium"
    else:
        level = "hard"

    board = [" "] * 9
    player = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(winner, "wins!")
            break

        if player == "X":
            move = input("Enter your move (1-9): ")
            if not move.isdigit():
                print("Enter number 1-9")
                continue
            move = int(move)
            if move < 1 or move > 9 or board[move - 1] != " ":
                print("Invalid move")
                continue
            board[move - 1] = "X"
            player = "O"
        else:
            print("AI is thinking...")
            move = ai_move(board, level)
            board[move] = "O"
            player = "X"

main()
