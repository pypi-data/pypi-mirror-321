import math
import numpy as np
from .kdbush import KDBush

OFFSET_ZOOM = 2
OFFSET_ID = 3
OFFSET_PARENT = 4
OFFSET_NUM = 5
OFFSET_PROP = 6

DEFAULT_OPTIONS = dict(
    {
        "min_zoom": 1,
        "max_zoom": 16,
        "min_points": 2,
        "radius": 40,
        "extent": 512,
        "node_size": 64,
        "log": False,
        "generate_id": False,
    }
)


def get_cluster_properties(data, i, cluster_props):
    count = data[i][OFFSET_NUM]

    prop_index = data[i][OFFSET_PROP]
    properties = {} if prop_index == -1 else cluster_props[prop_index]
    return {
        **properties,
        "cluster": True,
        "cluster_id": data[i][OFFSET_ID],
        "point_count": count,
    }


def lng_x(lng):
    return lng / 360 + 0.5


def lat_y(lat):
    if lat == 90:
        return 0
    if lat == -90:
        return 1
    sin = math.sin(lat * math.pi / 180)
    y = 0.5 - 0.25 * math.log((1 + sin) / (1 - sin)) / math.pi
    if y < 0:
        return 0
    if y > 1:
        return 1
    return y


# spherical mercator to longitude/latitude
def x_lng(x):
    return (x - 0.5) * 360


def y_lat(y):
    y2 = (180 - y * 360) * math.pi / 180
    return 360 * math.atan(math.exp(y2)) / math.pi - 90


class SuperCluster:
    def __init__(self, options = DEFAULT_OPTIONS):
        self.options = {**DEFAULT_OPTIONS, **options}
        # self.trees = np.empty((self.options["max_zoom"] + 2, 5))
        self.trees = list([None] * (self.options["max_zoom"] + 2))

    def load(self, points):
        self.points = points

        data = [[lng_x(item[0]), lat_y(item[1])] + [math.inf, i, -1, 1] for i, item in enumerate(points)]
        tree = self._create_tree(data)
        self.trees[self.options["max_zoom"] + 1] = tree
        for z in range(self.options["max_zoom"], self.options["min_zoom"], -1):
            tree = self._create_tree(self._cluster(tree, z))
            self.trees[z] = tree

        return self

    def _create_tree(self, data: np.array):
        tree = KDBush(points=data, node_size=self.options["node_size"], array_dtype=np.float32)
        return tree

    def _cluster(self, tree, zoom):
        r = self.options["radius"] / (self.options["extent"] * math.pow(2, zoom))
        data = tree.points
        next_data = list()
        for i in range(len(data)):
            if data[i][OFFSET_ZOOM] <= zoom:
                continue
            data[i][OFFSET_ZOOM] = zoom

            x = data[i][0]
            y = data[i][1]
            neighbor_ids = tree.within(x, y, r)

            num_points_origin = data[i][OFFSET_NUM]
            num_points = num_points_origin
            for neighbor_id in neighbor_ids:
                if data[neighbor_id][OFFSET_ZOOM] > zoom:
                    num_points += data[neighbor_id][OFFSET_NUM]

            if num_points > num_points_origin and num_points >= self.options["min_points"]:
                wx = x * num_points_origin
                wy = y * num_points_origin

                object_id = ((i or 0) << 5) + (zoom + 1) + len(self.points)

                for neighbor_id in neighbor_ids:
                    if data[neighbor_id][OFFSET_ZOOM] <= zoom:
                        continue
                    data[neighbor_id][OFFSET_ZOOM] = zoom

                    num_points2 = data[neighbor_id][OFFSET_NUM]
                    wx += data[neighbor_id][0] * num_points2
                    wy += data[neighbor_id][1] * num_points2

                    data[neighbor_id][OFFSET_PARENT] = object_id
                data[i][OFFSET_PARENT] = object_id
                next_data.append([wx / num_points, wy / num_points, math.inf, object_id, -1, num_points])
            else:
                next_data.append(data[i])
                if num_points > 1:
                    for neighbor_id in neighbor_ids:
                        if data[neighbor_id][OFFSET_ZOOM] <= zoom:
                            continue
                        data[neighbor_id][OFFSET_ZOOM] = zoom
                        next_data.append(data[neighbor_id])

        return np.array(next_data, np.float32)

    def format_point_or_cluster(self, point_or_cluster):
        return (
            {
                "id": np.uint32(point_or_cluster[OFFSET_ID]),
                "count": point_or_cluster[OFFSET_NUM],
                "lng": x_lng(point_or_cluster[0]),
                "lat": y_lat(point_or_cluster[1]),
                "cluster": True,
            }
            if point_or_cluster[OFFSET_NUM] > 1
            else {
                "id": np.uint32(point_or_cluster[OFFSET_ID]),
                "count": 0,
                "lng": self.points[np.uint32(point_or_cluster[OFFSET_ID])][0],
                "lat": self.points[np.uint32(point_or_cluster[OFFSET_ID])][1],
                "cluster": False,
            }
        )

    def get_clusters(self, bbox, zoom):
        min_lng = ((bbox[0] + 180) % 360 + 360) % 360 - 180
        min_lat = max(-90, min(90, bbox[1]))
        max_lng = 180 if bbox[2] == 180 else ((bbox[2] + 180) % 360 + 360) % 360 - 180
        max_lat = max(-90, min(90, bbox[3]))

        if bbox[2] - bbox[0] >= 360:
            min_lng = -180
            max_lng = 180
        elif min_lng > max_lng:
            eastern_hem = self.get_clusters([min_lng, min_lat, 180, max_lat], zoom)
            western_hem = self.get_clusters([-180, min_lat, max_lng, max_lat], zoom)
            return eastern_hem + western_hem
        tree = self.trees[self._limit_zoom(zoom)]
        ids = tree.range(lng_x(min_lng), lat_y(max_lat), lng_x(max_lng), lat_y(min_lat))
        clusters = list()
        for object_id in ids:
            point_or_cluster = tree.points[object_id]
            clusters.append(self.format_point_or_cluster(point_or_cluster))
        return clusters

    def _limit_zoom(self, zoom):
        return max(self.options["min_zoom"], min(math.floor(zoom), self.options["max_zoom"] + 1))

    def get_leaves(self, cluster_id, limit, offset):
        limit = limit or 10
        offset = offset or 0

        leaves = []
        self._append_leaves(leaves, cluster_id, limit, offset, 0)

        return leaves

    def _append_leaves(self, result, cluster_id, limit, offset, skipped):
        children = self.get_children(cluster_id)
        for child in children:
            if child["cluster"] is True:
                if skipped + child["count"] <= offset:
                    skipped += child["count"]
                else:
                    skipped = self._append_leaves(result, child["id"], limit, offset, skipped)
            elif skipped < offset:
                skipped += 1
            else:
                result.append(child)

            if len(result) == limit:
                break
        return skipped

    def get_children(self, cluster_id):
        origin_id = self._get_origin_id(cluster_id)
        origin_zoom = self._get_origin_zoom(cluster_id)
        error_msg = "No cluster with the specified id"

        tree = self.trees[origin_zoom]
        if tree is None:
            raise Exception(error_msg)

        if origin_id >= len(tree.points):
            raise Exception(error_msg)

        r = self.options["radius"] / (self.options["extent"] * math.pow(2, origin_zoom - 1))
        x = tree.points[origin_id][0]
        y = tree.points[origin_id][1]

        ids = tree.within(x, y, r)
        children = list()
        for id in ids:
            point_or_cluster = tree.points[id]
            if point_or_cluster[OFFSET_PARENT] == cluster_id:
                children.append(self.format_point_or_cluster(point_or_cluster))
        if len(children) == 0:
            raise Exception(error_msg)
        return children

    def _get_origin_id(self, cluster_id):
        return (cluster_id - len(self.points)) >> 5

    def _get_origin_zoom(self, cluster_id):
        return (cluster_id - len(self.points)) % 32
