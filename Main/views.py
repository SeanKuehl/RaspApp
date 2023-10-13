from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from .models import MealIdea
# Create your views here.


class HomePageView(TemplateView):
    template_name = "Home.html"



class CreateMealIdeaView(CreateView):
    model = MealIdea
    fields = ["meal"]
    template_name = "CreateMealIdea.html"

    def get_success_url(self):
        return reverse('Home')
    

class MealIdeaListView(ListView):
 
    # specify the model for list view
    model = MealIdea
    template_name = "MealIdeaList.html"