#!/usr/bin/python3
""" module for rebel ints  and operators"""


class MyInt(int):

    """Invert int operators == and !=."""

    def __eq__(self, Val):
        """funcion that overrides  != behaviors."""
        return self.real != Val

    def __ne__(self, Val):
        """funcion that overrides  == behavior."""
        return self.real == Val
