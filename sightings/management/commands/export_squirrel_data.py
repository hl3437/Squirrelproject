from django.core.management import BaseCommand
from sightings.models import Squirrel
import csv
import os
import sys

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, path, **options):
        with open(path, '
