import sys
from PyQt6 import QtWidgets, uic


def format_flag_colors(top, middle, bottom):
    """Возвращает строку цветов через запятую, игнорируя None значения."""
    parts = [p for p in (top, middle, bottom) if p]
    return ", ".join(parts) if parts else ""

class Task1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)
        self.btn_draw_flag.clicked.connect(self.on_draw)

    def on_draw(self):
        top = "Красный" if self.rb_top_red.isChecked() else ("Белый" if self.rb_top_white.isChecked() else None)
        mid = "Зелёный" if self.rb_mid_green.isChecked() else ("Синий" if self.rb_mid_blue.isChecked() else None)
        bot = "Красный" if self.rb_bot_red.isChecked() else ("Белый" if self.rb_bot_white.isChecked() else None)
        self.lbl_flag_result.setText(format_flag_colors(top, mid, bot))



def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Task1()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
