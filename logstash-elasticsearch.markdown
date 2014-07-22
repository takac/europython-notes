Logstash and Elasticsearch
==========================
Peter Hoffman
[@peterhoffmann](https://twitter.com/peterhoffmann)
[http://peter-hoffmann.com](http://peter-hoffmann.com)
[Slides](github.com/hoffmann)

graylog2 alternative

- Producers
- Transports
  - syslog
  - gelf
  - redis
  - RMQ
  - logfile/grok
- Routes/Filter
  - logstash
- Storage
- Analysis
  - kibana

gelf -> logstash -> elasticsearch -> kibana

### GELF
Graylog extended logging format
JSON over UDP - nonblocking
Not reliable
allows chunking

### Logstash
receiving, processing and outputting logs
JRuby
Pipes/filters pattern
configure: inputs, filters and outputs

### kibana
Utilises elastic search
No auth
single page JavaScript app
rich visualisations
time based analysis
create and share dashboards
non developer analysis

### Example Visualisations
Bettermap
Histograms
Sparklines - Tiny time charts
Terms - facet caclulations

### Logging Patterns

##### Adding Context

    log.debug('hello log', extra = {'a': 'stuff'})

Logging filters
Request Ids generated when request starts
Correlation ID - generated at entry of app passed in HTTP X- header

##### Other
Finger crossed handler - log all messages in memory until ERROR level then dump to transport
Logbook alternative to stdlib logging