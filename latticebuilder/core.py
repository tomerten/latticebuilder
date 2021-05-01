import queue
import re
from copy import deepcopy


class LatticeBuilderLine:
    """Class for building lattice tables"""

    def __init__(self):
        self.lattice = []
        self.definitions = []
        self.table = None

        # roll back queue
        self.history = queue.LifoQueue()

    def add_def(self, _def):
        """Add definitions dictionary to the definitions"""
        # roll back
        self.history.put(
            (deepcopy(self.definitions), deepcopy(self.lattice), deepcopy(self.table))
        )

        # length can not be zero - necessary for pos calc
        assert list(_def.values())[0].get("L", None) is not None

        # update definitions dicts
        self.definitions = {**self.definitions, **_def}

        # attempt update table
        self._update_table()
