from langchain.agents import tool
from memory import load_shopping_list, save_shopping_list

@tool
def add_product(items: dict) -> str:
    """
    Aggiunge dei prodotti alla lista della spesa.
    Argomento: items (dict) con nome prodotto come chiave e quantità come valore.
    Esempio: {"mele": 3, "latte": 1}
    """
    shopping_list = load_shopping_list()
    for item, qty in items.items():
        item = item.lower()
        if item in shopping_list:
            shopping_list[item] += qty
        else:
            shopping_list[item] = qty
    save_shopping_list(shopping_list)

    summary = "\n".join([f" {qty} x {item}" for item, qty in items.items()])
    return f"Prodotti aggiunti:\n{summary}"

@tool
def remove_product(items: dict) -> str:
    """
    Rimuove dei prodotti dalla lista della spesa.
    Argomento: items (dict) con nome prodotto come chiave e quantità da rimuovere.
    Esempio: {"mele": 2, "latte": 1}
    """
    shopping_list = load_shopping_list()
    messages = []
    print(items.items())
    for item, qty in items.items():
        item = item.lower()
        if item not in shopping_list:
            messages.append(f" '{item}' non è nella lista.")
            continue

        shopping_list[item] -= qty
        if shopping_list[item] <= 0:
            del shopping_list[item]
            messages.append(f" '{item}' rimosso completamente.")
        else:
            messages.append(f" {qty} x '{item}' rimosso. Rimane: {shopping_list[item]}")

    save_shopping_list(shopping_list)
    return "\n".join(messages)

@tool
def show_list() -> str:
    """Mostra la lista corrente della spesa con quantità."""
    shopping_list = load_shopping_list()
    if not shopping_list:
        return " La lista della spesa è vuota."
    items = "\n".join([f"- {item}: {qty}" for item, qty in shopping_list.items()])
    return f" Lista della Spesa:\n{items}"

@tool(return_direct=True)
def clear_list() -> str:
    """Svuota completamente la lista della spesa."""
    save_shopping_list({})
    return "🧹 Lista della spesa svuotata."

tools = [add_product, remove_product, show_list, clear_list]

# test_value={"pizze" : 2}
# test_value = {"items" : {"pizze" : 2}}
# print(type(test_value),"\n")
# print(add_product(test_value))
# test_value = {"pizze" : 2}
# print(type(test_value),"\n")
# print(add_product(test_value))

