import validation


def take_input():
    dna = input("\nEnter DNA sequence: ")

    dna = dna.replace(" ", "")
    dna = dna.upper()

    if dna == "":
        print("You did not enter anything.")
        return ""

    ok, bad = validation.check(dna)

    if ok == False:
        print("Invalid DNA sequence.")
        print("Wrong character(s):", ", ".join(bad))
        print("Use only A, T, G and C.")
        return ""

    return dna
