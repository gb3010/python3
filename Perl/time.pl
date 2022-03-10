use warnings;
use 5.18.0;
use POSIX qw(strftime);

my $t = time();
my $lt = localtime($t);
say $lt;
my $ft = strftime "%a %Y-%m-%d, %H:%M:%S", localtime;
say $ft;

