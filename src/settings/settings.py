from environs import Env

env: Env = Env()

# Read .env into os.environ
env.read_env()


def validate_port(port: int) -> bool:
    return 0 < port <= 65535


DEBUG: bool = env.bool('DEBUG', False)


# server config
SERVER_HOST: str = env.str('SERVER_HOST', default='0.0.0.0')
SERVER_PORT: int = env.int('SERVER_PORT', default=8080, validate=validate_port)


if __name__ == '__main__':
    from pprint import pprint
    pprint(env.dump())
