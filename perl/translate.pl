#!/usr/local/bin/perl
#
while(<STDIN>){
	$_ =~ tr/[A-Z]/[a-z]/;
	print;
}
