from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from app.serializers import *

@csrf_exempt
def cun(request):
    if request.method=='POST':
        data=json.loads(request.body)
        expression=data.get('code')
        result=eval(expression)
        Calculator.objects.create(expression=expression, result=result)
        result1={'frontend_data': result}
        return JsonResponse(result1)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def qu(request):
    last_ten_strings = {}
    if request.method == 'POST':
        last_ten_strings = Calculator.objects.order_by('-id')[:10]

        # print(last_ten_strings,'1111')

        result2 = []
        for item in last_ten_strings:
            serializer = CalculatorSerializer(item)
            result2.append({
                'expression': serializer.data['expression'],
                'result': serializer.data['result'],
            })
        result2 = {'frontend_data1': result2}

        print(result2,'2222')

        return JsonResponse(result2, safe=False)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



