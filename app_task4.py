import sys
from PyQt6 import QtWidgets, uic


def nim_ai_move(remaining, max_take=3):
    """
    Выигрышная стратегия для игры Ним с одной кучей, где каждый может взять до max_take предметов.
    Возвращает количество, которое должен взять ИИ (1..max_take). Если нет выигрышного хода, возвращает 1.
    """
    target = (max_take + 1)
    rem_mod = remaining % target
    if remaining == 0:
        return 0
    if rem_mod == 0:
        return 1 if remaining>=1 else 0
    else:
        take = rem_mod
        if take > max_take:
            take = 1
        return take if take<=remaining else remaining

class Task4(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task4.ui', self)
        self.btn_new_game.clicked.connect(self.on_new_game)
        self.btn_take.clicked.connect(self.on_take)
        self.remaining = 0

    def on_new_game(self):
        self.remaining = self.spin_start_n.value()
        self.lbl_nim_status.setText(f"Камней: {self.remaining}. Ход игрока.")
        self.spin_take.setMaximum(min(3, self.remaining))

    def on_take(self):
        take = self.spin_take.value()
        if take>self.remaining: 
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Недостаточно камней.")
            return
        self.remaining -= take
        if self.remaining == 0:
            self.lbl_nim_status.setText("Игрок выиграл!"); return
        ai_take = nim_ai_move(self.remaining,3)
        ai_take = min(ai_take, self.remaining)
        self.remaining -= ai_take
        if self.remaining==0:
            self.lbl_nim_status.setText(f"Компьютер взял {ai_take} — победа компьютера!")
        else:
            self.lbl_nim_status.setText(f"Компьютер взял {ai_take}. Осталось: {self.remaining}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Task4()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
