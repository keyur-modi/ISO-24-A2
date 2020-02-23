#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from PIL import Image
import pytesseract
import re
# Save Model Using Pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

def Predict_Image(image_name):
	# In[2]:


	filename = 'finalized_model.sav'
	# some time later... 
	# load the model from disk
	knn = pickle.load(open(filename, 'rb'))


	# In[3]:


	def ocr_core(filename_img):
		pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
		TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
		text = pytesseract.image_to_string(Image.open('image/'+filename_img))    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
		return text
	def get_val(s):
		i = text.find(s)
		a = text[i:]
		x = re.search(" [0-9.]*[ ,]", a)
		return a[x.start()+1:x.end()-1]
	text = ocr_core(image_name)
	dic = {}
	try:
		dic['pH'] = float(get_val('pH'))
		if(dic['pH']>10):
			dic['pH'] = dic['pH']/10
		dic['EC'] = float(get_val('EC'))    
		if(dic['EC']>1):
			dic['EC'] = dic['EC']/10
		dic['OC'] = float(get_val('Organic Carbon (OC)'))
		dic['N'] = int(float(get_val('Available Nitrogen (N)')))
		dic['P'] = int(float(get_val('Available Phosphorus (P)')))
		dic['K'] = int(float(get_val('Available Potassium (K)')))
		dic['S'] = float(get_val('Available Sulphur (S)'))
		dic['Z'] = float(get_val('Available Zinc (Zn)'))
		dic['B'] = float(get_val('Available Boron (B)'))
		dic['Fe'] = float(get_val('Available Iron (Fe)'))
		if(dic['Fe']>10):
			dic['Fe'] = dic['Fe']/100
		elif(dic['Fe']>10):
			dic['Fe'] = dic['Fe']/10
		dic['Mn'] = float(get_val('Available Manganese (Mn)'))
		if(dic['Mn']>100):
			dic['Mn'] = dic['Mn']/100
		elif(dic['Mn']>10):
			dic['Mn'] = dic['Mn']/10
		dic['Cu'] = float(get_val('Available Copper (Cu)'))
	except:
		dic['pH'] = float(get_val('1pH'))
		dic['EC'] = float(get_val('2EC'))
		dic['OC'] = float(get_val('3 Organic Carbon (OC)'))
		dic['N'] = int(float(get_val('4 Available Nitrogen (N)')))
		dic['P'] = int(float(get_val('5 Available Phosphorus (P)')))
		dic['K'] = int(float(get_val('6 Available Potassium (K)')))
		dic['S'] = float(get_val('7 Available Sulphur (S)'))
		dic['Z'] = float(get_val('8 Available Zinc (Zn)'))
		dic['B'] = float(get_val('9 Available Boron (B)'))
		dic['Fe'] = float(get_val('10 Available Iron (Fe)'))
		dic['Mn'] = float(get_val('11 Available Manganese (Mn)'))
		dic['Cu'] = float(get_val('12 Available Copper (Cu)'))



	# In[8]:


	return knn.predict([list(dic.values())])[0]

