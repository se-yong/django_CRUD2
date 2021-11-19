import json

from django.views  import View
from django.http   import JsonResponse
from .models       import Owner


class OwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body) ## json 데이터타입을 파이썬딕셔너리화 

            Owner.objects.create(
                name  = data['name'],
                email = data['email'],
                age   = data['age']
            )
            return JsonResponse({"Message" : "Created"}, status=201)

        except KeyError:
            return JsonResponse({"Message" : "Key_Error"}, status=405)

    def get(self, request):
        owners = Owner.objects.all()
        result = [] #1

        for owner in owners:
            dog_list=[] #3
            dogs = owner.dog_set.all()
            for dog in dogs:
                dog_information = {
                    'name' : dog.name,
                    'age'  : dog.age
                }
                dog_list.append(dog_information)
            #2 
                owner_info = {
                'name'     : owner.name,
                'email'    : owner.email,
                'age'      : owner.age,          
                'dog_list' : dog_list #3
                }
            result.append(owner_info)
        return JsonResponse({'result' : result}, status = 200)




#