# Updated task_02_room_calc.py

# Function to calculate the area and perimeter of a room based on user input

def calculate_room():
    length = float(input('Enter the length of the room: '))
    width = float(input('Enter the width of the room: '))
    area = length * width
    perimeter = 2 * (length + width)

    print(f'The area of the room is: {area}')
    print(f'The perimeter of the room is: {perimeter}')

# Main function
if __name__ == '__main__':
    calculate_room()