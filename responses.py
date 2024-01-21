from random import choice, randint

def get_responses(user_input: str) -> str:
    user_input = user_input.lower()

    if user_input == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in user_input:
        return 'Hello there!'
    elif 'how are you' in user_input:
        return 'Good, thanks for asking!'
    elif 'bye' in user_input:
        return 'See you!'
    elif 'roll dice' in user_input:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['What are we saying here?', 'I do not understand...', 'Huh?'])
    