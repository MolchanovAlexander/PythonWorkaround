import json
import os
import redis

redis_host = os.getenv("PUBLIC_IP")
redis_port = 6379
print("ip is present:", redis_host is not None)

redis_client = None
try:
    redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True,
                    socket_connect_timeout=6,  # seconds to wait when connecting
                    socket_timeout=6,  # seconds to wait for read/write
                    )
except redis.ConnectionError as e:
    print(f"Connection failed: {e}")

def set_key_value(key, value):
    try:
        redis_client.set(key, json.dumps(value))
    except redis.ConnectionError as ex:
        print(f"Connection failed: {ex}")


def get_value_by_key(key):
    try:
        return json.loads(redis_client.get(key))
    except redis.ConnectionError as ex:
        print(f"Connection failed: {ex}")