# Template to read and process the file
import os 
def read_file(file_path):
    """
    Reads a file containing pairs of numbers and processes them.
    
    Args:
        file_path (str): The path to the file.
        
    Returns:
        list of tuple: A list of tuples where each tuple contains a pair of integers.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and split the line into two numbers
                parts = line.strip().split()
                print(parts)
                if len(parts) == 2:  # Ensure the line has exactly two numbers
                    try:
                        num1, num2 = int(parts[0]), int(parts[1])
                        data.append((num1, num2))
                    except ValueError:
                        print(f"Skipping line due to non-integer values: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

if __name__ == "__main__":
    # Replace 'input.txt' with the actual path to your file
    file_path = "C:\\Users\\trung\\OneDrive\\Skrivbord\\Edvent of code\\Day_1\\input.txt"
    
    number_pairs = read_file(file_path)
    
    # Example: Print the first 10 pairs
    print("First 10 number pairs:", number_pairs[:10])
    
    # Add your custom processing logic here
