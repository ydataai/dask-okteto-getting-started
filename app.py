from dask_kubernetes import KubeCluster

cluster = KubeCluster.from_yaml(r'worker-spec.yml')
cluster.adapt()

# Example usage
from dask.distributed import Client
import dask.array as da

# Connect Dask to the cluster
client = Client(cluster)

# Create a large array and calculate the mean
array = da.ones((1000, 1000, 1000))
print(array.mean().compute())  # Should print 1.0