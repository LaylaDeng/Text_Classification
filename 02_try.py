#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:52:29 2018

@author: dengyuzhao
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier



train = pd.read_csv( '/Users/dengyuzhao/Downloads/达观杯/train_set.csv')
test = pd.read_csv( '/Users/dengyuzhao/Downloads/达观杯/test_set.csv')
y=(train["class"]-1).astype(int)


column = "word_seg"
test_id = test["id"].copy()


text_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1,2),min_df=3, 
                                                 max_df=0.9,use_idf=1,smooth_idf=1, 
                                                 sublinear_tf=1)),
                       
                      ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, random_state=42,
                                           max_iter=5, tol=None))])
                     

text_clf =text_clf.fit(train[column], y)
preds = text_clf.predict(test[column])


base = open('/Users/dengyuzhao/Downloads/达观杯/03_try.csv','w')


i=0
base.write("id,class"+"\n")
for item in preds:
    base.write(str(i)+","+str(item+1)+"\n")
    i=i+1
base.close()
