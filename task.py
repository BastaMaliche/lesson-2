myFavFruits = int(input("pila kabook akong fav fruits:"))
namesOfMyFavFruits = []

for i in range(myFavFruits):
    fruits = input("Enter Fruits:")
    namesOfMyFavFruits.append(fruits)

print(namesOfMyFavFruits)

for data in namesOfMyFavFruits:
    if data == "banana":
        break
    elif data == "apple":
        print("happy eating")