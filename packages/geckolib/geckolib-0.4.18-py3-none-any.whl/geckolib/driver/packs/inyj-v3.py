#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InYJ-V3'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InYJ-V3"

    @property
    def type(self):
        return 12

    @property
    def revision(self):
        return "39.0"
