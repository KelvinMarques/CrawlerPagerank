
# from typing import final
import os
from bs4 import BeautifulSoup
import re

from requests import get
import requests


from .Graph.graph import Graph
# from Crawler.links.views import crawlerView
# pages = set()

def Crawler(Url,cont, Urls, pages, arquivo,dicio,contadorDic):
    print("FUNCIONANDO")
    listUrl = []
    TrashList = []
    # Case Base
    if cont == 0:
            return pages, dicio
    else:
        
        response = requests.get(Url)
        pathUrl = Url.split('/')[2]
        page = response
        soup = BeautifulSoup(page.content, 'html.parser')
        pattern = re.compile("^(/)")
        Father = Url
        for allLink in soup.find_all("a"):
            if "href" in allLink.attrs:
                if allLink.attrs["href"] not in pages:
                    new_page = allLink.attrs["href"]
                    firstCharacter = new_page[:1]
                    if firstCharacter == "/":
                        aux = f'http://'+pathUrl+new_page
                    elif 'https://' in new_page or 'http://' in new_page:
                        aux = new_page
                    elif new_page[:1] == "#":
                        continue
                    else:
                        continue        
                    Son = aux
                    dicio[Father] = contadorDic
                    contadorDic+=1
                    dicio[Son] = contadorDic
                    contadorDic+=1
                    # print(dicio)
                    arquivo = open("Crawler\dataset.txt", "a", encoding="utf-8")
                    arquivo.write(f"{Father} || {Son} \n")
                    pages.add(aux)
                    # new_page == "https://" or new_page == "http://"
                    
                    Urls.append(aux)
                    # print(str(cont)+" "+ new_page)
                    a, dicio = Crawler(aux, cont-1 ,Urls, pages, arquivo, dicio, contadorDic)
                    pages.union(a)
        cont-=1    
            
        return pages, dicio

def translateFile(fname, dicioFinal):

    arquivo = open('Crawler\dataset_int.txt', 'w')

    
    with open(fname, encoding='utf8') as f:
        lines = f.readlines()

    for line in lines :
            try:
                [parent, child] = map(str ,line.strip(' ').split('||'))
                child = child.strip() 
                parent= parent.strip() 
                if parent in dicioFinal and child in dicioFinal:
                    
                    parent = dicioFinal[parent]
                    child = dicioFinal[child]
                arquivo.write(f"{parent} || {child} \n")
            except:
                pass    
          

    file_path = "Crawler\dataset_int.txt"
    arquivo.close()
    return file_path

def init_graph(fname):
    with open(fname, encoding='utf8') as f:
        lines = f.readlines()

    graph = Graph()
    
            
    for line in lines :
            try:
                # teste = line.strip().split(',')
                [parent, child] = map(str ,line.strip().split('||'))
                child = child.strip() 
                parent= parent.strip()
                print(parent+ " | AND |"+  child)
                graph.add_edge(parent, child)
            except:
                pass    

    # with open(fname, encoding='utf8') as f:
    #     for l in f.readlines() :
    #         for pair in l.strip().split('\n'):
    #             [parent, child] = pair.split(',')
    #             graph.add_edge(parent, child)
                
    try:
        graph.sort_nodes()
    except:
        pass

    import os

    try:
        os.remove('Crawler/dataset.txt')
        os.remove('Crawler/dataset_int.txt')
    except OSError as e:
        print(f"Error:{ e.strerror}")
    
    
    return graph