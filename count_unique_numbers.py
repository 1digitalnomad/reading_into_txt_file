# raul duenez
# write a function that takes a string of sorted numbers as parameters and returns the numbrer of unique numbers using a dictionary

d = {}

# count the unique numbers and add them to the dictionary


def count_unique(str):
    for i in str:
        if i not in d:
            d[i] = 1

    return len(d)


def main():
    print(count_unique("1112234446") == 5)
    print(d)
    # print(count_unique("7789") == 3)
    # print(count_unique("10002") == 3)


main()
