from products.models import category,detail
from django.http import JsonResponse
from .serializers import categoryserializers,detailserializers

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


def products(request):
    detail_list = detail.objects.all()
    serializer = detailserializers(detail_list, many=True)
    return JsonResponse(serializer.data, safe=False)