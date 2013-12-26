#!/bin/bash

#uptime
NUM=`w -h | awk '{ print $1 }' | sort | uniq | wc -l`
echo $NUM

if [ $NUM = 17 ]; then
	w
	echo $NUM
fi

if [ $USER = "cyereazt" ]; then
	ps aux | grep $USER
fi
