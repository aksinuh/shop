from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Contactform
from .models import ContactUs
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
# def contact(request):
#     form = Contactform()
#     if request.method == "POST":
#         form = Contactform(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Message has been succesfuly sent!")
#             return redirect(reverse_lazy('cantact'))
#     context = {
#         "form": form
#     }
#     return render(request, 'contact.html', context=context)


class CantactCreateView(CreateView):
    template_name = "contact.html"
    form_class = Contactform
    success_url = reverse_lazy("cantact")
    
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Message has been succesfuly sent!")
        return super().form_valid(form)
