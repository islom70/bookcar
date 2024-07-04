from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cars.models import Car
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .forms import BookingForm
from .models import Booking


def home(request):
    cars = Car.objects.filter(is_active=True)
    return render(request, 'home.html', {'cars': cars})


class CarDetailView(DetailView):
    model = Car
    template_name = 'detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm(initial={'car': self.object})
        return context

    @method_decorator(login_required, name='dispatch')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            self.object.is_active = False
            self.object.save()
            return redirect('profile')  # Adjust this redirect as needed
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'profile.html', {'bookings': bookings})


