#!/usr/local/bin/perl$startdir = "/lib";               
$level = 0;
list_dirs($startdir,$level);
sub list_dirs{ 
  my $dir  = shift (@_); 
  my $lev = shift (@_); 
  opendir(TOP,$dir); 
  my @files = readdir(TOP);  
  closedir(TOP);  
  @files = sort(@files);  
  shift(@files);  
  shift(@files);  
  foreach $file (@files){    
    if(-d "$dir/$file"){        
      spaces($lev);        
      print "$file\n";        
      list_dirs("$dir/$file",$lev+1);    
    }  
  }
}

sub spaces{ 
  my($num) = shift(@_); 
  for($i=0;$i<$num;$i++){    
    print " "; 
  }
} 

#The changes that were made to make the output look better were the introduction of a variable $level for the initial indention level of 
#the original call for the list_dirs function. Inside the list_dirs function the new variable $lev holds the current indention level
#of the current recursion. That's the reason why it was declared a local variable with the "my" keyword as with every succesive recursive
#call the local variable $lev will be increased by one. So initially the $level will be 0 as well as $lev will be 0. In the foreach loop
#if the $file is a directory it will be printed with the current indention level using the spaces function. Afterwards a recursive call with the indention level increased by 1 will be made.
#So on the second call $lev will be 1 and the directory will be printed and for each item a recursive call to list_dirs will be made with $lev increased again. This will be repeated as long 
#as a directory contains any subdirectory or as long as the if (-d $dir/$file) still yields true for any $file.
