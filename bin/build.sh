#!/usr/bin/env bash

pyinstaller --onefile -n RC-Controller Controller/application.py
pyinstaller --onefile -n RC-Vehicle RaspberryPi/vehicle_application.py