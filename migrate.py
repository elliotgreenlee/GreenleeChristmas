import csv

from app import app, db
from models import Gift


def create_database():
    with app.app_context():
        db.create_all()
        with open('gifts.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='|')
            fields = next(csv_reader)
            print(fields)
            for row in csv_reader:
                new_gift = Gift(name=row[0],
                                description=row[1],
                                image_url=row[2],
                                product_url=row[3])
                print('Adding new gift {:s}, {:s}, {:s}, {:s}'.format(row[0], row[1], row[2], row[3]))
                try:
                    db.session.add(new_gift)
                    db.session.commit()
                except:
                    print('Failed to store gift in database')


if __name__ == "__main__":
    create_database()
