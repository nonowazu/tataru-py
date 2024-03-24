from sys import exit
from os import environ

from dotenv import load_dotenv

from tataru.bot import get_bot


def main() -> int:
    bot = get_bot()

    bot.run(environ.get('DISCORD_TOKEN'))
    return 0

if __name__ == '__main__':
    load_dotenv()
    exit(main())