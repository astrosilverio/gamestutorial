import random

from make_state_transitions import hungry, full, tired, asleep


def transition_state(state, user_input):
    new_state = state.transitions.get(user_input, None)
    if new_state:
        return new_state
    return state


if __name__ == '__main__':
    state = random.choice([hungry, full, tired, asleep])
    print state.name
    while True:
        user_input = raw_input('> ')
        if user_input.lower() == 'exit':
            break
        state = transition_state(state, user_input)
        print state.name
