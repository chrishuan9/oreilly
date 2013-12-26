#!/usr/bin/perl
#

#function that takes in an array of numbers (of arbitrary size). 
#The function will then calculate the average of the numbers, 
#the total of all of the numbers added together, 
#and a new array of numbers which is comprised of the 
#original input numbers each divided by 2. It will then return
#a new list with all of that information.


sub doall{
  my @input = @_;
  $average = average(@input);
  $total = total(@input);
  my @divbytwo = dividebytwo(@input);
  my @output = ($average,$total,@divbytwo);
  return @output;
}

sub average{
  my @input = @_;

  my $total = total(@input);
  my $average  = $total / @input;
  return $average;
}

sub total{
  my @input = @_;
  my $total = 0;
  foreach $number (@input){
    $total += $number;
  }
  return $total;
}

sub dividebytwo{
  my @input = @_;
  foreach $number (@input){
    $number = $number/2;
  }
  return @input;
}

sub shuffleCards{
  my @startingdeck = @_;
  for ($j = 0; $j < 10; ++$j){
    for ($i = 0; $i < $count/2; ++$i){
      $last_element = pop(@startingdeck);
      $first_element = shift(@startingdeck);

      if(($i+$j) % 2){

        if ($first_element != undef){
          push(@newdeck,$first_element);
        }
        if ($last_element != undef){
          splice(@newdeck,($i/2-$i/4),0,$last_element);
        }

      }else{

        #insert first element into the middle of the array
        if ($first_element != undef){
          splice(@newdeck,($i/2),0,$first_element);
        }
        if ($last_element != undef){
          unshift(@newdeck,$last_element);
        }
      }
    }
    @startingdeck = @newdeck;
    @newdeck = ();
  }
  return @startingdeck;
}  

sub printArray{
  my @arrayToPrint = @_;
  print join(", ",@arrayToPrint); print "\n";
}

sub printTopFiveCards{
#print out the top five cards
#
@shuffleddeck = @_;
print "\n\nThe top five cards are \n";
for ($j = 0; $j < 5; ++$j){
  $cardtoprint = $shuffleddeck[$j];
  #$cardtoprint = shift @shuffleddeck;
  #\w for the first alphanumeric \s for the white space
  #\1 backreference to include the match in the replacement string
  $cardtoprint =~ s/([\w\s])H/\1hearts/;
  $cardtoprint =~ s/([\w\s])S/\1spades/;
  $cardtoprint =~ s/([\w\s])C/\1clubs/;
  $cardtoprint =~ s/([\w\s])D/\1diamonds/;

  print "$cardtoprint, ";
}
print "\n";




}

1
