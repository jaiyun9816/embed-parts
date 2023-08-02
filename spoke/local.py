from base.environment_manage import EnvironmentManagement


class Local(EnvironmentManagement):
    def __init__(self, local_ip, local_port):
        super().__init__()
        self.agent = {"local_ip": local_ip, "local_port" : local_port}

##agent : drone ip, drone port, 
# environment : local ip, local port, 