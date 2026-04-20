# Cara Core PDV — Guia Rápido de Primeiros Passos (v1.0.15)

Este guia ajuda o lojista a instalar e autorizar o Cara Core PDV quando o antivírus ou o SmartScreen bloquearem o instalador.

Pré-requisitos
- Windows 10/11
- Python 3.8+ (temporariamente necessário para o instalador script)

1) Executar o instalador
- Abra o `PowerShell` (ou `cmd`) e rode:

```powershell
python scripts\install_windows.py
```

2) Se o Windows Defender bloquear (recomendado)
- Se o instalador não puder adicionar automaticamente a exclusão, execute o PowerShell como Administrador e rode:

```powershell
Add-MpPreference -ExclusionPath "$env:APPDATA\CaraCore"
```

3) Se o SmartScreen mostrar "Windows protected your PC"
- Clique em "More info" e depois em "Run anyway".
- Alternativa: clique com o botão direito no executável, vá em "Properties" e marque "Unblock" se estiver disponível.

4) Verificando a instalação
- Arquivos principais: `%APPDATA%\CaraCore\`.
- Verifique `config.json` para o campo `java_home`.
- Logs de telemetria: `%APPDATA%\CaraCore\telemetry.log`.

5) Como autorizar manualmente no caso de bloqueios do antivírus de terceiros
- Abra o antivírus, procure por "Exclusions" ou "Exceptions" e adicione a pasta `%APPDATA%\CaraCore` como exceção.

6) O que fazer se ocorrer `BACKEND_TIMEOUT`
- Verifique primeiro conectividade da rede.
- Verifique se o processo Java está executando (Task Manager) e se o `java_home` está apontando para a JRE instalada.
- Consulte os logs do backend (local) em `%APPDATA%\CaraCore\logs` para timestamps do erro.
- Registre um evento de telemetria localmente:

```powershell
# Roda um pequeno POST manual (opcional se endpoint configurado)
python -c "from scripts.telemetry import telemetry_log_event; telemetry_log_event('backend_timeout', {'detail':'manual report'})"
```

7) Contato e suporte
- Se persistir, capture o arquivo `%APPDATA%\CaraCore\telemetry.log` e envie ao suporte técnico.

---
Este guia é intencionalmente simples para dar autonomia ao lojista em cenários 'bunker'.
