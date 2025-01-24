#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InXE-64K'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InXE-64K"

    @property
    def type(self):
        return 1

    @property
    def revision(self):
        return "39.0"
