from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing, Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.filter(is_published=True).order_by("-is_mvp", "hire_date")
    mvp_realtors = Realtor.objects.filter(is_mvp=True, is_published=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }

    return render(request, 'pages/about.html', context)
