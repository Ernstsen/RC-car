# Vehicle

This document will contain information about using this package to control the remote controlled vehicle.

## Camera

The code in the ``cam`` package attempts to import the ``picamera`` package, and will not work if it is not present. It
will, however, not crash if it is not present. This is to be able to test code using one or more files from the package
in a testing environment on a non-RPI computer.

## Configuration 
The configuration of the instance happens in the file ``vehicle_application.py``

## Commands

The supported commands can be split into two categories *stream* and *controls*

### Stream

* **STREAM-INITIALIZE(address: *str*, port: *int* )** Initializes video stream, aimed at server on *address:port*
* **STREAM-SERVE-FOOTAGE( )** Starts serving footage - *STREAM-INITIALIZE* must be called first
* **STREAM-STOP-STREAMING( )** Stops serving of footage
* **STREAM-TERMINATE( )** Terminates streaming connection. *STREAM-INITIALIZE* must be called, before being able to
  serve stream again

### Controls
Emulates the interface of the ``Controller`` class
* **DRIVE(val: *int*)** sets drive - may be 0(low) or 1(high)
* **GEAR(val: *int*)** sets gear
* **THROTTLE(val: *int*)** sets throttle - throttle value between 0 and 10 (inclusive), 0 being full stop.
* **DIRECTION(val: *int*)** sets direction value between 0 and 10 - 0 being left, 5 being forward and 10 being right