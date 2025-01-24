IDU Redis Client is dedicated for Redis use as message and status broker.

```python
from iduredis import RedisManager, LockManager
from iduconfig import Config

config = Config()
redis_manager = RedisManager(config)
lock_manager = LockManager(config)

redis_manager.push_to_list("MY_QUEUE", "MY_EVENT_123")
redis_manager.add_to_stream("STATUS_EVENT:123", {"state": "started"})
redis_manager.get_last_stream_data("STATUS_EVENT:123", b"state")
```