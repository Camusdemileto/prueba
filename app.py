from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def index():
    listaa = ['1','2','3','4'] 
    data = {
        
            'titulo':'Index', 
            'bienvenida':'Saludos',
            'lista' : listaa 
                
        }  
    return render_template('index.html',data = data)
 
if __name__ == '__main__':
    app.run( port= 4000 ,use_reloader=True)