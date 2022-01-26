#list - storage items in a single variable

food = ["pizza", "burger", "hot dog", "spaghetti"]
#print(food[0])

food[0] = "sushi"
#print(food[0])

food.append("ice cream")
food.remove("burger")
#food.pop()
food.insert(0, "cake")
food.sort()
#food.clear()   erase all elements of list

for i in food:
    print(i)

