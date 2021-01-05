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

from tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        raise NotImplementedError('EXERCISE')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('EXERCISE')

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        """Hint: use _subtree_inorder() function for make recursion """
        raise NotImplementedError('EXERCISE')

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        raise NotImplementedError('EXERCISE')

    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()                                 # make inorder the default
