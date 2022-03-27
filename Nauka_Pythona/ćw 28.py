#str.format()


animal = "cow"
item = "moon"

#print("The " + animal + " jumped over the " + item)
#print("The {} jumped over the {}".format("cow", "moon"))
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))    #positional arguments
print("The {animal} jumped over the {item}".format(animal= "cow", item= "moon"))    #keyword argument
print("The {item} jumped over the {animal}".format(animal= "cow", item= "moon"))    #keyword argument reverse

text = "The {} jumped over the {}"
print(text.format(animal,item))