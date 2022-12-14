import csv

output = []


def main():
    # question 1 dropping last six columns
    global output
    with open("lab_11_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            output.append(row[:-6])
    # question 2  dropping rows where %change is less than or equal -3
    output = list(filter(lambda x: float(x[-1]) >= -3, output[1:]))
    # question 3 calculating avg
    rows = list(map(lambda x: [float(x[1].replace(",", "")), float(
        x[2].replace(",", "")), float(x[3].replace(",", ""))], output))
    averages = list(map(lambda x: sum(x) / float(len(x)), zip(*rows)))
    with open("avg_output.txt", "w") as f:
        print(str(averages[0]), file=f)
        print(str(averages[1]), file=f)
        print(str(averages[2]), file=f)
    # question 4 displaying stocks starting with a letter
    letter = input("Enter the starting letter: ")
    stock_output = [x for x in output if x[0][0] == letter]
    [print(" ".join(x)) for x in stock_output]
    # question 5 writing the stocks starting with a letter in a file
    with open("stock_output.txt", "w") as f:
        [print(" ".join(x), file=f) for x in stock_output]


if __name__ == "__main__":
    main()
