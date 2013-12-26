#!/bin/bash

HOSTNAME=`hostname`
NUM=`w -h |awk '{ print $1 }' |wc -l`

if [ $NUM > 15 ]; then
	cat /etc/httpd/conf/httpd.conf | grep $HOSTNAME
fi
