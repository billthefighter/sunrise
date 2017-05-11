# sunrise
This is now a super cool rPi based cellular automota display, using 2 32x32 RGB LED arrays to display cellular automota to dazzle your friends and upset your neighbors. 

It also contains sunrise code, but it turns out that the RGB LED panels aren't really in the right color gamut and it looks really stupid. 

USED TO BE A Sunrise simulator using adafruit RGB hat and latest rzeller python drivers

notes:

To get everything to work, you need to compile the submodule in rpi-rgb-led-matrix/python/ by running the following (as listed in the readme)

Building
--------

Setting up rgb-led-matrix
------------------------------
The RGB LED array needs to have a C layer built - the instructions are pretty good here.
https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/python/README.md

Make sure you set the hardware flag on the makefile in the python subdirectory - 
https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/lib/Makefile#L26

I also found that Hzeller's hardware hack for the adafruit hat was helpful in reducing flicker:
https://github.com/hzeller/rpi-rgb-led-matrix#improving-flicker

In the root directory for the matrix library simply type

      $ make build-python
      $ make install-python

If you get an onboard sound error on first run after make, check here:
https://github.com/hzeller/rpi-rgb-led-matrix#troubleshooting
