
import logging
import time



# import sys
# from pathlib import Path
# # Current file's directory
# current_file_path = Path(__file__).resolve()
# # Add the desired path to the system path
# desired_path = current_file_path.parent.parent.parent
# sys.path.append(str(desired_path))
# print(desired_path)

# # Communication methodss
# from ArtusAPI.communication.WiFi.wifi_server import WiFiServer
# from ArtusAPI.communication.UART.uart import UART
# from ArtusAPI.ArtusAPI.communication.can import CAN

from .UART.uart import UART
from .WiFi.wifi_server import WiFiServer

class Communication:
    """
    This communication class contains two communication methods:
        - UART
        - WiFi
    """
    def __init__(self,
                 communication_method='UART',
                 communication_channel_identifier='COM9',logger = None,baudrate = 921600):
        # initialize communication
        self.communication_method = communication_method
        self.communication_channel_identifier = communication_channel_identifier
        self.communicator = None
        self.baudrate = baudrate
        # setup communication
        self._setup_communication()
        # params
        self.command_len = 33
        self.recv_len = 65

        if not logger:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

    
    ################# Communication: _Initialization ##################
    def _setup_communication(self):
        """
        Initialize communication based on the desired method; UART or WiFi
        """
        # setup communication based on the method
        if self.communication_method == 'UART':
            self.communicator = UART(port=self.communication_channel_identifier,baudrate=self.baudrate)
        elif self.communication_method == 'WiFi':
            self.communicator = WiFiServer(target_ssid=self.communication_channel_identifier)
        elif self.communication_method == 'None':
            pass
        else:
            raise ValueError("Unknown communication method")
    
    ################# Communication: Private Methods ##################
    def _list_to_byte_encode(self,package:list) -> bytearray:
        # data to send
        send_data = bytearray(self.command_len+1)

        # append command first
        send_data[0:1] = package[0].to_bytes(1,byteorder='little')

        for i in range(len(package)-1):
            try:
                send_data[i+1:i+2] = int(package[i+1]).to_bytes(1,byteorder='little',signed=True)
            except OverflowError as e:
                send_data[i+1:i+2] = int(package[i+1]).to_bytes(1,byteorder='little',signed=False)


        # set last value to '\n'
        send_data[-1:] = '\0'.encode('ascii')
        
        # print(send_data)
        # return byte array to send
        return send_data
    
    def _byte_to_list_decode(self,package:bytearray) -> tuple:
        recv_data = []
        i = 0
        while i < 65:
            if 17 <= i <= 49: # 16 bit signed integer to int
                recv_data.append(int.from_bytes(package[i:i+2],byteorder='big',signed=True))
                i+=2
            else:   # 8 bit signed integer to int
                recv_data.append(package[i].from_bytes(package[i:i+1],byteorder='little',signed=True))
                i+=1
        
        # extract acknowledge value
        ack = recv_data[0]
        del recv_data[0] # delete 0th value from array

        return ack,recv_data


    ################# Communication: Public Methods ##################
    def open_connection(self):
        """
        start the communication
        """
        try:
            self.communicator.open()
        except Exception as e:
            self.logger.error("unable to connect to Robot")
            print(e)

    def send_data(self, message:list,no_debug=1):
        """
        send message
        """
        try:
            # Test
            self.logger.info(f'data sent to hand {message}')
            if not no_debug:
                print(f'data sent to hand = {message}')
            byte_msg = self._list_to_byte_encode(message)
            self.communicator.send(byte_msg)
            return True
        except Exception as e:
            self.logger.warning("unable to send command")
            print(e)
            pass
        return False

    def receive_data(self) -> list:
        """
        receive message
        """
        byte_msg_recv = None
        try:    
            byte_msg_recv = self.communicator.receive()
            if not byte_msg_recv:
                # self.logger.warning("No data received")
                return None,None
            ack,message_received = self._byte_to_list_decode(byte_msg_recv)
            if ack == 9:
                self.logger.warning("[E] error ack")
            # print(ack)
        except Exception as e:
            self.logger.warning("unable to receive message")
            print(e)
            return None
        return ack,message_received

    def close_connection(self):
        self.communicator.close()


    def wait_for_ack(self):
        start_time = time.perf_counter()
        while 1:
            tmp,rc_csum = self.receive_data()
            if tmp is not None:
                print(f'ack received in {time.perf_counter() - start_time} seconds')
                return 1
            time.sleep(0.001)


##################################################################
############################## TESTS #############################
##################################################################
def test_wifi():
    communication = Communication(communication_method='WiFi', communication_channel_identifier='Artus3D')
    communication.open_connection()

def test_uart():
    communication = Communication(communication_method='UART', communication_channel_identifier='/dev/ttyUSB0')
    communication.open_connection()
    time.sleep(1)
    x = [0]*33
    x[0] = 210
    while True:
        communication.send_data(x)
        i=0
        while i < 6:

            # time.sleep(0.002)
            # print(communication.receive_data()[0])
            if communication.receive_data() is not None:
                i+=1
        time.sleep(0.5)

if __name__ == "__main__":
    # test_wifi()
    test_uart()



    
