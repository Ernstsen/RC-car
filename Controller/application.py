from typing import Dict, List, Tuple

from Controller.gui.application_gui import GUI
from Controller.gui.model import MiscControlSpec
from Controller.vehicle_control import VehicleController
from Controller.video import VideoStreamReceiver


def mini_car_config(controller: VehicleController) -> Tuple[Dict[str, bool], List[MiscControlSpec]]:
    """
    Generates and outputs configuration map

    :return: configuration for MiniCar, Misc map
    """
    enabled = {
        "misc": True,
        "throttle": True,
        "direction": True
    }

    misc = [
        MiscControlSpec("lights", lambda v: controller.set_lights((1 if v else 0)), param_type=bool, row=0, column=0,
                        description="Toggles lights on vehicle")
    ]

    return enabled, misc


if __name__ == "__main__":
    vehicle_controller: VehicleController = VehicleController("127.0.0.1", 8080)

    mini_enabled, mini_misc = mini_car_config(vehicle_controller)

    streamer = VideoStreamReceiver(8000)
    gui = GUI(viewer=streamer, controller=vehicle_controller, enabled=mini_enabled, misc_controls=mini_misc)

    vehicle_controller.start_stream()
    gui.mainloop()
