#!/usr/local/bin/perl
#

require 'mess-lib.pl';

open(PASSWD,"/etc/passwd");
@passwd = <PASSWD>;
close(PASSWD);

foreach $line (@passwd){
	$newline = messup($line);
	$newline = messup($newline);

	print "$newline\n";
}

