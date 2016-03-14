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
  ticker = request.form['ticker']
  print("Stock given:" + ticker)
  search = Quandl.search(ticker, authtoken="6AYaJmh1XPfLQrfWPnDP")

  try:
    test = Quandl.get(ticker, authtoken="6AYaJmh1XPfLQrfWPnDP")
    print "Quandle Queried"
    bokehscript, bokehdiv = build_plot(test, ticker)
    print "Bokeh snippet built"
    # print components(p)[0]
    return render_template("results.html", bokeh_script=bokehscript, bokeh_div=bokehdiv)
  except Quandl.ErrorDownloading as detail:
    print detail
  except Quandl.DatasetNotFound as detail:
    print detail

  codes = [s['code'] for s in search]
  error = "<div> Code not in the list. Try: <ul><li>" + "</li><li>".join(codes) + "</li></ul> </div>"
  print error 
  #message = Markup(error)
  #print "Marked up"
  #flash("test")
  #print "Flashed"
  return render_template("index.html", error=error)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=33507)
