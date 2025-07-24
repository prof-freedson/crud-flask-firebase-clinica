# Sistema CRUD de Pacientes - Flask + Firebase Firestore

Sistema completo de gerenciamento de pacientes desenvolvido com Flask, Firebase e Jinja2.

## 📋 Funcionalidades

- ✅ Criar novos pacientes
- ✅ Listar todos os pacientes
- ✅ Editar dados do paciente
- ✅ Excluir paciente
- ✅ Interface HTML simples (sem CSS)
- ✅ Dados armazenados no Firebase Firestore

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** - Framework web
- **Jinja2** - Template engine
- **Firebase Admin SDK** - Integração com Firebase
- **Firebase Firestore** - Banco de dados NoSQL

## 📦 Instalação

### 1. Instalar dependências
```powershell
pip install -r requirements.txt
```

### 2. Configuração do Firebase

#### Passo 2.1: Criar projeto no Firebase
1. Acesse [Firebase Console](https://console.firebase.google.com)
2. Clique em "Criar um projeto"
3. Digite o nome do projeto (ex: "clinica-pacientes")
4. Configure o Google Analytics se desejar
5. Clique em "Criar projeto"

#### Passo 2.2: Habilitar Firestore
1. No painel do Firebase, vá em "Firestore Database"
2. Clique em "Criar banco de dados"
3. Escolha "Iniciar no modo de teste" 
4. Selecione a localização (ex: southamerica-east1)
5. Clique em "Concluído"

#### Passo 2.3: Gerar chave de acesso
1. Vá em "Configurações do projeto" (ícone de engrenagem)
2. Clique na aba "Contas de serviço"
3. Clique no botão "Gerar nova chave privada" na seção "Chave privada do SDK Admin"
4. Confirme o download do arquivo JSON
5. Renomeie o arquivo baixado para `serviceAccountKey.json` (se necessário)
6. Coloque o arquivo `serviceAccountKey.json` na **raiz do projeto** (mesmo nível do arquivo `app.py`)

> **Atenção:**
> - Nunca compartilhe ou faça upload do arquivo `serviceAccountKey.json` em repositórios públicos.
> - Este arquivo é essencial para a autenticação do backend com o Firebase.
> - Se perder a chave, gere uma nova pelo mesmo caminho no console do Firebase.

#### Passo 2.4: Configurar variáveis de ambiente (opcional para produção)
- Para produção, configure a chave do Firebase como variável de ambiente `SERVICE_ACCOUNT_KEY` (veja o tutorial de deploy).

### 3. Executar aplicação

```powershell
python app.py
```

A aplicação estará disponível em: http://localhost:5000

## 📊 Estrutura dos Dados

### Tabela Paciente (Firebase Firestore Collection: 'pacientes')
```json
{
  "nome_pac": "João Silva",
  "data_nasc_pac": "1990-05-15",
  "peso_pac": 75.5,
  "alt_pac": 1.75,
  "tipo_sang": "O+"
}
```

## 🚀 Rotas da Aplicação

| Método | Rota                | Descrição                       |
|--------|---------------------|---------------------------------|
| GET    | `/`                 | Página inicial                  |
| GET    | `/pacientes`        | Lista todos os pacientes        |
| GET    | `/criar`            | Formulário para criar paciente  |
| POST   | `/criar`            | Criar novo paciente             |
| GET    | `/editar/<id>`      | Formulário para editar paciente |
| POST   | `/editar/<id>`      | Atualizar dados do paciente     |
| POST   | `/deletar/<id>`     | Excluir paciente                |

## 📁 Estrutura de Arquivos

```
crud-flask-firebase-clinica/
├── app.py                    # Aplicação Flask principal
├── requirements.txt          # Dependências Python
├── firebase-key.json.example # Exemplo de credenciais Firebase
├── serviceAccountKey.json    # Chave do Firebase (não versionada)
├── static/                   # Arquivos estáticos para PWA
│   ├── manifest.json         # Manifest do PWA
│   ├── service-worker.js     # Service Worker
│   └── icons/                # Ícones do app
├── templates/                # Templates HTML (Jinja2)
│   ├── index.html            # Página inicial
│   ├── pacientes.html        # Lista de pacientes
│   ├── criar.html            # Formulário de criação
│   └── editar.html           # Formulário de edição
├── views/                    # Templates EJS (alternativos)
│   ├── index.ejs             # Página inicial (EJS)
│   ├── pacientes.ejs         # Lista de pacientes (EJS)
│   ├── criar.ejs             # Formulário de criação (EJS)
│   └── editar.ejs            # Formulário de edição (EJS)
├── banco-clinica.sql         # Exemplo de estrutura SQL (opcional)
├── README.md                 # Este arquivo
├── TUTORIAL-PWA.md           # Tutorial PWA
├── TUTORIAL-EMPACOTAR.md     # Tutorial para empacotar
└── TUTORIAL-DEPLOY.md        # Tutorial de deploy em produção
```

## 🔧 Configurações Adicionais

### Regras de Segurança do Firestore
Para ambiente de desenvolvimento, use estas regras:
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

⚠️ **IMPORTANTE**: Para produção, configure regras mais restritivas!

## 🎯 Funcionalidades Extras

- Validação de dados nos formulários
- Confirmação antes de excluir pacientes
- Interface responsiva e simples
- Formatação automática de datas
- Mensagens de feedback para o usuário
- Templates EJS disponíveis para migração Node.js

## 🐛 Solução de Problemas

### Erro: "Não foi possível encontrar 'serviceAccountKey.json'"
- Certifique-se de ter baixado a chave do Firebase
- Verifique se o arquivo está na raiz do projeto
- Confirme se o nome está exato: `serviceAccountKey.json`

### Erro: "Permissão negada no Firestore"
- Verifique se o Firestore está habilitado no projeto
- Confirme se as regras de segurança permitem acesso
- Verifique a localização do banco de dados

### Erro ao empacotar com PyInstaller
- Use o parâmetro `--add-data` corretamente (veja o tutorial de empacotamento)
- Teste o executável em outro computador

## 📝 Comandos Úteis

```powershell
# Instalar dependências
pip install -r requirements.txt

# Executar localmente
python app.py

# Instalar Heroku CLI
winget install Heroku.HerokuCLI

# Fazer deploy para Heroku
heroku login
heroku create nome-do-app
heroku config:set SERVICE_ACCOUNT_KEY="<cole o conteúdo do seu serviceAccountKey.json>"
git push heroku main
```

## 🚀 Deploy (Opcional)

Para colocar em produção, você pode usar:
- **Railway** (recomendado para Python)
- **Heroku**
- **Vercel** (opcional, suporte limitado para Flask)
- **Google Cloud Platform**

Veja o tutorial [TUTORIAL-DEPLOY.md](./TUTORIAL-DEPLOY.md) para instruções detalhadas.

## 🧭 Orientação: Flexibilizando o sistema para outras plataformas

Para adaptar e ampliar o uso do sistema em diferentes plataformas (web, PWA, desktop), siga os tutoriais na ordem recomendada abaixo:

1. **[TUTORIAL-PWA.md](./TUTORIAL-PWA.md)**  
   Aprenda a transformar o sistema em um Progressive Web App (PWA), permitindo instalação no dispositivo, funcionamento offline e experiência de app nativo.

2. **[TUTORIAL-DEPLOY.md](./TUTORIAL-DEPLOY.md)**  
   Veja como publicar o sistema em nuvem, tornando-o acessível via internet, com HTTPS e pronto para uso universal. Este é o método recomendado e prioritário para produção.

3. **[TUTORIAL-EMPACOTAR.md](./TUTORIAL-EMPACOTAR.md)**  
   Caso precise de uma versão desktop (executável para Windows), siga este tutorial. Lembre-se: o sistema foi otimizado para rodar na web, então utilize o empacotamento apenas em situações específicas.

> **Recomendação:** Sempre priorize o uso via PWA e deploy em nuvem para maior compatibilidade, segurança e facilidade de manutenção. O empacotamento desktop é opcional e só deve ser feito se realmente necessário.

---

**Desenvolvido em**: 24/06/2025  
**Tecnologias**: Flask + Firebase + Jinja2  
**Objetivo**: Sistema CRUD de pacientes para clínica 