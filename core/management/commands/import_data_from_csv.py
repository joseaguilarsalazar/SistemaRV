import csv
from django.core.management.base import BaseCommand
from core.models import Catalogo01TipoDocumento, Catalogo06DocumentoIdentidad, CodigoMoneda, CodigoPais
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help='Load data from CSV files into the database'
    
    def handle(self, *args, **options):
        with open('core/management/commands/csv/tipo_moneda.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not CodigoMoneda.objects.filter(codigo = row['codigo']).exists():
                        CodigoMoneda.objects.create(codigo=row['codigo'], moneda=row['moneda'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_moneda data.'))
    
    
        with open('core/management/commands/csv/codigo_pais.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not CodigoPais.objects.filter(codigo = row['codigo']).exists():
                        CodigoPais.objects.create(codigo=row['codigo'], pais=row['pais'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded codigo_pais data.'))
        
        
        with open('core/management/commands/csv/tipo_comprobante.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not Catalogo01TipoDocumento.objects.filter(codigo = row['Codigo']).exists():
                        Catalogo01TipoDocumento.objects.create(codigo=row['Codigo'], tipo=row['Tipo'],un_1001=row["Descripcion"],serieSufix=row["F"])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_comprobante data.'))
        

        with open('core/management/commands/csv/tipo_documento.csv', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                    if not Catalogo06DocumentoIdentidad.objects.filter(codigo = row['Codigo']).exists():
                        Catalogo06DocumentoIdentidad.objects.create(codigo=row['Codigo'], descripcion=row['Descripcion'],abrev=row["ABREV"])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded tipo_documento data.'))