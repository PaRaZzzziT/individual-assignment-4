# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:17:31 2018

@author: Grani
"""

import requests

normal_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": []
}

localhost = "http://127.0.0.1:5000/{}"

def post_graph(normal_graph): 
    data = normal_graph
    request = requests.post(localhost.format('post_graph'), json=data)
    return request.json()



def degrees_of_separation(start, end, normal_graph): 
    data = normal_graph
    request = requests.put('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(start, end) , json=data)    
    return request.json()