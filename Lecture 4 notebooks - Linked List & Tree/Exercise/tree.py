# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#        Data Structures and Algorithms in Python
#        Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#        John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.    If not, see <http://www.gnu.org/licenses/>.

import collections

class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')
            
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)                        # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        raise NotImplementedError('EXERCISE')

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        raise NotImplementedError('EXERCISE')

    def is_empty(self):
        """Return True if the tree is empty."""
        raise NotImplementedError('EXERCISE')

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        raise NotImplementedError('EXERCISE')

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        raise NotImplementedError('EXERCISE')

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():                                                # use same order as positions()
            yield p.element()                                                    # but yield each element

    def positions(self):
        """Generate an iteration of the tree's positions. Hint: use preorder or postoder to iterate"""
        raise NotImplementedError('EXERCISE')

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        raise NotImplementedError('EXERCISE')

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        raise NotImplementedError('EXERCISE')

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        raise NotImplementedError('EXERCISE')

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        raise NotImplementedError('EXERCISE')