# Password Generator (Python)

A small command-line tool that creates a strong random password of the
length and character sets you choose.

## How to run

```bash
python3 password_generator.py
```

Answer the prompts (press Enter to accept each default):

```
Password length [16]:
Include lowercase letters? (Y/n):
Include UPPERCASE letters? (Y/n):
Include digits? (Y/n):
Include symbols (!@#$...)? (Y/n):
```

Example output:

```
Your password (16 characters):
k7#Qm2!xP9vZr4&
```

## Why it is safe to use as a generator

- It uses Python's `secrets` module, which is designed for
  security-sensitive randomness, not the plain `random` module.
- It guarantees at least one character from every set you selected,
  so a password that asks for symbols really contains one.
- Nothing is saved or sent anywhere — the password is only printed
  once, on your own screen.

## What was practiced

- `secrets` for cryptographically strong random choices
- Guaranteeing coverage of each selected character set, then shuffling
- Input validation with sensible defaults (Enter = default)
