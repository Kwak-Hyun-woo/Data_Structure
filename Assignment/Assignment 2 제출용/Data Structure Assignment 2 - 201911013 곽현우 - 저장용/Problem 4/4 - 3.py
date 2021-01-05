#4 - 3 answer)
    def add_first(self, e):
    """Insert element e at the front of the list and return new Position."""
        if self.is_empty():
            return self._insert_between(e, self._header, self._trailer)
        else:
            return self.add_before(self.first(), e)

    def add_last(self, e):
     """Insert element e at the back of the list and return new Position."""
        if self.is_empty():
            return self._insert_between(e, self._header, self._trailer)
        else:
            return self.add_after(self.last(), e)
