#!/usr/local/bin/perl
#
$oldfile = "/etc/passwd";
$newfile = "/users/cyereazt/passwd";

open(FILE,"$oldfile");
open(NEW,">$newfile");

while(<FILE>{
	$_ =~ s/\/sbin/\/sysbin/;
	print NEW;
}

close(FILE);
close(NEW);


