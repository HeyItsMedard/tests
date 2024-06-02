def is_final(state):
    # Check if the given state is a final state
    # Return True if it is, False otherwise
    pass

def utility(state):
    # Calculate and return the utility value of the given state
    pass

def next_states(state):
    # Generate and return a list of possible next states from the given state
    pass

def min_value(state, alpha, beta):
    if is_final(state):
        return utility(state)
    val = float('inf')
    for ns in next_states(state):
        val = min(val, max_value(ns, alpha, beta))
        if val < alpha:
            return val
        beta = min(beta, val)
    return val

## olivéré
def max_value(state, alpha, beta):
    if is_final(state):
        return utility(state)
    val = float('-inf')
    for ns in next_states(state):
        val = max(val, min_value(ns, alpha, beta))
        if val > beta:
            return val
        alpha = max(alpha, val)
    return val

def alpha_beta(state):
    return max_value(state, float('-inf'), float('inf'))