"""
Main interface for appflow service.

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_appflow import (
        AppflowClient,
        Client,
    )

    session = Session()
    client: AppflowClient = session.client("appflow")
    ```

Copyright 2025 Vlad Emelianov
"""

from .client import AppflowClient

Client = AppflowClient

__all__ = ("AppflowClient", "Client")
