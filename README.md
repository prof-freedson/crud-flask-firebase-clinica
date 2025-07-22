# Sistema CRUD de Pacientes - Flask + Firebase Firestore

Este é um sistema de gerenciamento de pacientes desenvolvido com Flask e Firebase Firestore, baseado na estrutura da tabela `paciente` do banco de dados da clínica.

## Funcionalidades

- ✅ **Criar** novos pacientes
- ✅ **Listar** todos os pacientes cadastrados  
- ✅ **Editar** dados de pacientes existentes
- ✅ **Excluir** pacientes do sistema

## Campos dos Pacientes

- Nome completo
- Data de nascimento
- Peso (kg)
- Altura (m)
- Tipo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-)

## Estrutura do Projeto

```
crud-flask-firebase-clinica/
├── app.py                    # Aplicação Flask principal
├── requirements.txt          # Dependências Python
├── firebase-key.json.example # Exemplo de credenciais Firebase
├── serviceAccountKey.json    # Credenciais Firebase (você precisa criar)
├── templates/                # Templates HTML
│   ├── index.html           # Página inicial
│   ├── pacientes.html       # Lista de pacientes
│   ├── criar.html           # Formulário de criação
│   └── editar.html          # Formulário de edição
├── views/                    # Templates EJS (alternativos)
│   ├── index.ejs            # Página inicial (EJS)
│   ├── pacientes.ejs        # Lista de pacientes (EJS)
│   ├── criar.ejs            # Formulário de criação (EJS)
│   └── editar.ejs           # Formulário de edição (EJS)
├── README.md                 # Este arquivo
└── TUTORIAL-PWA.md          # Tutorial para transformar em PWA
```

## Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Firebase (veja seção abaixo)

### 3. Executar a Aplicação

```bash
python app.py
```

A aplicação estará disponível em: http://localhost:5000

## Rotas da Aplicação

- `GET /` - Página inicial
- `GET /pacientes` - Lista todos os pacientes
- `GET /criar` - Formulário para criar paciente
- `POST /criar` - Processa criação do paciente
- `GET /editar/<id>` - Formulário para editar paciente
- `POST /editar/<id>` - Processa edição do paciente
- `POST /deletar/<id>` - Exclui paciente

## Configuração do Firebase

### Passo 1: Criar Projeto no Firebase

1. Acesse [console.firebase.google.com](https://console.firebase.google.com)
2. Clique em "Criar um projeto"
3. Dê um nome ao projeto (ex: "clinica-pacientes")
4. Desabilite o Google Analytics (opcional)
5. Clique em "Criar projeto"

### Passo 2: Configurar Firestore Database

1. No console do Firebase, vá em "Firestore Database"
2. Clique em "Criar banco de dados"
3. Escolha "Iniciar no modo de teste" (para desenvolvimento)
4. Selecione uma localização (ex: "southamerica-east1")
5. Clique em "Concluído"

### Passo 3: Gerar Chave de Serviço

1. No console do Firebase, vá em "Configurações do projeto" (ícone de engrenagem)
2. Vá na aba "Contas de serviço"
3. Clique em "Gerar nova chave privada"
4. Será baixado um arquivo JSON
5. **Renomeie este arquivo para `serviceAccountKey.json`**
6. **Coloque este arquivo na raiz do projeto**

> **Dica:** Use o arquivo `firebase-key.json.example` como referência para a estrutura das credenciais.

### Passo 4: Configurar Regras de Segurança (Opcional)

Para desenvolvimento, você pode usar estas regras no Firestore:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```

**⚠️ IMPORTANTE:** Para produção, configure regras mais restritivas!

## Estrutura dos Dados no Firestore

Os pacientes são armazenados na coleção `pacientes` com a seguinte estrutura:

```json
{
  "nome_pac": "João Silva",
  "data_nasc_pac": "1990-05-15",
  "peso_pac": 75.5,
  "alt_pac": 1.75,
  "tipo_sang": "O+"
}
```

## Tecnologias Utilizadas

- **Flask 2.3.3** - Framework web Python
- **Firebase Admin SDK 6.2.0** - SDK para integração com Firebase
- **Firestore** - Banco de dados NoSQL do Google
- **Jinja2** - Motor de templates (incluído no Flask)
- **HTML5** - Estrutura das páginas
- **CSS inline** - Estilização básica sem arquivos externos

## Características Técnicas

- Interface responsiva e simples
- Validação de formulários no frontend e backend
- Mensagens de feedback para o usuário
- Tratamento de erros
- Formatação automática de datas
- Confirmação antes de excluir registros

## Templates Disponíveis

O projeto inclui duas versões dos templates:
- **HTML puro** (pasta `templates/`) - Para uso direto com Flask
- **EJS** (pasta `views/`) - Para conversão para Node.js/Express se necessário

## Transformando em PWA

Veja o arquivo `TUTORIAL-PWA.md` para instruções sobre como transformar este sistema em um Progressive Web App (PWA).

## Possíveis Melhorias

- [ ] Adicionar paginação na lista de pacientes
- [ ] Implementar busca/filtros
- [ ] Adicionar validações mais robustas
- [ ] Cache de dados
- [ ] Testes automatizados
- [ ] Deploy em produção (Heroku, Railway, etc.)
- [ ] Autenticação de usuários
- [ ] Transformar em PWA (veja TUTORIAL-PWA.md) 