
str="acceleratron"
#making list

str1=""
res=list(str)
#print(res)
'''for x in range(len(res)):
    if res[x] == "a":
        res[x] = "i"
        str1 += res[x]
    else:
        str1 += res[x]

print(str1)'''


#without making list
for y in range(len(str)):
    if str[y] == "a":
        str1 += "i"
    else:
        str1 += str[y]
print(str1)

'''for character in str:
    if character == "a":
        str1 += "i"
    else:
        str1 += character

print(str1)'''


