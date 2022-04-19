from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import math

app = FastAPI(redoc_url=None)
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/platypus')
def fn_main(request: Request):
    return templates.TemplateResponse('calculator.html', context=
    {
        'request': request,
        'language': 'en',
        'title': 'Platypus',
        'result': 'NULL'
    })

@app.post('/platypus')
def fn_main(request: Request, entry: str = Form(None)):
    blacklist = ['exit', 'import', 'system']
    output = 'NULL'
    work = True
    if entry is not None:
        for elt in blacklist:
            if elt in entry:
                work = False
                output = 'ERROR'
        if work:
            try:
                output = eval(entry, {}, {'PI': math.pi})
            except:
                output = 'ERROR'
    
    return templates.TemplateResponse('calculator.html', context=
    {
        'request': request,
        'language': 'en',
        'title': 'Platypus',
        'result': output
    })