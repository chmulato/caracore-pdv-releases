# caracore-pdv-releases

Vitrine de releases do **CaraCore-PDV** (PDV Selo Verde) da Cara Core Informática: o PDV que paga sua própria mensalidade. Quando a internet cai, o caixa não para. Reforma Tributária 2026-2033, recibo digital, foco localhost e Windows Desktop (EXE em `localhost:8080`), banco SQLite, planos Free e Premium.

## CaraCore-PDV — Visão geral

- **Produto:** Ponto de Venda para o mercado brasileiro (PDV Selo Verde). Motor fiscal que acompanha as mudanças de alíquotas até 2033. Operação ininterrupta: venda mesmo quando a internet cai (contingência, SQLite local). Economia com papel (recibo digital).
- **Planos:** Free (100 vendas/mês, 10 SMS recibo/mês) e Premium (recuperação de senha por SMS, relatório ao contador, suporte prioritário).
- **Download:** Versão de Degustação (Free) — 100 vendas completas para teste real. Guia de início rápido na [loja oficial](https://pdv.caracore.com.br/download.html). Releases neste repositório quando publicadas.

## Este repositório (loja)

- **Vitrine:** mesma mensagem de produto (Selo CaraCore de Sustentabilidade, economia real, fluxo contínuo, pronto 2026). Download, tecnologia (Soluções), wiki interna da loja e canal de feedback. **Importante:** o conteúdo de `docs/` pode ser sincronizado a partir da **branch `master` da matriz**, mas isso **não** significa que o site e o **instalador v3.0.0** usem a mesma stack técnica — ver secção abaixo.
- **Canal de feedback:** suporte por e-mail (suporte@caracore.com.br), WhatsApp e Telegram. Não atendemos ligações telefônicas.

## Duas stacks: `master` (matriz) e release **v3.0.0** (loja / EXE)

- **Branch `master` do repositório `caracore-pdv`:** linha atual de **desenvolvimento** — stack própria (runtime, dependências e build conforme esse repo hoje; ex.: versão em `pom.xml` / `electron`).
- **Release [v3.0.0](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.0.0) e o EXE distribuído:** **outra stack** — a que foi congelada e empacotada para a loja pública. O número **3.0.0** identifica essa linha empacotada; **não** deve ser lido como continuação direta do número de artefacto na `master` (são **pilhas técnicas distintas**).

## Sincronização com a matriz (só a vitrine `docs/`)

A pasta `docs/` pode ser atualizada a partir do **caracore-pdv** branch **`master`** (conteúdo de vitrine / mensagem). Última sincronização: **2026-04-20** — commit `3091a36` na matriz. Isto **não** substitui nem reversiona o instalador **v3.0.0**; apenas alinha páginas estáticas quando fizer sentido editorialmente.

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

