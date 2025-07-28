# if a string is palindrome or not

def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
print(is_palindrome( "A man a plan a canal panama" )) 
print(is_palindrome( "hello" )) 
