RAG POC - Sophilabs

Este repositorio contiene la selección de fuentes y datos iniciales para construir un pipeline RAG usando LlamaIndex. El objetivo de esta parte fue recolectar y organizar la información relevante para que luego pueda ser procesada y vectorizada por los demás componentes del pipeline.

Estructura de carpetas

rag-poc-sophilabs/

data/

html/

pdfs/

projects.csv

src/

download_pages.py

README.md


Fuentes seleccionadas

HTML: páginas relacionadas con clientes, procesos internos y proyectos de Sophilabs.

PDFs: documentos internos de referencia, manuales y reportes relevantes.

CSV (projects.csv): tabla con datos de proyectos históricos y actuales, incluyendo cliente, año, tecnologías utilizadas y descripción.

Criterio de selección

Solo se incluyeron fuentes relevantes al corpus de conocimiento definido para este POC.

Se priorizó la información que pudiera ser útil para consultas posteriores por un LLM.

Se mantuvo consistencia en formatos y nomenclatura para facilitar el procesamiento posterior.

Repositorio

Este repositorio está preparado como POC con permisos de lectura para el equipo de desarrollo.

Los scripts y datos aquí contenidos son la base para el procesamiento y vectorización que realizará el pipeline.