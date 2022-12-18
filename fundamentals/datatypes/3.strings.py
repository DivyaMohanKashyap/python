print('\n\n\n\n')
x1 = "Hello World"                                      #str
x1_multiline = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""                    #multiline-string

print(f"X1 : {x1}")
# print(f"X1 Multiple Lines : \n{x1_multiline}")

"""Strings are Arrays
    # Getting String By Index
    # Looping through string
    # String Slicing
"""

a = "Hello Divye"
print(f"Variable a 1st index: {a[6]}")

for x in a:
    print(f"String at current position : {x}")

print(f"String length : {len(a)}")

"""
    1. Check if substring exist
    2. Check if substring does not exist 
"""

print('Divye' in a)
print('DIVYE' not in a)

print('\n\n\n')

""" 
    1. Slicing String
    2. Changing String Case (Upper, Lower, Strip - Camel case)
    3. Replacing Substring
    4. Splitting (Converting String to List)
    5. Concatenation
    6. Formatting & Char Escaping String 
"""

sliceString = "Culpa ex eu incididunt amet velit et sit id labore.";

print(f"Slicing String : {sliceString[2:19]}")
print(f"Slicing String : {sliceString[:19]}")
print(f"Slicing String : {sliceString[2:]}")
print(f"Slicing String : {sliceString[:]}")
print(f"Slicing String : {sliceString[-10:-2]}")
print(f"Slicing String : {sliceString[-10:]}")
print(f"Slicing String : {sliceString[:-2]}")
print('\n')
# Modifying

modifyString = "Nulla eu sint ex veniam proident ut dolor ad.";

# Changing String Cases
print(f"Modifying String : {modifyString.upper()}")
print(f"Modifying String : {modifyString.lower()}")
print(f"Modifying String : {modifyString.strip()}")
print('\n')
# Replace substring
print(f"Replacing Substring : {modifyString.replace('Nulla', 'Bulla')}")
print('\n')
# Splitting string to list
print(f"String to List Conversion : {type(modifyString.split(','))} {modifyString.split(',')} ")
print('\n')
# Concatenating String
substring = "Cupidatat magna amet Lorem nisi veniam."
paragraph = modifyString + " " + substring
print(f"Concatenation : {paragraph}")
print('\n')

# Formatting & Char Escaping
substr1 = "Divye Mohan"
substr2 = "Senior Software \"Engineer - Full Stack\""
substr3 = "Kashyap"
string = "Hi I am {0} and my surname is {2}. I am a {1}"
print(string.format(substr1, substr2, substr3))