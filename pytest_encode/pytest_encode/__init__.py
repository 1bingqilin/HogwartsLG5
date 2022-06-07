import pytest
import logging
from typing import List

logging.basicConfig(level=logging.INFO,
                    #日志格式
                    #时间、代码所在文件名、代码行号、日志级别名字、日志信信息
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(level)s %(message)s',
                    #打印日志时间
                    datefmt='%a,  %d %b %Y %H:%M:%S',
                    #日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    filemode='w'
                    )
logger = logging.getLogger(__name__)

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