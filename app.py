import os
from dotenv import load_dotenv
from flask import Flask, jsonify, send_from_directory 
from flask_cors import CORS
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__, static_folder='static', static_url_path='') 

CORS(app) 

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        response = supabase.from_('products').select('*').execute()
        products = response.data
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inicio')
def serve_inicio():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/')
def serve_root():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/nosotros')
def serve_nosotros():
    return send_from_directory(app.static_folder, 'nosotros.html')

@app.route('/contacto')
def serve_contacto():
    return send_from_directory(app.static_folder, 'contacto.html')

@app.route('/productos')
def serve_products_page():
    return send_from_directory(app.static_folder, 'products.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)