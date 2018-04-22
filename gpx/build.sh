#!/bin/bash -x

# NOTE(zapta): added this script to build gpx on mac. It required
# clang to be installed.

rm -f gpx
cc -w -lm getopt.c gpx.c gpx-main.c -o gpx
