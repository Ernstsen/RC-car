import argparse
from typing import Dict, List, Tuple, Callable

try:
    from Controller.gui.application_gui import GUI
    from Controller.gui.model import MiscControlSpec
    from Controller.vehicle_control import VehicleController
    from Controller.video import VideoStreamReceiver
except ModuleNotFoundError:
    from gui.application_gui import GUI
    from gui.model import MiscControlSpec
    from vehicle_control import VehicleController
    from video import VideoStreamReceiver


def default_vehicle_config(controller: VehicleController) -> Tuple[Dict[str, bool], List[MiscControlSpec]]:
    """
    Fallback configuration. Everything is disabled

    :param controller: the controller used in communicating with the vehicle
    :return: configuration for std vehicle, empty misc map
    """
    return {}, []


def mini_car_config(controller: VehicleController) -> Tuple[Dict[str, bool], List[MiscControlSpec]]:
    """
    Generates and outputs configuration map
    :param controller: the controller used in communicating with the vehicle
    :return: configuration for MiniCar, Misc map
    """
    mini_enabled = {
        "misc": True,
        "throttle": True,
        "direction": True
    }

    mini_misc = [
        MiscControlSpec("lights", lambda v: controller.set_lights((1 if v else 0)), param_type=bool, row=0, column=0,
                        description="Toggles lights on vehicle")
    ]

    return mini_enabled, mini_misc


if __name__ == "__main__":
    configuration_builders: Dict[str, Callable[[VehicleController], Tuple[Dict[str, bool], List[MiscControlSpec]]]] = {
        "Fallback": default_vehicle_config,
        "MiniCar": mini_car_config
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("-config", dest="config", default="Fallback", type=str)
    parser.add_argument("-vehicleAddress", dest="vehicle_address", default="192.168.0.105", type=str)
    parser.add_argument("-vehiclePort", dest="vehicle_port", default=8080, type=int)
    parser.add_argument("-streamPort", dest="stream_port", default=8000, type=int)

    args = parser.parse_args()

    if args.config in configuration_builders:
        vehicle_controller: VehicleController = VehicleController(args.vehicle_address, args.vehicle_port)

        enabled, misc = configuration_builders[args.config](vehicle_controller)

        streamer = VideoStreamReceiver(args.stream_port)
        gui = GUI(viewer=streamer, controller=vehicle_controller, enabled=enabled, misc_controls=misc)

        vehicle_controller.start_stream()
        gui.mainloop()
    else:
        print("Configuration '" + args.config + "' not found. Options are: " + ", ".join(
            list(configuration_builders.keys())))
