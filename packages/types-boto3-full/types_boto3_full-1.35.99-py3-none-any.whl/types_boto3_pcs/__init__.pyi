"""
Main interface for pcs service.

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_pcs import (
        Client,
        ListClustersPaginator,
        ListComputeNodeGroupsPaginator,
        ListQueuesPaginator,
        ParallelComputingServiceClient,
    )

    session = Session()
    client: ParallelComputingServiceClient = session.client("pcs")

    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compute_node_groups_paginator: ListComputeNodeGroupsPaginator = client.get_paginator("list_compute_node_groups")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```

Copyright 2025 Vlad Emelianov
"""

from .client import ParallelComputingServiceClient
from .paginator import ListClustersPaginator, ListComputeNodeGroupsPaginator, ListQueuesPaginator

Client = ParallelComputingServiceClient

__all__ = (
    "Client",
    "ListClustersPaginator",
    "ListComputeNodeGroupsPaginator",
    "ListQueuesPaginator",
    "ParallelComputingServiceClient",
)
