#!/usr/bin/perl
#
require 'obj13-lib.pl';


if (-t STDIN and not @ARGV){
  ## We're talking to a terminal, but have no command line arguments.
  ## Complainig loudly
  die("Usage: ./obj13.pl Integer1 Integer2 Integer 3 Integer 4 ... seperated by spaces and press enter\n");

}
else{
  ## We're either reading from a file or pipe, or we have arguments in 
  ## @ARGV to process
  if (@ARGV > 0){
    @array = @ARGV;
  }
  else{
    while (my $line = <STDIN>) {
      chomp $line;

      # use the string comparison operator...
      last if $line eq "0";
      # or use a match operator...
      # last if $line =~ m/^0$/;
      # or match on some special number
      # last if $line == 3.1415926;

      push @stdin, $line;
    }
    @array = @stdin;
  }
}

print join(", ",doall(@array)); print "\n"
