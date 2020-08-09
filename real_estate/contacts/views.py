from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user already made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,
                                                         user_id=user_id)
            if has_contacted:
                messages.error(request, "You already made inquiry for this listing. Please wait for the response.")
                return redirect('/listings/' + listing_id)

        # save to db
        Contact(listing=listing,
                listing_id=listing_id,
                name=name,
                email=email,
                phone=phone,
                message=message,
                user_id=user_id,
                ).save()

        # send email to realtor
        send_mail(
            f'New inquiry for {listing}',
            f'Hello :)\n\n'
            f'Please see inquiry details below:\n'
            f'Property: {listing}\n'
            f'User: {name}\n'
            f'Phone: {phone}\n'
            f'Email: {email}\n'
            f'Is_registered: {True if user_id else False}\n'
            f'Message: {message}\n',
            'real_estate@website.com',
            [realtor_email],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted. Realtor will get back to you as soon as possible.')
        return redirect('/listings/'+listing_id)
