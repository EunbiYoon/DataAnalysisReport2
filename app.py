from flask import Flask, render_template
from graph import legend2M, legend1M, legend0M, ABlabels, Avalues2M, Avalues1M, Avalues0M, Bvalues2M, Bvalues1M, Bvalues0M, Plabels, Pvalues,svc_data_html, min_data_html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', ABlabels=ABlabels,
    Avalues2M=Avalues2M, Avalues1M=Avalues1M, Avalues0M=Avalues0M,
    Bvalues2M=Bvalues2M,Bvalues1M=Bvalues1M,Bvalues0M=Bvalues0M,
    legend2M=legend2M, legend1M=legend1M, legend0M=legend0M, min_data_html=min_data_html)

@app.route("/charts")
def charts():
    return render_template('charts.html', ABlabels=ABlabels,
    Avalues2M=Avalues2M, Avalues1M=Avalues1M, Avalues0M=Avalues0M,
    Bvalues2M=Bvalues2M,Bvalues1M=Bvalues1M,Bvalues0M=Bvalues0M,
    Plabels=Plabels,Pvalues=Pvalues,
    legend2M=legend2M, legend1M=legend1M, legend0M=legend0M)

@app.route("/tables")
def tables():
    return render_template('tables.html',svc_data_html=svc_data_html)

@app.route("/layout_static")
def layout_static():
    return render_template('layout-static.html')

@app.route("/layout_sidenav")
def layout_sidenav():
    return render_template('layout-sidenav-light.html')

if __name__ == "__main__":
    app.run(debug=True)