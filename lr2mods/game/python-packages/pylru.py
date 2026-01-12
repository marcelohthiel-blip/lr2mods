
# Cache implementation with a Least Recently Used (LRU) replacement policy and
# a basic dictionary interface.

# Copyright (C) 2006-2022 Jay Hutchinson

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# The cache is implemented using a combination of a python dictionary (hash
# table) and a circular doubly linked list. Items in the cache are stored in
# nodes. These nodes make up the linked list. The list is used to efficiently
# maintain the order that the items have been used in. The front or head of
# the list contains the most recently used item, the tail of the list
# contains the least recently used item. When an item is used it can easily
# (in a constant amount of time) be moved to the front of the list, thus
# updating its position in the ordering. These nodes are also placed in the
# hash table under their associated key. The hash table allows efficient
# lookup of values by key.

import sys
from collections.abc import Mapping, Iterable

# Class for the node objects.
class _dlnode():
    __slots__ = ('empty', 'next', 'prev', 'key', 'value')

    def __init__(self) -> None:
        self.empty = True
        self.next = None
        self.prev = None
        self.key = None
        self.value = None


class LRUCache():
    def __init__(self, size, callback=None) -> None:
        self.callback = callback

        # Create an empty hash table.
        self.table = {}

        # Initialize the doubly linked list with one empty node. This is an
        # invariant. The cache size must always be greater than zero. Each
        # node has a 'prev' and 'next' variable to hold the node that comes
        # before it and after it respectively. Initially the two variables
        # each point to the head node itself, creating a circular doubly
        # linked list of size one.
        self.head = _dlnode()
        self.head.next = self.head
        self.head.prev = self.head

        self.list_size = 1

        # Now adjust the list to the desired size.
        self.size(size)

    def __len__(self) -> int:
        return len(self.table)

    def clear(self):
        for node in self.dli():
            node.empty = True
            node.key = None
            node.value = None

        self.table.clear()

    def __contains__(self, key) -> bool:
        return key in self.table

    # Looks up a value in the cache without affecting the cache's order.
    def peek(self, key):
        node = self.table[key]
        return node.value

    def __getitem__(self, key):
        node = self.table[key]

        # Update the list ordering. Move this node so that it directly
        # proceeds the head node. Then set the 'head' variable to it. This
        # makes it the new head of the list.
        self.mtf(node)
        self.head = node

        return node.value

    def get(self, key, default=None):
        if key not in self.table:
            return default

        return self[key]

    def __setitem__(self, key, value) -> None:
        # If any value is stored under 'key' in the cache already, then replace
        # that value with the new one.
        if key in self.table:
            node = self.table[key]

            # Replace the value.
            node.value = value

            # Update the list ordering.
            self.mtf(node)
            self.head = node

            return

        # Ok, no value is currently stored under 'key' in the cache. We need
        # to choose a node to place the new item in. There are two cases. If
        # the cache is full some item will have to be pushed out of the
        # cache. We want to choose the node with the least recently used
        # item. This is the node at the tail of the list. If the cache is not
        # full we want to choose a node that is empty. Because of the way the
        # list is managed, the empty nodes are always together at the tail
        # end of the list. Thus, in either case, by choosing the node at the
        # tail of the list our conditions are satisfied.

        # Since the list is circular, the tail node directly precedes the
        # 'head' node.
        node = self.head.prev

        # If the node already contains something we need to remove the old
        # key from the dictionary.
        if not node.empty:
            if self.callback is not None:
                self.callback(node.key, node.value)
            del self.table[node.key]

        # Place the new key and value in the node
        node.empty = False
        node.key = key
        node.value = value

        # Add the node to the dictionary under the new key.
        self.table[key] = node

        # We need to move the node to the head of the list. The node is the
        # tail node, so it directly precedes the head node due to the list
        # being circular. Therefore, the ordering is already correct, we just
        # need to adjust the 'head' variable.
        self.head = node

    def __delitem__(self, key) -> None:
        # Lookup the node, remove it from the hash table, and mark it as empty.
        node = self.table[key]
        del self.table[key]
        node.empty = True

        # Not strictly necessary.
        node.key = None
        node.value = None

        # Because this node is now empty we want to reuse it before any
        # non-empty node. To do that we want to move it to the tail of the
        # list. We move it so that it directly precedes the 'head' node. This
        # makes it the tail node. The 'head' is then adjusted. This
        # adjustment ensures correctness even for the case where the 'node'
        # is the 'head' node.
        self.mtf(node)
        self.head = node.next

    def update(self, *args, **kwargs):
        if len(args) > 0:
            other = args[0]
            if isinstance(other, Mapping):
                for key in other:
                    self[key] = other[key]
            elif hasattr(other, "keys"):
                for key in other:
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value

        for key, value in kwargs.items():
            self[key] = value

    __defaultObj = object()

    def pop(self, key, default=__defaultObj):
        if key in self.table:
            value = self.peek(key)
            del self[key]
            return value

        if default is self.__defaultObj:
            raise KeyError

        return default

    def popitem(self):
        # Make sure the cache isn't empty.
        if len(self) < 1:
            raise KeyError

        # Grab the head node
        node = self.head

        # Save the key and value so that we can return them.
        key = node.key
        value = node.value

        # Remove the key from the hash table and mark the node as empty.
        del self.table[key]
        node.empty = True

        # Not strictly necessary.
        node.key = None
        node.value = None

        # Because this node is now empty we want to reuse it before any
        # non-empty node. To do that we want to move it to the tail of the
        # list. This node is the head node. Due to the list being circular,
        # the ordering is already correct, we just need to adjust the 'head'
        # variable.
        self.head = node.next

        return key, value

    def setdefault(self, key, default=None):
        if key in self.table:
            return self[key]

        self[key] = default
        return default

    def __iter__(self):
        # Return an iterator that returns the keys in the cache in order from
        # the most recently to least recently used. Does not modify the cache's
        # order.
        for node in self.dli():
            yield node.key

    def items(self):
        # Return an iterator that returns the (key, value) pairs in the cache
        # in order from the most recently to least recently used. Does not
        # modify the cache's order.
        for node in self.dli():
            yield (node.key, node.value)

    def keys(self):
        # Return an iterator that returns the keys in the cache in order from
        # the most recently to least recently used. Does not modify the cache's
        # order.
        for node in self.dli():
            yield node.key

    def values(self):
        # Return an iterator that returns the values in the cache in order
        # from the most recently to least recently used. Does not modify the
        # cache's order.
        for node in self.dli():
            yield node.value

    def size(self, size=None):
        if size is not None:
            assert size > 0
            if size > self.list_size:
                self.add_tail_node(size - self.list_size)
            elif size < self.list_size:
                self.remove_tail_node(self.list_size - size)

        return self.list_size

    @property
    def byte_size(self):
        return sum(sys.getsizeof(x) for x in self.values())

    # Increases the size of the cache by inserting n empty nodes at the tail
    # of the list.
    def add_tail_node(self, n):
        for _ in range(n):
            node = _dlnode()
            node.next = self.head
            node.prev = self.head.prev

            self.head.prev.next = node
            self.head.prev = node

        self.list_size += n

    # Decreases the size of the cache by removing n nodes from the tail of the
    # list.
    def remove_tail_node(self, n):
        assert self.list_size > n
        for _ in range(n):
            node = self.head.prev
            if not node.empty:
                if self.callback is not None:
                    self.callback(node.key, node.value)
                del self.table[node.key]

            # Splice the tail node out of the list
            self.head.prev = node.prev
            node.prev.next = self.head

            # The next four lines are not strictly necessary.
            node.prev = None
            node.next = None
            node.key = None
            node.value = None

        self.list_size -= n

    # This method adjusts the ordering of the doubly linked list so that
    # 'node' directly precedes the 'head' node. Because of the order of
    # operations, if 'node' already directly precedes the 'head' node, or if
    # 'node' is the 'head' node, the order of the list will be unchanged.
    def mtf(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head.prev
        node.next = self.head.prev.next

        node.next.prev = node
        node.prev.next = node

    # This method returns an iterator that iterates over the non-empty nodes
    # in the doubly linked list in order from the most recently to the least
    # recently used.
    def dli(self):
        node = self.head
        for _ in range(len(self.table)):
            yield node
            node = node.next

    # The methods __getstate__() and __setstate__() are used to correctly
    # support the copy and pickle modules from the standard library. In
    # particular, the doubly linked list trips up the introspection machinery
    # used by copy/pickle.
    def __getstate__(self):
        # Copy the instance attributes.
        dictionary = self.__dict__.copy()

        # Remove those that we need to do by hand.
        del dictionary['table']
        del dictionary['head']

        # Package up the key/value pairs from the doubly linked list into a
        # normal list that can be copied/pickled correctly. We put the
        # key/value pairs into the list in order, as returned by dli(), from
        # most recently to least recently used, so that the copy can be
        # restored with the same ordering.
        elements = [(node.key, node.value) for node in self.dli()]
        return (dictionary, elements)

    def __setstate__(self, state):
        dictionary = state[0]
        elements = state[1]

        # Restore the instance attributes, except for the table and head.
        self.__dict__.update(dictionary)

        # Rebuild the table and doubly linked list from the simple list of
        # key/value pairs in 'elements'.

        # The list_size is the size of the original cache. We want this cache
        # to have the same size, but we need to reset it temporarily to set up
        # table and head correctly, so save a copy of the size.
        size = self.list_size

        # Setup a table and double linked list. This is identical to the way
        # __init__() does it.
        self.table = {}

        self.head = _dlnode()
        self.head.next = self.head
        self.head.prev = self.head

        self.list_size = 1

        # Now adjust the list to the desired size.
        self.size(size)

        # Fill the cache with the keys/values. Because inserted items are
        # moved to the top of the doubly linked list, we insert the key/value
        # pairs in reverse order. This ensures that the order of the doubly
        # linked list is identical to the original cache.
        for key, value in reversed(elements):
            self[key] = value
