# caracore-pdv-releases

Vitrine de releases do **CaraCore-PDV** (PDV Selo Verde) da Cara Core Informática: o PDV que paga sua própria mensalidade. Quando a internet cai, o caixa não para. Reforma Tributária 2026-2033, recibo digital, foco localhost e Windows Desktop (EXE em `localhost:8080`), banco SQLite, planos Free e Premium.

## CaraCore-PDV — Visão geral

- **Produto:** Ponto de Venda para o mercado brasileiro (PDV Selo Verde). Motor fiscal que acompanha as mudanças de alíquotas até 2033. Operação ininterrupta: venda mesmo quando a internet cai (contingência, SQLite local). Economia com papel (recibo digital).
- **Planos:** Free (100 vendas/mês, 10 SMS recibo/mês) e Premium (recuperação de senha por SMS, relatório ao contador, suporte prioritário).
- **Download:** Versão de Degustação (Free) — 100 vendas completas para teste real. Guia de início rápido na [loja oficial](https://pdv.caracore.com.br/download.html). Releases neste repositório quando publicadas.

## Este repositório (loja)

- **Vitrine:** mesma mensagem de produto (Selo CaraCore de Sustentabilidade, economia real, fluxo contínuo, pronto 2026). Download, tecnologia (Soluções), wiki interna da loja e canal de feedback. A **linha de instalador alinhada à `master`** está documentada abaixo (**v1.0.16-rc2**); outras tags (ex.: **v3.0.0**) correspondem a **outra stack** — ver secção seguinte.
- **Canal de feedback:** suporte por e-mail (suporte@caracore.com.br), WhatsApp e Telegram. Não atendemos ligações telefônicas.

## Linha de referência a partir da `master` — [**v1.0.16-rc2**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v1.0.16-rc2)

**Última versão da `master` a partir da qual se parte** (instalador Windows — PDV Selo Verde):

- **Versão de Degustação (Free):** 100 vendas para teste real; operação offline (SQLite).
- **Ofuscação:** código protegido contra engenharia reversa (segurança).
- **Java 21 Temurin:** JRE embarcado para compatibilidade e performance.
- **Atualização automática:** ficheiros `.yml` e `.blockmap` para **electron-updater**.
- **Guia:** **INSTALACAO.md** (anexo aos assets da release).
- **Apresentação e consultoria:** [caracore.com.br/delivery/pdv/](https://www.caracore.com.br/delivery/pdv/).
- **Changelog da matriz:** [chmulato/caracore-pdv](https://github.com/chmulato/caracore-pdv).

## Outras tags (ex.: **v3.0.0**) — stack distinta

O release [**v3.0.0**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.0.0) e o respetivo EXE pertencem a **outra linha técnica empacotada**, **não** à continuidade directa da mesma stack que origina o **v1.0.16-rc2** a partir da `master`. Não comparar números de versão entre tags dessas linhas como se fossem a mesma série de build.

## Sincronização com a matriz (só a vitrine `docs/`)

A pasta `docs/` pode ser atualizada a partir do **caracore-pdv** branch **`master`** (conteúdo de vitrine / mensagem). Última sincronização: **2026-04-20** — commit `3091a36` na matriz. Isto **não** substitui os instaladores publicados nas **releases**; apenas alinha páginas estáticas. A referência de produto empacotado a partir da `master` continua a ser o [**v1.0.16-rc2**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v1.0.16-rc2) até existir uma tag posterior explícita nessa linha.

## Publicação

O site da loja é publicado via **GitHub Pages** a partir da pasta `docs/`:

- Configurar em: **Settings → Pages → Source:** Deploy from a branch → Branch: main (ou master) → Folder: **/docs**.
- URL do site: `https://pdv.caracore.com.br/`
- Domínio próprio: ainda não ativo para esta loja (em planejamento).

## Qualidade do instalador (GitHub Actions)

Para aumentar a acuidade da entrega, este repositorio possui workflow dedicado de validacao do instalador:

- Workflow: `.github/workflows/installer-validation.yml`
- Gatilhos: publicacao de release e execucao manual (`workflow_dispatch`)
- Validacoes executadas no `windows-latest`:
	- download do asset EXE da release
	- verificacao de tamanho minimo e cabecalho PE (`MZ`)
	- hash SHA-256 (com comparacao automatica quando `checksum.sha256` existe na release)
	- smoke test de instalacao silenciosa (aceita codigos de sucesso `0` e `3010`)

Se qualquer etapa falhar, o workflow marca a release como nao conforme para distribuicao.

## Links

- **Repositório de releases (este repo):** `chmulato/caracore-pdv-releases` no GitHub (manutenção e CI; a loja pública usa apenas pdv.caracore.com.br).
- **Download EXE (mesmo domínio da loja):** [pdv.caracore.com.br/installers/](https://pdv.caracore.com.br/installers/) — publicar o `.exe` nesta pasta no deploy; detalhes em [download](https://pdv.caracore.com.br/download.html).
- **Loja oficial:** [pdv.caracore.com.br](https://pdv.caracore.com.br/) — vitrine, wiki e canal de feedback.
- **Cara Core Informática:** site institucional em `www.caracore.com.br` (fora do subdomínio da loja).

---

**Cara Core Informática** — CNPJ 23.969.028/0001-37

## Licenca

Este repositorio segue licenciamento proprietario institucional da Cara Core Informatica.
Consulte [LICENSE](LICENSE).

