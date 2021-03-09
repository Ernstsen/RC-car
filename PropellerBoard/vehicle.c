#include "simpletools.h"    // Include simple tools
#include "fdserial.h"       // serial communication

typedef struct {
    int8_t lights;      //Whether lights are on - acts like boolean
    int8_t drive;       //Low(0)/High(1) drive
    int8_t gear;        //Between 1 and 4
    int8_t throttle;    // between 0 and 10 - 0 being off
    int8_t direction;   //between 0 and 10, 5 being centered
} vehicle_state_struct;

void lights_loop(void *ptr);

int main() {
    simpleterm_close();

    vehicle_state_struct vs;
    vs.lights = 0;
    vs.drive = 0;
    vs.gear = 1;
    vs.throttle = 0;
    vs.direction = 5;

    fdserial *ser = fdserial_open(31, 30, 0, 115200);

    int val;

    char c;

    while (1) {
        c = fdserial_rxCheck(ser);
        if (c != -1) {

            switch (c) {
                case 'D' ://Drive
                    val = fdserial_rxCheck(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'G' ://Gear
                    val = fdserial_rxCheck(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'P' ://Throttle/Power
                    val = fdserial_rxCheck(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'T' ://Direction/Turn
                    val = fdserial_rxCheck(ser);
                    high(26);
                    pause(10000);
                    low(26);
                    break;
                case 'L' ://Lights
                    val = fdserial_rxCheck(ser);
                    if (val == 1) {

                    }
                    high(26);
                    pause(10000);
                    low(26);
                    break;
            }

            pause(150);
        }
    }
}

void lights_loop(void *ptr) {
    vehicle_state_struct *vs = (vehicle_state_struct *) ptr;
    int lights = 0;

    while (1) {
        if (vs->lights != lights) {
            lights = vs->lights;
            if (lights) {
                high(27);
            } else {
                low(27);
            }
        }
        pause(250);
    }
} 