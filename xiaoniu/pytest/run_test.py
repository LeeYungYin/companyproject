import os
import pytest

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(ROOT_PATH, "output")
REPORT_FILE = os.path.join(REPORT_PATH, "report.html")

if __name__ == '__main__':
    #pytest.main(["-m okr", f"{REPORT_FILE}"])  # 执行okr的用例，并打印到REPORT_FILE里
    pytest.main(["-m niu"])
    #pytest.main(["--returns 2"])  # 执行两次
