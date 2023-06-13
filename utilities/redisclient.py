from __future__ import print_function

import redis
from typing import Any, Dict


class RedisClient:
    def __init__(
        self,
        host="localhost",  # type: str
        port=6379,  # type: int
        db_id=0,  # type: int
    ):
        # type: (str, int, int) -> None
        self.client = redis.Redis(host=host, port=port, db=db_id)

    def hset(
        self,
        key,  # type: str
        fields,  # type: Dict[str, Any]
    ):
        # type: (str, Dict[str, Any]) -> bool
        """
        Set key with value of fields
        """
        return self.client.hmset(key, fields)

    def hget(
        self,
        key,  # type: str
    ):
        # type: (str) -> Dict[bytes, bytes]
        """
        Get value of key
        """
        fields = self.client.hgetall(key)
        return fields

    def hdel(
        self,
        key,  # type: str
    ):
        # type: (str) -> int
        """
        Delete key
        """
        return self.client.delete(key)

    def hupd(
        self,
        key,  # type: str
        fields,  # type: Dict[str, Any]
    ):
        # type: (str, Dict[str, Any]) -> bool
        """
        Update key with value of fields
        """
        return self.client.hmset(key, fields)


# We instantiate RedisClient here because what we want
# is a singleton of RedisClient that could be reuse everywhere
redisclient = RedisClient(db_id=0)
