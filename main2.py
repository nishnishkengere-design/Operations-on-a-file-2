# open a file and split the file into words
with open("sample_doc.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.spllit()
        print(word)

#  close the file
file.close()              