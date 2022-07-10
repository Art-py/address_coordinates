import os

from django.shortcuts import render
from dotenv import load_dotenv
from .forms import AddressForm

from dadata import Dadata

load_dotenv()

TOKEN = os.getenv('token')
SECRET = os.getenv('secret')
TEMPLATE = 'address/index.html'


def index(request):

    submitbutton = request.POST.get('submit')

    geo_lat = ''
    geo_lon = ''

    form = AddressForm(request.POST or None)
    if form.is_valid():
        dadata = Dadata(TOKEN, SECRET)
        result = dadata.clean('address', form.cleaned_data.get("address"))
        geo_lat = result['geo_lat']
        geo_lon = result['geo_lon']
        dadata.close()

    context = {'form': form, 'geo_lat': geo_lat,
               'geo_lon': geo_lon, 'token': TOKEN,
               'submitbutton': submitbutton}

    return render(request, TEMPLATE, context)
