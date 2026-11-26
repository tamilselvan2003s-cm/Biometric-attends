"""Compatibility WSGI entrypoint forwarding to config.wsgi."""
from config.wsgi import application

__all__ = ["application"]
