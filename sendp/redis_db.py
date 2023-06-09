import redis

class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)
    
    def set(self, key, fields):
        """
        存储键值对
        """
        return self.client.hmset(key, fields)
        
    def get(self, key):
        """
        获取键对应的值
        """
        fields = self.client.hgetall(key)
        return fields
    
    def delete(self, key):
        """
        删除指定的键值对
        """
        return self.client.delete(key)
    
    def update(self, key, fields):
        """
        更新指定的键值对，如果不存在则创建
        """
        return self.client.hmset(key, fields)
