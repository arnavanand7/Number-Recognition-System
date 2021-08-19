list = []

csv_file=open("mnist_train.csv", "r")
for line in csv_file:
        line = line.split(",",0)
        list.append("".join(line))

text_file=open("mnist_train.txt", "w")
for line in list:
        text_file.write(line)
        text_file.write("\n")

list2 = []

csv_file2=open("mnist_test.csv", "r")
for line in csv_file2:
        line = line.split(",",0)
        list2.append("".join(line))

text_file2=open("mnist_test.txt", "w")
for line in list2:
        text_file2.write(line)
        text_file2.write("\n")

