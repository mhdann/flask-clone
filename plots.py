from bokeh.plotting import *
from bokeh.plotting import figure
from bokeh.charts import Line
from bokeh.embed import components 

# Define a function that will return an HTML snippet. Cribbed:
# https://github.com/rpazyaquian/bokeh-flask-tutorial/blob/master/app/plots.py
def build_plot(data, ticker):
  # Set the output for our plot
  print "build_plot() reached"
  print "Data: "
  print data

  # construct the plot
  p = Line(data.High, title=ticker, xlabel='Date', ylabel='Price', width=800, height=800)
  print "Plot made"

  # Create an HTML snippet of our plot.
  snippet = components(p)
  print "js snippet set"
  print snippet[0]
  print snippet[1]
  # Return the snippet we want to place in our page.
  return snippet
