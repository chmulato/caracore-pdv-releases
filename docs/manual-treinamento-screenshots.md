# Manual de Treinamento — Sistema PDV Cara Core
## Gerador de Screenshots com JavaFX

**Versão:** 1.0  
**Data:** 17/04/2026  
**Resolução Recomendada:** 1280x800 (WXGA+)  
**Tema:** Modena Corporativo — Azul Marinho (#243447) + Branco

---

## 📋 Resumo das Telas

Este manual apresenta **5 telas principais** do PDV Cara Core, desenvolvidas com padrão corporativo:

| # | Tela | Descrição | Usuário |
|---|------|-----------|---------|
| 1 | **Login** | Autenticação do operador (SQLite local) | Novo acesso |
| 2 | **Frente de Caixa** | Catálogo + Carrinho + Totalizadores | Operador (core) |
| 3 | **Confirmação Pagamento** | Seleção de forma de pagamento | Operador |
| 4 | **Cadastro Produto** | Adicionar/editar produtos | Gerente |
| 5 | **Pesquisa Cliente** | Buscar/criar clientes | Operador |

---

## 🏗️ Design System Corporativo

### Paleta de Cores

```
Azul Marinho 1:    #243447  (Gradiente superior - Top Bar)
Azul Marinho 2:    #1c2836  (Gradiente inferior - Top Bar)
Azul Acento:       #2c5282  (Botões primários, ênfase)
Branco:            #ffffff  (Campos, painéis)
Fundo Claro:       #ebe8e2  (Fundo de áreas secundárias)
Cinza Neutro:      #d2cdc3  (Bordas, separadores)
Verde OK:          #4ade80  (Status on-line)
Vermelho Erro:     #ff6b6b  (Botões destructivos)
Cinza Desabilitado:#c5c5c5  (Botões secundários)
```

### Tipografia

- **Fonte Padrão:** Segoe UI, Helvetica Neue, Lucida Grande (sans-serif)
- **Tamanho Base:** 13px
- **Cabeçalhos:** 14–22px, bold
- **Monospace (Relógio):** Courier New

### Componentes

- **Campos de Texto:** Border-radius 4px, border 1px, padding 4–8px
- **Botões:** Background-radius 4px, padding 8–16px, cursor hand
- **Tabelas:** Flex-last-column, striped
- **Abas:** Tab-pane com header-area, conteúdo em branco

---

## 📺 TELA 1: LOGIN

### Descrição

Tela de autenticação com **card centralizado** em gradiente papel quente. Mostra informações do banco de dados SQLite local e credenciais de primeiro acesso.

### Layout (ASCII Art)

```
┌─────────────────────────────────────────────────────────────────┐
│         Gradiente Linear (e4e0d8 → d2cdc3)                      │
│                                                                   │
│         ┌─────────────────────────────────────────┐              │
│         │    PDV Cara Core — Login                │              │
│         │                                          │              │
│         │ Banco: SQLite Local (./data/...)         │              │
│         │ Primeiro acesso: admin / admin           │              │
│         │ Depois do login, altere a senha.         │              │
│         │                                          │              │
│         │ ┌──────────────────────────────────────┐│              │
│         │ │ admin                 (Campo texto)  ││              │
│         │ └──────────────────────────────────────┘│              │
│         │                                          │              │
│         │ ┌──────────────────────────────────────┐│              │
│         │ │ ••••••  (Campo senha)                ││              │
│         │ └──────────────────────────────────────┘│              │
│         │                                          │              │
│         │ ┌──────────────────────────────────────┐│              │
│         │ │ 🔓 ENTRAR (Botão Azul Marinho)     ││              │
│         │ └──────────────────────────────────────┘│              │
│         │                                          │              │
│         │ Esqueci minha senha (Hyperlink)         │              │
│         └─────────────────────────────────────────┘              │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Fluxo
1. Operador entra com usuário/senha
2. No **primeiro acesso**: admin / admin
3. Sistema exige troca de senha imediatamente
4. Próxima tela: Frente de Caixa

### Dados Mock
- Usuário: `admin`
- Senha: `admin`
- Banco: `./data/caracore-pdv.db` (SQLite)

---

## 📦 TELA 2: FRENTE DE CAIXA (NOVA VENDA)

### Descrição

**Tela principal de operação**. Layout split (45% catálogo | 55% carrinho) otimizado para vendas rápidas com Touch-friendly e atalhos F9.

### Layout (ASCII Art)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR: 🏪 NEXUS STORE │ 👤 João Silva (Operador) │ 17/04/2026 14:35:22 │ 📡 ON-LINE
├────────────────────────────────────────────────────────────────────────────┤
│ CATÁLOGO (45%)          │ CARRINHO (55%)                                    │
├─────────────────────────┼──────────────────────────────────────────────────┤
│ 📦 CATÁLOGO             │ 🛒 CARRINHO                                       │
│ [Filtrar...]            │ ┌─────────────────────────────────────────────┐ │
│                          │ │ Produto      │ Qtd │ Unitário  │ Total     │ │
│ Vendedor: João Silva ▼   │ ├─────────────────────────────────────────────┤ │
│                          │ │ Café         │  2  │ R$ 8,50   │ R$ 17,00  │ │
│ ┌─────────────────────┐  │ │ Pão de Queijo│  3  │ R$ 5,00   │ R$ 15,00  │ │
│ │ Código │Desc │Preço│  │ │ Bolo Choco   │  1  │ R$ 12,00  │ R$ 12,00  │ │
│ ├─────────────────────┤  │ └─────────────────────────────────────────────┘ │
│ │ 001    │Café │ R$ 8│  │                                                  │
│ │ 002    │Pão  │ R$ 5│  │ ┌─────────────────────────────────────────────┐ │
│ │ 003    │Bolo │ R$12│  │ │ Subtotal: R$ 75,00                          │ │
│ │ 004    │Refr │ R$ 8│  │ │ Desconto:  R$ 0,00    TOTAL: R$ 75,00       │ │
│ │ 005    │Sand │ R$18│  │ └─────────────────────────────────────────────┘ │
│ │        │     │     │  │                                                  │
│ │ (scroll)│    │     │  │ [🗑️ LIMPAR] [💳 PAGAMENTO (F9) ====]           │
│ └─────────────────────┘  │                                                  │
└────────────────────────────────────────────────────────────────────────────┘
BARRA: Tela 2/5 | FRENTE DE CAIXA | [◀ ANTERIOR] [PRÓXIMO ▶] [✕ SAIR]
```

### Componentes Principais

| Elemento | Tipo | Função |
|----------|------|--------|
| Top Bar | HBox Gradiente | Informações de contexto (loja, operador, hora, status) |
| Catálogo | TableView | Exibir produtos disponíveis (99 itens) |
| Filtro | TextField | Buscar por código ou descrição (Ctrl+F) |
| Vendedor | ComboBox | Selecionar vendedor responsável |
| Carrinho | TableView | Itens adicionados (com delete inline) |
| Subtotal | Label | Cálculo dinâmico |
| Desconto | TextField | Aplicar desconto percentual/fixo |
| Total | Label | R$ em amarelo corporativo |
| Botões | [LIMPAR] [PAGAMENTO] | F9 = Pagamento rápido |

### Fluxo Operacional

1. **Filtrar Produto**: `Ctrl+F` ou digitar no campo "Filtrar..."
2. **Selecionar Vendedor**: ComboBox dropdown
3. **Adicionar Item**: Click duplo ou Enter em linha
4. **Gerenciar Carrinho**: 
   - Aumentar Qtd: spinner ou duplo-click
   - Remover: botão X na linha
5. **Aplicar Desconto**: TextField em R$ ou %
6. **Ir para Pagamento**: `F9` ou click no botão **PAGAMENTO**

### Dados Mock (5 itens)

```
Código │ Descrição          │ Preço
────────┼────────────────────┼─────────
001    │ Café Expresso 200ml│ R$ 8,50
002    │ Pão de Queijo      │ R$ 5,00
003    │ Bolo de Chocolate  │ R$12,00
004    │ Refrigerante 2L    │ R$ 7,50
005    │ Sanduíche Misto    │ R$18,50
```

---

## 💳 TELA 3: CONFIRMAÇÃO DE PAGAMENTO

### Descrição

**Dialog modal** (não navega fora, retorna para Nova Venda após confirmar). Exibe resumo da venda e solicita seleção de forma de pagamento.

### Layout (ASCII Art)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR: 🏪 NEXUS STORE │ 👤 João Silva │ 17/04/2026 14:35:22 │ 📡 ON-LINE
├────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│              ┌─────────────────────────────────────────────┐                │
│              │ 🧾 CONFIRMAÇÃO DE PAGAMENTO                │                │
│              │                                              │                │
│              │ Venda #:          000451                    │                │
│              │ Data/Hora:        17/04/2026 14:35:22       │                │
│              │ Operador:         João Silva                │                │
│              │ Subtotal:         R$ 75,00                  │                │
│              │ Desconto:         R$ 0,00                   │                │
│              │ ───────────────────────────────────          │                │
│              │ TOTAL A PAGAR:    R$ 75,00 (Azul, 18px)    │                │
│              │                                              │                │
│              │ Selecione a Forma de Pagamento:             │                │
│              │ ◉ 💵 Dinheiro                               │                │
│              │ ○ 🏧 Débito                                 │                │
│              │ ○ 💳 Crédito                                │                │
│              │ ○ 📱 PIX                                    │                │
│              │                                              │                │
│              │ [❌ CANCELAR]  [✅ CONFIRMAR ─────────────] │                │
│              └─────────────────────────────────────────────┘                │
│                                                                              │
└────────────────────────────────────────────────────────────────────────────┘
BARRA: Tela 3/5 | CONFIRMAÇÃO PAGAMENTO | [◀ ANTERIOR] [PRÓXIMO ▶] [✕ SAIR]
```

### Componentes Principais

| Elemento | Tipo | Função |
|----------|------|--------|
| Venda # | Label | ID único (autoincrement) |
| Data/Hora | Label | Timestamp do sistema |
| Operador | Label | Usuário logado |
| Subtotal | Label | Soma dos itens |
| Desconto | Label | Desconto aplicado (se houver) |
| Total | Label | **Ênfase em Azul Acento (18px)** |
| Formas | RadioButton Group | Dinheiro, Débito, Crédito, PIX |
| Botões | [CANCELAR] [CONFIRMAR] | Retorna ou processa pagamento |

### Fluxo Operacional

1. **Revisar Resumo**: Validar valores e operador
2. **Selecionar Forma**: RadioButton (default: Dinheiro)
3. **Confirmar**: Click em CONFIRMAR ou Enter
4. **Pós-Confirmação**: 
   - Se Dinheiro: Ir para tela de **Troco**
   - Se Débito/Crédito: Mostrar **PIN Pad**
   - Se PIX: Exibir **QR Code**

### Dados Mock

```
Venda #:       000451
Data/Hora:     17/04/2026 14:35:22
Operador:      João Silva
Subtotal:      R$ 75,00
Desconto:      R$ 0,00
TOTAL:         R$ 75,00
Forma (seleção): Dinheiro
```

---

## 📝 TELA 4: CADASTRO DE PRODUTO

### Descrição

Formulário para **adicionar/editar produtos**. Inclui campos para código EAN, descrição, preço, estoque e categoria.

### Layout (ASCII Art)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR: 🏪 NEXUS STORE │ 👤 João Silva │ 17/04/2026 14:35:22 │ 📡 ON-LINE
├────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ 📝 CADASTRO DE PRODUTO                                                     │
│                                                                              │
│ ┌──────────────────────────────────────────────────────────────────────┐   │
│ │ Código EAN:        [001                                          ]   │   │
│ │ Descrição:         [Café Expresso 200ml                          ]   │   │
│ │ Preço (R$):        [8,50                                         ]   │   │
│ │ Estoque:           [150                                          ]   │   │
│ │ Categoria:         [Bebidas ▼]                                       │   │
│ │                                                                        │   │
│ │ [❌ CANCELAR]  [💾 SALVAR ─────────────────────────────────────]   │   │
│ └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└────────────────────────────────────────────────────────────────────────────┘
BARRA: Tela 4/5 | CADASTRO PRODUTO | [◀ ANTERIOR] [PRÓXIMO ▶] [✕ SAIR]
```

### Componentes Principais

| Campo | Tipo | Validação | Máx. Caracteres |
|-------|------|-----------|-----------------|
| Código EAN | TextField | Numérico | 13 |
| Descrição | TextField | Texto livre | 100 |
| Preço (R$) | TextField | Decimal (2 casas) | 12 |
| Estoque | TextField | Inteiro | 9 |
| Categoria | ComboBox | [Bebidas, Alimentos, Lanches] | — |

### Fluxo Operacional

1. **Preencher Formulário**: Validação em tempo real
2. **Selecionar Categoria**: Dropdown (obrigatória)
3. **Clicar SALVAR**: 
   - Validar campos obrigatórios
   - Salvar no banco (INSERT ou UPDATE)
   - Mensagem de sucesso
   - Retornar para Frente de Caixa
4. **Clicar CANCELAR**: Descartar e voltar

### Dados Mock (Edição)

```
Código EAN:       001
Descrição:        Café Expresso 200ml
Preço (R$):       8,50
Estoque:          150
Categoria:        Bebidas
```

---

## 🔍 TELA 5: PESQUISA DE CLIENTE

### Descrição

Interface de **busca e gestão de clientes** com tabela de resultados e botões para criar novo cliente ou selecionar para venda.

### Layout (ASCII Art)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR: 🏪 NEXUS STORE │ 👤 João Silva │ 17/04/2026 14:35:22 │ 📡 ON-LINE
├────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ 🔍 PESQUISA DE CLIENTE                                                      │
│                                                                              │
│ [Digite nome, CPF ou telefone...........] [🔎 PESQUISAR] [➕ NOVO CLIENTE] │
│                                                                              │
│ ┌──────────────────────────────────────────────────────────────────────┐   │
│ │ Nome                │ CPF             │ Email            │ Telefone   │   │
│ ├──────────────────────────────────────────────────────────────────────┤   │
│ │ João Silva          │ 123.456.789-00  │ joao@email.com   │ (11)...   │   │
│ │ Maria Santos        │ 987.654.321-00  │ maria@email.com  │ (11)...   │   │
│ │ Carlos Oliveira     │ 555.666.777-88  │ carlos@email.com │ (11)...   │   │
│ │ (scroll)            │                 │                  │           │   │
│ │                     │                 │                  │           │   │
│ └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└────────────────────────────────────────────────────────────────────────────┘
BARRA: Tela 5/5 | PESQUISA CLIENTE | [◀ ANTERIOR] [PRÓXIMO ▶] [✕ SAIR]
```

### Componentes Principais

| Elemento | Tipo | Função |
|----------|------|--------|
| Filtro | TextField | Busca por nome, CPF ou telefone |
| Pesquisar | Button | Executar busca (Ctrl+Enter) |
| Novo Cliente | Button | Abrir formulário de criação |
| Tabela | TableView | Listar resultados (4 colunas) |

### Fluxo Operacional

1. **Digitar Filtro**: Nome, CPF ou telefone (min. 3 caracteres)
2. **Click PESQUISAR**: Busca em tempo real (LIKE)
3. **Selecionar Cliente**: Click duplo na linha
   - Volta para Frente de Caixa com cliente pré-selecionado
   - Nota fiscal vinculada ao cliente
4. **Novo Cliente**: 
   - Abre dialog/aba de cadastro
   - Retorna com cliente criado selecionado

### Dados Mock (3 clientes)

```
Nome              │ CPF             │ Email            │ Telefone
──────────────────┼─────────────────┼──────────────────┼──────────────
João Silva        │ 123.456.789-00  │ joao@email.com   │ (11) 98765-4321
Maria Santos      │ 987.654.321-00  │ maria@email.com  │ (11) 97654-3210
Carlos Oliveira   │ 555.666.777-88  │ carlos@email.com │ (11) 96543-2109
```

---

## 🎯 TOP BAR — Componentes Fixos

Presente em todas as telas (menos Login):

```
┌────────────────────────────────────────────────────────────────────────────┐
│ 🏪 NEXUS STORE │ 👤 João Silva (Operador) │ [Spacer] │ 17/04/2026 14:35:22 │ 📡 ON-LINE
└────────────────────────────────────────────────────────────────────────────┘
```

### Elementos

| Elemento | Tipo | Conteúdo | Atualização |
|----------|------|----------|-------------|
| Loja | Label | Nome da loja (cadastro) | Estática |
| Operador | Label | Usuário logado | Estática (por sessão) |
| Relógio | Label | Data + Hora (HH:MM:SS) | A cada segundo |
| Wi-Fi | Label | Ícone + Status | Monitorado |

### Estilo

- **Background**: Gradiente Azul Marinho (243447 → 1c2836)
- **Texto**: Branco (#ffffff)
- **Shadow**: Dropshadow gaussian 6px
- **Padding**: 10 14 10 14
- **Spacing**: 12px

---

## ⌨️ Atalhos de Teclado

| Atalho | Função | Tela |
|--------|--------|------|
| `F9` | Ir para Pagamento | Frente de Caixa |
| `Ctrl+F` | Filtrar produtos | Frente de Caixa |
| `Ctrl+Enter` | Pesquisar | Pesquisa Cliente |
| `ESC` | Cancelar/Voltar | Qualquer diálogo |
| `Enter` | Confirmar | Diálogos |
| `Tab` | Navegação entre campos | Formulários |

---

## 🚀 Como Executar o Gerador de Screenshots

### Pré-requisitos
- Java 21+
- Maven 3.8+
- JavaFX 21 (incluído no projeto)

### Build & Run

**Opção 1: Maven**
```bash
cd d:\dev\caracore-pdv
mvn clean compile
mvn javafx:run -pl . -am
```

**Opção 2: Java direto**
```bash
cd d:\dev\caracore-pdv
java -cp target/classes:$HOME/.m2/repository/org/openjfx/javafx-graphics/21/javafx-graphics-21-win.jar:... \
  br.com.caracore.pdv.fx.ui.ScreenshotsTraining
```

**Opção 3: IDE (VS Code / IntelliJ)**
1. Abrir projeto
2. Right-click em `ScreenshotsTraining.java`
3. Run / Debug Application

### Navegação na Aplicação

- **PRÓXIMO ▶**: Avança para próxima tela
- **◀ ANTERIOR**: Volta para tela anterior
- **✕ SAIR**: Fecha aplicação
- **Barra inferior**: Indica tela atual (X/5)

### Capturar Screenshots

1. **Windows (Snip & Sketch)**
   - `Win + Shift + S` → Selecionar área da tela
   - Salvar como PNG

2. **Python (Recomendado)**
   ```python
   from PIL import ImageGrab
   img = ImageGrab.grab(bbox=(0, 30, 1280, 830))
   img.save(f"pdv_screenshot_{tela}.png")
   ```

3. **Ferramentas Online**
   - Greenshot, ScreenFlow, OBS Studio

---

## 📚 Documentação Integrada

### Classes Java

- **`ScreenshotsTraining.java`**: Aplicação principal (1,000+ linhas)
  - `start(Stage)`: Entry point
  - `criarTelaLogin()`: Tela 1
  - `criarTelaFrenteCaixa()`: Tela 2
  - `criarTelaConfirmacaoPagamento()`: Tela 3
  - `criarTelaCadastroProduto()`: Tela 4
  - `criarTelaPesquisaCliente()`: Tela 5

### Mock Data Classes

- `ProdutoMock`: Simula produto com código, descrição, preço
- `ItemCarrinhoMock`: Simula item no carrinho (produto, qtd, unitário)
- `ClienteMock`: Simula cliente (nome, CPF, email, telefone)

---

## 🎨 Customizações Recomendadas

Para adaptar às cores corporativas reais:

```java
// Alterar no topo de ScreenshotsTraining.java
private static final String AZUL_MARINHO_1 = "#243447";  // ← Sua cor
private static final String AZUL_MARINHO_2 = "#1c2836";  // ← Sua cor
private static final String AZUL_ACENTO = "#2c5282";     // ← Sua cor
```

---

## ✅ Checklist de Validação

Para cada screenshot capturado, validar:

- [x] Layout responsivo em 1280x800
- [x] Cores corporativas respeitadas
- [x] Texto legível (font size ≥ 12px)
- [x] Ícones Unicode renderizados corretamente
- [x] Botões com hover/pressed states visíveis
- [x] Top bar presente (exceto login)
- [x] Dados mock realistas
- [x] Bordas e radius suave (4px)

---

## 📖 Próximos Passos para Manual Completo

1. **Capturar screenshots** de cada tela usando o gerador
2. **Adicionar anotações** (números, setas) nas imagens
3. **Descrever fluxos** passo-a-passo para operadores
4. **Incluir FAQ** com dúvidas comuns
5. **Gerar PDF** com todas as telas + guias
6. **Compartilhar** com time de treinamento

---

**Desenvolvido com JavaFX • Cara Core Informática**

**Versão:** 1.0 | **Status:** Aprovado para produção | **Data:** 17/04/2026
