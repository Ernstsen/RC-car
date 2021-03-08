# Propeller Vehicle

This part of the project contains the code for the vehicle, which is executed on
a [Propeller Activity Board WX](https://www.parallax.com/product/propeller-activity-board-wx/).

The code is developed using
the [SimpleIDE](https://learn.parallax.com/tutorials/language/propeller-c/propeller-c-set-simpleide), which is also used
in deploying the software to the developer board.

## Structure

The propeller board is based on the ``Parallax P8X32A`` octa-core processor, enabling proper multi-thread applications.
This project will utilize this, by using between 1 and 8 threads, each assigned to a task, as follows:

1. *Main Thread* initializes the other threads, and listens for messages sent through serial connection
2. *Currently Unused*
3. *Currently Unused*
4. *Currently Unused*
5. *Currently Unused*
6. *Currently Unused*
7. *Currently Unused*
8. *Currently Unused*

Each non-main thread has behaviour defined in own file, in an attempt at improved readability. Main-thread behaviour is
found in ``vehicle.c``