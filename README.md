# Case Técnico BI

Uma solução de limpeza e análise de uma base de vendas (`base_vendas_clean.csv`) utilizando Python e Power BI. Inclui script de correção de encoding, modelo dimensional e dashboards interativos.

---

## 🗂 Estrutura de Pastas

```
/
├── data/
│   └── base_vendas_clean.csv        ← Base de vendas limpa (CSV)
├── scripts/
│   └── data_encoding.py             ← Script Python para detectar/fixar encoding
├── powerbi/
│   ├── case_tecnico_bi.pbit         ← Template Power BI
│   └── case_tecnico_bi.pbix         ← Relatório Power BI
├── docs/                             ← Documentação auxiliar (a ser inserida)
└── README.md                         ← Este arquivo
```

---

## 🔧 Pré-requisitos

- **Python 3.7+**
- **Power BI Desktop** (versão recente)
- Bibliotecas Python (instalar via pip):

  ```bash
  pip install requirements.txt
  ```

---

## 🚀 Como rodar

1. **Clonar repositório**
   ```bash
   git clone https://github.com/raulward/case_tecnico_bi.git
   cd case_tecnico_bi
   ```

2. **Limpar encoding do CSV**
   ```bash
   cd scripts
   python data_encoding.py
   ```
   - Gera (ou atualiza) `data/base_vendas_clean.csv` corrigido.

3. **Abrir o relatório no Power BI**
   - Abra `powerbi/case_tecnico_bi.pbit` (template).
   - Ao abrir, aponte o parâmetro de fonte para `data/base_vendas_clean.csv`.
   - Aguarde a atualização das consultas e do modelo.

4. **Explorar dashboards**
   - Use os slicers de Data, Produto, Vendedor e Canal para filtrar.
   - Navegue pelas páginas:
     1. **Vendas** (KPI, tendência)
     2. **Vendedores** (ranking, métricas, devoluções)
     3. **Produtos** (Top 10, diversidade, rentabilidade)

---

## 📑 Documentação (em breve)

Arquivos a serem adicionados em `docs/`:

- **Data Dictionary** (`data_dictionary.md`)
- **Diagrama de Modelo** (`model_diagram.md`)
- **Catálogo de Medidas DAX** (`measures.md`)
- **Guia de Visualizações** (`report_guide.md`)
- **Changelog** (`changelog.md`)
- **Roteiro de Vídeo** (`video_script.md`)

---

## ⚙️ Próximos Passos

- Publicar no Power BI Service com alertas de dados.
- Criar versão mobile e paginada.

---

## 🤝 Contribuição

1. Fork deste repositório
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas mudanças (`git commit -m 'Minha contribuição'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está disponível sob a [MIT License](LICENSE).
