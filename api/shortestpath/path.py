class Path:
    """
    Path of source to destination
    """

    src = None
    dst = None
    list_sub_path = None
    total_cost = None


    def __init__(self, src, dst, list_sub_path, total_cost):
        self.src = src
        self.dst = dst
        self.list_sub_path = list_sub_path
        self.total_cost = total_cost

    def __str__(self):
        return "Path:\n" \
               "src: {0}\n" \
               "dst: {1}\n" \
               "list_sub_path: {2}\n" \
               "total_cost: {3}\n".format(self.src, self.dst, self.list_sub_path, self.total_cost)


