a, b, c = (input().split(" "))
a, b, c = int(a), int(b), int(c)

number_list = [a, b, c]
number_list = [int(x) for x in number_list]
number_list.sort()

print(number_list[0])
print(number_list[1])
print(number_list[2])
print()
print(a)
print(b)
print(c)
