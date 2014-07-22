OpenStack - Marconi
===================
Yeela Kaplan
Redhat

Message Broker
Unified inter service communication
Queuing service, notification service
RESTful Light weight messaging API

Opensource alternative to Amazon's SQS (queues) and SNS (notifications)

Higher level API than typical AMQP

Composeable Architecture

- Auth
  - Keystone
  - HTTP
- Transport
  - HTTP
- API
  - Messages
  - Queues
  - Claims
- Storage
  - MongoDB
  - SQLAlchemy (not for prod)
  - Redis

Ability to use storage pools
Can use independent clusters

Characteristics
- FIFO guarantee
- Storage pools
- easy to scale

Roadmap
Live migration
Redis support - in memory queues
Queue flavours
AMQP support (future)
