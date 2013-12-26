#!/usr/local/bin/perl
#
$i = 0;

while($i <10){
	print "$i\n";
	if ($i == 5){
		$i +=4;
		next
	}
	$i++;
}
