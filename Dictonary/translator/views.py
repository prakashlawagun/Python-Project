from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def translate(request):
    if request.method == 'POST':
        data = request.POST
        word = data['word']
        payload = {'q':word}
        r = requests.get('https://www.englishnepalidictionary.com/',params=payload).text
        soup = bs(r,'html.parser')

        meaning = soup.find('div',class_= 'search-result').h3.text
        context = {
           'meaning':meaning
        }
        return render(request,'templates/index.html',context)


    return render(request,'templates/index.html')
