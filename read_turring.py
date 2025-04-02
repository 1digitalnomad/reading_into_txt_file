# open the file as read only and assign it to a variable
file = open("emhill.github.io_150_morea_10.dict__data_turing.txt", "r")

# set up an array to include each line in the text file in it
lines = []
# count how many lines are in the text file
count = 0
# loop through each line and add each line into the array. Also count each line
for line in file:
    lines.append(line.rstrip())
    count += 1

# print the first and last two lines
print(lines[0:1], lines[-2:])
print(count)

# close the file
file.close()
