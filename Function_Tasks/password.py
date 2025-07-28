# password strength checker

def is_strong_password(password):
    """ This function check weather a password is strong or not"""
    if len(password)< 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False 
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True
# calling the function
print(is_strong_password("WeakPassword"))   
print(is_strong_password("Str0ngPassword!"))