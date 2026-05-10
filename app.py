from flask import Flask, jsonify
import os

app = Flask(__name__)

# Simulasi database sederhana (pakai list, ini "add-on" in-memory)
todos = [
    {'id': 1, 'tugas': 'Belajar Flask', 'selesai': True},
    {'id': 2, 'tugas': 'Deploy ke Railway', 'selesai': False},
    {'id': 3, 'tugas': 'Ngerjain laporan', 'selesai': False}
]

# Endpoint 1 - Beranda
@app.route('/')
def beranda():
    return jsonify({
        'pesan': 'API To-Do List',
        'status': 'aktif',
        'versi': '1.0.0'
    })

# Endpoint 2 - Health check
@app.route('/health')
def health():
    return jsonify({'status': 'sehat'})

# Endpoint 3 - Daftar tugas
@app.route('/todos')
def get_todos():
    return jsonify({'todos': todos})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)