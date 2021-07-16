#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

nav = webdriver.Chrome()

#pesquisar cotação dolar
nav.get("https://www.google.com.br/")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = nav.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value') 
print(cotacao_dolar)
nav.get("https://www.google.com.br/")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = nav.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)
nav.get("https://www.melhorcambio.com/")
aba_original = nav.window_handles[0]
nav.find_element_by_xpath('/html/body/div[15]/div[2]/div/table[2]/tbody/tr[2]/td[2]/a/img').click()
aba_nova = nav.window_handles[1]
nav.switch_to.window(aba_nova)
cotacao_ouro = nav.find_element_by_id('comercial').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)

nav.quit()

import pandas as pd

produtos_df = pd.read_excel("Produtos.xlsx")
display(produtos_df)

produtos_df.loc[produtos_df['Moeda']=="Dólar","Cotação"] = float(cotacao_dolar)
produtos_df.loc[produtos_df['Moeda']=="Euro","Cotação"] = float(cotacao_euro)
produtos_df.loc[produtos_df['Moeda']=="Ouro","Cotação"] = float(cotacao_ouro)

produtos_df['Preço Base Reais'] = produtos_df['Cotação'] * produtos_df['Preço Base Original']
produtos_df['Preço Final'] = produtos_df['Ajuste'] * produtos_df['Preço Base Reais']
display(produtos_df)

produtos_df.to_excel("Produtos Atualizados.xlsx", index=False)


# In[2]:


import pandas as pd

produtos_df = pd.read_excel("Produtos.xlsx")
display(produtos_df)


# In[3]:


produtos_df.loc[produtos_df['Moeda']=="Dólar","Cotação"] = float(cotacao_dolar)
produtos_df.loc[produtos_df['Moeda']=="Euro","Cotação"] = float(cotacao_euro)
produtos_df.loc[produtos_df['Moeda']=="Ouro","Cotação"] = float(cotacao_ouro)

produtos_df['Preço Base Reais'] = produtos_df['Cotação'] * produtos_df['Preço Base Original']
produtos_df['Preço Final'] = produtos_df['Ajuste'] * produtos_df['Preço Base Reais']
display(produtos_df)


# In[4]:


produtos_df.to_excel("Produtos Atualizados.xlsx", index=False)


# In[ ]:




