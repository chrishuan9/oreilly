#!/usr/local/bin/perl
#
while(<STDIN>){
	if(/str([io])ng\1/){
		$vowel = $1;
		print "We matched $vowel\n";
	}
}
