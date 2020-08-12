from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HFPe6Ic0PhYCBZVKtty1sRiilouwzhU7QRwXv69FQp9YkO9jdRIViEPuE1M5g86wTGTLudMc0BBXV5s59xNYYOh00HRzAq37B',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)