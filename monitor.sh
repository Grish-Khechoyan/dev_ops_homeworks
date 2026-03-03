##-> Print the last field, wich shows the amount  of available RAM(MB).
##SYSTEM_STATS="System Check: Available RAM is $(free -m | awk '/Mem:/ {print $NF " MB"}')" 
##SYSTEM_STATS="System Check: Available RAM is $(free -m | awk '/Mem:/ {print $7 " MB"}')" 
##echo $SYSTEM_STATS

##-> The command prints the free (unused) space in the root file system without the % sign.
##SYSTEM_STATS="System Check: Root Disk Available is $(df / | awk 'NR==2 {print "Unused: " $5}' )" 
SYSTEM_STATS="System Check: Root Disk Available is $(df -hP / | awk 'NR==2 {print "Unused: " $5}')"
echo $SYSTEM_STATS
