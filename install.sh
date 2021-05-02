#!/bin/bash

<<codder
Mr. Sfx
codder
apd=apt
root="Are You Root ? "
echo $root
echo "# yes or no"
read r
if [ root == "yes" ]
then
sleep 2
echo $(clear)
echo "Welcome"
echo $(sudo $apd-get update)
echo $(sudo pip install N4Tools)
echo $(sudo $apd-get install nmap)
echo $(sudo $apd-get install python)
echo $(sudo $apd-get install python3)
echo $(sudo $apd-get install php)
echo $(sudo $apd-get install php5)

else
echo $(clear)
echo "Welcome"
echo $($apd update)
echo $($apd install python)
echo $($apd install python3)
echo $($apd install python3-pip)
echo $(pip install N4Tools)
echo $(python3 -m pip install N4Tools)
echo $($apd install nmap)
echo $($apd install php)
echo $($apd install php5)
<<finish
Good Bye ^_^
finish
fi
