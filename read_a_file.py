#read_a_file.py
# Program to read and display the content of a file
f = open("initial_file.txt", "r")  # Open file in read mode
info = f.read()  # Read the content of the file 
print(info)  # Print the content to the console
f.close()  # Close the file