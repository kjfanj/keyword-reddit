

def get_subreddits(filename):
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def main():
    # parse the subreddits file
    subreddits = get_subreddits('subreddits.txt')
    print(subreddits)


if __name__ == "__main__":
    main()
