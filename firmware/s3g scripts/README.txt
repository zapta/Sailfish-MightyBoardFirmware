Notes, zapta Apr 2017

Converting .gcode scripts to .x3g format:
* Using ReplicatorG 40r33 on Mac OSX. Download from thingiverse 32084.
* Copy paste the .gocode text into the ReplicatorG's gcode tab.
* Set machine type to 'The Replicator Single (Sailfish)'. Other machine types
  may generate slightly different x3g than the original Sailfish .x3g scripts
  here..
* Optional, test the script from ReplicatorG by connecting a printer with a USB cable.
* Generate the .x3g file using the toolbar icon 'Buidl to file for use with SD card'.
* Diff the old and new file for changes. (eg. Araxis, binary mode, 1 column, 8-bit, Decimal)

Updating the script in the C source files:
  * Use the loadDataFile.py utility to generate the C code. E.g.
    ./loadDataFile.py ReplicatorLeveling-XY-max.x3g LevelPlate
  * Replace the table code of the relevant table in the file
    firmware/src/MightyBoard/shared/Menu_locales.hh

