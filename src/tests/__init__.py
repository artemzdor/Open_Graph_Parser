import asyncio

import pytest


@pytest.yield_fixture(scope='session')
def event_loop():
    yield asyncio.get_event_loop()
