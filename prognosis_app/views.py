from django.shortcuts import render
from prognosis_app.functions import *

# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def algorithm(request):
    context = {'success': False, 'contents':'', 'id_header_index':''} #Эти данные пойдут в html страницу
    if request.method == 'POST':
        try:

            uploaded_file = request.FILES['document'] #Получаем файл от пользователя
            context['success'] = True

            uploaded_file.open() #Открываем поток чтения полученного файла
            contents = csv_text_to_list(uploaded_file.read().decode('utf-8')) #Открываем и считываем как .csv

            id_index = get_header_index(contents, 'id')
            context['id_header_index'] = id_index
            print(id_index)
            id_list = []

            for row in contents[1:]:
                if row[id_index] not in id_list: id_list.append(row[id_index])

            list_of_lists = []

            for id in id_list:
                list_of_lists.append(get_by_id_sort_by_date(contents, id))


            context['contents'] = list_of_lists
            uploaded_file.close()
        except: pass

    return render(request, 'algorithm.html', context)