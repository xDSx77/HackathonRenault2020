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

        # Those Are list because they can be multiple SubPaths
        # This is mainly the case in subway, where first subpath will be on foot to join the station
        # then second subpath in metro, etc.
        #
        # This can be weird for nodes_paths, as nodes are represented as list,
        # so is a subpath, so it will be a list(list(list()s))
        self.list_sub_path = list_sub_path
        self.transportation = []
        self.nodes_path = []
        self.nodes_costs = []

        self.set_path_values_from_list_sub_path(list_sub_path)
        self.total_cost = total_cost

    def set_path_values_from_list_sub_path(self, list_sub_path: dict) -> None:
        for sub_path in list_sub_path:

            # This is done cos their format is weird, trust me
            path = sub_path["cars"][0]

            self.transportation.append(path["id"])
            self.nodes_path.append(path["paths"])
            self.nodes_costs.append(path["costs"])

    def __str__(self):
        return "Path:\n" \
               "src: {0}\n" \
               "dst: {1}\n" \
               "medium of transportation: {2}\n" \
               "nodes path: {3}\n" \
               "nodes costs: {4}\n" \
               "list_sub_path: {5}\n" \
               "total_cost: {6}\n".format(self.src,
                                          self.dst,
                                          self.transportation,
                                          self.nodes_path,
                                          self.nodes_costs,
                                          self.list_sub_path,
                                          self.total_cost)


