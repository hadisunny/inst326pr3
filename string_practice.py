

import os

files_here = os.listdir()
print(files_here)

"file.txt".endswith(".txt") #true
"README.md".endswith(".txt") #false 

for file in files_here:
    print(f"lets check if {file} is a TXT file" )
    if file.endswith(".txt"):
        print(f"here are the first 100 bytes of the file {file}")
        with open(file) as file_connection:
            print(file_connection.read(100))



waitress_lines = [] #list of lines w word 
with open("spam_song.txt", "r") as file_connection: 
    for line in file_connection: #line is string 
        if line.startswith("Waitress"):
            waitress_lines.append(line)

print(waitress_lines)

print("\n".join(waitress_lines))


my_courses = ["inst126","inst314", "462"]

course_numbers= []
for course in my_courses:
    course_number = course.removeprefix("inst")
    course_numbers.append(course_number)
print(course_numbers)


#removes same way, for the end of a string 
print("filename.txt".removesuffix(".txt"))


print("\u2660")