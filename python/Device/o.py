import socket
import sys
import serial

class RFIDServer:
    def __init__(self, host, port, serial_port, baud_rate):
        self.host = host
        self.port = port
        self.baud_rate = baud_rate
        self.serial_port = serial_port
        self.sock = None
        self.ser = None

    def start(self):
        # Create a socket object and bind it to the address and port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((self.host, self.port))
        except socket.error as msg:
            print('Failed to bind socket: ' + str(msg))
            sys.exit()

        # Listen for incoming connections
        self.sock.listen(1)

        # Open the serial port connected to the RFID reader
        self.ser = serial.Serial(self.serial_port, self.baud_rate)

        # Loop indefinitely, waiting for incoming connections
        while True:
            # Accept a new connection
            conn, addr = self.sock.accept()
            print('Connected by', addr)

            # Loop indefinitely, reading data from the connection
            while True:
                # Read data from the connection
                data = conn.recv(1024).decode().strip()
                if not data:
                    break

                # Read the RFID tag value from the serial port
                rfid_value = self.ser.readline().decode().strip()

                # Process the data and generate a response
                response = self.process_data(rfid_value)

                # Send the response back to the client
                conn.sendall(response.encode())

            # Close the connection
            conn.close()

    def stop(self):
        if self.sock is not None:
            self.sock.close()

        if self.ser is not None:
            self.ser.close()

    def process_data(self, data):
        # Do something with the data (e.g. lookup in a database)
        response = 'Processed data: ' + data

        # Return the response
        return response