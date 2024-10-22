from sys import argv

script, file_name = argv

txt = open(file_name) #This opens a file within Python

print(f"Here's your file named '{file_name}':")
print(txt.read()) #This displays the contents of the file
txt.close()

print("Type the file_name again:")
file_again = input("> ") #User gives as input the name of the file

txt_again = open(file_again) #This opens a file within Python

print(txt_again.read()) #This displays the contents of the file
txt_again.close()
