#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os.path
from my_parser import parse
from tkinter import *
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def makecsv(pathlabel=None):
    from Scripts.Main import message_entry
    way = message_entry.get()  # Путь к папке с письмами
    files = os.listdir(way)
    folders = map(lambda name: os.path.join(way, name), files)
    data = list()
    mail_type = 1
    result = []
    for catalog in folders:
        if os.path.isdir(catalog):
            print(catalog)
            data = parse(catalog, mail_type)
            mail_type = mail_type + 1
            result = result + data

# Создание SVM
    columns = ['Mail type', 'Email text']
    df = pd.DataFrame(result, columns=columns)
    print(df)
    df.to_csv(r'C:\Email_Analisator\data.csv')


    #dataSVM = pd.read_csv('C:\Email_Analisator\cartridge_accounting.csv')
    #X = dataSVM['Email text'].values
    #y = dataSVM['Mail type'].values

    #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, shuffle=True)

    #cv = CountVectorizer()
    #X_train = cv.fit_transform(X_train)
    #X_test = cv.transform(X_test)

    #classifier = SVC(kernel='linear', probability=True)
   # classifier.fit(X_train, y_train)


