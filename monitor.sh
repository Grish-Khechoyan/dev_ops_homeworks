#!/bin/bash
##-> The command prints the free (unused) space in the root file system.
SYSTEM_STATS="System Check: Root Disk Available is $(df -hP / | awk 'NR==2 {print "Unused: " $5}')"
echo $SYSTEM_STATS
