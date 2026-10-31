#!/usr/bin/env python3
"""Password generator (Python).

Builds a random password of the length you choose, from the character
sets you pick. Uses the `secrets` module (made for security-sensitive
randomness) instead of the plain `random` module.

The generator guarantees at least one character from every set you
selected, so a password that asks for symbols will actually contain one.
"""

import secrets
import string


def ask_int(prompt, default, minimum):
    """Ask for a whole number; Enter accepts the default."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            value = int(raw)
            if value < minimum:
                print(f"  Please enter {minimum} or more.")
                continue
            return value
        except ValueError:
            print("  Please enter a whole number.")


def ask_yes_no(prompt, default=True):
    """Ask a y/n question; Enter accepts the default."""
    hint = "Y/n" if default else "y/N"
    while True:
        raw = input(f"{prompt} ({hint}): ").strip().lower()
        if raw == "":
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  Please answer y or n.")


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    """Return a password, or None if no character set was selected."""
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+")
    if not pools:
        return None
    if length < len(pools):
        return None
    # One guaranteed character from each selected set, then fill the rest.
    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]
    # Shuffle so the guaranteed characters are not always at the front.
    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]
    return "".join(chars)


def main():
    print("=== Password Generator ===")
    print("Press Enter to accept the default shown in [brackets].\n")
    length = ask_int("Password length [16]: ", 16, 4)
    use_lower = ask_yes_no("Include lowercase letters?", True)
    use_upper = ask_yes_no("Include UPPERCASE letters?", True)
    use_digits = ask_yes_no("Include digits?", True)
    use_symbols = ask_yes_no("Include symbols (!@#$...)?", True)

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    if password is None:
        print("\nNo character set selected (or length too short) — nothing to generate.")
        print("Run again and pick at least one character set.")
        return
    print(f"\nYour password ({len(password)} characters):")
    print(password)
    print("\nTip: store it in a password manager — never reuse it across sites.")


if __name__ == "__main__":
    main()
