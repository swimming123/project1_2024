import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from hhjsemi.models import ProjectModel
import pandas as pd
from collections import Counter
import re
import konlpy
from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor

# Create your views here.
@csrf_exempt
def projectList(request):
    subcategory = request.POST['select']
    start = request.POST['start']
    end = request.POST['end']
    Project_list = (subcategory, start, end)
    print(f'Project_list ={Project_list}')
    ref = ProjectModel()
    res = ref.ProjectList(Project_list)
    print(f'res = {res}')
    print('res',res)
    df = pd.DataFrame(res,columns=['newsTitle'])
    print('df',df)
    titleList = df['newsTitle'].to_list()
    titleStr = ""
    for i in titleList:
        titleStr += i
    cleaned_content = re.sub('[^\w\s]', '', titleStr)
    okt = Okt()
    cutStr = okt.morphs(cleaned_content)
    newcutting = [word for word in cutStr if len(word) > 1]

    word_counts = Counter(newcutting)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    textdf = pd.DataFrame(sorted_word_counts, columns=['단어', '빈도수'])
    toptendf = textdf[0:10]
    print(f'toptendf{toptendf}')
    keywords = textdf[:100].to_json(force_ascii=False, orient='records')
    top = toptendf.to_json(force_ascii=False, orient='records')
    print(f'top{top}')
    return JsonResponse({'top': top, 'keywords': keywords}, safe=False)


@csrf_exempt
def projectTitle(request):
    subcategory = request.POST['select']
    start = request.POST['start']
    end = request.POST['end']
    varname = request.POST['varname']
    Project_title = (subcategory, start, end, varname)
    print(f'Project_title ={Project_title}')
    ref = ProjectModel()
    res = ref.projectTitle(Project_title)
    return JsonResponse(res,safe=False)
