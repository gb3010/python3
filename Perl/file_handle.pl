#!/usr/bin/perl
use 5.18.0;
my $file1 = 'newtext.txt';
open( my $fh1,'>>',$file1) or die "Cannot locate file $file1";
#print while <$fh1>;
while ( my $line = <$fh1> )  {
	print $line;
}

close $fh1;