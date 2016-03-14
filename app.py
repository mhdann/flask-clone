from flask import Flask, render_template, request, redirect, flash, Markup
import Quandl
from plots import build_plot

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

#@app.route('/result')
#def result():
#  return "Result:" 

@app.route('/lookup', methods = ['POST'])
def signup():
  token = "6AYaJmh1XPfLQrfWPnDP"
  ticker = request.form['ticker']
  print("Stock given:" + ticker)
  try:
    test = Quandl.get(ticker, authtoken=token)
    print "Quandle Queried"
    bokehscript, bokehdiv = build_plot(test, ticker) 
    return render_template("results.html", bokeh_script=bokehscript, bokeh_div=bokehdiv)
  except Quandl.ErrorDownloading as detail:
    print detail
    return render_template('index.html', error="Error Downloading")
  except Quandl.DatasetNotFound as detail:
    search = Quandl.search(ticker, authtoken=token)
    codes = [s['code'] for s in search]
    error = "<div> Code not in the list. Try: <ul><li>" + "</li><li>".join(codes) + "</li></ul> </div>"
    print error  
    return render_template("index.html", error=error)
  except Quandl.CallLimitExceeded as detail:
    print detail
    return render_template('index.html', error="API Call limit exceeded")
  return render_template('index.html', error="Unknown Error")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=33507)
