#!/usr/bin/env python
from settings.common import PROJECT_ROOT
import os
import sys


# Corrects some pathing issues in various contexts, such as cron jobs, and
# the project layout still being in Django 1.3 format.
os.chdir(PROJECT_ROOT)
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))


# Run Django.
if __name__ == "__main__":
    settings_module = "settings.common"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
