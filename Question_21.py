#Create a function to calculate simple and compound interest.

def calculate_interest(principal, rate, time):
    simple = (principal * rate * time) / 100
    compound = principal * ((1 + rate / 100) ** time) - principal
    return simple, compound

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si, ci = calculate_interest(p, r, t)
print("Simple Interest:", round(si, 2))
print("Compound Interest:", round(ci, 2))
