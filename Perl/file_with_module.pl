#!/usr/bin/perl
use 5.18.0;
use IO::File;
my $filename = 'sample';
my $file = IO::File->new("< $filename") or die "The file $filename is not found $!";
print while <$file>;