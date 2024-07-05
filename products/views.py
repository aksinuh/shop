from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from .models import detail, product,size,category, color
from django.views.generic import ListView,DetailView
from .forms import commentform
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect


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
        return reverse("shop_detail", kwargs={"pk": self.object.pk})

  
def favorites(reguest):
    return render(reguest,"favorites.html" )


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
        
       
