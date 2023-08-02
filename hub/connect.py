from base.bootloader import BootLoader
import dill

class HubConnectLoader(BootLoader):
    def __init__(self):
        super().__init__()
        self.state = "CONNECT"
        self.parts = ["hub.simx"]


if __name__ == "__main__":
    loader = HubConnectLoader()
    with open("./bootloader/hub_connect.simx", "wb") as f:
        dill.dump(loader, f)
