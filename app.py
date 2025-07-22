from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os

app = Flask(__name__)

# Inicialização do Firebase
cred = credentials.Certificate('serviceAccountKey.json')  # Arquivo de credenciais do Firebase
firebase_admin.initialize_app(cred)
db = firestore.client()

# Função para formatar data
def formatar_data(data_str):
    """Converte string de data para formato brasileiro"""
    if isinstance(data_str, str):
        try:
            data_obj = datetime.strptime(data_str, '%Y-%m-%d')
            return data_obj.strftime('%d/%m/%Y')
        except:
            return data_str
    return data_str

def formatar_data_para_input(data_str):
    """Converte data brasileira para formato de input HTML"""
    if isinstance(data_str, str) and '/' in data_str:
        try:
            data_obj = datetime.strptime(data_str, '%d/%m/%Y')
            return data_obj.strftime('%Y-%m-%d')
        except:
            return data_str
    return data_str

@app.route('/')
def index():
    """Página inicial do sistema"""
    return render_template('index.html')

@app.route('/pacientes')
def listar_pacientes():
    """Lista todos os pacientes cadastrados"""
    try:
        pacientes_ref = db.collection('pacientes')
        docs = pacientes_ref.stream()
        
        pacientes = []
        for doc in docs:
            paciente = doc.to_dict()
            paciente['id'] = doc.id
            # Formatar data para exibição
            if 'data_nasc_pac' in paciente:
                paciente['data_nasc_pac'] = formatar_data(paciente['data_nasc_pac'])
            pacientes.append(paciente)
        
        return render_template('pacientes.html', pacientes=pacientes)
    except Exception as e:
        return render_template('pacientes.html', pacientes=[])

@app.route('/criar', methods=['GET', 'POST'])
def criar_paciente():
    """Criar novo paciente"""
    if request.method == 'POST':
        try:
            # Coletar dados do formulário
            paciente_data = {
                'nome_pac': request.form['nome_pac'],
                'data_nasc_pac': request.form['data_nasc_pac'],
                'peso_pac': float(request.form['peso_pac']),
                'alt_pac': float(request.form['alt_pac']),
                'tipo_sang': request.form['tipo_sang']
            }
            
            # Adicionar ao Firestore
            db.collection('pacientes').add(paciente_data)
            return redirect(url_for('listar_pacientes'))
            
        except Exception as e:
            pass
    
    return render_template('criar.html')

@app.route('/editar/<paciente_id>', methods=['GET', 'POST'])
def editar_paciente(paciente_id):
    """Editar paciente existente"""
    if request.method == 'POST':
        try:
            # Coletar dados do formulário
            paciente_data = {
                'nome_pac': request.form['nome_pac'],
                'data_nasc_pac': request.form['data_nasc_pac'],
                'peso_pac': float(request.form['peso_pac']),
                'alt_pac': float(request.form['alt_pac']),
                'tipo_sang': request.form['tipo_sang']
            }
            
            # Atualizar no Firestore
            db.collection('pacientes').document(paciente_id).update(paciente_data)
            return redirect(url_for('listar_pacientes'))
            
        except Exception as e:
            pass
    
    # GET - buscar dados do paciente para edição
    try:
        doc = db.collection('pacientes').document(paciente_id).get()
        if doc.exists:
            paciente = doc.to_dict()
            paciente['id'] = doc.id
            # Formatar data para input
            if 'data_nasc_pac' in paciente:
                paciente['data_nasc_pac'] = formatar_data_para_input(paciente['data_nasc_pac'])
            return render_template('editar.html', paciente=paciente)
        else:
            return redirect(url_for('listar_pacientes'))
    except Exception as e:
        return redirect(url_for('listar_pacientes'))

@app.route('/deletar/<paciente_id>', methods=['POST'])
def deletar_paciente(paciente_id):
    """Deletar paciente"""
    try:
        db.collection('pacientes').document(paciente_id).delete()
    except Exception as e:
        pass
    
    return redirect(url_for('listar_pacientes'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 