#!/bin/bash 
#
# usage:   
#  ./run.sh filename.gcode

input_path="$1"

echo "input_path: [$input_path]"

if [ "$input_path" == "" ]; then
    input_path="load.gcode"
    echo "No .gcode file specified, using $input_path"
fi

# Verify extension is .gcode
if [[ ! $input_path =~ ^.*[^/]\.gcode$ ]] ; then 
  echo "Expecting a .gcode input file"
  exit 
fi

# Remove the .gcode extension
base_path=${input_path%.*}

function check_last_cmd() {
  status="$?"
  if [ "$status" -ne "0" ]; then
    echo "Error while $1"
    exit 1
  fi
}

rm ${base_path}.x3g


./gpx \
  -v \
  -g \
  -p \
  -m r1d \
  ${base_path}.gcode \
  ${base_path}.x3g

check_last_cmd "compiling gcode"

echo "Generated ${base_path}.x3g"

#
# NOTE(zapta): using here a shell script from another github repository
# to upload the gpx file to the flashair SD card via wifi.
#
../../../misc/repo/simplify3d/start_flashair_uploader.sh \
  ./${base_path}.x3g



