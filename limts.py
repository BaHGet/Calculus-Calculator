from flask import Flask, request, render_template, redirect, url_for
import sympy as smp
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ff04f4eeee67d7a083fe2c278cddca78'

@app.route("/", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        way = request.form['bnt']
        fomrula = request.form['fomrula']
        sym = smp.symbols('x')

        if way == 'inter':
            i = smp.integrate(fomrula , sym)
            return( 
                "<h1 " +  "style='font-family:Roboto ,serif;'" + '>' + 'Integration  of '+ fomrula +' is: </h1>'
                
                "<h1 " +  "style='font-family:Roboto ,serif;'" + '>' + str(i) +'</h1>')
        if way == 'dif':
            d = smp.diff(fomrula , sym)
            return( 
                "<h1 " +  "style='font-family:Roboto ,serif;'" + '>' + 'Differentiation  of '+ fomrula +' is: </h1>'
                
                "<h1 " +  "style='font-family:Roboto ,serif;'" + '>' + str(d) +'</h1>')
    
    else:
        return render_template('my-form.html', title='type formula')





""" 


@app.route("/answer")
def answer(eq):
    
    return '<h1>'+ eq +'</h1>'



    if str(eq[0]) == 'inter':
        x = smp.symbols('x')
        f = smp.integrate(str(eq[1]) , x)
        return f'<h1>{str(f)}</h1>'
    else:
        x = smp.symbols('x')
        f = smp.diff(str(eq[1]) , x)
        return f'<h1>{str(f)}</h1>'
"""





if __name__ == '__main__':
    app.run()
