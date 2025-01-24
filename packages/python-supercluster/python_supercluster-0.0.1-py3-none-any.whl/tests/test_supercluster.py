import pytest
from python_supercluster import SuperCluster
from .fixtures import features

def test_generate_clusters_zoom_2():
  supercluster = SuperCluster().load(features)
  assert len(supercluster.get_clusters([-180, -90, 180, 90], 2)) == 100
  
  
def test_generate_clusters_zoom_3():
  supercluster = SuperCluster().load(features)
  assert len(supercluster.get_clusters([-180, -90, 180, 90], 3)) == 137
  
def test_get_right_zoom_origin():
  supercluster = SuperCluster().load(features)
  zoom = 3
  cluster = supercluster.get_clusters([-180, -90, 180, 90], zoom)[1]
  assert supercluster._get_origin_zoom(cluster["id"]) == zoom + 1
  
def test_get_right_leaves():
  supercluster = SuperCluster().load(features)
  cluster = supercluster.get_clusters([-180, -90, 180, 90], 3)[1]
  assert len(supercluster.get_leaves(cluster["id"], 10, 0)) == 2
