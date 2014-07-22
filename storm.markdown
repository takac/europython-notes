Apache Storm and Apache Kafka
=============================
Konark Modi
[@konarkmodi](https://twitter.com/konarkmodi)

StreamParse python
Petrel - Pure python storm
Nimbus deploys topology
Jython
distributed processing layer

Kafka:
- Messaging
- Clusters - set of brokers
- Topics - group of related messages
- Partition part of a topic, used for replication
- Log centric, high throughput

Java but with python libraries
- python-kafka
- Samsa

Storm
- Realtime computation system- Spouts, producers
- Bolts, processors
- DRPC
- Transactional topologies, intergrity of processing. Will procss message once only.
- Trident topologies
- Clojure DSL
