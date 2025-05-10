from text_editor import TextEditor

if __name__ == "__main__":
    editor = TextEditor()

    editor.set_content("Привіт, світ!")
    print(f"Початковий текст: {editor.get_content()}")

    editor.add_content(" Це тестовий документ.")
    print(f"Після додавання: {editor.get_content()}")

    editor.insert_content(7, " мій")
    print(f"Після вставки: {editor.get_content()}")

    editor.delete_content(0, 7)
    print(f"Після видалення: {editor.get_content()}")

    editor.undo()
    print(f"Після відміни (undo): {editor.get_content()}")

    editor.undo()
    print(f"Після ще одної відміни (undo): {editor.get_content()}")

    editor.redo()
    print(f"Після повернення (redo): {editor.get_content()}")

    editor.add_content(" І це фінальна версія!")
    print(f"Після додавання нового тексту: {editor.get_content()}")

    if editor.can_redo():
        editor.redo()
        print(f"Після redo: {editor.get_content()}")
    else:
        print("Redo неможливий, тому що були нові зміни.")