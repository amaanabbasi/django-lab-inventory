from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from inventory.models import Order, Item

def index(request):
    return render(request, 'inventory/index.html')

class OrdersView(generic.ListView):
    template_name = 'inventory/orders.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Order.objects.order_by('-created')


class OrderView(generic.DetailView):
    model = Order
    template_name = 'inventory/order.html'


class ItemView(generic.DetailView):
    model = Item
    template_name = 'inventory/item.html'