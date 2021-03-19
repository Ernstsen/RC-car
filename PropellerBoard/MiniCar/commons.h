#ifndef COMMONS_H_INCLUDED
#define COMMONS_H_INCLUDED

#include "simpletools.h"    // Include simple tools

/* Define pins for all interfacing */
#define SERIAL_PIN_1 30
#define SERIAL_PIN_2 31

#define MOTOR_PIN_LEFT 12
#define MOTOR_PIN_RIGHT 13

#define LIGHTS_PIN_1 27


typedef struct {
    int8_t lights;      //Whether lights are on - acts like boolean
    int8_t throttle;    //Whether vehicle moves forward - acts like boolean
    int8_t direction;   //0 = left, 1 forward, 2 right
} vehicle_state_struct;


#endif
