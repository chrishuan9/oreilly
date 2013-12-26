#!/usr/local/bin/perl
#
$key = "USER";
print $ENV{$key}."\n";

%names = ("john","smith",
	  "sally", "johnson",
	  "bill", "peterson");

foreach $key (keys(%names)){
	print "$key $names{$key}\n";
}
