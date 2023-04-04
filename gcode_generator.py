import math

# Function to generate G-code for a square
def generate_square_gcode(length, feed_rate):
    gcode = "G1 F" + str(feed_rate) + "\n"
    gcode += "G1 X" + str(length) + " Y0\n"
    gcode += "G1 X" + str(length) + " Y" + str(length) + "\n"
    gcode += "G1 X0 Y" + str(length) + "\n"
    gcode += "G1 X0 Y0\n"
    return gcode

# Function to generate G-code for a circle
def generate_circle_gcode(radius, feed_rate):
    gcode = "G1 F" + str(feed_rate) + "\n"
    num_segments = 20
    for i in range(num_segments):
        angle = i * 2 * math.pi / num_segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        gcode += "G1 X" + str(x) + " Y" + str(y) + "\n"
    return gcode

# # Ask user to select a design
# print("Select a design:")
# print("1. Square")
# print("2. Circle")
# choice = int(input("Enter your choice (1 or 2): "))

# # Generate G-code based on user's choice
# if choice == 1:
#     length = float(input("Enter the length of the square: "))
#     feed_rate = float(input("Enter the feed rate: "))
#     gcode = generate_square_gcode(length, feed_rate)
# elif choice == 2:
#     radius = float(input("Enter the radius of the circle: "))
#     feed_rate = float(input("Enter the feed rate: "))
#     gcode = generate_circle_gcode(radius, feed_rate)
# else:
#     print("Invalid choice")

# # Write G-code to file
# filename = input("Enter the filename to save the G-code: ")
# with open(filename, "w") as f:
#     f.write(gcode)

# print("G-code saved to", filename)
