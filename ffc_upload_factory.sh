#!/bin/bash

# Upload the factory hex file via the USB cable to the Flashforge Creator Pro

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
  -U flash:w:./build.factory/mighty_one_v7.2.0.hex


