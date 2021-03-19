#include "simpletools.h"    // Include Parallax SimpleTools
#include "fdserial.h"       // serial communication
#include "commons.h"        // Shared code between files
#include "lights.h"         // Lighting controls
#include "motor.h"          // Motor Controls

volatile vehicle_state_struct vs;

int main() {
    simpleterm_close();

    vs.lights = 0;
    vs.throttle = 0;
    vs.direction = 1;

    fdserial *ser = fdserial_open(SERIAL_PIN_2, SERIAL_PIN_1, 0, 115200);

    //Initialize Kernels
    int32_t stack_lights[100];
    cogstart(lights_loop, (void *) &vs, stack_lights, sizeof(int32_t) * 100);

    int32_t stack_motor[100];
    cogstart(motor_loop, (void *) &vs, stack_motor, sizeof(int32_t) * 100);

    int val;
    char c;

    while (1) {
        c = fdserial_rxChar(ser);
        if (c != -1) {

            switch (c) {
                case 'P' ://Throttle/Power
                    val = fdserial_rxChar(ser);
                    if (val == '1') {
                        vs.throttle = 1;
                    } else {
                        vs.throttle = 0;
                    }
                    break;
                case 'T' ://Direction/Turn
                    val = fdserial_rxChar(ser);
                    switch (val) {
                        case '0':
                            vs.direction = 0;
                            break;
                        case '1':
                            vs.direction = 1;
                            break;
                        case '2':
                            vs.direction = 2;
                            break;
                    }
                    break;
                case 'L' ://Lights
                    val = fdserial_rxChar(ser);
                    if (val == '1') {
                        vs.lights = 1;
                    } else {
                        vs.lights = 0;
                    }
                    break;
            }
        }
        pause(150);
    }
}