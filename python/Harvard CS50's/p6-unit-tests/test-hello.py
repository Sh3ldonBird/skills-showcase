from hello import hello

## First
#def test_hello():
#    hello("David") == "hello, David"

## Second
#def test_default():
#    assert hello() == "hello, world"
#
#def test_arguement():
#    assert hello("David") == "hello, David"

## Third
def test_default():
    assert hello() == "hello, world"

def test_arguement():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

