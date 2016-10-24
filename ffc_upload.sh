#!/bin/bash

cd firmware

platform="ff_creator-2560"

serial_port="/dev/tty.usbmodemFA131"

#avrdude_bin="/Applications/Arduino.app/Contents/Java/hardware/tools/avr/bin/avrdude"

# NOTE: since we run in ./firmware, using ../ to access the avrdude subdirectory.
avrdude_bin="../avrdude/avrdude"
avrdude_conf="../avrdude/avrdude.conf"

${avrdude_bin} \
  -v -v \
  -D -F -V \
  -p atmega2560 \
  -C ${avrdude_conf} \
  -P ${serial_port} \
  -c stk500v2 \
  -b 57600 \
  -U flash:w:build/${platform}/${platform}_v7.8.0.en.hex


