def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Please provide number"  # Or raise TypeError("Both arguments must be int or float")

def subt(a,b):
    return a-b

def neg(a):
    return a*-1

def add_one(a):
    return a+1