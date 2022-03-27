
text = "Smacznej kawusi\ni milego dzionka!\n:D\n"

#with open('notatka.txt','w') as file:       #overwrite last file
with open('notatka.txt','a') as file:        #append text to file
    file.write(text)