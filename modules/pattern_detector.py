import re

def detect_patterns(password):

    warnings = []

    if re.search(r"(123|234|345|456)", password):
        warnings.append("Sequential numbers detected")

    if re.search(r"(qwerty|asdf|zxcv)", password.lower()):
        warnings.append("Keyboard pattern detected")

    if re.search(r"(.)\1{3,}", password):
        warnings.append("Repeated characters detected")

    return warnings