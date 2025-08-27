#write_to_a_file.py
# Program to write a line of text to a file
f = open("initial_file.txt", "w")  # Open file in write mode
f.write("Hey there, this is Vikky!\n")  # Write a line to the file
f.write("Enjoy your day!\n")  # Write another line to the file
f.write("stay tuned for more updates.\n")  # Write another line to the file
f.close()  # Close the file
print("successfully written to a file.")
