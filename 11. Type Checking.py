# 11. Type Checking
value = input("Enter a value: ")
try:
    val = eval(value)
    print(f"Type: {type(val)}")
except:
    print("Type: String")
