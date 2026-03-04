#!/bin/bash
SYSTEM_STATS="System Check: Available RAM is $(free -m | awk '/Mem:/ {print $7 " MB"}')\nRoot Disk Available is $(df -hP / | awk 'NR==2 {print "Unused: " $5}')"
