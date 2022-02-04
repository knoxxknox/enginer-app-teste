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


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    if request.method == 'POST':
        return('<h1>AAAAAAAAAAAAAAAAAAA B</h1>')
	
    return('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" lang="en">
  
  <head><link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
    <title>Email template</title>
    <meta property="og:title" content="Email template">
    
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta http-equiv="refresh" content="500" >
    
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
          <a class="subtle-link" href="#">knox - Python</a>
          </td>
          <tr>
      </table>
  
  
  <! Banner --> 
         <table role="presentation" width="100%">
            <tr>
         
              <td bgcolor="#000000" align="center" style="color: white;">
                
                <h2> K N O X <p><h2>V1.0</h2></p> </h2>
                         
              </td>

              <tr>
                <td width="500" align="right" style="color: white;" bgcolor="#3d3d3d"><p>TOKEN_01</p></td>
            </tr>


        </table>


        <tr>
          <td>
              <table id="content-3" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td width="250" valign="top" bgcolor="#ffffff" style="padding:5px;">
                  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAgVBMVEUAAAD///9KSkqdnZ2NjY3l5eXY2Nhzc3P6+vrT09Ph4eHd3d2ZmZmioqLJycn19fUZGRlhYWFubm7v7++Tk5NUVFS3t7e+vr4yMjKoqKixsbFZWVnw8PBDQ0MuLi58fHwgICA8PDx6enqHh4cmJiYPDw9mZmY+Pj5HR0cLCwvExMQmHEpQAAAJBklEQVR4nO2d6XqqMBCGg6LiArgjWI+4t73/CzyCghDCkskEQh++v7V03oJZhm8mRJMnw7An1tY1++vjct97nP5d/dvPz/y6O2wWy6PeN11naBsSAwhFZFzUGAy9y/IxJ1W0WxzX3nAlI45Q6IQDq7//VwktpVvv6EyxYwmFSmhsR9XuWx7m3h1gxhMKj3BlbkToIn17X2ghhcIiHC8x8F5aODZSVIFwCLcnPL5Afh8lrFAYhNYOly+UiRBYKHHCFcrXL6u5i4CnIRBaNzmATz1QBlZRwr40vkBe84RyAZ/DqviiTozQlQxIyEkYUYhwIB2QkIMoohDhvgZC4bsoQmjVAUjIpjnCUT2ERGyBI0BoMMNZmCbiEvWlcUOETjaU5XsjuzqiEu4aIjTpQG7O54fWFRNx2wwhfZ+uqUyEjbndODVD2KPCsNI/niIS0teuiZCaDdf0zzNPsYDOjRBSQ2b2Az4iYiOEl1QIjHn5jEg4bIJQT4XAmJYxH1P4aIpG+Jv9wBiRMPMtr5+QMdphbj2WTRCuUyEwsioeIiF8+Y1GyPgn6znRQqTAPfSzHzggEo6aJ8x+EVEXNSoQ+nQqHvAGSjHCWXEQF2akrSYkeuFP/wIhOcXvOAffuICqED4Hdfe5gBx4+BkcZQilqSPsCDvCjrAj7Ag7wo6wIwRKtkuhecK/fw+9Rw8imD+zEUKgYPaGNhHCbHAdYb46Qnx1hMWEU4Ymha6plo2lbA+P/7g4uQUbxYTGZNufrfVZH08mzDJdSBiq57FvZQHh1FyAgpGicsKnZiyPfx6h7WK+ORJXJUIyn1UlXKFb00RVjfD5rGbqUViE9rrsOvWrKmHWUMAg9Hzp8fKrOiFdqZElxLUVYomDkDK+0IQr5PoeLPEQklkBYU3GZn5xEabuYpoQ0+ODKz7CpKs4RYjqLcAVJ+HNZhIOfqQGKSROQrJnEdq+xAhFxUv4GW0ShHeJAQqLm5CsMoQM671C4idc0oQ2qrkeXfyEkek2JsQ1+KALQLhPEw6lxYYjAOHbaRcRKrpYiwUh7CUJ1V3MvAUhJNMEodIzRSAQ4eVDOJEUF55AhORDqOaeMCkdROhEhCs5UWHKBRHuI8Ja3+bCtAURBku3kBDVryxHvzBC90XYgoc02tLyEt5fhJiVH7I0gBHujJBQ+cmQxNV5X7y/NwgJZUSErAV0+ewFhMqv2Mgny7vl/cVzQFirLwaoqMCSu6TxFBDSFcsqKno1yP/G6ItoK3lNgtB0eQMChgyHtGDVTcjkDQiYuV2ibiL/o3t0CwHZMp20YaCJc/SAF7d70oKdU3wLDUA+8ErqaRQkpPgdBGzmNoS6Vdahz2trWMGYjRwPuo4xIHAPpHqiNFHEDdyoc6/06tXiA8i7c4okv6mciBKA4PcOmO050JU0joB7UCichfJTPb7AJjvM1g64mqW8hvClF2abHExd0j7DX/iVlEzS9DzKRymyAZLUI1dAm/5EozQVWXhhtwYQkr/sWwyn71TIBoPYx/lxXnvb3/FkAFReF2/BHayPAkcW+lhS839D1GGAkqXpyzvaYCz8kIk7vU4ifRvL+BDM9MLbQ4yO1GzZHsogIWgUWkh6Plfj2QIpzSn2b8p9QO3pECbL2br66ICYxBUqq2C0oTOGrq5WFl1kTZMBHLgK5rUEBiuqgbGxVeveRYJXx1CDqK6qwxicEE7XPCqc7oHugA+p7596O5SPoFmM5JdQbXsxMBN1TwAqbr4FWk0GrQEksM1XYphRsJQvLdjLgE9rZrUzyoFAufJTDNiCd+QaZOn9aRqsVJqHJZ+Acsnxlkn9V+Swt9y9CFD5l4+ErEFOhbgVq/LjaDAbQhYk0XrGUHWxnZBFIGWV0XSv/kwRur6+fN5fiucKtdouMOUbBNBOJXoxW8eRXaIK3Zfcw0V0ToHAG6/atA0IuVemUYJN9SV3oNAFze2djiw8yq9nCPl+efV5123j1kz3wcxNAE9biwitFyHvnP8mVLg/QSzjRci7gXoTtsB6G1jGwlINTj/Gm1DhBGKkSUTI6dsct2XNFh5OQwDLrzehwm6qt6wPIV9KsS2Er6T1i5AvHdUWQi9ByJfKaAmhbyQJuVJmLSF8L5+jwj4ek3g7CKNTviJCnm9iOwgHFCHPEWKtIIztxZ/+NNXdD20g/NYyhBz1zm0gnDAIq5dNtYAwp19b1cYD6hMm+1+m+rVV/H3lCVOnTaZ67lXcCqtOmG7vme6bWG3LpzghZWSiel9WQlSasEebJen+pVXmDJUJdY1WpgftuHzmV5dwP6BxWF12jdKdlKqEJ+YJ7Kxe0F7JxKgk4fw8ZqDkEGqGW+j+Vo/w+/Kb6eNdSPhkdAqssEKEP2sdUZflpe8NgWcj2M7xxL6VQoTzomhkqPhsBHvC0vtf9icIC9URdoQ1qSMsUEeYI9BhbYd1eTzKEMK0LI+nI+wIO8KOsCMs0b08no6wI+wIO0JBLcrj6QhVILybv7YxdFlVPH+C8BqndFfZsve/QDhKZj0zpUr73DBaQ0jdJNr80n7COZ2Vp+z17Sd06KtTpoLWE/rZy6cbybWekAGQLlbaZD8gnxCzvNLMXj5dVdUIIeY9pI+41Wi3ZCOEmAd/MLoxpYeaRggxT43IWiiof2AjhJh1T4fs5dPVWL3sB+QTYlbn/ZRd/dEIIWa7gQt9cepbvmuEELUO2Cq+9r9GCCFHFeRqnvKjGfT+6TsvBrmEqP3cb4ml6TBz4OS5GULkcxXiHSJjLeEWxiGPkLtIukQ/S9M9MsuSGZa8WghrK8mHD6WihHXV5MMfUmFC1PE0VwK3UJywFkSmcbQ2whoQMwuemgl5isJAgs+FWISSK/OP5QFIJ9S+JLaeFRhGEQk1rdg3Ddd8WP63i4VFKKkBwazQ4FxJeISaZiLfx5ued5YAjzAJNdtBnDk29CkeQKESPmVvETrhE3Jaw5falLAJtaAd/kiolf3tvsW5ey9JIAy0smZ7AOa8d3amyKFIIgxkT5zZcVGtCdXtsby41kTGMQQSCd8yvsaeqR9Hy8Wm99hd57fbfO5f//3bHTb3s943XWe4MsQnhVz9B8PzlEvWXu49AAAAAElFTkSuQmCC" width="230" height="110"  />
                  </td>
                  <td width="15"></td>
              </tr>
              </table>
          </td>
          </tr>

    <! First Row --> 
  <p></p>
  <h2 align="center">AztwP#$12D</h2>
  <p></p>
  
  <table align="center"> 
    <tr >
      <td>
      <form method="POST" class="form-horizontal">
        <div class="control-group">
            <div class="controls form-inline">

                <label for="inputKey">User</label>
                <input type="text" class="input-small" placeholder="Your name" name="inputKey">
      
                <label for="inputValue">Password</label>
                <input type="password" class="input-small" placeholder="Your password" name="inputValue">
            </div>
        </div>
        <input type="submit"  value="Send">
    </form>
  </td>
  </tr>
</table>''')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
