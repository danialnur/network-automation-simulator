from netmiko import ConnectHandler
import time

def send_config(device, commands):
    try:
        print(f"Connecting to {device['device_name']}...")
        connection = ConnectHandler(
            device_type=device['device_type'],
            host=device['ip'],
            username=device['username'],
            password=device['password']
        )
        connection.enable()
        output = connection.send_config_from_file(commands)
        connection.disconnect()
        return output
    except Exception as e:
        return f"Error connecting to {device['ip']}: {e}"
