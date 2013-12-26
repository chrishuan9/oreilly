#!/usr/local/bin/perl
#
$month=9;
$day=11;
$year=85;

$answer = $month * 4;
$answer+=13;
$answer*=25;
$answer-=200;
$answer+=$day;
$answer*=2;
$answer-=40;
$answer*=50;
$answer+=$year;
$answer-=10500;

print "$answer\n";
