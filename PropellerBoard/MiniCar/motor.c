#include "simpletools.h"    // Include Parallax SimpleTools
#include "commons.h"        //Shared code between files
#include "motor.h"          //Motor controls

void motor_loop(void *ptr) {
    vehicle_state_struct *vs = (vehicle_state_struct *) ptr;

    int throttle = 0;
    int direction = 1;


    while (1) {

        if (vs->throttle != throttle || vs->direction != direction) {
            throttle = vs->throttle;
            direction = vs->direction;

            if (throttle) {
                if (direction == 0) {
                    high(MOTOR_PIN_LEFT);
                    low(MOTOR_PIN_RIGHT);
                } else if (direction == 2) {
                    high(MOTOR_PIN_RIGHT);
                    low(MOTOR_PIN_LEFT);
                } else {
                    high(MOTOR_PIN_LEFT);
                    high(MOTOR_PIN_RIGHT);
                }
            } else {
                low(MOTOR_PIN_LEFT);
                low(MOTOR_PIN_RIGHT);
            }
        }

        pause(250);
    }
}