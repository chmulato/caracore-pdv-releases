# caracore-pdv-releases

Vitrine de releases do **CaraCore-PDV** (PDV Selo Verde) da Cara Core Informática: o PDV que paga sua própria mensalidade. Quando a internet cai, o caixa não para. Reforma Tributária 2026-2033, recibo digital, foco localhost e Windows Desktop (EXE em `localhost:8080`), banco SQLite, planos Free e Premium.

## CaraCore-PDV — Visão geral

- **Produto:** Ponto de Venda para o mercado brasileiro (PDV Selo Verde). Motor fiscal que acompanha as mudanças de alíquotas até 2033. Operação ininterrupta: venda mesmo quando a internet cai (contingência, SQLite local). Economia com papel (recibo digital).
- **Planos:** Free (100 vendas/mês, 10 SMS recibo/mês) e Premium (recuperação de senha por SMS, relatório ao contador, suporte prioritário).
- **Download:** Versão de Degustação (Free) — 100 vendas completas para teste real. Guia de início rápido na [loja oficial](https://pdv.caracore.com.br/download.html). Releases neste repositório quando publicadas.

## Este repositório (loja)

- **Vitrine:** mesma mensagem de produto (Selo CaraCore de Sustentabilidade, economia real, fluxo contínuo, pronto 2026). A pasta **`docs/`** (GitHub Pages) é sincronizada a partir da branch **`java_21`** da matriz (stack **Quarkus + JavaFX**). A linha **Spring + Electron** na branch **`master`** mantém o seu próprio instalador de referência (**v1.0.16-rc2**) — ver secções abaixo.
- **Canal de feedback:** suporte por e-mail (suporte@caracore.com.br), WhatsApp e Telegram. Não atendemos ligações telefônicas.

## Linha `java_21` (Quarkus + JavaFX) — vitrine `docs/` e release [**v3.0.10**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.0.10)

- **Matriz:** branch [`java_21`](https://github.com/chmulato/caracore-pdv/tree/java_21) — `pom.xml` em **3.0.2**, empacotamento **jar** (hybrid: native tentado, fallback JVM), Quarkus 3, JavaFX, soberania localhost.
- **Loja:** o site em `docs/` segue o **conteúdo desta branch** (páginas HTML/CSS e wiki alinhadas à trilha Java 21).
- **Instalador público:** o ZIP e notas do [**v3.0.10**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v3.0.10) correspondem a esta **stack** (não à linha Spring da `master`).

## Linha `master` (Spring + Electron WAR) — [**v1.0.16-rc2**](https://github.com/chmulato/caracore-pdv-releases/releases/tag/v1.0.16-rc2)

**Última versão empacotada a partir da qual se parte** nesta linha (instalador Windows — PDV Selo Verde, stack anterior):

- **Versão de Degustação (Free):** 100 vendas para teste real; operação offline (SQLite).
- **Ofuscação:** código protegido contra engenharia reversa (segurança).
- **Java 21 Temurin:** JRE embarcado para compatibilidade e performance.
- **Atualização automática:** ficheiros `.yml` e `.blockmap` para **electron-updater**.
- **Guia:** **INSTALACAO.md** (anexo aos assets da release).
- **Apresentação e consultoria:** [caracore.com.br/delivery/pdv/](https://caracore.com.br/delivery/pdv/).
- **Changelog da matriz:** [chmulato/caracore-pdv](https://github.com/chmulato/caracore-pdv) (branch `master` atual em **1.0.17** no `pom.xml`).

## Sincronização da vitrine (`docs/`)

Última atualização: **2026-04-23** — conteúdo copiado a partir de **caracore-pdv** branch **`java_21`**, release **v3.0.10**. Não altera por si só os assets das **releases**; apenas a vitrine GitHub Pages. Páginas exclusivas da loja (CNAME, `installers/`, wikis de release, manuais operacionais adicionais, etc.) **mantêm-se** no repositório quando não existem equivalentes na matriz.

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

