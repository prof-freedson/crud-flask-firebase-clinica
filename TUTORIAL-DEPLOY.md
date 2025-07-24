# Tutorial: Publicando o Sistema CRUD de Pacientes Flask em Produção

> **ATENÇÃO:** O método recomendado para usar o sistema é via deploy em nuvem (Railway, Heroku, Vercel, etc). O uso de executáveis locais é opcional e só deve ser feito em casos específicos. Siga este tutorial para garantir acesso universal e manutenção facilitada.

---

## 1. Ajustes necessários no projeto

### a) Proteja arquivos sensíveis
- **NUNCA** suba `serviceAccountKey.json` para repositórios públicos.
- Adicione `serviceAccountKey.json` e `.env` ao `.gitignore` (já está configurado).

### b) Variáveis de ambiente
- O Flask pode ler variáveis de ambiente usando o pacote `os`.
- Para produção, configure a chave do Firebase e outras configs via variáveis de ambiente na plataforma escolhida.

### c) Ajuste o código para ler a chave do Firebase das variáveis de ambiente (opcional, recomendado para produção)
No `app.py`, troque:
```python
cred = credentials.Certificate('serviceAccountKey.json')
```
por:
```python
import json
service_account_info = json.loads(os.environ.get('SERVICE_ACCOUNT_KEY'))
cred = credentials.Certificate(service_account_info)
```
Assim, a chave será lida da variável de ambiente `SERVICE_ACCOUNT_KEY`.

> **Dica:** Para desenvolvimento local, mantenha o arquivo `serviceAccountKey.json`.

---

## 2. Subindo o projeto para o GitHub

1. Crie um repositório no GitHub.
2. Suba todos os arquivos do projeto, exceto o `.env` e `serviceAccountKey.json`.
3. No README, explique que esses arquivos devem ser configurados nas variáveis de ambiente da plataforma de deploy.

---

## 3. Opções de Deploy

> **Nota:** Damos prioridade a opções gratuitas. Por isso, Vercel aparece como primeira opção, mesmo com limitações para projetos Flask. Railway e Heroku são alternativas pagas, mas oferecem maior compatibilidade.

### A) Vercel (gratuito, para Python)

1. Crie uma conta em [vercel.com](https://vercel.com)
2. Importe seu repositório do GitHub
3. Configure as variáveis de ambiente:
   - `SERVICE_ACCOUNT_KEY` (cole o conteúdo do seu `serviceAccountKey.json`)
4. Vercel detecta Python automaticamente, mas pode ser necessário configurar o build/output.
5. Clique em "Deploy"

> **Nota:** O suporte a Flask no Vercel é limitado. Caso encontre dificuldades, utilize Railway ou Heroku.

> **Dica:** Clique [aqui](https://www.youtube.com/watch?v=o17Fk4Dcn-w) para assistir a um tutorial com um passo a passo de como publicar o sistema na Vercel

### B) Railway (pago, recomendado para Python)

1. Crie uma conta em [railway.app](https://railway.app)
2. Clique em "New Project" > "Deploy from GitHub repo"
3. Escolha seu repositório
4. Configure as variáveis de ambiente:
   - `SERVICE_ACCOUNT_KEY` (cole o conteúdo do seu `serviceAccountKey.json` como string JSON)
   - Outras variáveis, se necessário
5. Railway detecta Flask automaticamente. Se necessário, defina o comando de start:
   ```
   python app.py
   ```
6. Clique em "Deploy"
7. O sistema estará disponível em uma URL pública.

### C) Heroku (pago)

1. Crie uma conta em [heroku.com](https://heroku.com)
2. Instale o [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. No PowerShell, faça login:
   ```powershell
   heroku login
   ```
4. Crie um app:
   ```powershell
   heroku create nome-do-app
   ```
5. Adicione as variáveis de ambiente:
   ```powershell
   heroku config:set SERVICE_ACCOUNT_KEY="<cole o conteúdo do seu serviceAccountKey.json>"
   ```
6. Faça deploy:
   ```powershell
   git push heroku main
   ```
7. O sistema estará disponível em `https://nome-do-app.herokuapp.com`

> **Dica:** Para Flask, pode ser necessário um arquivo `Procfile` com:
> ```
> web: python app.py
> ```

---

## 4. Dicas de Produção

- Sempre use HTTPS em produção.
- Configure regras de segurança do Firestore para produção.
- Nunca exponha a chave do Firebase publicamente.
- Teste o sistema após o deploy: cadastre, edite e exclua pacientes.
- Consulte os logs da plataforma em caso de erro.

---

## 5. Comandos Úteis (PowerShell)

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

---

## 6. Observações finais

- O sistema continuará funcionando como PWA, inclusive offline (conforme o service worker).
- O backend Flask e os templates HTML são servidos normalmente pela plataforma.
- Para segurança, nunca exponha a chave do Firebase em repositórios públicos.
- Para dúvidas, consulte a documentação da plataforma escolhida (Railway, Heroku, Vercel).

---

**Desenvolvido em:** 24/06/2025  
**Tecnologias:** Flask + Firebase + Jinja2  
**Objetivo:** Sistema CRUD de pacientes para clínica 