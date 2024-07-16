from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from .models import detail, product,size,category, color,favorite
from django.views.generic import ListView,DetailView
from .forms import commentform
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

user = get_user_model()

# Create your views here.
# def shop_detail(reguest, id):
#     detal = get_object_or_404(detail, id=id)
#     sizes = size.objects.filter(products__product=detal.product)
#     all_details = detail.objects.all()
#     categorys = category.objects.all()
#     colors = color.objects.filter(produc__product=detal.product)
    
    
#     context = {
#         "sizes": sizes,
#         "all_details": all_details,
#         "products": detal,
#         "categorys": categorys,
#         "colors": colors
#     }
#     return render(reguest, 'detail.html', context= context)



class ShopDetailView(DetailView, FormMixin):
    model = detail
    template_name = 'detail.html'
    context_object_name = 'products'
    form_class = commentform

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detal = self.get_object()
        context['sizes'] = size.objects.filter(products__product=detal.product)
        context['all_details'] = detail.objects.all()
        context['categorys'] = category.objects.all()
        context['colors'] = color.objects.filter(produc__product=detal.product)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Kullanıcı giriş yapmamışsa giriş sayfasına yönlendirin
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (reverse('login'), request.path))
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.product = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


    def get_success_url(self) -> str:
        return reverse("shop_detail", kwargs={"slug": self.object.slug})

  

@login_required
def add_to_favorites(request, id):
    products = get_object_or_404(detail, id=id)
    favorite.objects.get_or_create(user=request.user, product=products)
    return redirect(reverse('shop_detail', kwargs={'slug': products.slug}))

@login_required
def remove_favorite(request, id):
    favorites = get_object_or_404(favorite, id=id, user=request.user)
    favorites.delete()
    return redirect(reverse('favorites'))

@login_required
def favorites(request):
    favourite_products = favorite.objects.filter(user=request.user)
    context = {
        'favorites': favourite_products
    }
    return render(request, 'favorites.html', context=context)



# def shop(reguest):
#     details = detail.objects.filter( display = True)
#     context = {
#         "detals": details
#     }
#     return render(reguest, 'shop.html', context= context)



class ShopListView(ListView):
    template_name = "shop.html"
    model = detail
    paginate_by = 4

    
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        cat_id = self.request.GET.get("category")
        if cat_id:
            queryset = detail.objects.filter(product__category__id=cat_id, display = True)
        else:
            queryset = detail.objects.filter(display=True)
            
        return queryset  
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Konteksdə səhifələnmiş obyektləri əlavə edir
        context['detals'] = context['page_obj']
        return context
        
       
