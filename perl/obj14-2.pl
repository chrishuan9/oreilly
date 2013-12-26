#!/usr/bin/perl
#
#
$username = "cyereazt";
$homedirectory = "/users/".$username."/";
$filename = "messages";
$logfile = $homedirectory.$filename;
$seperator = "\.";

#opening folder
opendir(CURRENT,$homedirectory);
@list = readdir(CURRENT);
closedir(CURRENT);

foreach $file (@list){
	#matches messages or messages.1 messages.2 etc but not messages.bob or messages.smith
	if($file =~ /(messages\.\d|^messages$)/){
		print "$file:\n";print "----------------\n";
		open(FILE,$homedirectory.$file);
		@file = <FILE>;
		close(FILE);
		print @file;print "\n\n\n";
	}
}
