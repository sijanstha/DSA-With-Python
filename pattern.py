
result = ""
n = 3
i = n
while i >= 1:
    j = n
    while j >= 1:
        for k in range(i):
            result += str(j) + " "
        j = j - 1
    result += "\n"
    i = i - 1
print(result)
