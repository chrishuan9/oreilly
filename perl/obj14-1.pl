#!/usr/bin/perl
#
#
$username = "cyereazt";
$homedirectory = "/users/".$username."/";
$filename = "messages";
$logfile = $homedirectory.$filename;
$seperator = "\.";

if (-e ($logfile.$seperator."3")){
	#messages3 exists -- move content to messages.4
	print "starting log rotation\n";
	for ($i = 3 ; $i > 0; --$i){
		$oldfilename = $logfile.$seperator.$i;
		$newindex = $i + 1;
		$newfilename = $logfile.$seperator.$newindex;
		if (-e $oldfilename){
			print "renaming $oldfilename to $newfilename\n";
			rename($oldfilename,$newfilename);
		}
	}
	##move message manually
	if(-e $logfile){
		print "renaming ".$logfile." to ".$logfile."\.1 \n";
		rename($logfile,$logfile."\."."1");
	}
}else{
	print "Error: messages.3 doesn't exist\n";
}


