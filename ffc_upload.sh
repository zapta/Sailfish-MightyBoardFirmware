#!/bin/bash

platform="ff_creator-2560"

serial_port="/dev/tty.usbmodem1411"

avrdude_bin="./avrdude/avrdude"
avrdude_conf="./avrdude/avrdude.conf"

# NOTE: add a few -v to increase verbosity
# NOTE: remove -V to perform read-after-write verification
${avrdude_bin} \
  -D -F -V \
  -p atmega2560 \
  -C ${avrdude_conf} \
  -P ${serial_port} \
  -c stk500v2 \
  -b 57600 \
  -U flash:w:./firmware/build/${platform}/${platform}_v7.8.0.en.hex


