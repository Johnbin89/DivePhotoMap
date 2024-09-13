from django.core.management.base import BaseCommand, CommandError
from markers.models import Marker, DiveSpot
from accounts.models import User
import csv
import glob

class Command(BaseCommand):
    help = 'Add divespots/markers from csv exported from google maps.'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename of the csv//same folder as manage.py')
        parser.add_argument(
            "--all",
            action="store_true",
            help="Read all csv in folder",
        )


    def handle(self, *args, **options):
        #python manage.py load_csv csv_spots --all
        if options["all"]: 
            try:
                folder = options.get('filename') 
                for filename in glob.glob(f"{folder}/*.csv"):
                    print('*'*20)
                    print(f'Opening: {filename}')
                    with open(filename, mode='r', encoding='utf8') as csv_file:
                            csv_reader = csv.DictReader(csv_file)
                            for row in csv_reader:
                                string_coordinates=row['WKT']
                                coordinates=string_coordinates[string_coordinates.find("(")+1:string_coordinates.find(")")].split(' ')
                                coordinates=[cord[0:8] for cord in coordinates]
                                print('*'*10)
                                print(f'Adding {row['name']} with posLat: {coordinates[1]}, posLng: {coordinates[0]}')
                                divespot=DiveSpot(
                                    name=row['name'], 
                                    description=row['description'], 
                                    accurate_location=True if row['Accurate Location']=='Yes' else False,
                                    access_type=row['access'] if row['access'] else DiveSpot.access_type.field.default,
                                    dive_type=row['type'] if row['type'] else DiveSpot.dive_type.field.default,
                                )
                                divespot.save()
                                user = User.objects.get(id=1) #jbin admin
                                marker=Marker(owner=user, public=True, 
                                                posLat=coordinates[1], 
                                                posLng=coordinates[0],
                                                divespot=divespot
                                        )
                                marker.save()
            except Exception as e:
                raise CommandError(f'Something bad hapenned: {e}')
            self.stdout.write(self.style.SUCCESS(f'Successfully added divespots from {filename} in {folder} with markers!'))
        else:
            try:
                filename = options.get('filename')
                with open(filename, mode='r', encoding='utf8') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for row in csv_reader:
                            string_coordinates=row['WKT']
                            coordinates=string_coordinates[string_coordinates.find("(")+1:string_coordinates.find(")")].split(' ')
                            coordinates=[cord[0:8] for cord in coordinates]
                            print('*'*10)
                            print(f'Adding {row['name']} with posLat: {coordinates[1]}, posLng: {coordinates[0]}')
                            divespot=DiveSpot(
                                name=row['name'], 
                                description=row['description'], 
                                accurate_location=True if row['Accurate Location']=='Yes' else False,
                                access_type=row['access'],
                                dive_type=row['type']
                            )
                            divespot.save()
                            user = User.objects.get(id=1) #jbin admin
                            marker=Marker(owner=user, public=True, 
                                            posLat=coordinates[1], 
                                            posLng=coordinates[0],
                                            divespot=divespot
                                    )
                            marker.save()
            except Exception as e:
                raise CommandError(f'Something bad hapenned: {e}')
            self.stdout.write(self.style.SUCCESS(f'Successfully added divespots from {filename} with markers!'))



