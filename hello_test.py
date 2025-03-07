import hello  # ✅ hello.py에서 함수를 가져옴

def test_hello():
    assert hello.hello_world() == "Hello World!"
