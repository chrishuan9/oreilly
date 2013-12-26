#!/usr/local/bin/perl
#
open(FILE, "/etc/yum.conf");
@lines = <FILE>;
close(FILE);

foreach $line (@lines){
	if($line =~ /log/){
		print $line;
	}
}
