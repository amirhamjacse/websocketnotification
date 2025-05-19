from django.shortcuts import render

# Create your views here.
# chat/views.py
from django.shortcuts import render

def notification_page(request):
    return render(request, 'chat/nt2.html')

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Item


@method_decorator(csrf_exempt, name='dispatch')
class CreateItemView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            if not name:
                return JsonResponse({'error': 'Name is required'}, status=400)

            item = Item.objects.create(name=name)
            return JsonResponse({'message': f'Item "{item.name}" created successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
