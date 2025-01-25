from PyQt5.QtGui import QFontDatabase, QFont
from pathlib import Path

class FontManager:
    def __init__(self):
        self.font_path = Path(__file__).parent / "TT Interphases Pro Trial Condensed DemiBold.ttf"
        self.font_family = None
        self._load_font()

    def _load_font(self):
        """Загружает шрифт при инициализации."""
        font_id = QFontDatabase.addApplicationFont(str(self.font_path))
        if font_id == -1:
            print(f"Ошибка: не удалось загрузить шрифт {self.font_path}.")
            return

        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if not font_families:
            print(f"Ошибка: не удалось получить семейство шрифтов из файла {self.font_path}.")
            return

        self.font_family = font_families[0]

    def get_font(self, size=12):
        """Возвращает объект QFont. Если шрифт не загружен, возвращает стандартный шрифт."""
        if self.font_family:
            return QFont(self.font_family, size)
        else:
            return QFont()
