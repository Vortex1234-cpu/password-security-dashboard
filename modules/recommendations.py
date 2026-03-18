def generate_recommendations(password, entropy):

    tips = []

    if len(password) < 12:
        tips.append("Increase password length")

    if entropy < 50:
        tips.append("Use more diverse characters")

    if password.isalpha():
        tips.append("Add numbers or symbols")

    return tips