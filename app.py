# app.py - Aplikasi To-Do List API
# Dibuat menggunakan Flask (Python)
# Di-deploy ke platform PaaS Railway

from flask import Flask, jsonify
import os

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi dari variabel lingkungan
APP_NAME = os.environ.get('APP_NAME', 'API To-Do List')
APP_VERSION = os.environ.get('APP_VERSION', '1.0.0')

# Simulasi data tugas (in-memory database)
todos = [
    {'id': 1, 'tugas': 'Belajar Flask', 'selesai': True},
    {'id': 2, 'tugas': 'Deploy ke Railway', 'selesai': False},
    {'id': 3, 'tugas': 'Ngerjain laporan', 'selesai': False}
]

# Endpoint 1 - Beranda
@app.route('/')
def beranda():
    return jsonify({
        'pesan': APP_NAME,
        'status': 'aktif',
        'versi': APP_VERSION
    })

# Endpoint 2 - Health check
@app.route('/health')
def health():
    return jsonify({'status': 'sehat'})

# Endpoint 3 - Daftar tugas
@app.route('/todos')
def get_todos():
    return jsonify({'todos': todos})

# Jalankan aplikasi
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)