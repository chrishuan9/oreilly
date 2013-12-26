#!/usr/bin/perl                                                                                                                                   
#                                                                                                                                                 
@startingdeck = ("A H","2 H","3 H","4 H","5 H","6 H","7 H","8 H",                                                                                 
  "9 H","10 H","J H","Q H","K H",                                                                                                                   
  "A D","2 D","3 D","4 D","5 D","6 D","7 D","8 D",                                                                                                  
  "9 D","10 D","J D","Q D","K D",                                                                                                                   
  "A C","2 C","3 C","4 C","5 C","6 C","7 C","8 C",                                                                                                  
  "9 C","10 C","J C","Q C","K C",                                                                                                                   
  "A S","2 S","3 S","4 S","5 S","6 S","8 S","8 S",                                                                                                  
  "9 S","10 S","J S","Q S","K S");             

print "Starting Set\n";
#echos the initial set
print join(", ",@startingdeck); print "\n\n";

$count = scalar @startingdeck;

#shuffling the cards
#
for ($j = 0; $j < 10; ++$j){
  for ($i = 0; $i < $count/2; ++$i){
    $last_element = pop(@startingdeck);
    $first_element = shift(@startingdeck);

    if(($i+$j) % 2){

      print "Switching elements: $last_element, $first_element \n";

      push(@newdeck,$first_element);
      splice(@newdeck,($i/2-$i/4),0,$last_element);

    }else{

      #insert first element into the middle of the array
      splice(@newdeck,($i/2),0,$first_element);
      unshift(@newdeck,$last_element);
    }
  }
@startingdeck = @newdeck;
@newdeck = ();
}


#echo new set
print "\nNew Set\n";

print join(", ",@startingdeck); print "\n";

#print out the top five cards
#
print "\n\nThe top five cards are \n";
for ($j = 0; $j < 5; ++$j){
  $cardtoprint = $startingdeck[$j];
  #\w for the first alphanumeric \s for the white space
  #\1 backreference to include the match in the replacement string
  $cardtoprint =~ s/([\w\s])H/\1hearts/;
  $cardtoprint =~ s/([\w\s])S/\1spades/;
  $cardtoprint =~ s/([\w\s])C/\1clubs/;
  $cardtoprint =~ s/([\w\s])D/\1diamonds/;

  print "$cardtoprint, ";
}
print "\n";
