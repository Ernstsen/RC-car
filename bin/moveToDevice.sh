#!/usr/bin/env bash

if [ $# -eq 1 ]; then
  scp -r RaspberryPi/ pi@$1:/home/pi/Desktop/
else
  echo "Must supply IP address as only parameter"
fi
