# README

I wanted to learn how to do MapReduce, so I decided to learn a bunch
of Hadoop things at the same time.

I used bogotobogo.com's tutorial at first which was kind of a pain,
so I switched to http://www.tutorialspoint.com/hadoop/hadoop_enviornment_setup.htm
after a bit which I think was better.

My kickstart script is probably broken now, but was always best effort.

A slight point of confusion for me when trying to install it was trying
to run the example jars with `java -jar`. The correct way is `hadoop jar`.

Another point of confusion is why the tutorials want me to create a
hadoop user instead of installing it under my own account. This is probably
something that matters much more when you're sharing a cluster among many
people, but doesn't make much of a difference for a standalone distribution
and which just serves to get me into a good habit.

The actual project I want to do with Hadoop is either to recreate
my PageRank results for QuisCustodiet or to do something slightly different,
where I try to guess how similar media are to each based on ... From my
Google Distributed Computing notes, I know that I can do both of these with
MapReduce.

Third point is that I installed my hadoop in /usr/local/share instead of
/usr/local. Reading some documentation on the differences, I've realized
that this is most likely a mistake since I'm not sure that hadoop is
architecture-independent.
