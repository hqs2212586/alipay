#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 返回操作系统所有的环境变量
    # os.environ.setdefault('HOME', '/home/hqs')  # 没有就添加字典，有则返回
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alipay.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
