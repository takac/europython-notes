Scalable Realtime Architectures
=======================
Jim Baker
[Europython Page](https://ep2014.europython.eu/en/accounts/profile/414/)
[@jimbaker](https://twitter.com/jimbaker)
[Slides](https://github.com/jimbaker/talks)

Key Ideas: Partitioning and Fault Tolerance

Realtime aggregation
Dashboards
Realtime decision making

Consuming streams of data as events
event oriented
bes effort low latency
complex event processing

Pipelining
Composition of reusable filters
Unix like pipelines

Small problems are easy
Divide and conquer big problems
Need horizontal scaling
The more machines the bigger chance of failure
Coordinate failures

Can't just add ZooKeeper 
ZooKeeper adds heartbeats and tracking

Storm
Strong support for fault tolerance and partitioning
Uses ZooKeeper internally

Spark streaming - mini-batch approach
LinkedIns's Samza

Topology and its invariants
Spouts - Source events, fully acked
Topology is DAG (directed acyclic graph) for event routing
Storm ensures the number of nodes for spouts and bolts is held constant

Computational Locality
Storm routes events consistently to specific node for a bolt
Use field grouping to route, all events of a given key to anode for some bolt
Move computation to the data

Caveats
Do not attempt to store all the data
No built-in query languages

Don't do tracking in ZooKeeper
Spouts are responsible for retries

Python Clamp to call Python from Java
