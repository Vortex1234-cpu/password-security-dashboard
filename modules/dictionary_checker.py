def dictionary_attack(password):

    try:

        with open("common_passwords.txt") as f:
            words = f.read().splitlines()

        return password.lower() in words

    except:
        return False