#!/bin/bash

#platform="ff_creator-2560"

serial_port="/dev/tty.usbmodem1411"

avrdude_bin="./avrdude/avrdude"
avrdude_conf="./avrdude/avrdude.conf"

${avrdude_bin} \
  -p atmega2560 \
  -C ${avrdude_conf} \
  -P ${serial_port} \
  -c stk500v2 \
  -b 57600 \


