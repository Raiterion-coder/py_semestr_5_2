import sys
from PyQt6 import QtWidgets, uic


from datetime import datetime

def add_event(events_list, name, date_obj, time_obj):
    """Добавляет событие как кортеж (datetime, name) в events_list и поддерживает сортировку."""
    if not name:
        raise ValueError("Название события не может быть пустым")
    dt = datetime(date_obj.year(), date_obj.month(), date_obj.day(),
                  time_obj.hour(), time_obj.minute(), time_obj.second())
    events_list.append((dt, name))
    events_list.sort(key=lambda x: x[0])

def format_event_item(dt, name):
    return f"{dt.strftime('%Y-%m-%d %H:%M')} — {name}"

class Task2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task2.ui', self)
        self.events = []
        self.btn_add_event.clicked.connect(self.on_add)

    def on_add(self):
        name = self.le_event_name.text().strip()
        date = self.calendar.selectedDate()
        time = self.timeEdit.time()
        try:
            add_event(self.events, name, date, time)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", str(e))
            return
        self.listEvents.clear()
        for dt, nm in self.events:
            self.listEvents.addItem(format_event_item(dt, nm))
        self.le_event_name.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Task2()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
