#!/usr/local/bin/perl
#
while(<STDIN>){
	$_ =~ s/^([^:]*:)([^:]*:)/\2\1/;
	print;
}
