#!/usr/bin/perl
use strict;
use warnings;

#Check command line arguments
if($num_args != 2){
  print "Please use perl failscan.pl [filename] [email]";
}

#check 3 command line arguemnt contains "@" symbol
if(!($argv[2] =~ m/@/))
{
  print "Please use a valid e-mail";
}

#open file based off command line
my $file = open($argv[1]);

#Create file
open my $fh, '>', 'logfile_scan.mmddyyyy';

sub add2file(){
  open($fh, '>', )
}

while(my $row = <$file>){
  if($line =~m/fail/){
      add2file($line)
  }

}
