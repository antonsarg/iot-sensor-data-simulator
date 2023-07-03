import time
import json
from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.hub import IoTHubRegistryManager
import os


class IoTHubHelper:
    # def __init__(self, connection_string):
    #     self.__connection_string = connection_string
    #     self.device_client = None
    #     self.init_device_client()

    def __init__(self):
        self.setup_registry_manager()

    def setup_registry_manager(self):
        connection_string = os.getenv("IOTHUB_CONNECTION_STRING")
        self.registry_manager = IoTHubRegistryManager(connection_string) # throws error: Error in sys.excepthook:

    def get_devices(self):
        return self.registry_manager.get_devices()

    def create_device(self, device_id):
        primary_key = os.getenv("IOTHUB_PRIMARY_KEY")
        secondary_key = os.getenv("IOTHUB_SECONDARY_KEY")
        status = "enabled"
        
        try:
            device = self.registry_manager.create_device_with_sas(device_id, primary_key, secondary_key, status)
            return Response(True, "Device {} erfolgreich erstellt".format(device_id), device)
        except Exception as e:
            return Response(False, "Fehler beim Erstellen: {}".format(e))

    def delete_device(self, device_id):
        try:
            self.registry_manager.delete_device(device_id)
        except Exception as e:
            return Response(False, "Fehler beim Löschen: {}".format(e))
        
        return Response(True, "Device {} erfolgreich gelöscht".format(device_id))


    # def init_device_client(self):
    #     self.device_client = IoTHubDeviceClient.create_from_connection_string(self.__connection_string)
    #     self.device_client.connect()

    # def close_connection(self):
    #     self.__connection_string = None
    #     self.device_client.shutdown()

    # def send_telemetry_messages(self, telemetry_messages):
    #     try:
    #         if not self.device_client:
    #             self.init_device_client()

    #         print("Start sending telemetry messages")
    #         for msg in telemetry_messages:
    #             # Convert the dictionary to JSON string
    #             json_data = json.dumps(msg)

    #             # Build the message with JSON telemetry data
    #             message = Message(json_data)

    #             # Send the message.
    #             print("Sending message: {}".format(message))
    #             self.device_client.send_message(message)
    #         print("Alle Daten erfolgreich gesendet")
    #         return Response(True, "Alle Daten erfolgreich gesendet")
            
    #     except Exception as e:
    #         print(e)
    #         return Response(False, "Fehler beim Senden: {}".format(e))

class Response:
    def __init__(self, success, message="", object=None):
        self.success = success
        self.message = message
        self.object = object