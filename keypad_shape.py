import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        lbl_display = QLabel('화면')
        pb_consonant = QPushButton("자음", self)
        pb_vowels = QPushButton('모음', self)
        pb_number = QPushButton('숫자', self)

        grid.addWidget(lbl_display, 0, 0, 3,3)      #화면 크기 설정
        grid.addWidget(QPushButton('시작'), 3, 0,)    #무언가를 시작하는 버튼
        grid.addWidget(QPushButton('정정'), 3, 1,)    #틀린건 고칠때 사용하는 버튼
        grid.addWidget(pb_consonant, 0, 3)          #자음으로 변환 버튼
        grid.addWidget(pb_vowels, 1, 3)             #모음변환 버튼
        grid.addWidget(pb_number, 2, 3)             #숫자 변환 버튼
        grid.addWidget(QPushButton('\u2191'), 4, 0) #다음으로 넘어가는 화살표 버튼(ex: 숫자)
        grid.addWidget(QPushButton('입력'), 4,1 )     #숫자, 자음등 글장 입력 버튼
        grid.addWidget(QPushButton('\u2193'), 4,2 ) #전으로 넘어가는 화살표 버튼
        grid.addWidget(QPushButton('확인'), 3, 2)     #
        grid.addWidget(QPushButton('취소'), 3, 3)     #

        lbl_display.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        self.setWindowTitle('시청각장애인_키패드')
        self.setGeometry(500, 200, 500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())







