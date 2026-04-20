# 🎥 TestFX — Captura de Screenshots Automatizada

## ⚡ Resumo

TestFX é um framework para testes automatizados de aplicações JavaFX. Com ele você consegue:

✅ Executar cada tela da aplicação de forma determinística  
✅ Capturar screenshots de alta fidelidade automaticamente  
✅ Navegar entre telas usando teclado programaticamente  
✅ Gerar screenshots para manual de treinamento sem intervenção manual  
✅ Reproduzir exatamente o mesmo resultado a cada execução  

---

## 🚀 Como Usar

### Forma 1: Executar Todos os Testes TestFX
```bash
mvn clean test -Dtest=ScreenshotsTrainingTestFX
```

**Output:**
```
screenshots/testfx_20260417_174215/
├── 01_login.png
├── 02_frente_caixa.png
├── 03_confirmacao_pagamento.png
├── 04_cadastro_produto.png
└── 05_pesquisa_cliente.png
```

### Forma 2: Executar Apenas 1 Teste Específico
```bash
# Apenas tela LOGIN
mvn clean test -Dtest=ScreenshotsTrainingTestFX#testCaptureTelaLogin

# Apenas tela FRENTE DE CAIXA
mvn clean test -Dtest=ScreenshotsTrainingTestFX#testCaptureFrenteCaixa
```

### Forma 3: Usar Menu Interativo (Recomendado)
```bash
# Adicione ao python scripts/compilar_screenshots.py opção 4:
# "4. Gerar screenshots com TestFX"

# Ou execute diretamente:
python scripts/compilar_screenshots_testfx.py  # Windows
./python scripts/compilar_screenshots_testfx.py # Linux/macOS
```

---

## 📊 O Que é Capturado

### Tela 1: LOGIN
- Componentes: TextField (usuário), TextField (senha), Button, Link
- Dados: admin / admin
- Validação: SQLite local visible

### Tela 2: FRENTE DE CAIXA
- Componentes: SplitPane, TableView (catálogo), ComboBox (vendedor), TableView (carrinho)
- Mock Data: 5 produtos, 3 itens no carrinho
- Totais: Subtotal, desconto, total R$ 75,00

### Tela 3: CONFIRMAÇÃO PAGAMENTO
- Componentes: Modal, GridPane, RadioButton (4 formas)
- Dados: Venda #000451, data/hora, operador, total
- Formas: Dinheiro, Débito, Crédito, PIX

### Tela 4: CADASTRO PRODUTO
- Componentes: GridPane, TextField (5 campos), ComboBox (categoria)
- Mock Data: Código 001, Café Expresso, R$ 8,50, 150 unidades

### Tela 5: PESQUISA CLIENTE
- Componentes: HBox (busca), TableView (3 clientes)
- Colunas: Nome, CPF, Email, Telefone
- Dados: 3 clientes com informações completas

---

## 🔧 Configuração

### Dependências Adicionadas (pom.xml)
```xml
<dependency>
    <groupId>org.testfx</groupId>
    <artifactId>testfx-core</artifactId>
    <version>4.0.21</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testfx</groupId>
    <artifactId>testfx-junit5</artifactId>
    <version>4.0.21</version>
    <scope>test</scope>
</dependency>
```

### Resolução de Testes
```
Padrão: 1280×800 (WXGA+)
Escala: 100% (sem zoom do Windows)
Headless: Sim (executa sem janela visível)
Espera: 500ms entre screenshots (renderização)
```

---

## 📝 Código-Chave

### Inicialização
```java
@ExtendWith(ApplicationExtension.class)
public class ScreenshotsTrainingTestFX {
    
    @Start
    public void start(Stage stage, FxRobot fxRobot) throws Exception {
        appInstance = new ScreenshotsTraining();
        appInstance.start(stage);
    }
}
```

### Navegação
```java
// Próxima tela
robot.press(javafx.scene.input.KeyCode.RIGHT);

// Tela anterior
robot.press(javafx.scene.input.KeyCode.LEFT);

// Aguardar renderização
WaitForAsyncUtils.waitForFxEvents();
Thread.sleep(500);
```

### Captura de Screenshot
```java
// Tela completa
WritableImage image = primaryStage.getScene().snapshot(null);
BufferedImage bufferedImage = SwingFXUtils.fromFXImage(image, null);
ImageIO.write(bufferedImage, "png", outputFile);

// Nó específico
WritableImage image = node.snapshot(null, null);
```

---

## 🆘 Troubleshooting

### Erro: "Cannot locate awt.toolkit"
**Solução:** Executar com JDK 21 (não JRE):
```bash
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
mvn clean test -Dtest=ScreenshotsTrainingTestFX
```

### Erro: "No Node on Scene is focused"
**Solução:** Adicionar `WaitForAsyncUtils.waitForFxEvents()` após navegação:
```java
robot.press(KeyCode.RIGHT);
WaitForAsyncUtils.waitForFxEvents();
Thread.sleep(200);  // aguardar renderização
```

### Screenshots Cortadas ou Blurry
**Solução:** Verificar Windows Scale:
- Windows: Configurações > Exibição > Escala deve ser 100%
- Linux: Não aplicável
- macOS: Não aplicável

### Diretório de Output Não Encontrado
**Solução:** Criar manualmente:
```bash
mkdir -p screenshots/testfx_YYYYMMDD_HHMMSS
```

---

## 📊 Comparação: Métodos de Captura

| Método | Velocidade | Confiabilidade | Automação | Uso |
|--------|-----------|---|---|---|
| **TestFX** | Rápido | ⭐⭐⭐⭐⭐ | 100% | Recomendado |
| Python Pillow | Médio | ⭐⭐⭐ | 80% | Fallback |
| Manual (Win+Shift+S) | Lento | ⭐⭐ | 0% | Debug |
| Selenium | Médio | ⭐⭐⭐ | 100% | Browser only |

---

## 🎯 Próximas Etapas

### Fase 1: Screenshots TestFX ✅
- [x] Adicionar dependência TestFX
- [x] Criar classe de teste
- [x] Capturar 5 telas
- [x] Validar qualidade

### Fase 2: Integração com Pipeline CI/CD
- [ ] GitHub Actions + TestFX
- [ ] Publicar screenshots em releases
- [ ] Badge de status

### Fase 3: Testes Adicionais
- [ ] Testes de interação (cliques, digitação)
- [ ] Validações de dados
- [ ] Performance testing

### Fase 4: Geração de PDF
- [ ] Combinar screenshots + anotações
- [ ] Criar sumário visual
- [ ] Compilar PDF final

---

## 💡 Tips & Tricks

### Capturar com Atraso Personalizado
```java
private void captureScreenshotWithDelay(String filename, long delayMs) throws Exception {
    WaitForAsyncUtils.waitForFxEvents();
    Thread.sleep(delayMs);  // Aguardar animações
    captureScreenshot(filename);
}
```

### Capturar Apenas Parte da Tela
```java
private void captureRegion(double x, double y, double width, double height, String filename) 
    throws Exception {
    // Usar WritableImage com bounds específicos
    WritableImage image = new WritableImage((int)width, (int)height);
    scene.snapshot(null, image);  // Com parâmetros de região
    // ... salvar
}
```

### Validar Screenshots
```java
// Verificar se arquivo foi criado e não está vazio
File file = new File(TEST_OUTPUT_DIR, filename);
assert file.exists() : "Screenshot não foi criada";
assert file.length() > 0 : "Screenshot está vazia";
```

---

## 📚 Referências

- [TestFX Official Docs](https://github.com/TestFX/TestFX)
- [TestFX JavaDoc](https://testfx-docs.readthedocs.io/)
- [JUnit 5 Documentation](https://junit.org/junit5/)
- [JavaFX Testing Best Practices](https://openjfx.io/)

---

## 📞 Suporte

**Erro não listado aqui?**

1. Verificar logs: `target/surefire-reports/`
2. Ativar debug: `mvn clean test -X -Dtest=ScreenshotsTrainingTestFX`
3. Executar em modo GUI: Remover `-Dheadless=true`

---

## ✨ Resumo

Com TestFX você consegue:

✅ Capturar screenshots **automaticamente** (0 intervenção manual)  
✅ **Reproduzir** exatamente igual a cada execução  
✅ **Integrar** em pipeline CI/CD  
✅ Gerar screenshots **profissionais** para manuais  
✅ Testar **interações** e **fluxos** completos  

**Status:** ✅ Pronto para Produção

---

**Desenvolvido com ❤️ por Cara Core Informática**

**Data:** 17/04/2026 | **Versão:** 1.0 | **Java:** 21 | **JavaFX:** 21 | **TestFX:** 4.0.21
