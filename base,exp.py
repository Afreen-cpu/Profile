print("Afreen - 03")
def power(base, exp):
    result = 1
    for _ in range(abs(exp)):
        result *= base
    if exp < 0:
        return 1 / result
    return result
base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))


print(f"{base} raised to the power of {exp} is {power(base, exp)}")
