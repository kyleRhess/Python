
""" A Ring Buffer object
A circular buffer, circular queue, cyclic buffer or ring buffer.
A data structure that uses a single, fixed-size buffer connected end-to-end.
"""


class RingBuffer:
    def __init__(self, N=1000):
        """A Ring Buffer object.
        N = length of buffer object (list)
        Default = 1000
        """
        self.N = N
        self.buffer = [None] * self.N
        self.wIdx = 0
        self.rIdx = 0
        self.buffFull = False

    def push_elem(self, element):
        """Add element to the buffer.
        Adds an element to the end of the buffer.
        Overwites existing data if overflown.
        """
        self.buffer[self.wIdx] = element
        # If the buff is full, increase read index with write.
        if self.is_full():
            self.rIdx = (self.rIdx + 1) % self.N

        # Always increment write index.
        self.wIdx = (self.wIdx + 1) % self.N

        # If caught up to read index, then it's full.
        if self.wIdx == self.rIdx:
            self.buffFull = True

    def pop_elem(self):
        """Return the next element from the buffer.
        Raises an IndexError if the buffer is empty.
        """
        element = None

        # Only modify pointers if buffer has elements to return.
        if not self.is_empty():
            element = self.buffer[self.rIdx]
            self.buffFull = False
            self.rIdx = (self.rIdx + 1) % self.N
        else:
            raise IndexError('Cannot read from an empty ring buffer.')
        return element

    def is_full(self):
        """Return if buffer is full.
        """
        return self.buffFull

    def is_empty(self):
        """Return if buffer is empty.
        """
        return not self.buffFull and self.wIdx == self.rIdx

    def get_size(self):
        """Return maximum number of buffer elements.
        """
        return self.N

    def get_remaining(self):
        """Get the number of un-read elements.
        """
        if self.is_full():
            return self.N
        elif self.is_empty():
            return 0
        elif self.rIdx > self.wIdx:
            return self.N - abs(self.rIdx - self.wIdx)
        else:
            return self.wIdx - self.rIdx

    def reset(self):
        """Reinitializes the buffer to an empty state;
        """
        self.wIdx = 0
        self.rIdx = 0
        self.buffFull = False
