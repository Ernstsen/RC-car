from Controller.gui.application_gui import GUI
from Controller.vehicle_control import VehicleController

if __name__ == "__main__":
    controller: VehicleController = VehicleController("127.0.0.1", 8080)

    gui = GUI(controller=controller)
    gui.mainloop()
