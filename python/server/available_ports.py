import json
import serial.tools.list_ports



def getPorts():
    ports = serial.tools.list_ports.comports()
    port_list = []
    for port in ports:
        port_dict = {
            'device': port.device,
            'name': port.name,
            'description': port.description,
            'hwid': port.hwid,
            'vid': port.vid,
            'pid': port.pid,
            'serial_number': port.serial_number,
            'location': port.location,
            'manufacturer': port.manufacturer,
            'product': port.product,
            'interface': port.interface,
        }
        port_list.append(port_dict)

    # Convert the list of dictionaries to a JSON formatted string
    port_json = json.dumps(port_list)
    #print(port_json)
    return port_json   