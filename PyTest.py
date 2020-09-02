# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:43:15 2020

@author: ghaith
"""
#Librairie qui fait des tests statistiques
import cmath
import math
import statistics
from scipy.stats import norm
from scipy.stats import t

#Fonctiond qui font des tests avec la loi normal
#Test avec le loi normale pour H0 > H1
def Test_Loi_Normal_Sup(data,moy,marge_erreur):
    ts = (statistics.mean(data) - moy) / (statistics.stdev(data)/math.sqrt(len(data)))
    m_erreur = marge_erreur / 100 
    PH0 = norm.ppf(m_erreur)
    P_value = norm.cdf(ts)
    if ts > PH0:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null",marge_erreur,'%')

#Test avec le loi normale pour H0 < H1        
def Test_Loi_Normal_Inf(data,moy,marge_erreur):
    ts = (statistics.mean(data) - moy) / (statistics.stdev(data)/math.sqrt(len(data)))
    m_erreur = marge_erreur / 100 
    PH0 = -(norm.ppf(m_erreur))
    P_value = norm.cdf(ts)
    if ts < PH0:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null",marge_erreur,'%')
        
#Test avec le loi normale pour H0 =/= H1       
def Test_Loi_Normal_Eg(data,moy,marge_erreur):
    ts = (statistics.mean(data) - moy) / (statistics.stdev(data)/math.sqrt(len(data)))
    m_erreur = (marge_erreur/2) / 100 
    PH0 = norm.ppf(m_erreur)
    PH01= -(norm.ppf(m_erreur))
    P_value = norm.cdf(ts)
    if ts > PH0 or ts < PH01:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null")
        


    


#Test de Student

def Test_Loi_Student_Sup(data,moy,marge_erreur):
    c = []
    for i in range(len(data)):
        c.append((data[i]-statistics.mean(data))*(data[i]-statistics.mean(data)))
        Sn2 = sum(c)/ (len(data)-1)
    ts =  (math.sqrt(len(data))*(statistics.mean(data) - moy)) / (math.sqrt(Sn2))  
    PH0 = 1 - (marge_erreur / 100) 
    df = len(data)-1
    Kalpha = t.ppf(PH0,df)
    if ts > Kalpha:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null")

def Test_Loi_Student_Inf(data,moy,marge_erreur):
    c = []
    for i in range(len(data)):
        c.append((data[i]-statistics.mean(data))*(data[i]-statistics.mean(data)))
        Sn2 = sum(c)/ (len(data)-1)
    ts =  (math.sqrt(len(data))*(statistics.mean(data) - moy)) / (math.sqrt(Sn2))  
    PH0 = 1 - (marge_erreur / 100) 
    df = len(data)-1
    Kalpha = -(t.ppf(PH0,df))
    if ts < Kalpha:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas HO au niveau", marge_erreur,'%')
        
#Test de comparaison 

def Test_Comparaison_Student_Sup(data1,data2,marge_erreur):
    c = []
    for i in range(len(data1)):
        c.append((data1[i]-statistics.mean(data1))*(data1[i]-statistics.mean(data1)))
        Sn2 = sum(c)/ (len(data1)-1)
    d = []
    for i in range(len(data2)):
        d.append((data2[i]-statistics.mean(data2))*(data2[i]-statistics.mean(data2)))
        Pn2 = sum(d)/ (len(data2)-1)
    Snp2 = (Sn2+Pn2)/(len(data1)+len(data2)-2)
    df = len(data1)+len(data2)-2
    PH0 = 1 -  (marge_erreur / 100) 
    Kalpha = t.ppf(PH0,df)
    if ts < Kalpha:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null")

def Test_Comparaison_Student_Inf(data1,data2,marge_erreur):
    c = []
    for i in range(len(data1)):
        c.append((data1[i]-statistics.mean(data1))*(data1[i]-statistics.mean(data1)))
        Sn2 = sum(c)/ (len(data)-1)
    d = []
    for i in range(len(data2)):
        d.append((data2[i]-statistics.mean(data2))*(data2[i]-statistics.mean(data2)))
        Pn2 = sum(d)/ (len(data)-1)
    Snp2 = (Sn2+Pn2)/(len(data1)+len(data2)-2)
    df = len(data1)+len(data2)-2
    PH0 = 1 -  (marge_erreur / 100) 
    Kalpha = -(t.ppf(PH0,df))
    if ts < Kalpha:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null")
        

def Test_Comparaison_Student_Eq(data1,data2,marge_erreur):
    c = []
    for i in range(len(data1)):
        c.append((data1[i]-statistics.mean(data1))*(data1[i]-statistics.mean(data2)))
        Sn2 = sum(c)/ (len(data)-1)
    d = []
    for i in range(len(data2)):
        d.append((data2[i]-statistics.mean(data1))*(data2[i]-statistics.mean(data2)))
        Pn2 = sum(d)/ (len(data)-1)
    Snp2 = (Sn2+Pn2)/(len(data1)+len(data2)-2)
    df = len(data1)+len(data2)-2
    PH0 = 1 -  ((marge_erreur/2) / 100) 
    Kalpha0 = -(t.ppf(PH0,df))
    Kalpha1 = t.ppf(PH0,df)
    if ts < Kalpha0 or ts > Kalpha1:
        print("On rejette H0 au niveau", marge_erreur,'%')
    else :
        print("On ne rejette pas l'hypothése null")
    
  
#Module qui calcule le coefficient de correation:
def ProduitListe(a,b,c): #Module qui fait le produit d'une liste
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c
    
        


def correlation(a,b):
    x = sum(a) #Somme des valeurs de la première liste nommée a.
    y = sum(b) #Somme des valeurs de la seconde liste nommée b.
    x2= x ** 2  #Somme des valeurs de la liste a le tout au carré
    y2 = y ** 2 #Somme des valeurs de la liste a le tout au carré
    
    CarreeDeAB = []
    ScareAB = ProduitListe(a,b,CarreeDeAB) #On fait le produit de la liste a avec la b
    
    CarreeDeA = []  
    ScareA = ProduitListe(a,a,CarreeDeA) #On fait le produit la list a avec elle-même.
    
    CarreeDeB = []
    ScareB = ProduitListe(b,b,CarreeDeB) #On fait le produit la list b avec elle-même.
    
    SommeCarreeDeAB = sum(ScareAB) 
    SommeCarreeDeA = sum(ScareA) #Somme des valeurs de A au carré
    SommeCarreeDeB = sum(ScareB)
    
    z = len(a)
    #On appelle le coefficient de correlation R
    
    r = (z*SommeCarreeDeAB - x*y) / (math.sqrt(z*SommeCarreeDeA - x2) * math.sqrt(z*SommeCarreeDeB - y2))
    
    

    
    if r >= -0.1 and r < 0.1:
        print("Le coéfficient de correlation est de ",r,", donc il n'y a pas de correlation entre les 2 variables")
    elif r > 0.1 and r < 0.5:
        print("Le coéfficient de correlation est de ",r,", donc il y a  correlation positive très faible entre les 2 variables")
    elif r >= 0.5 and r < 1:
        print("Le coéfficient de correlation est de ",r,", donc il y a une correlation positive très forte entre les 2 variables")
    elif r == 1:
        print("Le coéfficient de correlation est de ",r,", donc il y a une correlation  positive parfaite entre les 2 variables")
    