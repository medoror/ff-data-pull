#!/bin/bash

# build a docker image for the project
# Usage: ./build-docker.sh

# build the docker image
docker build -t medoror/ff-data-pull:1.0 .