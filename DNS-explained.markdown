DNS Explained
=============
Lynn Root
[@roguelynn](https://twitter.com/roguelynn)
[rogue.ly/dns](rogue.ly/dns)
[Europython Page](https://ep2014.europython.eu/en/schedule/sessions/5/)
[Talk Recording](https://www.youtube.com/watch?v=ZqKNDn56Aoo)
[https://speakerdeck.com/roguelynn/europython-2014-for-lack-of-a-better-name-server-dns-explained](https://speakerdeck.com/roguelynn/europython-2014-for-lack-of-a-better-name-server-dns-explained)

Distibutd storage for reosurce records
Record: lable, class, type and data

scaPy for sniffing

port udp:53

Trailing Dot?
Absolute with trailing dot
Relative without trailing dot

To follow DNS traffice

    dig +trace python.org

CName record - other name, another lookup required
A record - ip
NS Record - delegate to another NS

DNS Spoofing
Can respond with spoofed names


dnsmap
local dns cache
run python dns

### Using DNS
DANE - Auth based on DNS
Binding certs to names

Service discovery.
SRV lookups for load balancing

DHT Ring
Distributd hash table - key value store
Uses TXT records
