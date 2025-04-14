from django.http import JsonResponse
from django.views import View
from .models import Equipment, User


class EquipmentAutocomplete(View):
    def get(self, request):
        query = request.GET.get('term', '')
        equipments = Equipment.objects.filter(title__icontains=query)[:10]
        results = [equipment.title for equipment in equipments]
        return JsonResponse(results, safe=False)
    
   
class ProfileAutocomplete(View):
    def get(self, request):
        query =  request.GET.get('term', '')   
        users = User.objects.filter(last_name__icontains=query)[:10]
        results = [user.__str__() for user in users]
        return JsonResponse(results, safe=False)

