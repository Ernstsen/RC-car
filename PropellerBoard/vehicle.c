/*
  Blank Simple Project.c
  http://learn.parallax.com/propeller-c-tutorials 
*/
#include "simpletools.h"                      // Include simple tools
#include "fdserial.h"                         // serial communication          
  
int main()                                    // Main function
{
  simpleterm_close();
  
  fdserial *ser = fdserial_open(31, 30, 0, 115200);
  
  int val;  
   
  char c;
 
  while(1)
  {
    c = fdserial_rxCheck(ser);
    if(c != -1){
      
      switch(c) {
        case 'D' ://Drive
          val = fdserial_rxCheck(ser);
          break;
      }         
      pause(150);
    }
  }    
}
