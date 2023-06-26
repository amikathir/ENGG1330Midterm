# Amaresh Kathiresan ENGG1330 Midterm Program 5 UID: 3035962556
input_list = input("Input sentence: ").lower().split()
input_list_length = len(input_list)
input_list_unique = []
frequency_list = []
highest = 0

for x in range(input_list_length):
    string = ""
    word = input_list[x]
    for y in word:
        if y.isalpha():
            string = string + y
    input_list[x] = string

for i in range(0, input_list_length):
    for j in range(i + 1, input_list_length):
        if input_list[i] > input_list[j]:
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp

for item in input_list:
    if item not in input_list_unique:
        input_list_unique.append(item)

for item3 in input_list_unique:
    frequency_list.append([item3, 0])

for item1 in frequency_list:
    for item2 in input_list:
        if item1[0] == item2:
            item1[1] += 1
            if item1[1] > highest:
                highest = item1[1]

print("Frequency: ", end = "")
print(frequency_list)
for item4 in frequency_list:
    if item4[1] == highest:
        print("{:<15}".format(item4[0]), end = "")
        print("{:>3}".format(str(item4[1])))
