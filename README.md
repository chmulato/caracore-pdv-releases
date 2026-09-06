# CaraCore-PDV - Loja e Releases

Canal público de vitrine, documentação e distribuição do **CaraCore-PDV** para pequenas operações de balcão e varejo local.

Mensagem central do produto: **quando a internet cai, o caixa não pode parar**. A oferta pública atual combina operação local em Windows, Linux e macOS com SQLite, recibo digital, leitura fiscal em linguagem simples e validação prática do básico antes de ampliar estrutura.

---

## Produto

O CaraCore-PDV foi desenhado para lojistas que precisam de:

- venda em balcão com operação local e previsível;
- continuidade de atendimento mesmo com internet instável;
- recibo digital e economia com bobinas/impressoras;
- controle básico de produtos, operadores, estoque e vendas;
- leitura simples do caixa e do fechamento do dia;
- configuração fiscal no escopo atual com NFC-e, alíquotas e NCM;
- trilha de evolução para Premium depois que o básico estiver validado.

Este repositório não deve ser lido como catálogo de promessa ampla. A leitura correta da oferta pública atual é:

- desktop local (Windows, Linux e macOS) com SQLite;
- NFC-e no escopo atual;
- PIX configurável e pagamento misto no fluxo vigente;
- validação de aderência para pequena loja antes de expansão.

Não tratar como promessa pública vigente neste README:

- TEF dedicado;
- voucher integrado;
- SAT, MFE ou appliance fiscal legado como cobertura ampla;
- ERP completo como mensagem central da oferta;
- integrações específicas sem homologação e validação comercial prévia.

A matriz de desenvolvimento fica no repositório **caracore-pdv**. Este repositório, **caracore-pdv-releases**, é a loja pública: GitHub Pages, releases, wikis de versão e materiais de apoio.

---

## Versão atual

| Campo | Valor |
| ----- | ----- |
| Versão | `v3.2.3-free` (maduro) · `v4.0.0-rc2` (candidato) |
| Status | Oferta pública atual + pré-release Qute |
| Publicação | 06/09/2026 |
| Linha | `free-edition` sobre a trilha `java_25` |
| Stack da oficina | Java 25 + Quarkus 3 + SQLite local (v4 Qute em homologação; canal público é v3.2.3-free) |
| Delivery publicado | Multi-plataforma: Windows, Linux e macOS — release FREE multiplataforma Java 25 |
| Requisito | Java 25+ instalado no sistema ([Temurin 25](https://adoptium.net/)) |
| Acesso | `http://localhost:8080/login` · primeiro acesso `admin` / `admin` |
| Release | <https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.2.3-free> |
| Loja | <https://pdv.caracore.com.br/> |

### Artefatos v3.2.3-free

| Artefato | Plataforma | SHA256 |
| -------- | ---------- | ------ |
| `caracore-pdv-v3.2.3-free-free-windows-x64.zip` | Windows 10/11 x64 | Publicado no `SHA256SUMS.txt` da release |
| `caracore-pdv-v3.2.3-free-free-linux-x64.zip` | Linux x64 (Ubuntu 20.04+) | Publicado no `SHA256SUMS.txt` da release |
| `caracore-pdv-v3.2.3-free-free-macos-x64.zip` | macOS 12+ x64 (Intel) | Publicado no `SHA256SUMS.txt` da release |
| `RELEASE_MANIFEST.json` | Manifesto técnico da publicação | Publicado no `SHA256SUMS.txt` da release |
| `SHA256SUMS.txt` | Lista oficial de hashes da release | Fonte de verificação |

### Candidato v4.0.0-rc1

| Artefato | Plataforma | SHA256 |
| -------- | ---------- | ------ |
| `caracore-pdv-4.0.0-rc1-qute-portable.zip` | Windows · Linux · macOS | `30b18951301a4f1523b64a0be8316e4182faefee4d107eda60de0286fe98ba0c` |
| Release | Pré-release | <https://github.com/chmulato/caracore-pdv-releases/releases/tag/v4.0.0-rc1> |

---

## Atualização operacional - 06/09/2026

- `v3.2.3-free` é a oferta pública atual: porta 8080, `/login` de operador, launcher valida Java 25+, boot `3.2.3-free`.
- `v3.2.2-free` rebaixada: backend subia, mas `/login` dava 404 e a porta era 8765.
- Pipeline CI/CD (`release-free.yml`) atualizado para `java-version: '25'` (Temurin 25).
- Alinhamento completo PDV Rust → Java: zonas de nav, InactivityLock, status bar, supervisor elevation, SetupGate.
- `v3.1.2-free` rebaixada para "anterior imediata" na trilha de versões da loja.
- `v3.0.10` permanece como referência histórica da série 3.x anterior à degustação Free.

---

## Linhas de versão

### Linha atual: `java_25`

A vitrine em `docs/` segue a trilha Java 25 da matriz, com SQLite local e soberania localhost. O download público maduro é a tag `v3.2.3-free`. O candidato `v4.0.0-rc2` (Quarkus + Qute) está como pré-release e não substitui a degustação Free. O GA do v4 permanece previsto para 08/11/2026.

Notas da versão atual: <https://pdv.caracore.com.br/wiki-release-v3-2-3-free.html>

Lista de versões: <https://pdv.caracore.com.br/versoes.html>

Documentação de produto: <https://wiki.caracore.com.br/projeto-pdv.html>

### Linhas anteriores

Tags antigas permanecem no GitHub Releases. A documentação de produto vive em `wiki.caracore.com.br`. A linha Spring + Electron WAR da branch `master` é só referência histórica.

---

## Degustação Free e planos

A loja comunica a **Versão de Degustação (Free)** como teste real, com até **100 vendas por mês** para validar o fluxo principal da pequena operação. O objetivo da Free é provar aderência de caixa, operação local, clareza fiscal e entendimento do escopo atual.

O plano Premium deve ser lido como ampliação segura depois da prova do básico, com mais estrutura operacional, suporte prioritário e evolução comercial compatível com a necessidade real da loja.

Qualquer narrativa de automação futura, integrações externas específicas ou contingência avançada deve passar primeiro por validação técnica, homologação e enquadramento comercial antes de entrar como promessa pública.

Download e onboarding:

<https://pdv.caracore.com.br/download.html>

---

## Estrutura do repositório

| Caminho | Conteúdo |
| ------- | -------- |
| `README.md` | Visão institucional e operacional deste repositório |
| `docs/` | Portal da loja em GitHub Pages |
| `docs/index.html` | Landing page comercial |
| `docs/download.html` | Página de download da Degustação Free (Windows, Linux e macOS) |
| `docs/pwa.html` | PWA da vitrine (não é o caixa) |
| `docs/tecnologia.html` | Soluções e pilares técnicos |
| `docs/versoes.html` | Versão atual e próxima versão |
| `docs/wiki-release-v3-2-2-free.html` | Notas da versão atual |
| `docs/wiki-release-v4-0-0-rc1.html` | Notas da próxima versão |
| `docs/wiki*.html` | Redirects para o wiki central ou para Versões |
| `docs/installers/` | Espelho opcional de instaladores no mesmo domínio da loja |
| `.github/workflows/` | Workflows de validação e publicação |

---

## Portal da loja (GitHub Pages)

O portal está publicado em <https://pdv.caracore.com.br/> via GitHub Pages, usando a pasta `/docs`.

Páginas principais:

- Loja: <https://pdv.caracore.com.br/>
- Download: <https://pdv.caracore.com.br/download.html>
- PWA da loja: <https://pdv.caracore.com.br/pwa.html>
- Soluções: <https://pdv.caracore.com.br/tecnologia.html>
- Versões: <https://pdv.caracore.com.br/versoes.html>
- Wiki do produto: <https://wiki.caracore.com.br/projeto-pdv.html>
- Guia fiscal: <https://wiki.caracore.com.br/pdv/wiki-fiscal.html>
- Consultoria: <https://pdv.caracore.com.br/consultoria.html>
- Canal de feedback: <https://pdv.caracore.com.br/canal-feedback.html>

Para ativar o GitHub Pages em um fork ou repositório novo: Settings -> Pages -> Deploy from a branch -> branch principal -> `/docs`.

---

## Qualidade de entrega

Este repositório pode validar instaladores e assets publicados por GitHub Actions. A política de release prioriza:

- assets públicos baixáveis sem autenticação pelo cliente final;
- SHA256 documentado por release;
- página de download apontando para a tag pública `v3.2.2-free` (Windows, Linux e macOS);
- wikis de release preservando contexto técnico e orientação de atualização;
- operação Windows com foco em previsibilidade no balcão;
- coerência entre promessa pública, escopo real e evidência documental;
- linguagem comercial honesta para pequena loja, sem sobrepromessa de integrações não homologadas.

---

## Ecossistema Cara Core

| Papel | Repositório / Endereço |
| ----- | ---------------------- |
| Oficina (código-fonte) | `caracore-pdv` |
| Loja (vitrine e releases) | `caracore-pdv-releases` (este repositório) |
| Loja pública | <https://pdv.caracore.com.br/> |
| Matriz institucional | <https://www.caracore.com.br/> |

---

**Cara Core Informática** - CNPJ 23.969.028/0001-37

## Licença

Este repositório segue licenciamento proprietário institucional da Cara Core Informática. Consulte [LICENSE](LICENSE).
