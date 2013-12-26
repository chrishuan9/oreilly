#!/usr/bin/perl                                                                                                               
#         
#         
@array1 = ("1","2","3","4","5","6","7","8","9","0");
@array2 = ("00","00");

splice(@array1,$#array1/2,0,@array2);

print join(", ",@array1);print "\n";
