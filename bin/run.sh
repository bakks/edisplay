#!/bin/bash
set -e

OUTPUT=$(./fetch | tail -1)
./display -1.14 $OUTPUT
