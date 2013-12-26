#!/usr/bin/perl
#
$string = "The IP address is 216.108.225.236";

if($string =~ /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/){
  $ip = $1;
}
print "$ip\n";
print "$string\n";
