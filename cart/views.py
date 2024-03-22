from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import CheckoutForm
from django.contrib import messages
from product.models import Product
#from django.views.decorators.csrf import csrf_exempt
import json


#@csrf_exempt  #Bỏ qua kiểm tra CSRF nếu bạn không sử dụng CSRF token
@require_http_methods(["POST"])
def add_to_cart(request):
    try:
        data = json.loads(request.body)
        #Debug
        product_id = data.get('id')
        quantity = data.get('quantity')
        # Lấy giỏ hàng từ session
        cart = request.session.get('cart', [])

        # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa
        for item in cart:
            if item['id'] == product_id:
                # Nếu có, tăng số lượng
                item['quantity'] += quantity
                break
        else:
            # Nếu không, thêm sản phẩm mới vào giỏ hàng
            cart.append({'id': product_id, 'quantity': quantity})

        # Lưu giỏ hàng vào session
        request.session['cart'] = cart
        
        #reponse to client
        data = {
            'success': True,
            'message': 'Thêm giỏ hàng thành công !'
        }
        return JsonResponse(data)

    except Exception as e:  # Bắt lỗi cụ thể
        data = {
            'success': False,
            'message': 'Error: '+ str(e)  # In ra thông điệp lỗi
        }
        return JsonResponse(data)

@require_http_methods(["POST"])
def increase_quantity(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('id')
        
        cart = request.session.get('cart', [])
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] += 1
                break
        request.session['cart'] = cart
        #reponse to client
        data = {
            'success': True,
            'message': 'Thành công !'
        }
        return JsonResponse(data)
    except Exception as e:  # Bắt lỗi cụ thể
        data = {
            'success': False,
            'message': 'Error: '+ str(e)  # In ra thông điệp lỗi
        }
        return JsonResponse(data)

@require_http_methods(["POST"])
def decrease_quantity(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('id')
        
        cart = request.session.get('cart', [])
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] = max(0, item['quantity'] - 1)
                break
        request.session['cart'] = cart
        #reponse to client
        data = {
            'success': True,
            'message': 'Thành công !'
        }
        return JsonResponse(data)
    except Exception as e:  # Bắt lỗi cụ thể
        data = {
            'success': False,
            'message': 'Error: '+ str(e)  # In ra thông điệp lỗi
        }
        return JsonResponse(data)


@require_http_methods(["GET","POST"])
def cartList(request):
    try:
        # del request.session['cart']
        cart = request.session.get('cart', [])
        print(cart)
        
        # Tạo mảng products rỗng
        products = []
        totalAmount = 0
        # Lặp qua mỗi item trong cart
        for item in cart:
            # Lấy id và quantity từ item
            product_id = item['id']
            quantity = item['quantity']

            # Lấy sản phẩm từ cơ sở dữ liệu
            product = Product.objects.get(pk=product_id)
            amount = product.price * quantity * (1 - product.discount)
            totalAmount += amount
            # Thêm sản phẩm và quantity vào mảng products
            products.append({
                'id': product.id,
                'name': product.product_name,
                'price': product.price,
                'discount': product.discount,
                'thumbnail': product.thumbnail,
                'quantity': quantity,
                'amount': amount
            })
            #Thêm price, discount, amount vào cho cart
            item['name'] = product.product_name
            item['price'] = float(product.price)
            item['discount'] = float(product.discount)
            item['amount'] = float(amount)
           
            

        print(products)
        #Cap nhat lai cart
        request.session['cart'] = cart
        
        # Create a response
        response = TemplateResponse(request, "cart_list.html", {
            'products': products,
            'total': totalAmount
            }
        )
        # Return the response
        return response
    except Exception as e:  # Bắt lỗi cụ thể
        #TODO: Hiển thị lỗi Friendly ra app message
        raise Exception('Error: '+ str(e))

# Trang cảm ơn khi đặt hàng thành công
@require_http_methods(["GET"])
def cartThanks(request):
    # Create a response
    cart = request.session.get('cart', [])
    print(cart)
    
    response = TemplateResponse(request, "cart_thanks.html")
    # Return the response
    return response

#Hiển thị màn hình Checkout
@require_http_methods(["GET", "POST"])
def cartCheckout(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CheckoutForm(request.POST)
       
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #print(customer_form.cleaned_data.get('customer_firstName'))
            #print(payment_form.cleaned_data.get('payment_type'))
            print(request.POST)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/cart/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckoutForm()
        cart = request.session.get('cart', [])
        print(cart)
        # Tạo mảng products rỗng
        products = []
        totalAmount = 0
        # Lặp qua mỗi item trong cart
        for item in cart:
            # Lấy id và quantity từ item
            product_id = item['id']
            # Lấy sản phẩm từ cơ sở dữ liệu
            product = Product.objects.get(pk=product_id)
            totalAmount += item['amount']
            # Thêm sản phẩm và quantity vào mảng products
            products.append({
                'id': product.id,
                'name': product.product_name,
                'price': item['price'],
                'discount':item['discount'],
                'thumbnail': product.thumbnail,
                'quantity': item['quantity'],
                'amount': item['amount']
            })           
            
    # Create a response
    response = TemplateResponse(request, "cart_checkout.html", {
        "form": form,
        "products": products,
        "total": totalAmount
        })
    # Return the response
    return response
    