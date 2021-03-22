class VehicleControllerI(object):
    """
    Class handling the translation between commands and messages sent to the vehicle
    """

    def set_drive(self, val: int) -> None:
        """
        Changes between high and low gearing(Drive) of the vehicle

        :param val: value to set drive to - may be 0(low) or 1(high)
        """
        raise NotImplementedError

    def set_gear(self, val: int) -> None:
        """
        Tells the vehicle to change into the specified gear.

        NOTE: depending on the vehicle, it may take a while if the gearbox is sequential,
         and there is a big gap between the current and the chosen gear

        :param val: the gear to change to
        """
        raise NotImplementedError

    def set_throttle(self, val: int) -> None:
        """
        Sends the wanted throttle to the vehicle

        :param val: throttle value between 0 and 10 (inclusive), 0 being full stop.
        """
        raise NotImplementedError

    def set_direction(self, val: int) -> None:
        """
        Tels the vehicle which direction is wanted

        :param val: value between 0 and 10 - 0 being left, 5 being forward and 10 being right
        """
        raise NotImplementedError
