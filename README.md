# CaraCore-PDV - Loja e Releases

Canal público de vitrine, documentação e distribuição do **CaraCore-PDV**, o PDV Selo Verde da Cara Core Informática para o varejo brasileiro.

Mensagem central do produto: **quando a internet cai, o caixa não pode parar**. O sistema combina operação local com SQLite, recibo digital, redução de custos com papel, preparação para a Reforma Tributária 2026-2033 e planos Free/Premium.

---

## Produto

O CaraCore-PDV foi desenhado para lojistas que precisam de:

- venda em balcão com operação local e previsível;
- continuidade de atendimento mesmo com internet instável;
- recibo digital e economia com bobinas/impressoras;
- gestão de produtos, clientes, operadores, estoque e vendas;
- dashboard administrativo e relatórios gerenciais;
- motor fiscal preparado para CBS/IBS e transição tributária;
- trilha de evolução para PIX, SEFAZ, Premium e Premium+.

A matriz de desenvolvimento fica no repositório **caracore-pdv**. Este repositório, **caracore-pdv-releases**, é a loja pública: GitHub Pages, releases, wikis de versão e materiais de apoio.

---

## Versão atual

| Campo | Valor |
|-------|-------|
| Versão | `v3.1.0-free` |
| Status | Oferta pública atual |
| Publicação | 05/2026 |
| Linha | `free-edition` sobre a trilha `java_21` |
| Stack da oficina | Java 21 + JavaFX + Quarkus 3 + SQLite local |
| Delivery publicado | Windows Desktop portátil da degustação `v3.1.0-free` |
| Release | <https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.1.0-free> |
| Loja | <https://pdv.caracore.com.br/> |

### Artefatos v3.1.0-free

| Artefato | Descrição | SHA256 |
|----------|-----------|--------|
| `caracore-pdv-v3.1.0-free-windows-portable.zip` | Pacote portátil Windows da degustação pública | Publicado no `SHA256SUMS.txt` da release |
| `INSTALACAO.md` | Guia de instalação anexado à release | Publicado no `SHA256SUMS.txt` da release |
| `RELEASE_MANIFEST.json` | Manifesto técnico da publicação | Publicado no `SHA256SUMS.txt` da release |
| `SHA256SUMS.txt` | Lista oficial de hashes da release | Fonte de verificação |

---

## Atualização operacional - 05/2026

- `v3.1.0-free` consolidada como oferta pública atual da loja para degustação no Windows.
- A comunicação comercial da loja foi atualizada para enfatizar bunker digital, operação local soberana, prontidão para 2026 e evolução para o Premium.
- A wiki da loja passou a incluir uma leitura comercial específica da versão atual para apoiar CTA, demonstração e proposta de valor.
- `v3.0.10` permanece como referência histórica da série 3.x anterior à degustação Free.

---

## Linhas de versão

### Linha atual: `java_21`

A vitrine em `docs/` segue a trilha Java 21 da matriz, com foco em Quarkus, JavaFX, SQLite local e soberania localhost. A oficina atual declara JavaFX nativo como caminho principal; scripts e materiais baseados em Electron permanecem como histórico ou como empacotamento específico da release `v3.0.10`.

A página de novidades da versão atual fica em:

<https://pdv.caracore.com.br/wiki-release-v3-1-0-free.html>

A página de leitura comercial da versão atual fica em:

<https://pdv.caracore.com.br/wiki-analise-v3-1-0-free.html>

### Linhas anteriores

As versões `v1.x` e `v2.x` seguem preservadas como histórico da loja, incluindo páginas de wiki por release e referências aos instaladores antigos. A linha Spring + Electron WAR da branch `master` permanece como referência histórica, não como canal principal atual.

---

## Degustação Free e planos

A loja comunica a **Versão de Degustação (Free)** como teste real, com 100 vendas completas para validar o fluxo em operação. O plano Premium acrescenta recursos como PIX automático, vendas ilimitadas, automações, suporte prioritário e relatórios ao contador. O Premium+ cobre cenários com Android/SMS e configuração assistida compatível com LGPD.

Download e onboarding:

<https://pdv.caracore.com.br/download.html>

---

## Estrutura do repositório

| Caminho | Conteúdo |
|---------|----------|
| `README.md` | Visão institucional e operacional deste repositório |
| `docs/` | Portal da loja em GitHub Pages |
| `docs/index.html` | Landing page comercial |
| `docs/download.html` | Página de download da Degustação Free |
| `docs/tecnologia.html` | Soluções e pilares técnicos |
| `docs/wiki.html` | Índice operacional da wiki da loja |
| `docs/wiki-release-*.html` | Páginas por versão |
| `docs/installers/` | Espelho opcional de instaladores no mesmo domínio da loja |
| `.github/workflows/` | Workflows de validação e publicação |

---

## Portal da loja (GitHub Pages)

O portal está publicado em <https://pdv.caracore.com.br/> via GitHub Pages, usando a pasta `/docs`.

Páginas principais:

- Loja: <https://pdv.caracore.com.br/>
- Download: <https://pdv.caracore.com.br/download.html>
- Soluções: <https://pdv.caracore.com.br/tecnologia.html>
- Documentação: <https://pdv.caracore.com.br/readme.html>
- Wiki: <https://pdv.caracore.com.br/wiki.html>
- Wiki fiscal: <https://pdv.caracore.com.br/wiki-fiscal.html>
- Consultoria: <https://pdv.caracore.com.br/consultoria.html>
- Canal de feedback: <https://pdv.caracore.com.br/canal-feedback.html>

Para ativar o GitHub Pages em um fork ou repositório novo: Settings -> Pages -> Deploy from a branch -> branch principal -> `/docs`.

---

## Qualidade de entrega

Este repositório pode validar instaladores e assets publicados por GitHub Actions. A política de release prioriza:

- assets públicos baixáveis sem autenticação pelo cliente final;
- SHA256 documentado por release;
- página de download sempre apontando para o latest release público;
- wikis de release preservando contexto técnico e orientação de atualização;
- operação Windows com foco em previsibilidade no balcão.

---

## Ecossistema Cara Core

| Papel | Repositório / Endereço |
|-------|------------------------|
| Oficina (código-fonte) | `caracore-pdv` |
| Loja (vitrine e releases) | `caracore-pdv-releases` (este repositório) |
| Loja pública | <https://pdv.caracore.com.br/> |
| Matriz institucional | <https://www.caracore.com.br/> |

---

**Cara Core Informática** - CNPJ 23.969.028/0001-37

## Licença

Este repositório segue licenciamento proprietário institucional da Cara Core Informática. Consulte [LICENSE](LICENSE).

