from base.parts_model import PartsModel
import dill
import socket

class TakeoffModel(PartsModel):
    def __init__(self):
        super().__init__()

        
    def run_parts(self):      
        print("flip", self.agent)
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.environment['local_ip', self.environment['local_posrt']])##(ip, part)
        
        tello_address = (self.agent['drone_ip'], self.agent['drone_port'])
        self.socket.sendto('takeoff'.encode('utf-8'), tello_address)
        
        
if __name__ == "__main__":
    loader = TakeoffModel()
    with open("./partsmodel/takeoff.simx", "wb") as f:
        dill.dump(loader, f)

##agent : drone ip, drone port,  local ip, local port, 