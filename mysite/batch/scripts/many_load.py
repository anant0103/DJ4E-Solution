import csv
from unesco.models import Category, State, Region, Iso, Site

def run():
    fhand = open('../batch/unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)
        try:
            y = int(row[3])
        except:
            y = None
        try:
            x = float(row[4])
        except:
            x = None
        try:
            z = float(row[5])
        except:
            z = None
        try:
            a = float(row[6])
        except:
            a = None
        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        site = Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=x,latitude=z,area_hectares=a,category=c,state=s,region=r,iso=i)
        site.save()