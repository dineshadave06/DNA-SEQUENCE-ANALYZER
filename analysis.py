def count(dna):
    a = 0
    t = 0
    g = 0
    c = 0

    for x in dna:
        if x == "A":
            a += 1
        elif x == "T":
            t += 1
        elif x == "G":
            g += 1
        elif x == "C":
            c += 1

    return a, t, g, c


def do_analysis(dna):
    a, t, g, c = count(dna)

    total = len(dna)
    gc = ((g + c) / total) * 100

    answer = {
        "dna": dna,
        "length": total,
        "a": a,
        "t": t,
        "g": g,
        "c": c,
        "gc": gc
    }

    return answer
