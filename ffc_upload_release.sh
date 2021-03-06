#!/bin/bash

# Upload the github original hex file via the USB cable to the Flashforge Creator Pro

serial_port="/dev/tty.usbmodem1411"

avrdude_bin="./avrdude/avrdude"
avrdude_conf="./avrdude/avrdude.conf"

${avrdude_bin} \
  -v -v \
  -D -F -V \
  -p atmega2560 \
  -C ${avrdude_conf} \
  -P ${serial_port} \
  -c stk500v2 \
  -b 57600 \
  -U flash:w:./build.release/ff_creatorx-2560-Sailfish-v7.7.0-r1591.hex


