#include "simpletools.h"    // Include simple tools
#include "fdserial.h"       // serial communication
#include "commons.h"        // Shared code between cores
#include "lights.h"         // Lighting controls


volatile vehicle_state_struct vs;

int main() {
    simpleterm_close();

    vs.lights = 0;
    vs.drive = 0;
    vs.gear = 1;
    vs.throttle = 0;
    vs.direction = 5;

    fdserial *ser = fdserial_open(SERIAL_PIN_2, SERIAL_PIN_1, 0, 115200);

    //Initialize Kernels
    int32_t stack_lights[100];
    cogstart(lights_loop, (void *) &vs, stack_lights, sizeof(int32_t) * 100);

    int val;
    char c;

    while (1) {
        c = fdserial_rxChar(ser);
        if (c != -1) {

            switch (c) {
                case 'D' ://Drive
                    val = fdserial_rxChar(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'G' ://Gear
                    val = fdserial_rxChar(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'P' ://Throttle/Power
                    val = fdserial_rxChar(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'T' ://Direction/Turn
                    val = fdserial_rxChar(ser);
                    high(26);
                    pause(10000);
                    low(26);
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