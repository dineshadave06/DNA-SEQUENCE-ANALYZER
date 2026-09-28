def check(dna):
    allowed = "ATGC"
    bad = []

    for x in dna:
        if x not in allowed:
            if x not in bad:
                bad.append(x)

    if len(bad) == 0:
        return True, bad
    else:
        return False, bad
