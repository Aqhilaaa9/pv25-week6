import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FontAdjusterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Week 6.ui", self)

        # Ambil widget dari file UI
        self.labelNIM = self.findChild(QtWidgets.QLabel, "labelNIM")

        # Slider
        self.sliderFontSize = self.findChild(QtWidgets.QSlider, "sliderFontSize")
        self.sliderFontColor = self.findChild(QtWidgets.QSlider, "sliderFontColor")
        self.sliderBgColor = self.findChild(QtWidgets.QSlider, "sliderBgColor")

        # Label di kiri slider
        self.labelFontSize = self.findChild(QtWidgets.QLabel, "labelFontSize")
        self.labelFontColor = self.findChild(QtWidgets.QLabel, "labelFontColor")
        self.labelBgColor = self.findChild(QtWidgets.QLabel, "labelBgColor")

        # Label nilai slider (kanan)
        self.labelFontSizeValue = self.findChild(QtWidgets.QLabel, "labelFontSizeValue")
        self.labelFontColorValue = self.findChild(QtWidgets.QLabel, "labelFontColorValue")
        self.labelBgColorValue = self.findChild(QtWidgets.QLabel, "labelBgColorValue")

        # Set teks label di kiri slider
        self.labelFontSize.setText("Font Size:")
        self.labelFontColor.setText("Font Color:")
        self.labelBgColor.setText("Background Color:")

        self.labelNIM.setAlignment(Qt.AlignCenter)

        # Atur range dan nilai awal slider
        self.sliderFontSize.setRange(20, 60)
        self.sliderFontColor.setRange(0, 255)
        self.sliderBgColor.setRange(0, 255)

        self.sliderFontSize.setValue(20)
        self.sliderFontColor.setValue(0)
        self.sliderBgColor.setValue(255)

        # Hubungkan event slider ke fungsi
        self.sliderFontSize.valueChanged.connect(self.updateStyle)
        self.sliderFontColor.valueChanged.connect(self.updateStyle)
        self.sliderBgColor.valueChanged.connect(self.updateStyle)

        self.updateStyle()

    def updateStyle(self):
        font_size = self.sliderFontSize.value()
        font_gray = self.sliderFontColor.value()
        bg_gray = self.sliderBgColor.value()

        # Update label nilai slider
        self.labelFontSizeValue.setText(str(font_size))
        self.labelFontColorValue.setText(str(font_gray))
        self.labelBgColorValue.setText(str(bg_gray))

        # Ubah font dan style
        font = QFont("Arial", font_size)
        self.labelNIM.setFont(font)

        self.labelNIM.setStyleSheet(f"""
            background-color: rgb({bg_gray}, {bg_gray}, {bg_gray});
            color: rgb({font_gray}, {font_gray}, {font_gray});
        """)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FontAdjusterApp()
    window.show()
    sys.exit(app.exec_())
