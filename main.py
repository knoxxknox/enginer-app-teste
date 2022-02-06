# This Python file uses the following encoding: utf-8

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask
from google.cloud import storage
import pandas as pd
from google.cloud import bigquery
import os
import pyarrow

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


# Bsuca de dados executando query na tabela
def consultaDados(query,cred_json):
    '''Consulta de dados em tabela'''

    caminho = str(os.getcwd().replace("\\", "/")) + "/"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = caminho + cred_json
    
    client = bigquery.Client()
    df_result = client.query(query).to_dataframe()
    
    return(df_result)


@app.route('/teste')
def teste():
	
    query ='''
        SELECT Transaction.TransactionDate.AuthorizationTimestamp, Transaction.TransactionMerchant.Name, 
        Transaction.AccountNumber.ExpirationDate, Transaction.AccountType, 
        Transaction.TransactionPointOfInteraction.Type
        
        FROM `infinite-deck-340122.dset_testes.table_01`
        
        WHERE Transaction.TransactionKey=45511700128772
       '''

    cred_json="infinite-deck-340122-5ec3e9c74ff3.json"

    dados = consultaDados(query,cred_json)	

    a=dados['AuthorizationTimestamp'][0]
    b=dados['Name'][0]
    c=dados['ExpirationDate'][0]
    d=dados['AccountType'][0]
    e=dados['Type'][0]

    return('''<h1>ESTE PROCESSO ESTÁ FAZENDO UMA CHAMADA EM NO BIGQUERY E EXECUTNDO UM CONSULTA</h1><p></p><h2>DATA: ''' + str(a) + '''</h2><p></p><h2>NOME: ''' + b + '''</h2><p></p><h2>DATA_VENC: ''' + c + '''</h2><p></p><h2>TIPO: ''' + d + '''</h2><p></p><h2>TESTE: ''' + e + '''</h2>''')



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""


    return('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" lang="en">
  
  <head><link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
    <title>Email template</title>
    <meta property="og:title" content="Email template">
    
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style type="text/css">
   
      a{ 
        text-decoration: underline;
        color: inherit;
        font-weight: bold;
        color: #253342;
      }
      
      h1 {
        font-size: 56px;
      }
      
        h2{
        font-size: 28px;
        font-weight: 900; 
      }
      
      p {
        font-weight: 100;
      }
      
      td {
    vertical-align: top;
      }
      
      #email {
        margin: auto;
        width: 800px;
        background-color: white;
      }
            
      .subtle-link {
        font-size: 12px; 
        text-transform:; 
        letter-spacing: 1px;
        color: #CBD6E2;
      }
      
    </style>
    
  </head>
    
    <body bgcolor="#F5F8FA" style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#33475B; word-break:break-word">
  
 <! View in Browser Link --> 
      
<div id="email">
      <table align="center" role="presentation">
        <tr>
          <td>
          <a class="subtle-link" href="#">Stone - Operações Autorizador - Analytics</a>
          </td>
          <tr>
      </table>
  
  
  <! Banner --> 
         <table role="presentation" width="100%">
            <tr>
         
              <td bgcolor="#00bd19" align="center" style="color: white;">
                
                <h2> Report operacional de análise do Deploy do Autorizador <p><h2>Versão TOKEN_VERSAO </h2></p> </h2>
                         
              </td>
              <tr>
                <td width="500" align="right" style="color: white;" bgcolor="#00bd19"><p>Desde às TOKEN_DATA  </p></td>
            </tr>
        </table>
        <tr>
          <td>
              <table id="content-3" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td width="250" valign="top" bgcolor="#ffffff" style="padding:5px;">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Stone_pagamentos.png" width="230" height="110"  />
                  </td>
                  <td width="15"></td>
              </tr>
              </table>
          </td>
          </tr>
  
    <! First Row --> 
  
  <table role="presentation" border="0" cellpadding="0" cellspacing="0px" style="padding: 30px 30px 10px 30px;">
     <tr>
       <td>
        <h2> Escopo da análise</h2>
            <p>
              O deploy está sendo analisado através de quatro KPIs, sendo eles: Conversão, erros, tempo das aplicações e volume. A cada 30 minutos um novo report será gerado, explorando pontos as métricas e sinalisando pontos de atenção caso existam.
            </p>
      </td> 
          </tr>
  </table>
  
  <table role="presentation" border="0" cellpadding="0" cellspacing="0px" style="padding: 30px 30px 10px 30px;">
    <tr>
      <td>
        <h3>Conversão</h3>
        <tr>
		TOKEN_01
		TOKEN_02
        </tr>
     </td>
    </tr>
    <td> Este gráfico representa a conversão de cada máquina em todos os DCs.</td>
 </table>
  <table role="presentation" border="0" cellpadding="0" cellspacing="0px" style="padding: 30px 30px 10px 30px;">
    <tr>
      <td>
        <h3>Volume</h3>
        <tr>
		TOKEN_03
		TOKEN_04
        </tr>
     </td>
    </tr>
   <td> Este gráfico representa a volumetria de cada máquina em todos os DCs.</td>
 </table>
  <table role="presentation" border="0" cellpadding="0" cellspacing="0px" style="padding: 30px 30px 10px 30px;">
    <tr>
      <td>
        <h3>Tempo</h3>
        <tr>
		TOKEN_05
        </tr>
     </td>
      <td> Este gráfico representa a corelação de tempos das aplicações.</td>
    </tr>
 </table>
  <table role="presentation" border="0" cellpadding="0" cellspacing="0px" style="padding: 30px 30px 10px 30px;">
    <tr>
      <td>
        <h3>Erros Máquina</h3>
        <tr>
		TOKEN_06
        </tr>
     </td>
      <td> Este gráfico representa a volumetria de erros por máquina em todos os DCs.</td>
    </tr>
 </table>
              
  </table>
     
        <! Banner Row --> 
  <table role="presentation" bgcolor="#EAF0F6" width="100%" style="margin-top: 50px;" >
      <tr>
          <td align="center" style="padding: 30px 30px;">
            
         <h2> Time de operações do Autorizador - Analytics </h2>
            <p>
              Este documento foi gerado por uma automação de análises de dados das informações transacionais do Autorizador - Stone. Em caso de dívida por gentileza nos acionar através do seguinte endereço: 
      
              </p>
              <a href="#">auth.analytics@stone.com.br</a>      
          </td>
          </tr>
      </table>
  
        <! Unsubscribe Footer --> 
      
  <table role="presentation" bgcolor="#F5F8FA" width="100%" >
      <tr>
          <td align="left" style="padding: 30px 30px;">
            <p style="color:#99ACC2"> Stone CO &hearts; Autorizador - Analytics </p>
    
          </td>
          </tr>
      </table> 
      </div>
    </body>
      </html>''')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
	
# [END gae_python3_app]
# [END gae_python38_app]
