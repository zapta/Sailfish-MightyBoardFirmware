#!/bin/bash

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
  -U flash:w:./build.original/ff_creator-2560_v7.8.0.en.hex


