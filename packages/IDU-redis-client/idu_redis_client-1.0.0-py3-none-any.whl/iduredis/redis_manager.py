from typing import Any

from redis.asyncio import Redis

from iduconfig import Config


class RedisManager:
    def __init__(self, config: Config):
        self.config = config
        self.redis = Redis(
            host=self.config.get("REDIS_HOST"),
            port=int(self.config.get("REDIS_PORT")),
            db=0,
        )

    async def push_to_list(self, key: str, value: str):
        """Put event into list queue.

        Args:
            key (str): name of queue.
            value (str): name of event.
        """
        res = await self.redis.rpush(key, value)
        return res

    async def get_message(self, key: str) -> str | None:
        """Get message from top of queue and delete it.

        Args:
            key (str): name of queue.
        Returns:
            str | None: `str` if queue is not empty, otherwise `None`.
        """

        result = await self.redis.lpop(key)
        return result.decode("utf-8") if result else None

    async def get_first_message(self, key: str) -> str | None:
        """Get message from top of queue without deleting.

        Args:
            key (str): name of queue.
        Returns:
            str | None: `str` if queue is not empty, otherwise `None`.
        """

        res = await self.redis.lrange(key, 0, 0)
        return None if len(res) == 0 else res[0].decode("utf-8")

    async def save_bytes(self, key: str, value: bytes):
        """Save bytes into STRING structure.

        Args:
            key (str): name of queue.
            value (bytes): bytes.
        """

        return await self.redis.set(key, value)

    async def get_bytes(self, key: str) -> Any:
        """Get bytes from STRING structure.

        Args:
            key (str): name of queue.
        """

        return await self.redis.get(key)

    async def get_string_list(self) -> list[str]:
        """Get list of keys in STRING structure.

        Returns:
            list[str]: list of keys.
        """

        res = [string.decode("utf-8") for string in (await self.redis.scan(cursor=0, _type="STRING"))[1]]
        return res

    async def set_ttl(self, key: str, value: int):
        """Set Time-To-Expire parameter for event.

        Args:
            key (str): name of event.
            value (int): time to expire in seconds.
        """

        return await self.redis.expire(key, value)

    async def get_stream_list(self, _filter: str | None = None) -> list[str]:
        """Get list of keys in STREAM structure.

        Args:
            _filter (str): if keys should be filtered (by queue name as an example).
        Returns:
            list[str]: list of all keys or filtered keys if _filter is set.
        """

        res = [
            stream.decode("utf-8") for stream in (await self.redis.scan(cursor=0, _type="STREAM"))[1]
            if _filter and _filter in stream.decode("utf-8")
        ]
        return res

    async def add_to_stream(self, key: str, value: dict):
        """Put event into status queue.
        Key can contain more than one status updating previous one.

         Args:
             key (str): name of event.
             value (dict): key-value parameter for data in status event.
        """

        return await self.redis.xadd(key, value)

    async def get_last_stream_data(self, key: str, status_key: bytes) -> str:
        """Get latest status from status event.

        Args:
            key (str): name of event.
            status_key (bytes): this is a byte string parameter. Used to access data from key-value status data.
        Returns:
             str: value of status field.
        """

        tmp = await self.redis.xrevrange(key, count=1)
        res = tmp[0][1][status_key].decode("utf-8")
        return res

    async def len_of_stream(self, key: str):

        res = await self.redis.xlen(key)
        return res

    async def del_event(self, key: str):
        """Delete any queue or status event.

        Args:
            key (str): name of queue or status event.
        """

        return await self.redis.delete(key)
