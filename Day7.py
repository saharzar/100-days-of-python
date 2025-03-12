def calculate_area(length, width):
    area = length * width
    return area
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the Rectangle Area Calculator!")

    length = get_float_input("Enter the length of the rectangle: ")
    width = get_float_input("Enter the width of the rectangle: ")

    area = calculate_area(length, width)

    print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")

    while True:
        repeat = input("Do you want to calculate the area of another rectangle? (yes/no): ").lower()
        if repeat == 'yes':
            main()
            break
        elif repeat == 'no':
            print("Thank you for using the Rectangle Area Calculator!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
