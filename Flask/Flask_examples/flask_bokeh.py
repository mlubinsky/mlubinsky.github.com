import os
pjoin = os.path.join

from flask import Flask, render_template, request
import bokeh.plotting as bk
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
route = app.route

template_dir = 'templates'
if not os.path.exists(template_dir):
    os.mkdir(template_dir)
plot_file = pjoin(template_dir, 'generated_plot.html')

@route('/')
def plot():
    p = bk.figure(title="Polynomial")
    xs = list(range(11))
    ys = [x ** 2 for x in xs]

    p.line(xs, ys, line_width=2)

    html = file_html(p, CDN, "plot")
    with open(plot_file, 'w') as f:
        f.write(html)
    return render_template('generated_plot.html')


if __name__ == '__main__':
    app.debug = True
    app.run()