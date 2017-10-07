import string 

# s = "hello, ? ; "




with open('trainC.txt', 'r') as myfile:
    data=myfile.read()

s = data.translate(None, string.punctuation)

# print s

text_file = open("final_train.txt", "w")
text_file.write(s)
text_file.close()