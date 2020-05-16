from unit_test_example import A
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import raises

class TestA():
    def test_init(self):
        a = A()
        assert_equal(a.value, "Some Value")
        assert_not_equal(a.value, "Incorrect Value")

    def test_return_true(self):
        a = A()
        assert_equal(a.return_true(), True)
        assert_not_equal(a.return_true(), False)

    @raises(KeyError)
    def test_raise_exception(self):
        a = A()
        a.raise_exception("A message")

def main():
    test = TestA()
    test.test_init()
    test.test_return_true()
    test.test_raise_exception()


if __name__ == '__main__':
    main()        