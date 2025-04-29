import redis

# Replace with PC A's IP address
redis_host = '192.168.1.110'  # IP of PC A

redis_port = 6379

try:
    r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    # Set a key
    r.set('greeting', 'Hello from PC B!')
    r.set('aaaa1', 'UGGGGGG!')

    # Get the key
    value = r.get('greeting')
    value2 = r.get('aaaa1')
    print(f"Value from Redis: {value}, {value2}")

except redis.ConnectionError as e:
    print(f"Connection failed: {e}")
