# Importing common libraries for networking and camera
import socket
import os
from time import sleep
import struct
from picamera import PiCamera
from gpiozero import Servo, AngularServo

# Init message and setup servos
print("Start!")
servo_latch = Servo("GPIO24")
servo_rotate = AngularServo("GPIO23", min_angle=0, max_angle=180, min_pulse_width = 0.0005, max_pulse_width = 0.0024)

# Constant private address of the host server to run the ML eval
address = "### ENTER SERVER ADDRESS HERE ###"

# Port the socket will bind to (also the same as minecraft port cause why not)
port = 25565
sock = socket.socket()
print("Trying to connect...")
sock.connect((address, port))
camera = PiCamera()

# Simple capture function that captures camera and fetches data from the server
def capture():
        # Delete old picture (if any), capture, and open file
        os.remove("./image.jpg")
        print("Capturing camera...")
        camera.capture('./image.jpg')
        image = "./image.jpg"
        file = open(image, mode="br",)
        print("Captured!")

        # Send the file size first
        filesize = os.path.getsize(image)
        sock.send(struct.pack("<Q", filesize))

        # Then send each individual chunk (1024 bytes = 1 chunk)
        print("Checking file: " + image)
        while read_bytes := file.read(1024):
                sock.sendall(read_bytes)

        # Read back result from server and return color and confidence
        sizeBytes = sock.recv(struct.calcsize("<Qf"))
        val = struct.unpack("<Qf", sizeBytes)
        return val[0], val[1]

while True:
        sleep(1.5)
        (result, confi) = capture()

        # Const array of the colors and relative servo positions
        unique_colours = ['blue','green','red','yellow']

        # Servo position values for each contrainer. Trial and error was used to figure these out 
        color_positions = [-0.6, -0.13, 0.6, 1]

        # Select based on given color index
        chosen_color = unique_colours[int(result)]
        angle_slant = color_positions[int(result)]

        # Call the Servos' API to rotate and open latch temporarily
        print("Predicted color: " + chosen_color + " with " + str(confi*100) + "%% confidence")
        servo_rotate.value=(angle_slant)
        sleep(0.5)
        servo_latch.max()
        sleep(0.5)
        servo_latch.min()
        sleep(0.5)