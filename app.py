# ----------------------------------------------------------
# 🧠 DEMO: Creación de prompts personalizados con LangChain y OpenAI
# ----------------------------------------------------------
# Este script construye una conversación estructurada usando plantillas (prompts)
# que combinan mensajes del sistema (rol de la IA) y del humano (petición del usuario).
# Finalmente, se envía la conversación a un modelo de OpenAI y se imprime la respuesta.
# ----------------------------------------------------------

# 📦 Importaciones necesarias
from langchain.chains.question_answering.refine_prompts import chat_qa_prompt_template  # (no se usa en este ejemplo)
from langchain.prompts import (
    ChatPromptTemplate, PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain_openai import ChatOpenAI   # Permite conectar con los modelos de OpenAI
from openai import api_key                # (no se usa realmente)
from sqlalchemy import result_tuple       # (no se usa en este ejemplo)


# ----------------------------------------------------------
# 🧩 1️⃣ Crear las plantillas de prompts
# ----------------------------------------------------------

# 🔹 Plantilla del mensaje del sistema
# Este mensaje define la "personalidad" y el rol del asistente (IA)
system_template = (
    "Eres una IA especializada en coches de tipo {tipo_coches} "
    "y generar articulos que se leen en {tiempo_lectura}."
)

# Convertimos la cadena en una plantilla formal para LangChain
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# Mostramos las variables que esta plantilla espera
print(system_message_prompt.input_variables)
# 👉 ['tipo_coches', 'tiempo_lectura']


# ----------------------------------------------------------
# 🔹 Plantilla del mensaje del usuario
# Este mensaje representa lo que el usuario pide a la IA
human_template = "Necesito un articulo para vehiculos con motor {peticion_tipo_motor}"

# Convertimos la cadena en una plantilla de tipo humano
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Mostramos las variables necesarias
print(human_message_prompt.input_variables)
# 👉 ['peticion_tipo_motor']


# ----------------------------------------------------------
# 🧩 2️⃣ Combinar ambas plantillas en una plantilla de chat completa
# ----------------------------------------------------------

# Combinamos el mensaje del sistema (rol) y el del humano (petición)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# Mostramos todas las variables que se necesitan para rellenar el prompt
print(chat_prompt.input_variables)
# 👉 ['tipo_coches', 'tiempo_lectura', 'peticion_tipo_motor']


# ----------------------------------------------------------
# 🧩 3️⃣ Rellenar la plantilla con valores reales
# ----------------------------------------------------------

# Formateamos la plantilla con valores específicos
# y la convertimos a una lista de mensajes lista para enviar al modelo
solicitd_completa = chat_prompt.format_prompt(
    peticion_tipo_motor="Hibrido enchufable",
    tiempo_lectura="10 min",
    tipo_coches="japoneses"
).to_messages()

# En este punto, `solicitd_completa` contendrá algo así como:
# [
#   SystemMessage(content="Eres una IA especializada en coches de tipo japoneses y generar articulos que se leen en 10 min."),
#   HumanMessage(content="Necesito un articulo para vehiculos con motor Hibrido enchufable")
# ]


# ----------------------------------------------------------
# 🗝️ 4️⃣ Conectar con el modelo de OpenAI
# ----------------------------------------------------------

# Abrimos el fichero que contiene la clave de API
# ⚠️ Este archivo debe estar en la raíz del proyecto y contener solo la clave
f = open('api_key.txt')

# Leemos el contenido del fichero (la API key)
api_key = f.read()

# Cerramos el archivo (buena práctica)
f.close()

# Creamos el objeto ChatOpenAI pasando la clave de API
# Esto permite conectarse con el modelo (por defecto, gpt-4o-mini)
chat = ChatOpenAI(api_key=api_key)


# ----------------------------------------------------------
# 🤖 5️⃣ Ejecutar la solicitud y obtener la respuesta del modelo
# ----------------------------------------------------------

# Enviamos los mensajes al modelo
result = chat.invoke(solicitd_completa)

# Imprimimos la respuesta obtenida de la IA
print(result)
# 👉 Ejemplo de salida:
# AIMessage(content='Aquí tienes un artículo sobre los coches japoneses híbridos enchufables...')
