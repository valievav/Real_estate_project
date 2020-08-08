from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  # desc order

    paginator = Paginator(listings, 6)  # 6 per page
    page = request.GET.get('page')  # page 2, 3 etc.
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    keywords = request.GET.get('keywords')
    city = request.GET.get('city')
    state = request.GET.get('state')
    bedrooms = request.GET.get('bedrooms')
    price = request.GET.get('price')

    if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
    if city:
        queryset_list = queryset_list.filter(city__iexact=city)
    if state:
        queryset_list = queryset_list.filter(state__iexact=state)
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if price:
        queryset_list = queryset_list.filter(price__lte=price)

    context = {
        "listings": queryset_list,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)
