def security_score(entropy, breach, common):

    score = min(entropy,50)

    if breach == 0:
        score += 25

    if not common:
        score += 25

    return min(score,100)