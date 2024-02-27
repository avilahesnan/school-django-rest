import redis

try:
    r = redis.Redis(host='localhost', port=6379)
    r.ping()
    print('Connection to Redis established successfully!')
except redis.ConnectionError:
    print('Unable to connect to Redis.')
