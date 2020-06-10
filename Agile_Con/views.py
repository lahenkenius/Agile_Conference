from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = AttendeeCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html')


@login_required
def attendees_list(request):
    customer = Presentation.objects.filter()
    return render(request, 'attendees_list.html',
                  {'attendees': Attendee})


# Create your views here.
def customer_order_list(request):
    customer_order = CustomerOrder.objects.all()
    return render(request, 'customer_order_list.html',
                  {'customer_orders': customer_order})


def customer_order_edit(request, pk):
    customer_order = get_object_or_404(CustomerOrder, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerOrderForm(request.POST, instance=customer_order)
        if form.is_valid():
            customer_order = form.save(commit=False)
            customer_order.save()
            customer_order = CustomerOrder.objects.all()
            return render(request, 'customer_order_list.html',
                          {'customer_orders': customer_order})
    else:
        # edit
        form = CustomerOrderForm(instance=customer_order)
    return render(request, 'customer_order_edit.html', {'form': form})


def customer_order_delete(request, pk):
    customer_order = get_object_or_404(CustomerOrder, pk=pk)
    customer_order.delete()
    return redirect('customer_order_list')


def about(request):
    return render(request, "about.html")


def contact_us(request):
    return render(request, "contact_us.html")


def presentations(request):
    presentations = Presentation.objects.all()
    return render(request, "presentations.html", {'presentations': presentations})


def attendee_landing(request):
    customer_orders = CustomerOrder.objects.all()
    username = Attendee.username
    return render(request, "registration/attendee_landing.html", {'customer_orders': customer_orders,
                                                                  'username': username})


def login_landing(request):
    return render(request, "registration/login_landing.html")

def presenter_landing(request):
    presenter_id = Presenter.presenter_id
    presentations = Presentation.objects.all()
    return render(request, 'registration/presenter_landing.html', {'presenter_id': presenter_id, 'presentations':
        presentations})

