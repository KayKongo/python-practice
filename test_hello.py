from hello import hello_to_person

def test_hello_default():
    assert hello_to_person() == "hello, world"

def test_hello():
    assert hello_to_person("Kay") == "hello, Kay"