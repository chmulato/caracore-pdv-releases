# Upgrade Spring Boot 3 - Checklist Dirigido

## Fase 1 - Quick Wins Aplicados

- JasperReports: `6.20.0` -> `6.21.5`
- Commons DBCP2: `2.1.1` -> `2.14.0`
- Maven Failsafe Plugin: `2.22.2` -> `3.2.5`

## Validacao da Fase 1

- `mvn -q -DskipITs=true -DskipTests=true clean test-compile` passou
- Testes focados de relatorio/dashboard nao fecharam verdes em runtime, mas os erros observados foram `NoClassDefFoundError` para classes/repositorios da propria aplicacao, nao uma quebra direta de API do JasperReports

## Bloqueadores Exatos para Spring Boot 3

### javax.persistence

- `src/main/java/br/com/caracore/pdv/converter/StatusVendaConverter.java`
- `src/main/java/br/com/caracore/pdv/listener/CriptografiaEntityListener.java`
- `src/main/java/br/com/caracore/pdv/model/AliquotaReformaTributaria.java`
- `src/main/java/br/com/caracore/pdv/model/CertificadoFiscalConfig.java`
- `src/main/java/br/com/caracore/pdv/model/ChaveAtivacao.java`
- `src/main/java/br/com/caracore/pdv/model/Cliente.java`
- `src/main/java/br/com/caracore/pdv/model/ConfiguracaoEmail.java`
- `src/main/java/br/com/caracore/pdv/model/ConfiguracaoFiscal.java`
- `src/main/java/br/com/caracore/pdv/model/ConfiguracaoPlano.java`
- `src/main/java/br/com/caracore/pdv/model/Estoque.java`
- `src/main/java/br/com/caracore/pdv/model/HistoricoAliquota.java`
- `src/main/java/br/com/caracore/pdv/model/ItemVenda.java`
- `src/main/java/br/com/caracore/pdv/model/Loja.java`
- `src/main/java/br/com/caracore/pdv/model/Ncm.java`
- `src/main/java/br/com/caracore/pdv/model/NfceFilaContingencia.java`
- `src/main/java/br/com/caracore/pdv/model/OfflineTransaction.java`
- `src/main/java/br/com/caracore/pdv/model/Operador.java`
- `src/main/java/br/com/caracore/pdv/model/OutboxMessage.java`
- `src/main/java/br/com/caracore/pdv/model/Pagamento.java`
- `src/main/java/br/com/caracore/pdv/model/PagamentoPix.java`
- `src/main/java/br/com/caracore/pdv/model/Produto.java`
- `src/main/java/br/com/caracore/pdv/model/TabelaFiscalVigente.java`
- `src/main/java/br/com/caracore/pdv/model/Venda.java`
- `src/main/java/br/com/caracore/pdv/model/Vendedor.java`

### javax.validation

- `src/main/java/br/com/caracore/pdv/controller/ClientesController.java`
- `src/main/java/br/com/caracore/pdv/controller/ConfiguracaoEmailController.java`
- `src/main/java/br/com/caracore/pdv/controller/EstoquesController.java`
- `src/main/java/br/com/caracore/pdv/controller/FiscalConfigController.java`
- `src/main/java/br/com/caracore/pdv/controller/ItensController.java`
- `src/main/java/br/com/caracore/pdv/controller/LojasController.java`
- `src/main/java/br/com/caracore/pdv/controller/PagamentosController.java`
- `src/main/java/br/com/caracore/pdv/controller/ProdutosController.java`
- `src/main/java/br/com/caracore/pdv/controller/VendasController.java`
- `src/main/java/br/com/caracore/pdv/controller/VendedoresController.java`
- `src/main/java/br/com/caracore/pdv/model/AliquotaReformaTributaria.java`
- `src/main/java/br/com/caracore/pdv/model/Cliente.java`
- `src/main/java/br/com/caracore/pdv/model/ConfiguracaoEmail.java`
- `src/main/java/br/com/caracore/pdv/model/ConfiguracaoFiscal.java`
- `src/main/java/br/com/caracore/pdv/model/Estoque.java`
- `src/main/java/br/com/caracore/pdv/model/ItemVenda.java`
- `src/main/java/br/com/caracore/pdv/model/Loja.java`
- `src/main/java/br/com/caracore/pdv/model/Ncm.java`
- `src/main/java/br/com/caracore/pdv/model/Operador.java`
- `src/main/java/br/com/caracore/pdv/model/Pagamento.java`
- `src/main/java/br/com/caracore/pdv/model/Produto.java`
- `src/main/java/br/com/caracore/pdv/model/TabelaFiscalVigente.java`
- `src/main/java/br/com/caracore/pdv/model/Venda.java`
- `src/main/java/br/com/caracore/pdv/model/Vendedor.java`
- `src/main/java/br/com/caracore/pdv/service/ClienteService.java`
- `src/main/java/br/com/caracore/pdv/service/PagamentoService.java`
- `src/test/java/br/com/caracore/pdv/service/ClienteServiceTest.java`

### javax.servlet

- `src/main/java/br/com/caracore/pdv/config/CustomErrorController.java`
- `src/main/java/br/com/caracore/pdv/config/GlobalExceptionHandler.java`
- `src/main/java/br/com/caracore/pdv/config/WebSecurityConfig.java`
- `src/main/java/br/com/caracore/pdv/controller/DashboardController.java`
- `src/main/java/br/com/caracore/pdv/controller/LicencaController.java`
- `src/main/java/br/com/caracore/pdv/controller/RelatoriosController.java`
- `src/main/java/br/com/caracore/pdv/controller/VendasController.java`
- `src/main/java/br/com/caracore/pdv/security/JwtAuthenticationFilter.java`
- `src/main/java/br/com/caracore/pdv/security/RateLimitingFilter.java`

### Spring Security 6

- `src/main/java/br/com/caracore/pdv/config/WebSecurityConfig.java`
  - Trocar `antMatchers(...)` por `requestMatchers(...)`
  - Trocar `ignoringAntMatchers(...)` por `ignoringRequestMatchers(...)`

### Dependencia Maven que precisa mudar na Fase 2

- `pom.xml`
  - Trocar `thymeleaf-extras-springsecurity5` por `thymeleaf-extras-springsecurity6`

## Hotspots Prioritarios

1. `src/main/java/br/com/caracore/pdv/config/WebSecurityConfig.java`
2. `src/main/java/br/com/caracore/pdv/controller/RelatoriosController.java`
3. `src/main/java/br/com/caracore/pdv/listener/CriptografiaEntityListener.java`
4. `src/main/java/br/com/caracore/pdv/security/JwtAuthenticationFilter.java`
5. `src/main/java/br/com/caracore/pdv/security/RateLimitingFilter.java`

## Status Atual Validado (2026-04-09)

- Full suite no branch `upgrade/spring-boot-3-prep`: **1393 testes, 0 falhas, 0 erros**.
- Migracao de anotacoes de teste para Spring 6.2 concluida (`@MockBean/@SpyBean` -> `@MockitoBean/@MockitoSpyBean`) e validada.
- Ajustes de estabilidade (equals e fixtures de repositorio H2) concluidos e validados.

## Blocos de Commit Propostos (sem commitar)

### Bloco 1 - Plataforma Boot 3/Jakarta + SQLite

Escopo:
- `pom.xml` (Boot 3.4.13, dialetos/deps base, Tomcat, JJWT, etc.)
- migracao `javax.*` -> `jakarta.*` em `src/main/java/**` e `src/test/java/**`
- remocao de `src/main/java/br/com/caracore/pdv/config/SQLiteDialect.java`
- propriedades de dialeto/open-in-view em `src/main/resources/application-*.properties` e `src/test/resources/application-test.properties`
- `src/main/resources/ValidationMessages*.properties`

Staging sugerido:
- `git add pom.xml`
- `git add src/main/java/br/com/caracore/pdv/config`
- `git add src/main/java/br/com/caracore/pdv/model`
- `git add src/main/java/br/com/caracore/pdv/converter`
- `git add src/main/java/br/com/caracore/pdv/listener`
- `git add src/main/java/br/com/caracore/pdv/controller`
- `git add src/main/java/br/com/caracore/pdv/service`
- `git add src/main/java/br/com/caracore/pdv/security`
- `git add src/main/resources/ValidationMessages.properties src/main/resources/ValidationMessages_pt_BR.properties`
- `git add src/main/resources/application-contingency.properties src/main/resources/application-sqlite.properties src/test/resources/application-test.properties`

### Bloco 2 - Security Hardening + JWT

Escopo:
- `src/main/java/br/com/caracore/pdv/config/WebSecurityConfig.java`
- `src/main/java/br/com/caracore/pdv/security/JwtTokenProvider.java`
- `src/main/java/br/com/caracore/pdv/security/JwtAuthenticationFilter.java`
- `src/main/java/br/com/caracore/pdv/security/RateLimitingFilter.java`

Staging sugerido:
- `git add src/main/java/br/com/caracore/pdv/config/WebSecurityConfig.java`
- `git add src/main/java/br/com/caracore/pdv/security/JwtTokenProvider.java`
- `git add src/main/java/br/com/caracore/pdv/security/JwtAuthenticationFilter.java`
- `git add src/main/java/br/com/caracore/pdv/security/RateLimitingFilter.java`

### Bloco 3 - Testes de Dominio/Repositorio + Deprecations

Escopo:
- `src/test/java/br/com/caracore/pdv/model/VendaTest.java`
- `src/test/java/br/com/caracore/pdv/model/ItemVendaTest.java`
- `src/test/java/br/com/caracore/pdv/repository/OperadorRepositoryTest.java`
- `src/test/java/br/com/caracore/pdv/repository/VendedorRepositoryTest.java`
- `src/main/java/br/com/caracore/pdv/config/RestTemplateConfig.java`
- `src/main/java/br/com/caracore/pdv/service/ItemVendaService.java`

Staging sugerido:
- `git add src/test/java/br/com/caracore/pdv/model/VendaTest.java src/test/java/br/com/caracore/pdv/model/ItemVendaTest.java`
- `git add src/test/java/br/com/caracore/pdv/repository/OperadorRepositoryTest.java src/test/java/br/com/caracore/pdv/repository/VendedorRepositoryTest.java`
- `git add src/main/java/br/com/caracore/pdv/config/RestTemplateConfig.java src/main/java/br/com/caracore/pdv/service/ItemVendaService.java`

### Bloco 4 - Migracao Mockito em Testes Web/Integration/Service

Escopo:
- todos os testes alterados de `MockBean/SpyBean` para `MockitoBean/MockitoSpyBean`
- inclui `src/test/java/br/com/caracore/pdv/controller/**`, `src/test/java/br/com/caracore/pdv/integration/FluxoVendaIntegrationTest.java`, `src/test/java/br/com/caracore/pdv/service/SmsService*.java`

Staging sugerido:
- `git add src/test/java/br/com/caracore/pdv/controller`
- `git add src/test/java/br/com/caracore/pdv/integration/FluxoVendaIntegrationTest.java`
- `git add src/test/java/br/com/caracore/pdv/service/SmsServiceTest.java src/test/java/br/com/caracore/pdv/service/SmsServiceSemBaseUrlTest.java`

### Bloco 5 - Artefatos de Relatorio/Checklist de Upgrade

Escopo:
- `src/main/resources/reports/.gitignore`
- remocao de `.jasper` versionados
- `docs/upgrade-spring-boot-3-checklist.md`

Staging sugerido:
- `git add src/main/resources/reports/.gitignore`
- `git add src/main/resources/reports/relatorio_estoques_por_loja.jasper src/main/resources/reports/relatorio_vendas_por_loja.jasper src/main/resources/reports/relatorio_vendas_por_vendedor.jasper`
- `git add docs/upgrade-spring-boot-3-checklist.md`

## Riscos Residuais

1. JasperReports 7 ainda e bloqueador tecnico (formato JRXML legado nao compativel com parser novo).
2. Branch principal esta verde em testes, mas ainda com alto volume de mudancas locais sem checkpoints atomicos.
3. `src/main/resources/reports/*.jasper` removidos: depende de runtime compilar `.jrxml` (ok para 6.21.5, mas requer monitoramento de performance/erros na inicializacao de relatorios).

## Ordem Recomendada de Publicacao

1. Publicar release de estabilizacao Spring Boot 3 **sem** Jasper 7 (manter Jasper 6.21.5).
2. Criar release patch curto de observabilidade/hardening caso apareca regressao de runtime apos deploy inicial.
3. Em paralelo, concluir migracao dedicada de relatórios para Jasper 7 em branch isolado e publicar como release separado (minor) apos homologacao completa dos PDFs.

