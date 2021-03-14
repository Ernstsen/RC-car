#include "lights.h"
#include "commons.h"

void lights_loop(void *ptr) {
    vehicle_state_struct *vs = (vehicle_state_struct *) ptr;

    int lights = 0;

    while (1) {
        if (vs->lights != lights) {
            lights = vs->lights;
            if (lights == 1) {
                high(27);
            } else {
                low(27);
            }
        }
        pause(250);
    }
} 
