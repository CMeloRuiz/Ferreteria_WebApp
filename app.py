from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS 
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='static') # Apunta a la nueva carpeta 'static'
CORS(app)

try:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Las variables de entorno SUPABASE_URL o SUPABASE_SERVICE_ROLE_KEY no están configuradas.")

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("DEBUG: Cliente de Supabase inicializado correctamente.")

except Exception as e:
    print(f"ERROR CRÍTICO: Fallo al inicializar el cliente de Supabase: {e}")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Esta ruta manejará todos los otros archivos estáticos (CSS, JS, imágenes)
    return send_from_directory(app.static_folder, path)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Obtiene todos los productos de la base de datos Supabase.
    """
    try:
        result = supabase.from_('products').select('*').execute()

        productos = result.data

        if not productos and result.count is not None and result.count > 0:
            pass

        return jsonify(productos), 200

    except Exception as e:
        print(f"ERROR EN RUTA /api/products: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
