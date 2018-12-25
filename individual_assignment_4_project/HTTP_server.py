# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:18:15 2018

@author: Grani
"""

from flask import Flask, jsonify, request


server = Flask("graphD")

@server.route("/postgraph")
def post_graph():
    body = request.get_json()
    return jsonify(body)
    

@server.route("/degrees-of-separation/<start>/<end>")
def find_path(normal_graph, start, end, path=[]):
        
    graph = request.get_json()
    
    graph = jsonify(graph)
    
    path = path + [start]
    
    if start == end:
        return jsonify(path)
    
    if start not in graph:
        return jsonify(None)

    for connection in graph[start]:
        if connection not in path:
            new_path = find_path(graph, connection, end, path)
            
            if new_path is not None:
                return new_path
server.run()


normal_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": []
}


