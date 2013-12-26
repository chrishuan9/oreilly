#!/usr/bin/perl
#
$username = "cyereazt";
$filename = "/users/".$username."/.bash_login";

if($size = -s $filename){
	#open(FILE,"$filename");
	#while(<FILE>){ print };
	#close(FILE);
	print "$filename has a size of $size\n"
}else{
	print "Error: $filename doesn't exist\n";
}
