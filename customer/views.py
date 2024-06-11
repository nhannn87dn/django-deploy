from django.template.response import TemplateResponse

# Create your views here.
def customers_dashboard(request):
    # Truyền các biến xuống template
    context = {

    }
    # Create a response
    response = TemplateResponse(request, "customers_dashboard.html", context)

    # Return the response
    return response


def customers_profile(request):
    # Truyền các biến xuống template
    context = {

    }
    # Create a response
    response = TemplateResponse(request, "customers_profile.html", context)

    # Return the response
    return response


def customers_orders(request):
    # Truyền các biến xuống template
    context = {

    }
    # Create a response
    response = TemplateResponse(request, "customers_orders.html", context)

    # Return the response
    return response