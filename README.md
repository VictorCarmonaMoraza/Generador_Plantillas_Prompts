# 🧠 GeneradorPlantillas

GeneradorPlantillas es una aplicación Python que utiliza **LangChain** y **OpenAI** para generar respuestas inteligentes o plantillas conversacionales con diferentes personalidades.  
El proyecto está pensado para experimentar con modelos de lenguaje (LLMs) y aprender cómo ajustar su comportamiento mediante prompts y roles del sistema.

---

## 🚀 Características

- Integración con **LangChain** y **OpenAI GPT-4o-mini**  
- Ejemplos de invocaciones simples (`invoke`) y múltiples (`generate`)  
- Control de personalidad mediante mensajes del tipo `SystemMessage` y `HumanMessage`  
- Entorno virtual aislado (`.venv`) para una instalación limpia  
- Configuración mediante archivo `api_key.txt` para mantener segura tu clave

---

## 🧩 Requisitos

- Python **3.12**
- Una **API key** de [OpenAI](https://platform.openai.com/)
- Paquetes indicados en `requirements.txt`  

Contenido sugerido de `requirements.txt`:
```txt
langchain
langchain-openai
openai


## Creacion de fichero requirement
pip freeze > requirements.txt 