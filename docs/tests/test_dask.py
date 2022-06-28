from dask_jobqueue import PBSCluster
cluster = PBSCluster()
cluster.scale(jobs=10)    # Deploy ten single-node jobs

from dask.distributed import Client
client = Client(cluster)  # Connect this local process to remote workers


import dask.array as da
import numpy as np
import dask

# on peut transformer un fonction en 
# génération de noeud de graph
@dask.delayed
def inc(x):
   return x + 1

data = np.arange(100_000).reshape(200, 500)
a = da.from_array(data, chunks=(100, 100))
m = inc( np.sin( a ) ).mean()
m.visualize()

print( m.compute() )
