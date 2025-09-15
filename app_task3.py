import sys
from PyQt6 import QtWidgets, uic


def add_contact(contacts_list, name, phone):
    if not name:
        raise ValueError("Имя контакта не может быть пустым")
    contacts_list.append((name, phone))

class Task3(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task3.ui', self)
        self.contacts = []
        self.btn_add_contact.clicked.connect(self.on_add)

    def on_add(self):
        name = self.le_contact_name.text().strip()
        phone = self.le_contact_phone.text().strip()
        try:
            add_contact(self.contacts, name, phone)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", str(e))
            return
        self.listContacts.addItem(f"{name} — {phone}")
        self.le_contact_name.clear(); self.le_contact_phone.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Task3()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
