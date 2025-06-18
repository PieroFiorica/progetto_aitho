from langchain.agents import tool 
from memory import load_shopping_list, save_shopping_list


@tool
def add_product(item: str) -> str:
    """Aggiunge un prodotto alla lista della spesa."""
    shopping_list = load_shopping_list()
    shopping_list.append(item)
    save_shopping_list(shopping_list)
    return f"✅ '{item}' aggiunto alla lista."

@tool
def remove_product(item: str) -> str:
    """Rimuove un prodotto dalla lista della spesa."""
    shopping_list = load_shopping_list()
    if item in shopping_list:
        shopping_list.remove(item)
        save_shopping_list(shopping_list)
        return f"🗑️ '{item}' rimosso dalla lista."
    else:
        return f"⚠️ '{item}' non è presente nella lista."

@tool
def show_list() -> str:
    """Mostra la lista della spesa."""
    shopping_list = load_shopping_list()
    if shopping_list:
        return "🛒 Lista della Spesa:\n" + "\n".join(f"- {item}" for item in shopping_list)
    else:
        return "📭 La lista della spesa è vuota."

tools = [add_product, remove_product, show_list]