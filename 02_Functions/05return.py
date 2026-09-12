def add (a, b):
    print (a+b)

result = add (19, 89)
print (result)
 # this gave a none output because the function add does not return any value,
 # it only prints the sum of a and b.
 # To fix this, you can modify the function to return the sum instead of printing it:

def add (a, b):
    return a + b  

result = add (19, 89)
print (result)  # This will now print 108, which is the sum of  19 and 89.
