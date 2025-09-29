from django.shortcuts import render

def product_list(request):
    products = [
        {"name": "Laptop", "price": 999.99},
        {"name": "Mouse", "price": 25.50},
        {"name": "Teclado", "price": 45.75},
        {"name": "Monitor", "price": 200.00},
    ]
    return render(request, "products.html", {"products": products})