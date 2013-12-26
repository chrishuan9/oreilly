#!/usr/bin/perl                                                                                                                                   
#
#
#I assume that first hand refers to the first set of cards
#the classic hearts game consist of three cards so my best
#guess was to run the shuffle on 3 cards at a time
require 'obj13-lib.pl';

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
printArray(@startingdeck);
$count = scalar @startingdeck;
print "\nnumber of cards: $count\n";

#shuffling the cards: 3 at a time
@shuffleddeck = ();
while (@startingdeck){
  #as long as there cars in the set .. take 4 cards
  for($i=0;$i<4;++$i){
    #take card from deck
    my $card = pop @startingdeck;
    last if $card == undef; 
    push @shuffleddeck, $card;
  }
  print "\nshuffling "; printArray(@shuffleddeck); print "\n";
  #shuffle the 3 cards, repeat until there are no
  #cards in the starter deck
  @shuffleddeck = shuffleCards(@shuffleddeck);
}


#echo new set
print "\nNew Set\n";

printArray(@shuffleddeck);

printTopFiveCards(@shuffleddeck);
#feedback from Kelly: Remember to shuffle again and 
#print another five cards(elements). You should have two shuffles and 
#a total of ten unique cards printed when the script is run.
#

#echo: shuffling 2nd time for dealing another hand
#
#remove the top five cards from the deck and reshuffle
for($j = 0; $j < 5; ++$j){
  shift @shuffleddeck;
}
printArray(@shuffleddeck);
#reshuffle
@shuffleddeck = shuffleCards(@shuffleddeck);
printArray(@shuffleddeck);
printTopFiveCards(@shuffleddeck);
