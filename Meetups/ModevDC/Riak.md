# ModevDC Riak Talk

Slides will be available later.

## Speaker
Sasha Sicular, developer from Columbia University.
Director of Medica Informatics. Was recruited to Basho due
to being a power user of Riak, now a Senior Solution Architect.

## Path to the Platform
1. Start with what you have.
2. Solve problems as they arise.
3. Get to the point where you can't scale.
4. Use a more scalable solution.

"We're getting slow that means we succeeded."

Billions of mobile devices
20 TB of data per day

Worked through store example:
We have a product catalogue. We want speed for customers,
we want to analyze data, we want a search feature.

Distribution is the hard part.
Amazon has a 2007 paper "Dynamo: Amazon's Highly available Key-Value store"
about this, but there problem was that they were losing a lot of
money for every minute they weren't available.

Scalable Riak has a masterless architecture in which every node
in a cluster is capable of serving read and write requests. Requests
are routed to nodes using standard load balancing.

Due to data access pattern one host will be more popular than the
others. 

We divide the range of SHA-1 into buckets which are assigned to
a number of virtual nodes that are evenly (as possible) divided
among hosts. This somewhat looks like a ring. SHA-1 was chosen
because its output has a uniform distribution. This system prioritizes
availability over consistency.

Nodes use a gossip protocol to share their view as to what the ring state
is. Hinted handoff allows people to takeover for failed nodes.

There's a theorem that out of availability - partition tolerance - consistency
you can only have two. Riak is AP. Relational are AC.

Traditionally, Riak has stuff on three nodes. So, you start losing
data at three node failures.

Multiple data centers are done with a cluster of clusters approach.
Miniclusters are supposed to have low latency for performance reasons.

### Fault tolerance

Read repair is attempted on every successful read where we try
to update people who are out of date.

Active anti-entropy (AAE) runs in the background and exchanges
Merkle tree hashes between nodes to improve data congruency.

Erlang allows you to dial-in to a running Erlang VM and change behavior.
(Sounds like buzzwords?)

Multi-cluster replication gives us very flexible topologies.

Geo-data locality lets you store data in a certain location. For example,
if there's legal issues about where you store finance, health care,
customer data.

Riak Data Types: Type of *convergent replicated data type*. Track updates
  in an eventually consistent environment without relying on clocks. Have
  a predetermined merge strategy. Use vector clocks. You can use other
  types, but if so you need to do your own merging.
* Counter - Tracks inc and decs of integer.
* Flag - boolean.
* Set - Collection of binary values. Support add / remove.
* Map -
* Register - Named field in a map.

Apache Solr Integration: Full-text searching engine. Wraps Lucene.

Basho Data Platform:
* redis for caching
* spark for analytics
* Riak KV

For time-series, we want data locality so we have a combined
key to make that happen.

Why is Redis awesome? If you get an 80% hit rate, then your process is
5X faster. They're thinking of closer integration with Redis. They usually
use a time-to-live to expire things from the cache.

Spark is data storage agnostic in a way that map-reduce is not.
