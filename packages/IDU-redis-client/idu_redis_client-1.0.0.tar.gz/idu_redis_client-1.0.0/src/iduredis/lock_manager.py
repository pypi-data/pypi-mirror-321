from aioredlock import Aioredlock, Lock, LockError
from iduconfig import Config
from loguru import logger


class LockManager:
    def __init__(self, config: Config):
        self.lock_manager = Aioredlock(
            [{"host": config.get("REDIS_HOST"), "port": int(config.get("REDIS_PORT")), "db": 0}]
        )
        self._lock: Lock | None = None

    async def is_locked(self, resource: str | Lock) -> bool:
        """Check if resource is locked.
        Positive locking can work better eliminating several race conditions.

        Args:
            resource (str | Lock): name of resource (this is different from queue names).
        Returns:
            bool: True if resource is locked otherwise False.
        """

        return await self.lock_manager.is_locked(resource)

    async def lock(self, resource: str, lock_timeout: int):
        """Lock resource for certain timeout.

        Args:
            resource (str): name of resource (this is different from queue names).
            lock_timeout (int): lock timeout in seconds.
        """

        self._lock = await self.lock_manager.lock(resource, lock_timeout=lock_timeout)
        if not self._lock.valid:
            self._lock = None
            raise LockError
        return self._lock

    async def valid(self) -> bool:
        """Check if lock you acquired is valid.

        Returns:
            bool: True if lock is valid otherwise False.
        """

        if self._lock:
            return self._lock.valid
        return False

    async def unlock(self):
        """Unlock resource."""

        if self._lock:
            try:
                await self.lock_manager.unlock(self._lock)
            except BaseException as e:
                logger.error(e)
            self._lock = None
