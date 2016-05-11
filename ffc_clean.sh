#!/bin/bash

platform="ff_creator-2560"

cd firmware

scons -c platform=${platform} 
