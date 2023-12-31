#!/bin/bash

# build a docker image for the project
# Usage: ./build-docker.sh

# build the docker image
docker build -t medoror/ff_data_pull:1.0 .