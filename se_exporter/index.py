from prometheus_client import Gauge, start_http_server, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR
import a2s
import socket
import time
REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(REGISTRY._names_to_collectors['python_gc_objects_collected_total'])

def query(port):
    try:
        addr = "68.132.88.209", int(port)
        resp = a2s.info(addr)
    except socket.timeout:
        return 0
    return int(resp.player_count)

s1 = Gauge('S1', 'Stiglord Server Count')
s2 = Gauge('S2', 'Avalon Server Count')
s3 = Gauge('S3', 'Roach Server Count')
s4 = Gauge('S4', 'Dead Worlds Server Count')
s5 = Gauge('S5', 'Paradise Server Count')
s6 = Gauge('S6_ALL', 'All Server Count')

start_http_server(8750)
while True:
    s1a = query(27024)
    s1.set(s1a)

    s2a = query(27025)
    s2.set(s2a)

    s3a = query(27023)
    s3.set(s3a)

    s4a = query(27026)
    s4.set(s4a)

    s5a = query(27027)
    s5.set(s5a)

    s6a = s1a + s2a + s3a + s4a + s5a
    s6.set(s6a)

    time.sleep(5)
