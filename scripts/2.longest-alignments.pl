#!/mnt/lustre/genkvg/perl/bin/perl -w
#USAGE: ./2.longest-alignments.pl samFile > purifiedSamFile

%sam=();
open (S, "$ARGV[0]");
while (<S>)
{
chomp;
if ($_=~/^\@/)
    {
    print "$_\n";
    }
else
    {
    @S=split(/\t/);
    $S[11]=~s/AS:i://;
    $S[15]=~s/NM:i://;
    if (exists $sam{$S[0]})
	{
	@T=split(/\t/, $sam{$S[0]});
	$T[11]=~s/AS:i://;
	$T[15]=~s/NM:i://;
	if ($S[11]>$T[11] and $T[15]>-1)
	    {
	    $sam{$S[0]}=$_
	    }
	}
    else {if ($S[15]>-1) {$sam{$S[0]}=$_}}
    }
}
close S;

foreach $s (sort {$a cmp $b} keys %sam)
{
print "$sam{$s}\n";
}
