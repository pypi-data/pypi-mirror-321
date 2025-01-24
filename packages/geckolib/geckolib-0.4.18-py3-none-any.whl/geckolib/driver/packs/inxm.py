#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InXM'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InXM"

    @property
    def type(self):
        return 6

    @property
    def revision(self):
        return "39.0"
