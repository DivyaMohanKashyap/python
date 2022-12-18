"""Numbers
"""
x1 = "Hello World"                                      #str
x1_multiline = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""                    #multiline-string
x2 = 20                                                 #int
x3 = 20.5                                               #float
x4 = 1j                                                 #complex
"""Collections
    # List
    # Tuples
    # Range
    # Dictionary
    # Set
    # FrozenSet
"""
x5 = ["apple", "banana", "cherry"]	                    #list	
x6 = ("apple", "banana", "cherry")	                    #tuple
x7 = range(6)                                           #range
x8 = {"name" : "John", "age" : 36}	                    #dict
x9 = {"apple", "banana", "cherry"}	                    #set
x1_1 = frozenset({"apple", "banana", "cherry"})         #frozenset

"""Other
"""
x1_2 = True                                             #bool
x1_3 = b"Hello"                                         #bytes
x1_4 = bytearray(5)                                     #bytearray
x1_5 = memoryview(bytes(5))                             #memoryview
x1_6 = None                                             #None

"""TypeCastings
# Int
# Float
# Str
"""

tc_int = int("12") 
tc_str = str(12)
tc_float = float(123)

print(f"\n\n\ntc_int : ({type(tc_int)}) {tc_int} \ntc_float : ({type(tc_float)}) {tc_float} \ntc_str : ({type(tc_str)}) {tc_str}")
