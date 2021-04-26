import redis
REDIS_HOST = '192.168.185.28'
REDIS_PORT = 6379
REDIS_DB = 12
REDIS_PASSWORD = ''



class RedisBase(object):
    def __init__(self,REDIS_HOST, REDIS_DB, REDIS_PORT=6379,REDIS_PASSWORD=''):
        self.REDIS_HOST = REDIS_HOST
        self.REDIS_PORT = REDIS_PORT
        self.REDIS_DB = REDIS_DB
        self.REDIS_PASSWORD = REDIS_PASSWORD
        self.pool = redis.ConnectionPool(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            decode_responses=True)
        self.redis_c = redis.Redis(connection_pool=self.pool)

    def getInit(self):
        try:
            if self.redis_c.ping():
                return redis
        except Exception:
            return None
        return None


    def ttl(self, key):
        return self.redis_c.ttl(key)


    def get(self, key):
        return self.redis_c.get(key)


    def set(self, key, val, expire=None):
        if not expire:
            return self.redis_c.set(key, val)
        return self.redis_c.setex(name=key, time=expire, value=val)


    def delete(self, key):
        if self.redis_c.exists(key):
            return self.redis_c.delete(key)
        else:
            return True


    def exist(self, key):
        return self.redis_c.exists(key)


    def sadd(self, key, val):
        return self.redis_c.sadd(key, val)


    def sismember(self, key, val):
        return self.redis_c.sismember(key, val)


    def srem(self, key, val):
        return self.redis_c.srem(key, val)


    def smembers(self, key):
        return self.redis_c.smembers(key)


    def hset(self, name, key, val):
        return self.redis_c.hset(name, key, val)

    def publish(self, channel, msg):
        return self.redis_c.publish(channel, msg)

    def lpush(self, name, val):
        return self.redis_c.lpush(name, val)



