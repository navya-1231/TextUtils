from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyse(request):
    if request.method == 'GET':
        input_text=request.GET.get('text')
        removepunc=request.GET.get('removepunc',"off")
        capitalise=request.GET.get('capitalize',"off")
        lowercase=request.GET.get('lowercase',"off")

        analysed_text=input_text

        if removepunc=="on":
            punctuation="""!()-[]{};:'\"\\,<>./?@#$%^&*_~"""
            temp=""
            for char in analysed_text:
                if char not in punctuation:
                    temp=temp+char
            analysed_text=temp

        if capitalise == "on" and lowercase == "on":
            analysed_text = analysed_text.swapcase()  

        elif capitalise == "on":
            analysed_text = analysed_text.upper()

        elif lowercase == "on":
            analysed_text = analysed_text.lower()
        data={
            'text':analysed_text,
        }
    else:
        return HttpResponse("Error")   

    return render(request, 'analyse.html',data)