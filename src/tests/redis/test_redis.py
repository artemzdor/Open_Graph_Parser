from typing import List, TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    from src.apps.resources.redis.base import RedisApi


@pytest.mark.asyncio
class TestRedis:

    @pytest.mark.asyncio
    async def test_redis_keys(self, redis_api: 'RedisApi'):
        keys: List[str] = ["000", "111"]

        composite_key: str = redis_api.create_composite_key(keys=keys)

        assert composite_key == "ids:" + ":".join(keys)
        await redis_api.set_split_keys(composite_key=composite_key, ttl=redis_api.get_ttl_default())

        for key_iter in keys:
            ck_iter = await redis_api.get_composite_key(key=key_iter)
            assert ck_iter == composite_key

        assert ["ids:000", "ids:111"] == redis_api.get_split_key_composite(composite_key=composite_key)
