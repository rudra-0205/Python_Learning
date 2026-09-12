# Validating either an input password is of 8 characters

def is_valid_password(password):
    return len(password) >= 8

print (is_valid_password("password123"))
print (is_valid_password("pass"))