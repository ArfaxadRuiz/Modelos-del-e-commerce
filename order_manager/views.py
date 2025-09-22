from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Order

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "dashboard.html")

class SalesDataView(View):
    def get(self, request, *args, **kwargs):
        data = {
            "labels": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
            "sales": [12, 19, 3, 5, 2],  # datos de ejemplo
        }
        return JsonResponse(data)