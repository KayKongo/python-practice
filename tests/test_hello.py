from hello import hello_to_person

def test_default():
    assert hello_to_person() == "hello, world"

def test_argument():
    assert hello_to_person("Peekaboo") == "hello, Peekaboo"