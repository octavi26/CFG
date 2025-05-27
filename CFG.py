# Nume: Radu DImitrie Octavian
# Grupa: 152
# Compilator: python3
import random

def Parse():
    text_file = input("Config file name: ")
    if "." in text_file:
        text_file = text_file[:text_file.find(".")]
    fin = open(text_file + ".txt", "r")

    NT = []
    Sigma = []
    Start = 'S'
    Prod = {}

    state = "end"
    for line in fin:
        # Scapam de comentarii (comentariu ironic)
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == "#":
            continue
        if "#" in line:
            line = line[:line.find("#")]
        
        if line in ["Nonterminals:", "Sigma:", "Productions:", "End"]:
            state = line.lower()[:len(line) - 1 if ":" in line else len(line)]
            continue

        # print(state)

        if state == "nonterminals":
            L = line.replace(",", " ").split()
            if len(L) > 1:
                Start = L[0]
            if L[0] not in NT:
                NT.append(L[0])


        elif state == "productions":
            L = line.replace(" ", "").split("->")
            Prod[L[0]] = ["" if x == '~' else x for x in L[1].split("|")]


        elif state == "sigma":
            if line not in Sigma:
                Sigma.append(line)

        else:
            continue

    return (NT, Sigma, Start, Prod)

def Generate(CFG, word):
    NT, Sigma, Start, Prod = CFG
    for i in range(len(word)):
        symbol = word[i]
        if symbol in NT:
            pos = random.randint(0, len(Prod[symbol])) % len(Prod[symbol])
            seq = Prod[symbol][pos]
            word = word[:i] + seq + word[i + 1:]
            break
    else:
        return word
    return Generate(CFG, word)

def Verify(CFG, Step, word):
    NT, Sigma, Start, Prod = CFG

    if Step == word:
        return True
    
    shape = Step
    for symbol in NT:
        shape = shape.replace(symbol, "*")
    if '*' not in shape:
        return False
    L = shape.split("*")
    if len(L):
        group = L[0]
        pos = word.find(group)
        if pos != 0 and shape[0] != '*':
            return False
        
        start = 0
        for i in range(len(L) - 1):
            group = L[i]
            pos = word[start:].find(group)
            if pos == -1:
                return False
            start = i + len(group)

        group = L[-1]
        pos = word.rfind(group)
        if pos == -1 or (pos + len(group) != len(word) and shape[-1] != '*'):
            return False

    for i in range(len(Step)):
        symbol = Step[i]
        if symbol in NT:
            for seq in Prod[symbol]:
                newStep = Step[:i] + seq + Step[i + 1:]
                if Verify(CFG, newStep, word):
                    Solution.append(newStep)
                    return True

if __name__ == "__main__":
    # Task 1
    CFG = Parse()
    NT, Sigma, Start, Prod = CFG
    print(*CFG, sep="\n")

    # Task 2
    for i in range(10):
        print(i, ": ", Generate(CFG, Start), sep="")

    # Task 3,4
    n = int(input("Number of checks: "))
    for i in range(n):
        word = input("String " + str(i + 1) + ": ")
        Solution = []
        if Verify(CFG, Start, word):
            Solution.append(Start)
            Solution.reverse()
            print(*Solution, sep=" -> ")
            # print("The string is a match!")
        else:
            print("The string can't be replicated.")