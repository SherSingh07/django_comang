#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company.settings")

    from django.core.management import execute_from_command_line
    from department.templatetags import extra_tags

    execute_from_command_line(sys.argv)
