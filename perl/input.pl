#!/usr/local/bin/perl
#
#@input = `cat /etc/protocols`;
#@input = <STDIN>;

#foreach $line (@input){
#	if($line =~ /ICMP/){
#		print $line;
#	}
#}

open(FILE,"/etc/protocols");

while (<FILE>){
	if(/ICMP/){
		print;
	}
}
close (FILE);
