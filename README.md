# challenge

“Framework” for creating web-based puzzle-like challenges.
Normally used for PsyChic Challenge at Polar Party.


# Installing

Tested with Python 3 and Apache 2 with modwsgi.

We recommend running challenge in a virtualenv.


# Background and history

## PsyChic

Short for Polar Systems Coders and Human Interface Coordinators.
It consists of developers, sysadmins and "friendly users" for the systems used
by Polar Party.
(Polar Party is a medium sized computer party in Norway, www.polarparty.no)

PsyChic as a group was founded in 2004, but some of the developers had already
been working with systems for many years.
These days a lot the systems (tickets and seating ie.) have been outsourced to
a commercial entity, but some of the original PsyChic members are still working
on those systems.


## PsyChic Challenge

The first traces of a PsyChic Challenge that we have the source for was made
for the event miniPolar 2, winter 2005.
Our participants (and volunteer crew) loved the challenge.

Stian Skjelstad continued to make these challenges for one or two events each
year, probably up until 2010.

The challenges were made in PHP and more or less hardcoded for each level.

During the preparations for Polar Party 19 the technical crew discussed making
our own PsyChic Challenge without Stian who didn't have time for it anymore.
Some of us were already members of PsyChic, so we "stole" the name and made it
our own.

This Python/Django-application was actually written back then in 2010, but 
we decided not to use it because most of the developers then didn't know
Python. Instead we wrote yet another quick PHP, hardcoded hack.
And then we did the same for PP20 in 2011, and PP21 in 2012.

Then came Polar Party 22, fall 2013.
The technical crew was tired, had other obligations and generally wasn't up
for (making) the challenge!

But all of a sudden some of us were convinced by fans of the challenge.
We remembered that we had this framework laying around that we never really
used, and thought that we could make something quick using that.

Well... We did. And using the 2010-codebase with some small addons we made
yet another great PsyChic Challenge.


## Contributors

Some are developers, some are testers, some are puzzle-makers and some are
probably forgotten...

* Stian Sebastian Skjelstad
* Rebekka Hansen
* Mathias Bøhn Grytemark
* Tonette Marie Stensrud Grytemark
* Lars Åge Kamfjord
* Marius Davidsen
* Bjørn Gustav Baklid
* Ludvig Anderssen
* Bjørn Elias Hesthamar

And of course: Thanks to all those who enjoys PsyChic Challenge!

# License

'challenge' is licensed under Affero General Public License, see the LICENSE-file.
Django is licensed under the BSD license, see the file LICENSE-Django.

