#!/bin/bash

cd firmware

platform={ff_creator-2560}

serial_port="/dev/tty.usbmodemFA131"

avrdude_dir="/Applications/ReplicatorG.app/Contents/Resources/tools"

${avrdude_dir}/avrdude \
  -v -v \
  -D -F -V \
  -C ${avrdude_dir}/avrdude.conf  \
  -p atmega2560 \
  -P ${serial_port} \
  -c stk500v2 \
  -b 57600 \
  -U flash:w:build/${platform}/${platform}_v7.8.0.en.hex


