import tkinter as tk
from tkinter import messagebox


def gcd_two_numbers(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two positive integers.

    Args:
        a: The first positive integer.
        b: The second positive integer.

    Returns:
        The GCD of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a


def lcm_two_numbers(a: int, b: int) -> int:
    """
    Calculates the least common multiple (LCM) of two positive integers.

    Args:
        a: The first positive integer.
        b: The second positive integer.

    Returns:
        The LCM of the two numbers.
    """
    return (a * b) // gcd_two_numbers(a, b)


def gcd_and_lcm(numbers: list) -> tuple:
    """
    Calculates the greatest common divisor (GCD) and the least common multiple (LCM) of a list of positive integers.

    Args:
        numbers: A list of positive integers.

    Returns:
        A tuple containing the GCD and LCM of the list of numbers.
    """
    if not numbers:
        raise ValueError("Empty list provided. Please provide at least one positive integer.")

    gcd = numbers[0]
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        gcd = gcd_two_numbers(gcd, numbers[i])
        lcm = lcm_two_numbers(lcm, numbers[i])

    return gcd, lcm


def calculate_gcd_and_lcm():
    try:
        numbers = [int(num_entry.get()) for num_entry in num_entries if num_entry.get()]
        if not numbers:
            raise ValueError("No valid numbers provided. Please enter at least one positive integer.")
        
        result_text = ""
        if gcd_var.get():
            gcd = gcd_and_lcm(numbers)[0]
            result_text += f"GCD: {gcd}\n"
        if lcm_var.get():
            lcm = gcd_and_lcm(numbers)[1]
            result_text += f"LCM: {lcm}\n"
        if not result_text:
            result_text = "No calculations selected"
        
        result_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def add_number_entry():
    entry = tk.Entry(root, width=10, font=("Arial", 14))
    entry.grid(row=len(num_entries) + 1, column=1, padx=10, pady=10)
    num_entries.append(entry)


def validate_positive_integer(value):
    if not value.isdigit() or int(value) <= 0:
        return False
    return True


root = tk.Tk()
root.title("GCD and LCM Calculator")
root.geometry("400x400")
root.config(bg="white")

# Number of entries
num_count_label = tk.Label(root, text="Number of Integers:", font=("Arial", 16), bg="white")
num_count_label.grid(row=0, column=0, padx=10, pady=10)

num_entries = []

# Add number entry fields dynamically
add_number_entry_btn = tk.Button(root, text="Add Number", command=add_number_entry, font=("Arial", 14))
add_number_entry_btn.grid(row=0, column=1, padx=10, pady=10)

# Result frame
result_frame = tk.Frame(root, bg="white", bd=2, relief=tk.SOLID)
result_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.S)

# Checkbuttons for selecting calculations
gcd_var = tk.BooleanVar()
gcd_checkbutton = tk.Checkbutton(result_frame, text="GCD", variable=gcd_var, font=("Arial", 14), bg="white")
gcd_checkbutton.pack(anchor=tk.W)

lcm_var = tk.BooleanVar()
lcm_checkbutton = tk.Checkbutton(result_frame, text="LCM", variable=lcm_var, font=("Arial", 14), bg="white")
lcm_checkbutton.pack(anchor=tk.W)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate GCD and LCM", command=calculate_gcd_and_lcm, font=("Arial", 16), bg="white")
calculate_btn.grid(row=0, column=2, padx=10, pady=10, sticky=tk.N)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.S)

# Validate positive integers
validate_positive_integer_cmd = root.register(validate_positive_integer)

for i in range(1):
    entry = tk.Entry(root, width=10, font=("Arial", 14), validate="key",
                     validatecommand=(validate_positive_integer_cmd, "%P"))
    entry.grid(row=i+1, column=1, padx=10, pady=10)
    num_entries.append(entry)

root.mainloop()
