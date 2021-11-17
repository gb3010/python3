use warnings;
use 5.18.0;
use IO::File;

my $file = "testfile";
my $fh = IO::File->new( $file, "r");
my $count = 0;

while($fh->getline) {
  $count++
}

say "Number of lines in $file is $count"
