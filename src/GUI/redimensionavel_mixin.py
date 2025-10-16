# gui/redimensionavel_mixin.py
class RedimensionavelMixin:
    def permitir_redimensionamento(self):
        self.root.resizable(True, True)
