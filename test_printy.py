import printy


def test_printc():
    printy.printc()
    printy.printc('test')
    printy.printc('test', (231, 231, 1))
    printy.printc('test', (231, 231, 1), 'bold')
    printy.printc('test', (231, 231, 1), 'underline')
    printy.printc('test', (231, 231, 1), 'bold', 'underline', 'nothing')
