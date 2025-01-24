import ctpy
from ctpy import CTPYclient


def test_connect(ctpy_mock):
    ctpy_mock.get('/login', cookies={'RSNASESSION': '123'}, status_code=302)

    build = "2021.04.01 at 11:04:40 CDT"
    ip = "10.42.0.83"
    java = "1.7"
    ctpy_mock.get('/server', text=f"""<?xml version="1.0" encoding="UTF-8" ?>\n<server build="{build}" ip="{ip}" java="{java}" port="1080" />""")

    connection = ctpy.connect(ctpy_mock.uri, port=ctpy_mock.port, username="test", password="secret")

    assert isinstance(connection, CTPYclient)
    assert connection.server.build == build
    assert connection.server.ip == ip
    assert connection.server.java == java
