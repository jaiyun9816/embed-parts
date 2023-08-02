from base.parts_model import PartsModel
import dill
import socket

class FlipModel(PartsModel):
    def __init__(self):
        super().__init__()

        
    def run_parts(self):      
        print("flip", self.agent)
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.environment['local_ip', self.environment['local_posrt']])##(ip, part)
        
        tello_address = (self.agent['drone_ip'], self.agent['drone_port'])
        self.socket.sendto('flip'.encode('utf-8'), tello_address)
        
        
if __name__ == "__main__":
    loader = FlipModel()
    with open("./partsmodel/flip.simx", "wb") as f:
        dill.dump(loader, f)
