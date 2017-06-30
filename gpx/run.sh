#!/bin/bash 

basename="$1"


function check_last_cmd() {
  status="$?"
  if [ "$status" -ne "0" ]; then
    echo "Error while $1"
    exit 1
  fi
}


rm ${basename}.x3g


./gpx \
  -v \
  -g \
  -p \
  -m r1d \
  ${basename}.gcode \
  ${basename}.x3g

check_last_cmd "compiling gcode"


../../../misc/repo/simplify3d/start_flashair_uploader.sh \
  ./${basename}.x3g



