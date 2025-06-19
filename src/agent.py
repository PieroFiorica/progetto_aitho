from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain.chat_models.base import init_chat_model
from tools import tools

from langchain.globals import set_debug
#########################################################
set_debug(True)

import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL")
groq_model = os.getenv("GROQ_MODEL")
groq_temperature = os.getenv("GROQ_TEMPERATURE")

agent_prompt ="""
Sei un assistente intelligente che aiuta l'utente a gestire la lista della spesa.

Il tuo compito è interpretare il comando scritto dall'utente e decidere quale funzione chiamare tra queste quattro:

1. `add_product(item: dict)` -> Quando l'utente vuole aggiungere dei prodotti alla lista.
2. `remove_product(item: dict)` -> Quando l'utente vuole rimuovere dei prodotti dalla lista.
3. `show_list()` -> Quando l'utente vuole vedere la lista corrente.
4. `clear_list()` -> Quando l'utente vuole eliminare completamente la lista (es: "svuota la lista", "cancella tutto", "ripulisci", "elimina ogni cosa").


Esempi:

- "Aggiungi il pane e il latte" -> chiama `add_product({"items" : {"latte" : 1 , "pane" : 1} })`. 
- "Togli le uova" -> chiama `remove_product({"items" : {"uova" : 1}})`.
- "Mostra lista" -> chiama `show_list`.

Rispondi spiegando all'utente, in modo conciso, le operazioni effettuate dai tools che hai chiamato.

Gestisci comandi scritti in linguaggio naturale, anche vaghi o informali, e risolvi correttamente l'intento dell'utente.
"""

llm = init_chat_model(
        model=groq_model,
        model_provider="groq",
        temperature=groq_temperature,
        base_url=groq_base_url,
        api_key=groq_api_key
        ) 

agent = create_react_agent(
                model=llm.bind_tools(tools=tools,parallel_tool_calls=False),
                tools=tools,
                prompt=agent_prompt
                )