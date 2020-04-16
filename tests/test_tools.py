def raise_test_exception(msg=''):
    raise TestException('Simulated Exception', msg)


class TestException(Exception):
    pass
