import numpy as np

class TicTacToe:
    def __init__(self):
        self.row_count = 3
        self.column_count = 3
        self.action_size = self.row_count * self.column_count
    
    def get_initial_state(self):
        return np.zeros((self.row_count,self.column_count))
    
    def get_next_stage(self,state,action,player):
        row = action // self.column_count
        column = action % self.column_count
        state[row,column]=player
        return state
    
    def get_valid_moves(self,state):
        return (state.reshape(-1) == 0).astype(np.uint8)

    def check_win(self, state, action):
        if action == None:
            return False

        row = action // self.column_count
        column = action % self.column_count
        player = state[row,column]

        return (
            np.sum(state[row, : ]) == player * self.column_count
            or np.sum(state[ : ,column]) == player * self.row_count
            or np.sum(np.diag(state)) == player * self.row_count
            or np.sum(np.diag(np.flip(state))) == player * self.row_count
        )

    def get_value_and_terminated(self,state,action): 
        if self.check_win(state, action):
            return 1, True
        if np.sum(self.get_valid_moves(state)) == 0:
            return 0, True
        return 0, False

    def get_opponent(self,player):
        return -player
    def get_opponent_value(self,value):
        return -value

tick=TicTacToe()
player=1
state= tick.get_initial_state()

while True:
    print(state)
    valid_moves = tick.get_valid_moves(state)
    print("valid_move" , [i for i in range(tick.action_size) if valid_moves[i] == 1])
    action = int(input(f"{player}:"))

    if valid_moves[action] == 0:
        print("action not valid")
        continue

    state = tick.get_next_stage(state, action, player)

    value, is_terminal = tick.get_value_and_terminated(state, action)

    if is_terminal:
        print(state)
        if value == 1:
            print(player, "won")
        else:
            print("draw")
        break
    player = tick.get_opponent(player)

