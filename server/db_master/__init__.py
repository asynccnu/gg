import redis

db = redis.StrictRedis(host='redis-master', port=6388, db=0)
