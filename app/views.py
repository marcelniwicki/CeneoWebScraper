from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/extract')
def extract():
    pass

@app.route('/products')
def products():
    pass

@app.route('/opinions/<productId>')
def opinions(product_id):
    pass

@app.route('/charts/<productId>')
def charts(product_id):
    pass