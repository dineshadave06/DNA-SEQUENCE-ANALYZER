def print_answer(answer):
    print("\n-----------------------------")
    print("DNA Analysis")
    print("-----------------------------")

    print("Sequence:", answer["dna"])
    print("Length:", answer["length"])

    print("\nA =", answer["a"])
    print("T =", answer["t"])
    print("G =", answer["g"])
    print("C =", answer["c"])

    print("\nGC Content = {:.2f}%".format(answer["gc"]))
    print("-----------------------------")
