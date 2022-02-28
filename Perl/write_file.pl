#!/usr/bin/perl
use 5.18.0;
use IO::File;

my $filename = 'sample';
my $outputfile = 'output';
my $count = 1;
my $f1 = IO::File->new("< $filename");
my $f2 = IO::File->new("> $outputfile");

while ( my $line = <$f1>) {
	$f2->print("$count $line"); # Print content with line number
	$count += 1;
}