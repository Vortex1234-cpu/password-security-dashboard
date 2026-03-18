import hashlib
import requests

def check_breach(password):

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    res = requests.get(url)

    hashes = res.text.splitlines()

    for h in hashes:

        hash_suffix,count = h.split(":")

        if hash_suffix == suffix:
            return int(count)

    return 0