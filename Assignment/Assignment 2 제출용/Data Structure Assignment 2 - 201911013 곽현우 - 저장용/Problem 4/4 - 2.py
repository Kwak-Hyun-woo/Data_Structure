#4 - 2 answer)
def __reverse__(self):
    """Generate a forward iteration of the elements of the list."""
    cursor = self.last()
    while cursor is not None:
      yield cursor.element()
      cursor = self.before(cursor)
