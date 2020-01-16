from django.shortcuts import redirect
from .models import *

def fosdem_tag_to_id(request, fosdemtag):
    try:
        id = VideoGear.objects.get(fosdem_tag=fosdemtag).id
    except:
        return redirect('/admin/videogear/')
    url = '/admin/videogear/videogear/'+str(id)+'/change/'
    return redirect(url)
