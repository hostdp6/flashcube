#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD:services/api-old/manage.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flashcube.settings.base')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flashcube.settings.local')
>>>>>>> 42d03479639db545cb8a5ad1e4d410abc5abf137:flashcube/manage.py
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
