# CaraCore PDV - Instalacao (Windows)

Arquivos desta entrega:
- CaraCorePDV.exe
- checksum.sha256
- checksum.md5

## Validacao de integridade

No PowerShell, na pasta de artefatos:

```powershell
Get-FileHash -Path .\CaraCorePDV.exe -Algorithm SHA256
Get-FileHash -Path .\CaraCorePDV.exe -Algorithm MD5
```

Compare os valores com os arquivos checksum.sha256 e checksum.md5.

## Execucao

1. Execute CaraCorePDV.exe como usuario local do Windows.
2. Conclua o assistente de instalacao.
3. Abra o PDV e valide o acesso local em localhost:8080.

Login de degustacao:
- usuario: admin
- senha: 123456

Canal oficial:
- ../download.html
