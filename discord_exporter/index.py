from prometheus_client import Gauge, start_http_server, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR
import time
import requests
REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(REGISTRY._names_to_collectors['python_gc_objects_collected_total'])

s1 = Gauge('DISCORD_ONLINE', 'Online Users in the Discord')
s2 = Gauge('DISCORD_ALL', 'Users in the discord')

def srvcount():
    try:
        r = requests.get("https://discord.com/api/invite/3QDu47TkS2?with_counts=True")
        x = r.json()
    except Exception as e:
        print(e)
        return 0, 0
    return x["approximate_member_count"], x["approximate_presence_count"]

start_http_server(8760)
while True:
    e, a = srvcount()
    s1.set(a)
    s2.set(e)

    time.sleep(240)
