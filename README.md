# RAG POC - Sophilabs

## 📂 Corpus
- **PDFs**: About, Case Studies (guardados en `data/pdfs/`).
- **CSVs**: Projects dataset de ejemplo (`data/projects.csv`).
- **HTML**: Homepage, Services, Case Studies (descargados con `src/download_pages.py`).

## 🎯 Criterio de selección
- Páginas que describen servicios, casos de uso y clientes (info técnica).
- Se evita contenido promocional o de blog.
- Se usan formatos variados (PDF, CSV, HTML) para probar robustez del pipeline.

## ▶️ Cómo correr
```bash
# Crear entorno (si no existe)
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install llama-index pypdf requests

# Descargar HTMLs
python src/download_pages.py

