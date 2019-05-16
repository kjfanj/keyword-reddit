class Posts:
    # static
    ids = []

    def add_post(self, id):
        Posts.ids.append(id)

    def check_if_id_exists(self, id):
        return True if id in Posts.ids else False

    def print_stat(self):
        print("Size {}".format(len(Posts.ids)))
        print(Posts.ids)
