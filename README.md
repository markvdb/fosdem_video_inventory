# Fosdem video inventory
micro webapp for FOSDEM rental video gear inventory - quick hack, but it works

All functionality is in the admin.

One view outside the admin: https://server/tag/fosdem_tag will point to https://server/admin/videogear/videogear/$id/change/ .

## Import fosdem tags
<pre>import csv
with open('video_rental_tags.csv', newline='\n') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
         t=VideoGear(fosdem_tag=row['fosdem_tag'], gear_type=int(row[' type']))
         t.save()
</pre>
