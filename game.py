import random

def sumOfSquares(table):
    sum = 0
    for i in table:
        for j in i:
            sum += i * i
    return sum

class Game:

    def __init__(self, n, rewardFunction=sumOfSquares):
        self.reward = rewardFunction
        self.n = n
        self.table = [[0 for _ in range(n)] for _ in range(n)]
        self.actions = (0, 1, 2, 3)


    def getState(self):
        return self.table

    def gameOver(self):
        for i in self.table:
            if 0 in i: 
                return False
        return True

    def getReward(self, state=[]):
        if state == []: state = self.table
        return self.reward(state)

    def update(self, string):
        stack = []
        f = True
        for i in string:
            if i == 0: continue
            if len(stack) == 0: stack.append(i)
            elif stack[-1] == i and f: 
                stack[-1] *= 2
                f = False
                continue
            else: stack.append(i)
            f = True
        while len(stack) < len(string): stack.append(0)
        return stack

    def up(self, state):
        n = self.n
        for j in range(n):
            line = []
            for i in range(n): line.append(state[i][j])
            line = self.update(line)
            for i in range(n): state[i][j] = line[i]

    def left(self, state):
        n = self.n
        for i in range(n):
            state[i] = self.update(state[i])

    def down(self, state):
        n = self.n
        for j in range(n):
            line = []
            for i in range(n - 1, -1, -1): 
                line.append(state[i][j])
            line = self.update(line)
            for i in range(n - 1, -1, -1): state[i][j] = line[self.n - i - 1]

    def right(self, state):
        n = self.n
        for i in range(n):
            line = []
            for j in range(n - 1, -1, -1): line.append(state[i][j])
            line = self.update(line)
            for j in range(n - 1, -1, -1): state[i][j] = line[self.n - 1 - j]

    def add2(self, state):
        empty = []
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] == 0: empty.append((i, j))
        if len(empty) == 0: return state
        position = random.choice(empty)
        state[position[0]][position[1]] = 2

    def strangeState(self, vector, table):
        if vector == [0 for _ in range(self.n * self.n)]: return False
        return vector == self.vector(table)

    def vector(self, table):
        vect = []
        for i in table:
            for j in i:
                vect.append(j)
        return vect

    def step(self, action):
        state = self.table
        copy = self.vector(state)

        if action == 0: self.up(state)
        elif action == 1: self.left(state)
        elif action == 2: self.down(state)
        elif action == 3: self.right(state)

        if self.strangeState(copy, state): return
        self.add2(state)

    def render(self, table=[]):
        if table == []: table = self.table
        for i in table: print(i)
