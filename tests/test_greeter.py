from myfunctions.greeter import say_hello

def test_say_hello():
    assert say_hello("DevOps") == "Hello, DevOps!"
    assert say_hello() == "Hello, World!"