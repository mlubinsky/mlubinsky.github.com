import os
pjoin = os.path.join

from flask import Flask, render_template, request
import bokeh.plotting as bk
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
route = app.route

template_dir = 'templates'
HTML_file='generated_plot.html'

if not os.path.exists(template_dir):
    os.mkdir(template_dir)

plot_file = pjoin(template_dir, HTML_file)

@route('/')
def plot():
    p = bk.figure(title="Polynomial")
    xs = list(range(11))
    ys = [x ** 2 for x in xs]

    p.line(xs, ys, line_width=2)

    html = file_html(p, CDN, "plot")
    with open(plot_file, 'w') as f:
        f.write(html)
    return render_template(HTML_file)


if __name__ == '__main__':
    print "http://127.0.0.1:5000/"
    app.debug = True
    app.run()
