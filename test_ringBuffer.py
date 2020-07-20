import ringBuffer

SIZE = 100
rb = ringBuffer.RingBuffer(N=SIZE)


def test_init():
    errors = []
    if not rb.wIdx == 0:
        errors.append('Init write index failed.')
    if not rb.rIdx == 0:
        errors.append('Init read index failed.')
    if rb.buffFull:
        errors.append('Init buffer state failed.')
    if not rb.get_size() == SIZE:
        errors.append('Init buffer size is wrong.')
    assert not errors, 'Errors:{}'.format(", ".join(errors))


def test_push_elem():
    rb = ringBuffer.RingBuffer(N=SIZE)
    errors = []
    init_read_idx = rb.rIdx

    # Fill buffer
    for i in range(SIZE):
        rb.push_elem('element')

    # Check results
    if not rb.is_full():
        errors.append('Buffer failed to fill on push.')
    if not rb.wIdx == 0:
        errors.append('Buffer write index failed to wrap.')
    if not rb.rIdx == init_read_idx:
        errors.append('Buffer read index failed to remain constant.')

    assert not errors, 'Errors:{}'.format(", ".join(errors))


def test_pop_elem():
    rb = ringBuffer.RingBuffer(N=SIZE)
    errors = []

    # Fill buffer
    for i in range(SIZE):
        rb.push_elem('element')

    # Read all elements
    results = []
    while not rb.is_empty():
        results.append(rb.pop_elem())

    # Check results
    if not len(results) == SIZE:
        errors.append('Wrong number of popped elements.')
    if not rb.rIdx == rb.wIdx:
        errors.append('Read/write pointers failed to match after pops.')
    if not rb.get_remaining() == 0:
        errors.append('Non-zero number of elements remain after push & pop.')

    # Reset buffer and check results
    rb.reset()
    if not rb.wIdx == 0:
        errors.append('Reset write index failed.')
    if not rb.rIdx == 0:
        errors.append('Reset read index failed.')
    if rb.buffFull:
        errors.append('Reset buffer state failed.')

    assert not errors, 'Errors:{}'.format(", ".join(errors))
