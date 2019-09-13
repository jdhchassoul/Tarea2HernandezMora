import Tarea2HernandezMora


def test_func():
    assert Tarea2HernandezMora.main(45, 5)[0] > 0


def test_failmin():
    assert Tarea2HernandezMora.main(5, 45) > 0


def test_failit():
    assert Tarea2HernandezMora.main("a", "b") > 0
