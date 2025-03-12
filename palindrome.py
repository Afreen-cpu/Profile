
print("Afreen - 03")
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]
result = is_palindrome("A people")
print(result)
  
