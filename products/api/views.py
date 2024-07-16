from products.models import category,detail
from django.http import JsonResponse
from .serializers import categoryserializers,detailserializers,detailCreateserializers,productserializers
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



def categorys(request):
    category_list = category.objects.all()
    serializer = categoryserializers(category_list, many=True)
    # category_dict = []
    # for categoryis in category_list:
    #     category_dict.append(
    #         {
    #             "category_id": categoryis.id,
    #             "category_name": categoryis.name,
    #         }
    #     )
        
    return JsonResponse(serializer.data, safe=False)

# @api_view(http_method_names= ["GET","POST"])
# def products(request):
#     if request.method == "POST":
#         serelazer = detailCreateserializers(data=request.data)
#         if serelazer. is_valid():
#             serelazer.save()
#             return JsonResponse(data=serelazer.data, safe=False)
#         return JsonResponse(data=serelazer.errors, safe=False)
#     detail_list = detail.objects.all()
#     serializer = detailserializers(detail_list, context={"request": request}, many=True)
#     return JsonResponse(serializer.data, safe=False)


@api_view(http_method_names= ["PUT","PATCH"])
def products_update(request,id):
    product = get_object_or_404(detail,id=id)
    if request.method == "PUT":
        serelazer = detailCreateserializers(data=request.data, context={"request": request}, instance=product)
        if serelazer. is_valid():
            serelazer.save()
            return JsonResponse(data=serelazer.data, status=201, safe=False)
        return JsonResponse(data=serelazer.errors,status=400, safe=False)
    if request.method == "PATCH":
        serelazer = detailCreateserializers(data=request.data, partial=True, context={"request": request}, instance=product)
        if serelazer. is_valid():
            serelazer.save()
            return JsonResponse(data=serelazer.data, status=201, safe=False)
        return JsonResponse(data=serelazer.errors,status=400, safe=False)
    
    
class praductListAPIView(ListCreateAPIView):
    serializer_class = detailCreateserializers
    permission_classes= [AllowAny]
    queryset = detail.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return detailserializers
        return super().get_serializer_class()
    
    
    def get_queryset(self):
        keyword = self.request.GET .get("keyword")
        if keyword:
            queryset = detail.objects.filter(title__icontains=keyword)
            return queryset
        return super().get_queryset()
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('keyword', openapi.IN_QUERY, description="keyword to filter name", type=openapi.TYPE_STRING)
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
        

class praductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = detailCreateserializers
    permission_classes= [AllowAny]
    queryset = detail.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return detailserializers
        return super().get_serializer_class()
    
    
class productCreateAPIView(CreateAPIView):
    serializer_class = productserializers
    permission_classes= [AllowAny]