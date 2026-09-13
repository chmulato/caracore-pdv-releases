# CaraCore-PDV - Loja e Releases

**Download da loja = tag `v3.2.6-free`.** Não use a pré-release do topo da lista (`v4.0.0-rc2`) como se fosse o Free.

Não misture pasta nem data. Canais independentes.

Canal público de vitrine, documentação e distribuição do **CaraCore-PDV** para pequenas operações de balcão e varejo local. Mensagem central: **quando a internet cai, o caixa não pode parar**.

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
- Free: venda no navegador, sem PIX integrado e sem NF-e/NFC-e;
- PIX integrado e NFC-e no Premium, após demonstração;
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
| Download da loja | `v3.2.6-free` (Free / balcão) |
| Prévia | `v4.0.0-rc2` — **não é o download da loja** |
| Publicação | 13/09/2026 |
| Launcher Free | `iniciar-pdv.bat` (hífen) · navegador em `http://localhost:8080/login` |
| Banco Free | `%APPDATA%\caracore\` (Windows) · `~/.caracore/` (Linux/macOS) |
| Requisito Free | Java 25+ ([Temurin 25](https://adoptium.net/)) |
| Release | <https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.2.6-free> |
| Loja | <https://pdv.caracore.com.br/download.html> |

O trecho `free-free` no nome do ZIP é o nome publicado, não um segundo plano.

### Artefatos v3.2.6-free

| Artefato | Plataforma | SHA256 |
| -------- | ---------- | ------ |
| `caracore-pdv-v3.2.6-free-free-windows-x64.zip` | Windows 10/11 x64 | `4b15a12dbe9b525bdb31be59aff5c226f32cbb40f766eca752744996fda634d9` |
| `caracore-pdv-v3.2.6-free-free-linux-x64.zip` | Linux x64 (Ubuntu 20.04+) | `028e5987d35650fd0b2f5f4b2146033e92707b413c0cc8242d05df27e1a26e72` |
| `caracore-pdv-v3.2.6-free-free-macos-x64.zip` | macOS 12+ x64 (Intel) | `7e617aebe895d87ffe0446643751886263f29cbab7422a9e2ac3bcdd0aa5deff` |

### Prévia v4.0.0-rc2 — not store download

| Artefato | Plataforma | SHA256 |
| -------- | ---------- | ------ |
| `caracore-pdv-4.0.0-rc2-qute-portable.zip` | Windows · Linux · macOS | `5e5d55b6d376c7f1d6ce91a9fb9a73f6d606289af27b508adf2d9eb2cdcd955d` |
| Launcher | `iniciar_pdv.bat` (underscore) | Edge em modo aplicativo |
| Banco | só `./data/caracore-pdv.db` | Não abre `%APPDATA%\caracore\` |
| Reqs | Java 25+ e Python 3 | |

### Outra linha — Rust v0.1.4

A tag `v0.1.4` (MSI/EXE/ZIP) é o piloto Rust em <https://pdv-rust.caracore.com.br/>. Não é o Free desta loja.

---

## Atualização operacional - 13/09/2026

- `v3.2.6-free` é a oferta pública atual: patch de UX (shell PDV em coluna + caixa tipo registradora), porta 8080, `/login`, Java 25+.
- Sem PIX integrado e sem NF-e/NFC-e no Free. Pagamentos: dinheiro, débito, crédito e outros — “outros” não é PIX integrado.
- `v3.2.5-free` rebaixada a histórico imediato (shell com menu lateral e seed opcional).
- `v3.2.4-free` / `v3.2.3-free` / `v3.2.2-free` permanecem históricas.
- Pipeline CI/CD (`release-free.yml`) atualizado para `java-version: '25'` (Temurin 25).
- `v3.1.2-free` permanece referência histórica na trilha de versões da loja.
- `v3.0.10` permanece como referência histórica da série 3.x anterior à degustação Free.

---

## Linhas de versão

### Linha atual: `java_25`

A vitrine em `docs/` segue a trilha Java 25 da matriz, com SQLite local e soberania localhost. O download público maduro é a tag `v3.2.6-free`. O candidato `v4.0.0-rc2` (Quarkus + Qute) está como pré-release e não substitui a degustação Free. O GA do v4 permanece previsto para 08/11/2026.

Notas da versão atual: <https://pdv.caracore.com.br/wiki-release-v3-2-6-free.html>

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
| `docs/versoes.html` | Versão atual (3.2.6-free) e prévia (4.0.0-rc2) |
| `docs/wiki-release-v3-2-6-free.html` | Notas do canal Free atual |
| `docs/wiki-release-v3-2-5-free.html` | Notas históricas da 3.2.5-free |
| `docs/wiki-release-v4-0-0-rc2.html` | Notas da prévia (não é o download da loja) |
| `docs/wiki-release-v3-2-3-free.html` | Notas históricas da 3.2.3-free |
| `docs/wiki-release-v3-2-2-free.html` | Notas históricas da 3.2.2-free |
| `docs/leia-me/` | Texto canônico do LEIA-ME dos ZIPs |
| `docs/release-notes/` | Corpos das releases no GitHub |
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
- página de download apontando para a tag pública `v3.2.6-free` (Windows, Linux e macOS);
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
