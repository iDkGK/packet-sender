import redis
from typing import Any


class RedisClient:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def hset(self, key: str, fields: dict[str, Any]):
        """
        Set key with value of fields
        """
        return self.client.hmset(key, fields)

    def hget(self, key: str):
        """
        Get value of key
        """
        fields = self.client.hgetall(key)
        return fields

    def hdel(self, key: str):
        """
        Delete key
        """
        return self.client.delete(key)

    def hupd(self, key: str, fields: dict[str, Any]):
        """
        Update key with value of fields
        """
        return self.client.hmset(key, fields)
