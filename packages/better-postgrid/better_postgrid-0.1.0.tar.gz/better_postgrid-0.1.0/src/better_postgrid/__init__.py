"""A client library for accessing PostGrid Print & Mail"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
