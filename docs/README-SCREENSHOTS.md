# 📚 Manual de Treinamento PDV — Guia de Uso

## 🎯 Objetivo

Este diretório contém um **gerador automatizado de screenshots** para criar um manual de treinamento visual do PDV Cara Core com layout profissional, theme corporativo e dados realistas.

---

## 📦 Conteúdo

```
docs/
├── manual-treinamento-screenshots.md  ← GUIA COMPLETO (este arquivo)
└── index.html                         ← Galeria de screenshots (gerada)

scripts/
├── capturador-screenshots.py          ← Script Python para captura automática
├── run_pdv_javafx_windows.py          ← Launcher do PDV (existente)
└── ...

src/main/java/br/com/caracore/pdv/fx/ui/
├── ScreenshotsTraining.java           ← App JavaFX principal (1,000+ linhas)
├── NovaVendaController.java           ← Controlador original (existente)
└── ...

screenshots/
└── YYYYMMDD_HHMMSS/
    ├── 01_login.png
    ├── 02_frente_caixa.png
    ├── 03_confirmacao_pagamento.png
    ├── 04_cadastro_produto.png
    ├── 05_pesquisa_cliente.png
    └── index.html                     ← Galeria HTML
```

---

## 🚀 Como Usar

### Opção 1: Captura Manual (Simples)

**Passo 1: Compilar o projeto**
```bash
cd <repositorio>/caracore-pdv
mvn clean compile -DskipTests
```

**Passo 2: Executar aplicação JavaFX**
```bash
mvn javafx:run
```

**Passo 3: Navegar e capturar**
- Usar botões **PRÓXIMO ▶** e **◀ ANTERIOR** para navegar entre telas
- Para cada tela:
  - Windows: `Win + Shift + S` (Snip & Sketch)
  - macOS: `Cmd + Shift + 4`
  - Linux: `gnome-screenshot`
- Salvar como PNG em `screenshots/` com nome descritivo

**Exemplo:**
```
screenshots/
├── 01_login.png
├── 02_frente_caixa.png
├── 03_confirmacao_pagamento.png
├── 04_cadastro_produto.png
└── 05_pesquisa_cliente.png
```

---

### Opção 2: Captura Automática (Recomendada)

**Pré-requisitos (Windows):**
```bash
pip install Pillow pywinauto appium-python-client
```

Opcional para backend Appium:
- WinAppDriver em execução (`http://127.0.0.1:4723`)

**Executar script:**
```bash
python scripts/capturador-screenshots.py --backend auto --upscale 2
```

**O que o script faz:**
1. ✅ Compila o projeto (Maven)
2. ✅ Inicia aplicação JavaFX
3. ✅ Localiza e foca a janela com pywinauto
4. ✅ Preenche campos com dados realistas para treinamento
5. ✅ Navega automaticamente entre as 5 telas
6. ✅ Captura screenshot em alta resolução (upscale)
7. ✅ Organiza saída por backend e funcionalidade
8. ✅ Gera manifesto JSON e log da execução
9. ✅ Fecha aplicação
```
screenshots/gui_automation/20260417_174215_auto/
├── 01_autenticacao/
│   └── 01_login_manual_treinamento.png
├── 02_venda/
│   └── 02_frente_caixa_manual_treinamento.png
├── 03_pagamento/
│   └── 03_confirmacao_pagamento_manual_treinamento.png
├── 04_cadastro_produto/
│   └── 04_cadastro_produto_manual_treinamento.png
├── 05_pesquisa_cliente/
│   └── 05_pesquisa_cliente_manual_treinamento.png
├── manifest.json
└── run.log
```
└── index.html
```

---

## 📱 5 Telas do Manual

| # | Tela | Descrição | Dados Mock |
|---|------|-----------|-----------|
| **1** | **Login** | Autenticação com SQLite local | admin/admin |
| **2** | **Frente de Caixa** | Catálogo + Carrinho + Totalizadores | 5 produtos, 3 itens |
| **3** | **Confirmação Pagamento** | Resumo + Formas de pagamento | Venda #000451 |
| **4** | **Cadastro Produto** | Formulário com EAN, preço, estoque | Café Expresso |
| **5** | **Pesquisa Cliente** | Busca + Tabela com 3 clientes | João, Maria, Carlos |

---

## 🎨 Design System

### Cores Corporativas

```css
/* Tema: Modena Corporativo */
--azul-marinho-1:    #243447  /* Top Bar superior */
--azul-marinho-2:    #1c2836  /* Top Bar inferior */
--azul-acento:       #2c5282  /* Botões primários */
--branco:            #ffffff  /* Campos, painéis */
--fundo-claro:       #ebe8e2  /* Fundo secundário */
--cinza-neutro:      #d2cdc3  /* Bordas, separadores */
--verde-ok:          #4ade80  /* Status online */
--vermelho-erro:     #ff6b6b  /* Destructivos */
```

### Resolução

- **Padrão (WXGA+):** 1280 × 800px
- **Mínimo:** 1024 × 700px
- **Recomendado para captura:** 1280 × 800px (full)

### Tipografia

- **Fonte:** Segoe UI, Helvetica Neue, sans-serif
- **Tamanho Base:** 13px
- **Cabeçalhos:** 14–22px, bold
- **Monospace:** Courier New (relógio)

---

## ⌨️ Atalhos de Teclado

Na aplicação:

| Tecla | Ação |
|-------|------|
| **→ (Direita)** | Próxima tela |
| **← (Esquerda)** | Tela anterior |
| **ESC** | Fechar aplicação |
| **F9** | Ir para Pagamento (Frente de Caixa) |
| **Ctrl+F** | Filtrar produtos (Frente de Caixa) |

---

## 🔧 Personalizar Design

Para alterar cores corporativas, edite `ScreenshotsTraining.java`:

```java
// Linhas 25-31
private static final String AZUL_MARINHO_1 = "#243447";  // ← Alterar aqui
private static final String AZUL_MARINHO_2 = "#1c2836";  // ← Alterar aqui
private static final String AZUL_ACENTO = "#2c5282";     // ← Alterar aqui
private static final String BRANCO = "#ffffff";
private static final String FUNDO_CLARO = "#ebe8e2";
private static final String CINZA_NEUTRO = "#d2cdc3";
```

Depois recompile:
```bash
mvn clean compile
```

---

## 📋 Dados Mock

### Produtos (Tela 2 - Frente de Caixa)

```
001 │ Café Expresso 200ml    │ R$ 8,50
002 │ Pão de Queijo          │ R$ 5,00
003 │ Bolo de Chocolate Fatia│ R$12,00
004 │ Refrigerante 2L        │ R$ 7,50
005 │ Sanduíche Misto        │ R$18,50
```

### Itens no Carrinho (Tela 2)

```
Café Expresso    │ 2 unidades │ R$ 8,50  │ R$ 17,00
Pão de Queijo    │ 3 unidades │ R$ 5,00  │ R$ 15,00
Bolo Chocolate   │ 1 unidade  │ R$12,00  │ R$12,00
─────────────────┴────────────┴──────────┴─────────
TOTAL                                      R$ 75,00
```

### Clientes (Tela 5)

```
João Silva     │ 123.456.789-00 │ joao@email.com   │ (11) 98765-4321
Maria Santos   │ 987.654.321-00 │ maria@email.com  │ (11) 97654-3210
Carlos Oliveira│ 555.666.777-88 │ carlos@email.com │ (11) 96543-2109
```

---

## ✅ Validação de Screenshots

Após capturar cada screenshot, validar:

- [ ] **Resolução:** 1280 × 800 px
- [ ] **Cores:** Azul Marinho + Branco visíveis
- [ ] **Texto:** Legível (font-size ≥ 12px)
- [ ] **Ícones:** Renderizados (emojis Unicode)
- [ ] **Layout:** Sem elementos cortados
- [ ] **Top Bar:** Presente (loja, operador, hora, wi-fi)
- [ ] **Dados:** Mock data visível e realista
- [ ] **Sombras:** Border-radius 4px suave

---

## 📖 Próximos Passos

### Fase 1: Screenshots ✅
- [x] Gerar código JavaFX
- [x] Compilar projeto
- [x] Capturar 5 telas

### Fase 2: Anotações (Manual)
- [ ] Adicionar números/setas nas imagens
- [ ] Descrever cada elemento
- [ ] Incluir callouts de ação

### Fase 3: Guias Operacionais
- [ ] Passo-a-passo de cada fluxo
- [ ] Dicas de performance
- [ ] Troubleshooting comum

### Fase 4: PDF Final
- [ ] Compilar em PDF high-quality
- [ ] Adicionar índice e sumário
- [ ] Incluir apêndices de referência

### Fase 5: Distribuição
- [ ] Compartilhar com time de treinamento
- [ ] Publicar em wiki interno
- [ ] Versionar em releases

---

## 🆘 Troubleshooting

### Problema: JavaFX não inicia
**Solução:**
```bash
mvn clean install
mvn javafx:run
```

### Problema: Script capturador não funciona
**Solução:**
```bash
# Verificar dependências de automação instaladas
pip install --upgrade Pillow pywinauto appium-python-client

# Executar com verbose
python -u scripts/capturador-screenshots.py
```

### Problema: Screenshots cortadas/blurry
**Solução:**
1. Usar Windows Scale de 100% (não 125% ou 150%)
2. Executar em monitor nativo (não virtual)
3. Aumentar resolução em `FxTheme.java`:
   ```java
   public static final double SCENE_MAIN_WIDTH = 1920;
   public static final double SCENE_MAIN_HEIGHT = 1080;
   ```

### Problema: Cores diferentes de esperado
**Solução:**
1. Verificar paleta em `ScreenshotsTraining.java`
2. Limpar cache Maven: `mvn clean`
3. Recompiler: `mvn compile`

---

## 📚 Referências

- [Manual Completo](manual-treinamento-screenshots.md)
- [JavaFX Docs](https://openjfx.io/javadoc/21/)
- [CSS Reference](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/doc-files/cssref.html)
- [Pillow Docs](https://pillow.readthedocs.io/)

---

## 📝 Licença

Desenvolvido por **Cara Core Informática** para treinamento interno.

**Status:** ✅ Pronto para Produção  
**Versão:** 1.0  
**Data:** 17/04/2026

---

## 👥 Suporte

- **Issues:** GitHub Issues
- **Dúvidas:** Wiki Interno
- **Consultoria:** consultoria@caracore.com.br

---

**Última atualização:** 17/04/2026 • Tema: Modena Corporativo • Java 21 + JavaFX
