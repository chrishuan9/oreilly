#!/usr/bin/perl
#
@array = (5,3,2,1,4);
#initialisation
$max = $array[0];

#check every element in the array
foreach $elem (@array){
	#if the current element is greater than the current maximum
	if($max < $elem){
		#then replace current maxium with the new element
		$max = $elem;
		print "Found new maximum: $max \n"
	}
}
#print out the answer
print "Maximum in array: $max \n";
