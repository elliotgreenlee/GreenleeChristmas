# GreenleeChristmas
This is the Christmas Gift Catalogue Website for my family and friends.

The database_url in .env sets the location; it can be set to localdb instead of the vercel postgres.

To recreate the database from the csv, run:
* `python migrate.py`

To fully clear holdover duplicates on hosted postgres run:
* `/opt/homebrew/Cellar/postgresql@15/15.10/bin/psql` or wherever with the psql command on Vercel.
* `\dt` to see tables.
* `SELECT * FROM gift;` to see rows.
* `DELETE FROM gift CASCADE;` to remove rows.
* `SELECT * FROM gift;` to confirm.

Forms handled by Formspree.
Hosting and Deployment handled by Vercel through Github.
Don't forget to deploy database changes with migrate.py!
