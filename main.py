import input_file
import analysis
import output


def start():
    print("\nDNA Sequence Analyzer")

    dna = input_file.take_input()

    if dna == "":
        return

    answer = analysis.do_analysis(dna)
    output.print_answer(answer)


while True:
    print("\n1. Analyze DNA")
    print("2. Exit")

    option = input("Choose an option: ")

    if option == "1":
        start()
    elif option == "2":
        print("Program ended.")
        break
    else:
        print("Wrong option.")
        
