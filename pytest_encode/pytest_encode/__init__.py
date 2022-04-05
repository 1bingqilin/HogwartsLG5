import pytest
from typing import List

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        #item.name  用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        #item.nodeid 用例的路径
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')

        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)

    items.reverse()