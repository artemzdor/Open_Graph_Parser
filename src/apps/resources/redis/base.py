import asyncio
from typing import Optional, List, TYPE_CHECKING

from src.settings import settings
from aioredis import Redis


class RedisApi:
    redis: Optional[Redis]
    FIRST_TTL_SEC: int = 7 * 60
    PREFIX: str = 'ids:'

    def __init__(self):
        self.redis = None

    async def setup(self) -> 'RedisApi':

        from aioredis import create_redis_pool

        try:
            self.redis = await create_redis_pool(
                f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
                minsize=settings.REDIS_MIN_POOL_SIZE,
                maxsize=settings.REDIS_MAX_POOL_SIZE,
                db=settings.REDIS_DB
            )
        except Exception as e:
            print(f'Redis [{settings.REDIS_HOST}:{settings.REDIS_PORT}] unavailable, due to {e}')
        return self

    async def __aenter__(self) -> 'RedisApi':
        return await self.setup()

    async def teardown(self) -> None:
        self.redis and await self.redis.wait_closed()

    async def __aexit__(self, exc_type, exc_value, exc_tb) -> None:
        await self.teardown()

    @classmethod
    def get_ttl_default(cls, ttl=FIRST_TTL_SEC):
        return ttl

    @classmethod
    def create_composite_key(cls, keys: List[str]) -> str:
        return cls.PREFIX + ':'.join(keys)

    @classmethod
    def key_map(cls, key: str) -> str:
        return f'{cls.PREFIX}{key}'

    @classmethod
    def get_split_key_composite(cls, composite_key: str) -> List[str]:
        return [cls.key_map(key=i) for n, i in enumerate(composite_key.split(':')) if n != 0]

    async def set_split_keys(self, composite_key: str, ttl: int) -> None:
        for key in self.get_split_key_composite(composite_key=composite_key):
            await self.redis.set(key=key, value=composite_key, expire=ttl)

    async def get_composite_key(self, key: Optional[str], keys: Optional[List[str]] = None) -> Optional[str]:
        if key:
            composite_key: Optional[bytes] = await self.redis.get(key=self.key_map(key=key))
            if composite_key:
                return composite_key.decode('utf-8')
            return composite_key
        if keys:
            for key in keys:
                composite_key: Optional[bytes] = await self.redis.get(key=self.key_map(key=key))
                if composite_key:
                    return composite_key.decode('utf-8')
                return composite_key


if __name__ == '__main__':

    async def main():
        redis: RedisApi = await RedisApi().setup()
        keys: List[str] = ['2', '3', '4']
        composite_key: str = redis.create_composite_key(keys=keys)

        await redis.set_split_keys(
            composite_key=composite_key,
            ttl=redis.get_ttl_default()
        )

        print(composite_key)
        ck_1: Optional[str] = await redis.get_composite_key(key='1')
        ck_2: Optional[str] = await redis.get_composite_key(key='2')

        assert ck_1 == None
        assert ck_2 == redis.PREFIX + '2:3:4'
        print(ck_2)


    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    loop.run_until_complete(task)
