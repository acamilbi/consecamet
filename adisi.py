# Create an empty dictionary
my_dict = {}

# Prompt the user for key-value pairs until they're done
while True:
    key = input("Enter a key (or 'done' to finish): ")
    if key == "done":
        break
    value = input("Enter a value: ")
    my_dict[key] = value
