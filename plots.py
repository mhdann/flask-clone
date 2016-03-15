from bokeh.plotting import *
from bokeh.plotting import figure
from bokeh.charts import Line
from bokeh.embed import components 
import numpy as np

def datetime(x):
  # Converte to numpy datetime explicitly
  # http://bokeh.pydata.org/en/latest/docs/gallery/stocks.html
  return np.array(x, dtype=np.datetime64)


# Define a function that will return an HTML snippet. Cribbed:
# https://github.com/rpazyaquian/bokeh-flask-tutorial/blob/master/app/plots.py
def build_plot(data, ticker):
  # Set the output for our plot
  print "build_plot() reached"
  print "Data: "
  print data
  p = figure(x_axis_type = 'datetime', width=800, height=800)
  p.title = ticker 
  p.xaxis.axis_label = 'Date'

  if 'Close' in data.columns:
    # construct the plot
   p.line(datetime(data.Date), data.Close)
   p.yaxis.axis_label = 'Price'

  else:
    col = 0
    p.yaxis.axis_label = data.columns[col]
    p.line(datetime(data.index), data.iloc[:,col])

  print "Plot made"

  # Create an HTML snippet of our plot.
  snippet = components(p)

  print "js snippet set"
  # print snippet[0]
  # print snippet[1]
  # Return the snippet we want to place in our page.
  return snippet
