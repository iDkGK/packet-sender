import redis
from typing import Any


class RedisClient:
    def __init__(
        self, host: str = "localhost", port: int = 6379, db_id: int = 0
    ) -> None:
        self.client = redis.Redis(host=host, port=port, db=db_id)

    def hset(self, key: str, fields: dict[str, Any]) -> bool:
        """
        Set key with value of fields
        """
        return self.client.hmset(key, fields)

    def hget(self, key: str) -> dict[bytes, bytes]:
        """
        Get value of key
        """
        fields = self.client.hgetall(key)
        return fields

    def hdel(self, key: str) -> int:
        """
        Delete key
        """
        return self.client.delete(key)

    def hupd(self, key: str, fields: dict[str, Any]) -> bool:
        """
        Update key with value of fields
        """
        return self.client.hmset(key, fields)


# We instantiate RedisClient here because what we want
# is a singleton of RedisClient that could be reuse everywhere
redisclient = RedisClient(db_id=0)
