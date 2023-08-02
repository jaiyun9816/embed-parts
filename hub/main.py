from base.execution_engine import ExecutionEngine

from rx import create
from multiprocessing import Pool

if __name__ == "__main__":  
    #drone = Drone('192.168.10.1', 8889)
    #local = Local('', 8890)
    
    engine = ExecutionEngine(1)
    engine.append_bootloader("HUB_CONNECT", "./bootloader/hub_connect.simx")
    engine.append_bootloader("SEND_TELLO", "./bootloader/tello.simx")
    
    engine.state = "HUB_CONNECT"
    
    #engine.set_agent_source(drone.get_source())
    #engine.set_env_source(local.get_source())
    
    engine.run_boot_loader()
        
    for i in range(3) :
        engine.run_multi_parts()
    