from base.agent_manage import AgentManagement


class Drone(AgentManagement):
    def __init__(self, drone_ip, drone_port):
        super().__init__()
        self.agent = {"drone_ip": drone_ip, "drone_port": drone_port}

##agent : drone ip, drone port, 
# environment : local ip, local port, 