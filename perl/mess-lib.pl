sub messup {
	my $line = shift(@_);
	
	$line =~ s/^([^:]*:)([^:]*:)/\2\1/;
	$line =~ tr/[A-Z]/[a-z]/;
	@fields = split(/:/,$line);
	chomp(@fields);
	@rfields = reverse(@fields);
	$newline = join(":",@rfields);

	return $newline;
}
#every library needs to end with a 1
1;
