#!/usr/bin/perl
use 5.18.0;
use IO::File;
my $filename = 'sample';
my $count = 1;
my $f1 = IO::File->new("< $filename");
while ( my $line = <$f1>) {
	print "$count $line";
	$count += 1;
}