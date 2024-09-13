from django.core.management.base import BaseCommand, CommandError
from markers.models import Marker, DiveSpot
from accounts.models import User
import csv

class Command(BaseCommand):
    help = 'Add divespots/markers from csv exported from google maps.'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename of the csv//same folder as manage.py')

    def handle(self, *args, **options):
        try:
            filename = options.get('filename')
            with open(filename, mode='r', encoding='utf8') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                      string_coordinates=row['WKT']
                      coordinates=string_coordinates[string_coordinates.find("(")+1:string_coordinates.find(")")].split(' ')
                      coordinates=[cord[0:8] for cord in coordinates]
                      print('*'*10)
                      print(f'Adding {row['name']} with posLat: {coordinates[1]}, posLng: {coordinates[0]}')
                      marker=Marker.objects.filter(
                                    posLat=coordinates[1], 
                                    posLng=coordinates[0],
                            ).first()
                      
                      #Example edit name
                      print(f'Adding: {row['name']}')
                      divespot = marker.divespot
                      divespot.name = row['name']
                      divespot.save()
        except Exception as e:
            raise CommandError(f'Something bad hapenned: {e}')
        self.stdout.write(self.style.SUCCESS('Successfully added divespots with markers!'))