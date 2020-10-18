from environs import Env

env: Env = Env()

# Read .env into os.environ
env.read_env()


def validate_port(port: int) -> bool:
    return 0 < port <= 65535


DEBUG: bool = env.bool('DEBUG', False)


# server config
SERVER_HOST: str = env.str('SERVER_HOST', default='0.0.0.0')
SERVER_PORT: int = env.int('SERVER_PORT', default=50051, validate=validate_port)


REDIS_HOST: str = env.str('REDIS_HOST', default='redis')
REDIS_PORT: int = env.int('REDIS_PORT', default=6379, validate=validate_port)
REDIS_DB: int = env.int('REDIS_DB', default=6, validate=lambda n: n > 0)
REDIS_MIN_POOL_SIZE: int = env.int('REDIS_MIN_POOL_SIZE', default=5)
REDIS_MAX_POOL_SIZE: int = env.int('REDIS_MAX_POOL_SIZE', default=10)


if __name__ == '__main__':
    from pprint import pprint
    pprint(env.dump())
