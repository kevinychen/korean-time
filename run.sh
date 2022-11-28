#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

printf -v h "%02d" $((1 + RANDOM % 12))
printf -v m "%02d" $((RANDOM % 60))

echo "$h:$m"
afplay "$SCRIPT_DIR/korean_time/mp3s/$h:$m.mp3"
