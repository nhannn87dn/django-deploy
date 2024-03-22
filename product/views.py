from django.template.response import TemplateResponse
from .models import Product

#Hiển thị danh sách sản phẩm
def productList(request):
    #Lấy 20 sản phẩm đầu tiên
    top_product_list = Product.objects.values()[:20]
    #Truyền các biến xuống template
    context = {
        "products": top_product_list,
    }
    # Create a response
    response = TemplateResponse(request, "product_list.html", context)
    
    # Return the response
    return response

#Hiển thị chi tiết sản phẩm
def productDetail(request, id):
    #Lấy thông tin sản phẩm có id
    product = Product.objects.get(pk=id)
    #Truyền các biến xuống template
    context = {
        "product": product,
    }
    # Create a response
    response = TemplateResponse(request, "product_detail.html",context)
    
    # Return the response
    return response