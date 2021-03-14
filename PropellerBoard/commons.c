#include "simpletools.h"    // Include simple tools

typedef struct {
    int8_t lights;      //Whether lights are on - acts like boolean
    int8_t drive;       //Low(0)/High(1) drive
    int8_t gear;        //Between 1 and 4
    int8_t throttle;    // between 0 and 10 - 0 being off
    int8_t direction;   //between 0 and 10, 5 being centered
} vehicle_state_struct;
