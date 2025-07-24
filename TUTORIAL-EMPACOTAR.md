# Como Transformar o Sistema em Executável e Instalador (Windows)

> **ATENÇÃO:** O método recomendado e prioritário para usar o sistema é via deploy em nuvem (Railway, Heroku, etc) ou como PWA. O empacotamento desktop (PyInstaller) só deve ser utilizado em casos muito específicos, pois o sistema foi otimizado para rodar 100% na web.

Este tutorial ensina como empacotar seu sistema Flask + Firebase em um executável (.exe) usando PyInstaller e criar um instalador (.exe) para Windows.

**⚠️ IMPORTANTE:** O executável desktop depende de arquivos sensíveis (como a chave do Firebase). Nunca distribua esses arquivos publicamente. Prefira sempre o uso web/PWA para maior segurança e praticidade.

---

## 1. Gerar Executável com PyInstaller

O [PyInstaller](https://pyinstaller.org/) permite criar executáveis a partir de aplicações Python, empacotando tudo em um arquivo .exe.

### Passo 1: Instalar o PyInstaller
Abra o PowerShell na raiz do projeto e execute:
```powershell
pip install pyinstaller
```

### Passo 2: Gerar o executável
Execute o comando abaixo para empacotar sua aplicação Flask:
```powershell
pyinstaller --onefile --add-data "templates;templates" --add-data "views;views" --add-data "serviceAccountKey.json;." --add-data "banco-clinica.sql;." app.py
```
- O parâmetro `--add-data` garante que as pastas e arquivos necessários sejam incluídos no executável.
- Se precisar incluir outros arquivos (como `.env`), adicione mais `--add-data`.

> **Atenção:**  
> No Windows, use ponto e vírgula `;` para separar o arquivo da pasta de destino.  
> Exemplo: `"templates;templates"`  
> No Linux/Mac seria dois pontos `:`.

### Passo 3: Encontrar o executável
O executável será gerado na pasta `dist/` com o nome `app.exe` (ou o nome do seu script principal).

### Passo 4: Testar o executável
No PowerShell, execute:
```powershell
./dist/app.exe
```
A aplicação Flask será iniciada. Acesse pelo navegador em `http://localhost:5000` (ou a porta configurada).

---

## 2. Criar Instalador com Inno Setup

O [Inno Setup](https://jrsoftware.org/isinfo.php) é uma ferramenta gratuita para criar instaladores Windows.

### Passo 1: Baixar e instalar o Inno Setup
- Acesse: https://jrsoftware.org/isdl.php
- Baixe e instale o Inno Setup.

### Passo 2: Preparar os arquivos para o instalador
Crie uma pasta, por exemplo `dist/instalador/`, e coloque dentro:
- O executável gerado (`app.exe`)
- Pasta `templates/`
- Pasta `views/`
- `serviceAccountKey.json`
- `banco-clinica.sql`
- (Se houver) `.env`

> **Nunca inclua** arquivos sensíveis em repositórios públicos!

### Passo 3: Criar o script do instalador
Exemplo de script (`instalador.iss`):
```iss
[Setup]
AppName=CRUD Clínica Pacientes
AppVersion=1.0
DefaultDirName={pf}\CRUDClinica
DefaultGroupName=CRUD Clínica
OutputDir=.
OutputBaseFilename=Instalador-CRUD-Clinica

[Files]
Source: "dist/instalador/*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\CRUD Clínica"; Filename: "{app}\app.exe"
```

### Passo 4: Compilar o instalador
- Abra o Inno Setup.
- Carregue o script `instalador.iss`.
- Clique em "Compile".
- O instalador será gerado na pasta configurada (ex: `Instalador-CRUD-Clinica.exe`).

---

## 3. Como Usar o Sistema Instalado

- Basta abrir o executável instalado. Ele rodará o sistema localmente em `http://localhost:5000`.
- Não é necessário rodar comandos Python manualmente.
- O sistema funcionará normalmente, inclusive como PWA, se instalado pelo navegador.

---

## 4. Solução de Problemas

### O sistema não carrega ou aparece erro de chave Firebase
- Verifique se o arquivo `serviceAccountKey.json` está presente junto ao executável.
- Certifique-se de que a chave é válida para o projeto Firebase configurado.

### Erro ao empacotar com PyInstaller
- Use o parâmetro `--add-data` corretamente (veja exemplos acima).
- Teste o executável em outro computador.

### Problemas com portas ocupadas
- Certifique-se de que a porta 5000 está livre antes de rodar o executável.

---

## 5. Referências
- [Tutorial de Deploy em Nuvem (prioritário)](./TUTORIAL-DEPLOY.md)
- [Documentação do PyInstaller](https://pyinstaller.org/en/stable/)
- [Inno Setup](https://jrsoftware.org/isinfo.php)

---

> **Recomendação:** Sempre priorize o uso via PWA e deploy em nuvem para maior compatibilidade, segurança e facilidade de manutenção. O empacotamento desktop é opcional e só deve ser feito se realmente necessário.
