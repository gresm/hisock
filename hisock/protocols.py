"""
This module contains different additional connection protocols that can be used by client an server.

====================================
...
====================================
"""

from __future__ import annotations
from abc import ABC, abstractmethod

import socket


class BaseProtocol(ABC):
    """
    Base protocol class, subclass to create custom behavoiurs.
    """

    sock: socket.socket
    _fill_from_socket: bool = True

    def __init__(self) -> None:
        super().__init__()
        self.sock = self._create_socket()

    def __getattr__(self, name):
        if self._fill_from_socket:
            return getattr(self.sock, name)
        else:
            raise AttributeError

    # def setblocking()
    @abstractmethod
    def _create_socket(self) -> socket.socket:
        """Create socket for the protocol

        :return: socket
        :rtype: socket.socket
        """


class TCP_IP4_Protocol(BaseProtocol):
    """
    Default TCP_IP protocol for IPv4.
    """

    def _create_socket(self) -> socket.socket:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
