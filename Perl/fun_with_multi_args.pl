#!/usr/bin/perl
use 5.18.0;
use warnings;
sub sum {
  my $a = $_[0];
  my $b = $_[1];
  return($a+$b);
}

my $sum_value=sum(10,20);
print "Sum of values is: $sum_value";
