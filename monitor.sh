#!/bin/bash
##-> Print the last field, wich shows the amount  of available RAM(MB).
SYSTEM_STATS="System Check: Available RAM is $(free -m | awk '/Mem:/ {print $7 " MB"}')" 
echo $SYSTEM_STATS
