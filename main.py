import praw
from dotenv import load_dotenv
from pathlib import Path  # python3 only


def get_subreddits(filename):
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def main():
    # parse the subreddits file
    subreddits = get_subreddits('subreddits.txt')
    print(subreddits)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


if __name__ == "__main__":
    main()
