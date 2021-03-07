# Vehicle Control

This package implements methods of controlling the vehicle, to be specified in the ``GUI`` constructor

## Controller interface

The ``Controller`` class specifies the interface to be used in communicating with the vehicle, using the following
functions

* ``set_drive``
* ``set_gear``
* ``set_throttle``
* ``set_direction``

There are two standard implementations

### ControllerSimulator

This implementation simulates controlling a vehicle, by keeping and updating an internal state

### VehicleController

This implementation sends commands through a socket connection to the vehicle, thus controlling the actual vehicle