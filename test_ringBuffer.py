import unittest
import ringBuffer


class TestRingBuffer(unittest.TestCase):

    def test_push_elem(self):
        rb = ringBuffer.RingBuffer()
        rb.push_elem('element')
        self.assertTrue(True)
