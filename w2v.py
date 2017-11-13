#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


import numpy as np
import pandas as pd


## calculate the number of sentences which include each dictionary word
def idf(dic, text):
    idf = []
    for i in dic.index:
        #print i
        n_i = 0
        for j in text:
            if i in j:
                n_i += 1
        idf.append(n_i)    
    return idf

## calculate the number of each dictionary word in a sentence
def tf_sent(dic, sentence):     
    tf = []
    for i in dic.index:
        n_i = 0
        for j in sentence:
            if i == j:
                n_i += 1
        tf.append(n_i)   
    return tf

## calculate the ifidf of each dictionary word in a sentence
def ifidf_sent(sentence, tf, idf):
    ifidf = np.log(idf)*tf
    return ifidf


## turn a document to a vector, by the means of if-idf algorithm
def docu_to_vec(documents):

    ## pre handle data, drop stop-words
    stoplist = set('for a of the and to in'.split())
    text = [[word for word in document.lower().split() if word not in stoplist]
            for document in documents]
    #print text

    words_unique = set()
    for i in text:
        for j in i:
            words_unique.add(j)
    #print words_unique

    dic = pd.DataFrame(range(len(words_unique)),index = words_unique)
    #print dic
    
    idf_list = idf(dic, text)
    
    ifidf_list = []
    for sentence in text:
        tf = tf_sent(dic, sentence)
        ifidf = ifidf_sent(sentence, tf, idf_list)
        ifidf_list.append(ifidf)
        
    return ifidf_list


documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

print docu_to_vec(documents)

        
    





