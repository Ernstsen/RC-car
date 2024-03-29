[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6e5bb01af8bd4b939eaf68b096ddbc98)](https://app.codacy.com/gh/Ernstsen/RC-car/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
# RC-car

Repository for code used in creating a remote-controlled car. The car is controlled through a python interface, on a
laptop on the same network as the car

# Devices

The project consists of multiple devices, working together. This section will describe the devices and the connection.
The devices are

- [Raspberry Pi Zero](https://thepihut.com/collections/raspberry-pi-kits-and-bundles/products/raspberry-pi-zero-essential-kit)
  with [camera](https://www.raspberrypi.org/products/camera-module-v2/). This will host the interface to the car, and
  supply a video feed from its front.
- [Propeller Activity Board WX](https://www.parallax.com/product/propeller-activity-board-wx/). This octa-core
  microprocessor will be the heart of the car. It will control the DC-motor, lights etc.

## Vehicles

Different vehicle configurations and setups can be created using the repository. As they are created and tested they
will be found in the [wiki](https://github.com/Ernstsen/RC-car/wiki).

# Getting started

A guide for setting up and getting started using this repository can be
found [here](https://github.com/Ernstsen/RC-car/wiki/Setup).

