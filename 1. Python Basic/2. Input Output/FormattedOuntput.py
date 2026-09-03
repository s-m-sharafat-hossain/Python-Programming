"""Python practice: Python Basic / Input Output / FormattedOuntput. Short example for learning Python."""


# To show value in string we use {} curly braces.
# We can use f before the string to format it. {a:.2f} means to show 2 decimal places.

                    # Formatted output
a = 12.34567
print(f"Formatted value: {a:.2f}")  # Output: 12.35

# You can also use format() method for formatted output
b = 12.34567
print("Formatted value: {:.2f}".format(b))  # Output: 12.35

# Another examples:
name = "Alice"
age = 30
print(f"{name} is {age} years old.")


pi = 3.14159265359
print(f"Pi rounded to 3 decimal places: {pi:.3f}")  


width = 10
height = 5
area = width * height
print(f"Area of rectangle: {area}")
