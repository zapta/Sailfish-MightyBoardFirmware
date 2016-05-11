#!/bin/bash

platform="ff_creator-2560"

cd firmware

scons platform=${platform} 

ls -l build/${platform}


