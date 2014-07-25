Home Automation Using AsyncIO
=============================
Dougal Matthews
[@d0ugal](https://twitter.com/d0ugal)
[Europython Page](https://ep2014.europython.eu/en/schedule/sessions/107/)
[www.dougalmatthews.com](www.dougalmatthews.com)

Home automation using
rasp pi
RFXCom TRXrfx radio trans
on 433 khz
Works on USB
Electricity monitoring

Temperature and humidity - transmit only
sockets and light switches - light wave rf, rcv only

Events streaming

### Asyncio
[PEP 3157](http://legacy.python.org/dev/peps/pep-3156/)

Provides infrastructure for writing single threaded concurrent code using
coroutines, multplexing IO access over sockets and other resources, running
network clients and servers, and other related primitives.

    import asyncio

    @asyncio.coroutine
    def compute(...):
        ...
        return ..

    @asyncio.coroutine
    def print_compute(...):
        result = yield from compute(x,y)
        print result


### Summary
Asyncio eco system is young
coroutines and futures are better than callbacks
documentation is lacking
Graphite good for timesieres
