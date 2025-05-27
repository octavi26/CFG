# Context-Free Grammar String Generator and Verifier

This Python project allows you to:

- Parse a context-free grammar (CFG) from a configuration text file.
- Generate random strings based on the CFG.
- Verify if a given string can be generated using the CFG.

## 📁 File Structure

- `main.py`: The main program that handles parsing, generation, and verification.
- `config.txt`: Your CFG configuration file (you'll be prompted to enter its name at runtime).

## 📌 Grammar Configuration File Format

The grammar config file must follow this structure:

```
# Example CFG config file

Nonterminals:
S, A

Sigma:
a
b

Productions:
S -> aA | b
A -> a | ~

End
```

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
```

3. Enter the name of your config file when prompted (e.g., enter `config` for `config.txt`).
4. The program will:
   - Display the parsed CFG.
   - Generate 10 random strings.
   - Ask how many strings you want to check.
   - Verify each string and display the derivation path if valid.

## 🧠 Features

- Robust parsing of CFG with support for comments.
- Random string generation based on productions.
- String verification using recursive descent and backtracking.

## 📎 Example Output

```
Config file name: config
['S', 'A']
['a', 'b']
S
{'S': ['aA', 'b'], 'A': ['a', '']}
0: a
1: a
2: b
3: aa
...
Number of checks: 1
String 1: aa
S -> aA -> aa
```

## ✅ Requirements

- Python 3.x

## 👤 Author

**Radu Dimitrie Octavian**  
Grupa 152

## 📄 License

This project is licensed under the MIT License.
