from kivy.app import App
from kivy.core.window import Window

from yolo_detector import YOLODetector
from blynk_service import BlynkService
from kivy_ui import FallUI


class FallApp(App):

    def build(self):

        Window.size = (1000, 700)

        detector = YOLODetector("best.pt")
        blynk = BlynkService()

        ui = FallUI(detector, blynk)

        ui.start()

        return ui


if __name__ == "__main__":
    FallApp().run()