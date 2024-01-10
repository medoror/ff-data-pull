#!/bin/bash

# build a docker image for the project
# Usage: ./dev-build-docker.sh

# build the docker image
docker build -t medoror/ff-data-pull:2.1 . --platform linux/amd64