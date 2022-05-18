# Conditional Execution

hrs = input("Enter hours? ")

hrs = input("Enter Hours:")
h = float(hrs)
RR = input("Enter the rate")
x = float(RR)
if h <= 40:
   print(h * x)
    elif h > 40:
   print(40*x + (h-40)*1.5*x)