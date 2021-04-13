from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import os
import csv
from django.urls import path

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(path, 'r') as fp:
            reader = csv.reader(fp)
            reader.next()

            for row in reader:
                _, created = Squirrel.objects.get_or_create(
                        Latitude = row[0],
                        Longitude = row[1],
                        Unique_Squirrel_ID = row[2],
                        Shift = row[4],
                        Date = row[5],
                        Age = row[7],
                        Primary_Fur_Color = row[8],
                        Location = row[12],
                        Speific_Location = row[14],
                        Running = True if row[15] == 'TRUE' else False,
                        Chasing = True if row[16] == 'TRUE' else False,
                        Climbing = True if row[17] == 'TRUE' else False,
                        Eating = True if row[18] == 'TRUE' else False,
                        Foraging = True if row[19] == 'TRUE' else False,
                        Other_Activities = True if row[20] == 'TRUE' else False,
                        Kuks = True if row[21] == 'TRUE' else False,
                        Quaas = True if row[22] == 'TRUE' else False,
                        Moans = True if row[23] == 'TRUE' else False,
                        Tail_flags = True if row[24] == 'TRUE' else False,
                        Tail_twitches = True if row[25] == 'TRUE' else False,
                        Approaches = True if row[26] == 'TRUE' else False,
                        Indifferent = True if row[27] == 'TRUE' else False,
                        Runs_from = True if row[28] == 'TRUE' else False,
                        )
