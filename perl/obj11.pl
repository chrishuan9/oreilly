#!/usr/local/bin/perl
#
@input = `cat /httpd/conf/httpd.conf`;

foreach $line (@input){
	if($line =~ /\/cgi-bin/){
		print $line;

	}
}
