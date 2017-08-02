# -*- coding: utf-8 -*-
import sys

from threebot_crypto import generate_key, pad_text, unpad_text, encrypt, decrypt

SECRET = "secret"


def main(argv):
    key = generate_key(SECRET, "salt", 10)
    assert key

if __name__ == "__main__":
    main(argv=sys.argv[1:])
