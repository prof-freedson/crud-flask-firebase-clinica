# Como Transformar o Sistema em Executável e Instalador (Windows)

Este tutorial ensina como empacotar seu sistema Flask + Firebase em um executável (.exe) usando PyInstaller e criar um instalador (.exe) para Windows, facilitando a distribuição e instalação em outros computadores.

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

## 3. Observações Importantes
- O executável depende dos arquivos de configuração e das views. Sempre distribua juntos.
- O Firebase requer a chave `serviceAccountKey.json` e o `.env` (se usado).
- O arquivo `firebase-key.json.example` é apenas um modelo de exemplo para você preencher e renomear como `serviceAccountKey.json` com os dados reais do seu projeto Firebase.
- Teste o instalador em outro computador antes de distribuir.

---

## 4. Referências
- [Documentação do PyInstaller](https://pyinstaller.org/en/stable/)
- [Inno Setup](https://jrsoftware.org/isinfo.php)

---
