from functools import reduce
import glob


numbers_in_files = list()
for txt_file in glob.glob("*.txt"):
    with open(txt_file) as file:
        numbers_in_file = [int(line) for line in file.readlines()]
    numbers_in_files.append(numbers_in_file)

# result = [x for x in [set(numbers_in_files[0]).intersection(x) for x in numbers_in_files[1:]][-1]]
# result = [set(numbers_in_files[0]).intersection(x) for x in numbers_in_files[1:]]

result = reduce(lambda a,b: list(set(a).intersection(set(b))), numbers_in_files)

print(result)