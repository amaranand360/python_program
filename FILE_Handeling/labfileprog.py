# print("circle")
# r =float(input("Enter radious of circle r= "))
# print("Parimeater of circle is = ",2*3.14*r)
# print("Area of the circle is = ",3.14*r*r)
# print("Cylinder")
# h =float(input("Enter hieght of Cylinder h= "))
# print("lateral surface area of cylinder = ",2*3.14*r*h);
# print("Volume of Cylinder = ",3.14*r*r*h)
# print("Sphere")
# print("Volume of sphere = ",4/3*3.14*r*r*r)


# Open the file in read mode
with open('file.txt', 'r') as file:
  # Read the contents of the file into a list
  lines = file.readlines()
 
  # Count the number of lines in the file
  line_count = len(lines)
 
  # Initialize a variable to store the longest word
  longest_word = ''
 
  # Iterate through each line in the list
  for line in lines:
    # Split the line into a list of words
    words = line.split()
    # Iterate through each word in the list
    for word in words:
      # If the current word is longer than the longest word, update the longest word
      if len(word) > len(longest_word):
        longest_word = word
 
  # Print the number of lines and the longest word
  print(f'Number of lines: {line_count}')
  print(f'Longest word: {longest_word}')