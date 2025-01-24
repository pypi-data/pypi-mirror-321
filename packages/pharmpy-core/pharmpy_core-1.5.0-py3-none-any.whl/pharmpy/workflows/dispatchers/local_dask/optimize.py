import dask


def optimize_task_graph_for_dask_distributed(client, graph):
    from dask.distributed import Future

    optimized = {key: _scatter_computation(Future, client, value) for key, value in graph.items()}
    from dask.optimization import fuse

    fused = fuse(optimized)[0]
    return fused


def _scatter_computation(Future, client, computation):
    # NOTE: According to dask's graph spec (https://docs.dask.org/en/stable/spec.html):
    # A computation may be one of the following:
    #  - Any key present in the Dask graph like 'x'
    #  - Any other value like 1, to be interpreted literally
    #  - A task like (inc, 'x') (see below)
    #  - A list of computations, like [1, 'x', (inc, 'x')]
    if isinstance(computation, tuple):
        if len(computation) == 0:  # Avoid further interpreting empty argument
            return computation
        else:
            return (
                computation[0],
                *map(lambda c: _scatter_computation(Future, client, c), computation[1:]),
            )

    if isinstance(computation, list):
        return list(map(lambda c: _scatter_computation(Future, client, c), computation))

    return _scatter_value(Future, client, computation)


def _scatter_value(Future, client, value):
    # TODO: We could automatically compute whether object size is above
    # threshold with a slight twist on https://stackoverflow.com/a/30316760
    if isinstance(value, (dict, int, str, float, bool, range, Future)) or callable(value):
        return value
    else:
        dask_version = tuple(int(i) for i in dask.__version__.split('.'))
        if dask_version >= (2024, 2, 1):
            # This is a workaround for https://github.com/dask/distributed/issues/8576
            future = client.scatter(value, hash=False)
        else:
            future = client.scatter(value)
        return future
