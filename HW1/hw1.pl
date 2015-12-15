#!/usr/bin/perl

use strict;
use warnings;
use Socket;



#Take file arg
my $file = $ARGV[0] or die "Please use hw1.pl <file>\n";

#OPen file
open(my $data, '<', $file) or die "Could not open file";

#init array to hold ip addresses
my @ipArray=qw();

#Parse file for dest IP
while(my $line = <$data>) {
  chomp $line;
  my @parts = split(',',$line);
  push(@ipArray, $parts[3]);
  print "$parts[3]\n";

}

#Print array
my @ips=sort{$a<=>$b}(@ipArray);
foreach(@ips){
  print "Tada: $_\n"
}
