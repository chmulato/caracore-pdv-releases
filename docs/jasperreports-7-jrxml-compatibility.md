# JasperReports 7 - Compatibilidade JRXML (Spike)

## Objetivo

Validar migracao de `net.sf.jasperreports:jasperreports` para `7.0.6` mantendo os relatórios atuais em `src/main/resources/reports/*.jrxml`.

## Resultado da Investigacao

Status: **nao compativel diretamente** com os JRXML legados do projeto.

Evidencias obtidas no spike:

1. `JRXmlLoader` no Jasper 7 usa `JacksonReportLoader`.
2. O loader detecta JRXML apenas quando o elemento raiz `jasperReport` esta sem namespace XML.
3. Mesmo removendo namespace, os templates atuais continuam falhando por incompatibilidades estruturais do formato legado.

Erros observados (representativos):

- `Unrecognized field "band" ... JasperDesign["title"]->JRDesignBand["band"]`
- `Unrecognized field "isFloatColumnFooter" ... JasperDesign["isFloatColumnFooter"]`
- `Unrecognized field "staticText" ... JRDesignBand["staticText"]`

Esses erros indicam que o parser novo espera um formato JRXML diferente do layout antigo (tags e atributos do legado 6.x nao sao aceitos sem conversao).

## O que foi tentado no spike

- Upgrade para `jasperreports:7.0.6` + `jasperreports-pdf:7.0.6`.
- Remocao de `.jasper` precompilados para forcar fluxo em `.jrxml`.
- Ajuste de raiz JRXML (sem namespace) nos templates.
- Prototipos de adaptacao automatica (namespace/atributos/encapsulamento de bandas).

Resultado: sem sucesso completo; os templates exigem migracao estrutural para o formato aceito pelo parser do Jasper 7.

## Conclusao Tecnica

A migracao para Jasper 7 **nao e drop-in** neste repositório.

Para concluir com seguranca, o caminho recomendado e:

1. Migrar cada template JRXML para o formato do Jasper 7 (reexport/regeracao em toolchain compativel ou transformacao assistida com validacao por template).
2. Validar cada relatório com teste automatizado de geracao de PDF.
3. So depois integrar no branch principal.

## Recomendacao de Release

- Manter release principal no branch de upgrade com `jasperreports 6.21.5`.
- Tratar Jasper 7 como trilha separada de modernizacao de relatórios, com homologacao dedicada.
