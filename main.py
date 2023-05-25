system = {}
actions = []
conditions = [(0, 0)]
rewards = []
probabilities = [
    [[0.9, 0.1], [0.1, 0.9], [0, 0], [0, 0], [0, 0]],
    [[0.9, 0.1], [0, 0], [0.1, 0.9], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0.9, 0.1], [0, 0], [0.1, 0.9]],
    [[0, 0], [0, 0], [0, 0], [0.9, 0.1], [0.1, 0.9]],
]
strategy = []
V = []

iterations = 1000
beta = 0.9
accuracy = 1


# create system with certain parameters, write down all the possible conditions
def create_system(lam, c, k, d, r, act):
    global V
    global strategy

    system['lambda'] = lam
    system['c'] = c
    system['k'] = k
    system['d'] = d
    system['r'] = r
    system['actions'] = act
    system['con'] = get_conditions()

    get_actions()
    get_rewards()

    V = [0 for c in range(len(conditions))]
    strategy = [0 for c in range(len(conditions))]
    return system


# creates a list of all possible conditions of system
def get_conditions():
    for i in range(1, system['k'] + 1):
        for j in range(system['c']):
            conditions.append((i, j))
    return len(conditions)


# creates a list of possible actions
def get_actions():
    for a in range(system['actions']):
        actions.append(a)
    return


# calculates income for different conditions
def rewards_helper(k, t, action):
    if action == 0:
        return 0
    return system['d'] - system['r'] * (system['c'] * k - t)


# creates a list of one-step rewards for different conditions
def get_rewards():
    for con in conditions:
        rewards.append([rewards_helper(con[0], con[1], actions[0]),
                        rewards_helper(con[0], con[1], actions[1])])
    return


# finds an optimal strategy for given system
def optimal_strategy():
    for i in range(iterations):
        for j in range(iterations):
            delta = 0
            for index, item in enumerate(conditions):
                v = rewards[index][strategy[index]]
                for index2, item2 in enumerate(conditions):
                    v += probabilities[index][index2][strategy[index]] * beta * V[index2]
                delta = max(delta, abs(v - V[index]))
                V[index] = v
            if delta < accuracy:
                break
        if not improve_strategy():
            break


# helps to improve existing strategy
def improve_strategy():
    strategy_improved = False
    for index, item in enumerate(conditions):
        v_current = V[index]
        for a in actions:
            v = rewards[index][a]
            for index2, item2 in enumerate(conditions):
                v += probabilities[index][index2][a] * beta * V[index2]
            if v > v_current and strategy[index] != a:
                strategy[index] = a
                v_current = v
                strategy_improved = True
    return strategy_improved


def main():
    create_system(3, 2, 2, 5, 2, 2)
    optimal_strategy()
    print('Optimal strategy:', strategy)
    print('Vector of rewards:', V)


main()
