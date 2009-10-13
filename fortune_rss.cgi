#!/usr/bin/perl

use strict;
use warnings;

use CGI::RSS;
use HTML::Entities;

my $rss = new CGI::RSS;

print $rss->header;
print $rss->begin_rss(
	title => "Fortune quote",
	link  => "http://genshiken.dk/~arkanoid/cgi-bin/fortune_rss.cgi",
	desc  => "A random fortune cookie quote"
);

chomp(my $fortune = `/usr/games/fortune -s`);
$fortune =~ s:\n:<br />:g;
$fortune = encode_entities($fortune);

print $rss->item(
	$rss->title($fortune),
	$rss->description($fortune),
	$rss->date(scalar localtime)
);
print $rss->finish_rss;
