#!/usr/bin/perl
use 5.18.0;
use warnings;
sub hello {
  my $name = $_[0];
  print "Hello $name!";
}

hello("John");
