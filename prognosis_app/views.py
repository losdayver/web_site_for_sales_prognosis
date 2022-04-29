from django.shortcuts import render
from prognosis_app.functions import *

# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def algorithm(request):
    #print(csv_text_to_list('ID;Название;Категория;Цена закупки;Цена продажи;Количество в наличии;Количество закупленного;Количество проданного;Цена закупки на следующие сделки;Дата сделки\n1;HP V2;Монитор;44,4;55;100;50;66;47;14.03.2022'))

    context = {'success': False, 'contents':''}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            context['success'] = True

            uploaded_file.open()
            contents = csv_text_to_list(uploaded_file.read().decode('utf-8'))
            context['contents'] = contents
            uploaded_file.close()
        except: pass

    return render(request, 'algorithm.html', context)