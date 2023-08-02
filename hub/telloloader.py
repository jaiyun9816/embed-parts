from base.bootloader import BootLoader
import dill

class TelloLoader(BootLoader):
    def __init__(self):
        super().__init__()
        self.state = "TELLO"
        self.parts = ["flip.simx", "land.simx", "takeoff.simx"]


if __name__ == "__main__":
    loader = TelloLoader()
    with open("./bootloader/tello.simx", "wb") as f:
        dill.dump(loader, f)
