import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
i = 1

for port in ports:
    portsList.append(port.device)
    print(f"{i}: {port.device} - {port.description} (Manufacturer: {port.manufacturer})")
    i += 1

val = input("Select Port: ")

portVar = portsList[int(val) - 1]

print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

print("Type messages below. Type 'exit' to close the console")

while True:
    msg = input("> ")
    if msg.lower() == 'exit':
        break
    serialInst.write(msg.encode())
    message = serialInst.readline().decode('ascii').strip()
    print("ESP32: " + message)

serialInst.close()
print("Connection Closed")