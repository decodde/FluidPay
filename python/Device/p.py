import socket
import sys
import serial
from flask import Flask, render_template

app = Flask(__name__)

# Define the address and port for the socket connection
HOST = 'localhost'  # Change this to the IP address of the device running the socket server
PORT = 8449

# Create a socket object and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
except socket.error as msg:
    print('Failed to connect to socket: ' + str(msg))
    sys.exit()

# Open the serial port connected to the RFID reader
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change this to the appropriate serial port for your setup

# Define a route to display the RFID tag value
@app.route('/')
def display_rfid():
    # Read the RFID tag value from the serial port
    rfid_value = ser.readline().decode().strip()

    # Send the RFID tag value to the socket server
    sock.sendall(rfid_value.encode())

    # Receive a response from the socket server
    response = sock.recv(1024).decode().strip()

    # Render a template that displays the RFID tag value and the response from the server
    return render_template('rfid.html', rfid_value=rfid_value, response=response)

if __name__ == '__main__':
    app.run(debug=True)
