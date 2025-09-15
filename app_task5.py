import sys
from PyQt6 import QtWidgets, uic


def similarity_ratio(textA, textB):
    """
    Простая оценка схожести: доля идентичных строк (после очистки) от среднего количества строк.
    Возвращает процент 0..100.
    """
    a_lines = [l.strip() for l in textA.splitlines() if l.strip()]
    b_lines = [l.strip() for l in textB.splitlines() if l.strip()]
    if not a_lines and not b_lines:
        return 100.0
    if not a_lines or not b_lines:
        return 0.0
    set_a = set(a_lines)
    set_b = set(b_lines)
    common = set_a.intersection(set_b)
    avg_len = (len(set_a) + len(set_b)) / 2.0
    if avg_len == 0:
        return 0.0
    return (len(common) / avg_len) * 100.0

class Task5(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task5.ui', self)
        self.btn_check.clicked.connect(self.on_check)
        self.statusBar = self.statusbar

    def on_check(self):
        a = self.textA.toPlainText()
        b = self.textB.toPlainText()
        ratio = similarity_ratio(a,b)
        thr = self.dsb_threshold.value()
        txt = f"Сходство: {ratio:.1f}% (порог {thr}%)"
        self.statusBar.showMessage(txt)
        if ratio>=thr:
            self.statusBar.setStyleSheet("QStatusBar { background: rgb(254,0,0); }")
        else:
            self.statusBar.setStyleSheet("QStatusBar { background: rgb(29,232,29); }")

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Task5()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
