from fnmatch import translate
from bs4 import BeautifulSoup
from django.core.validators import URLValidator
from django.http import request, response
from django.shortcuts import redirect, render
from links.forms import UrlForm
import requests
import re
from links.utils import Crawler
import networkx as nx
from .utils import init_graph, translateFile
# Create your views here.
from .PageRank import PageRank
def getURL(request):
    
        form = UrlForm()
        return render(request, 'links/input_url.html',{'form': form})


def crawlerView(request):
    if request.method == 'POST':
        pages = set()
        context ={}
        dicio = {}
        contadorDic = 0
        form = UrlForm()
        context['form']= form    
        if request.POST.get('Url'): 
            Url = request.POST.get('Url')   
        cont = 5
        Url = str(Url)
        Urls = [Url]

        arquivo = open(f"Crawler\dataset.txt", "a")
        SetUrl, dicioFinal = Crawler(Url, cont, Urls, pages, arquivo, dicio, contadorDic)


        
        file_path = "Crawler\dataset.txt"
        fileTranslated = translateFile(file_path, dicioFinal)
        fname1 = "Crawler\dataset_int.txt"
        graph = init_graph(fname1)
        # G=nx.dual_barabasi_albert_graph(len(graph),2) 
        pr=PageRank(graph, 0.15, 100)
        nx.pagerank
        Orderpr = graph.get_pagerank_list() 
        # Orderpr= sorted(Orderpr, reverse=True)
        print("Lista")
        print(Orderpr)   
        ListLinks = list(dicioFinal.keys())
        outFinal = []
        for i, x in zip(Orderpr, ListLinks):
            outFinal.append(f"{x}")

        return render(request, 'links/update_crawler.html', {'Url': outFinal})
    
    # Função onde o crawler irá funcionar
    