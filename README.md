# Context-Free Grammar String Generator and Verifier

This Python project allows you to:
1. Parse a context-free grammar (CFG) from a configuration text file.
2. Generate random strings based on the CFG.
3. Verify if a given string can be generated using the CFG.

## 📁 File Structure

- `main.py`: The main program that handles parsing, generation, and verification.
- `config.txt`: Your CFG configuration file (you'll be prompted to enter its name at runtime).

## 📌 Grammar Configuration File Format

The grammar config file must follow a specific format. Here's an example structure:

## Example CFG config file
Nonterminals:
S, A

Sigma:
a
b

Productions:
S -> aA | b
A -> a | ~

End

- `Nonterminals:` — List of non-terminal symbols, first one is the **start symbol**.
- `Sigma:` — Terminal alphabet.
- `Productions:` — Grammar rules (`~` represents the empty string).
- `End` — Marks the end of the grammar section.

Lines starting with `#` are treated as comments.

## ▶️ How to Run

Make sure you have Python 3 installed.

1. Save your CFG configuration in a `.txt` file (e.g., `config.txt`).
2. Run the script:

```bash
python3 main.py


