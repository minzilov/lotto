from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render (request, 'home.html')
    
def result(request):




    number_list = list()

    for i in range(6):
        number = request.GET['number' + str(i+1)]
        number_list.append(int(number))

    #랜덤수
    random_list = list()
    for j in range(7): 
        number = random.randrange(1,46) #1~45까지 수 랜덤으로 뽑기
        while number in random_list :
            number = random.randrange(1,46)

        random_list.append(number)

    #맞은 개수
    count = 0
    for i in range(6):
        for j in range(7):
            if (number_list[i]==random_list[j]):
                count=count +1
                
        

    return render (request, 'result.html', {'number_list':number_list, 'random_list':random_list, 'count':count})
