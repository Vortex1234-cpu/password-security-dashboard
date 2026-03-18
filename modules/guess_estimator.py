def crack_time_estimate(entropy):

    guesses_per_second = 1e9

    combinations = 2 ** entropy

    seconds = combinations / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"

    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"

    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"

    else:
        return f"{seconds/31536000:.2f} years"