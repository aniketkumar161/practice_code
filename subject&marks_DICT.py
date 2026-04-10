# Start with an empty dictionary
marks = {}

# Taking input from user and updating dictionary
sub1 = input("Enter first subject name: ")
m1 = int(input(f"Enter marks for {sub1}: "))
marks.update({sub1: m1})

sub2 = input("Enter second subject name: ")
m2 = int(input(f"Enter marks for {sub2}: "))
marks.update({sub2: m2})

sub3 = input("Enter third subject name: ")
m3 = int(input(f"Enter marks for {sub3}: "))
marks.update({sub3: m3})

# Display the dictionary
print("\nStudent Marks Dictionary:")
print(marks)
