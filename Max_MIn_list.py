# Create an empty list to store numbers
numbers = []

# Loop to take user input
while True:
    x = input("Enter an integer or type 'done' to quit: ").strip().lower()
    
    if x == "done":
        break  # Exit loop when the user types "done"

    try:
        num = int(x)  # Convert input to integer
        numbers.append(num)  # Add to the list
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Display results
if numbers:  # Check if list is not empty
    print("Maximum number:", max(numbers))
    print("Minimum number:", min(numbers))
else:
    print("No numbers were entered.")
