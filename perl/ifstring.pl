#!/usr/local/bin/perl
#
$var1 ="hello";
$var2 ="goodbye";
$var3 ="hello";

if($var1 eq $var3){
	print "These two strings are the same: $var1 $var3\n"
}
if($var1 ne $var2){
	print "These two strings are no the same: $var1 $var2\n"
}
if($var1 lt $var2){
	print "$var1 comes before $var2\n";
}else{
	print "$var1 comes after $var2\n";
}
