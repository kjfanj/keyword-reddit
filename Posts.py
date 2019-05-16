class Posts:
    # static variable that keep track of sent posts
    ids = []

    def add_post(self, id):
        """
        add the id to static ids, need to check if id existed in ids
        """
        Posts.ids.append(id)

    def check_if_id_exists(self, id):
        """
        return True if id existed in static ids, else False
        """
        return True if id in Posts.ids else False

    def print_stat(self):
        """
        to see how many total is sent
        """
        print("Total sent: {}".format(len(Posts.ids)))
