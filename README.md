# sunrise
This is now a super cool rPi based cellular automota display, using 2 32x32 RGB LED arrays to display cellular automota to dazzle your friends and upset your neighbors. 

It also contains sunrise code, but it turns out that the RGB LED panels aren't really in the right color gamut and it looks really stupid. 

USED TO BE A Sunrise simulator using adafruit RGB hat and latest rzeller python drivers

notes:

To get everything to work, you need to compile the submodule in rpi-rgb-led-matrix/python/ by running the following (as listed in the readme)

Building
--------

In the root directory for the matrix library simply type

      $ make build-python
      $ make install-python
