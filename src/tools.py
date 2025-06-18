from langchain.agents import tool
from memory import load_shopping_list, save_shopping_list

@tool(return_direct=True)
def add_product(item: str, quantity: int = 1) -> str:
    """Aggiunge una quantità specifica di un prodotto alla lista della spesa."""
    item = item.lower()
    shopping_list = load_shopping_list()
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity
    save_shopping_list(shopping_list)
    return f" Aggiunti {quantity} x '{item}' alla lista."

@tool(return_direct=True)
def remove_product(item: str, quantity: int = 1) -> str:
    """Rimuove una quantità specifica di un prodotto dalla lista della spesa."""
    item = item.lower()
    shopping_list = load_shopping_list()
    if item not in shopping_list:
        return f" Il prodotto '{item}' non è nella lista."
    shopping_list[item] -= quantity
    if shopping_list[item] <= 0:
        del shopping_list[item]
        message = f"🗑️ '{item}' rimosso completamente dalla lista."
    else:
        message = f" Rimosso {quantity} x '{item}'. Quantità rimanente: {shopping_list[item]}"
    save_shopping_list(shopping_list)
    return message

@tool(return_direct=True)
def show_list() -> str:
    """Mostra la lista corrente della spesa."""
    shopping_list = load_shopping_list()
    if not shopping_list:
        return "La lista della spesa è vuota."
    items = "\n".join([f"- {item}: {qty}" for item, qty in shopping_list.items()])
    return f" Lista della Spesa:\n{items}"

@tool(return_direct=True)
def clear_list() -> str:
    """Svuota completamente la lista della spesa."""
    save_shopping_list({})
    return "🧹 Lista della spesa svuotata."

tools = [add_product, remove_product, show_list, clear_list]
