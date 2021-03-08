#include "simpletools.h"    // Include simple tools
#include "fdserial.h"       // serial communication

typedef struct {
    int8_t lights;      //Whether lights are on - acts like boolean
    int8_t drive;       //Low(0)/High(1) drive
    int8_t gear;        //Between 1 and 4
    int8_t throttle;    // between 0 and 10 - 0 being off
    int8_t direction;   //between 0 and 10, 5 being centered
} vehicle_state;

int main()
{
    simpleterm_close();

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
            }

            pause(150);
        }
    }
}
