use warnings;
use 5.18.0;

my $file = "testfile";
open(FH,'<',$file);
my @lines = <FH>;
my $size =  @lines;
print $size ;
