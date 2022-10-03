list = ["apple", "banana", "coconut"]
print (list)
fruit_basket = ["apple", "banana", "mango"]

for word in fruit_basket:
    if word not in list:
        list.append(word)

print (list)