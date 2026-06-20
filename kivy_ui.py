from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.label import Label
import cv2
import time

class FallUI(BoxLayout):

    def __init__(self, detector, blynk_service, **kwargs):

        super().__init__(**kwargs)

        self.detector = detector
        self.blynk = blynk_service

        self.orientation = "vertical"

        self.video = Image()
        self.add_widget(self.video)

        self.status = Label(text="System Ready")
        self.add_widget(self.status)

        self.running = False
        self.alert_sent = False

        Clock.schedule_interval(self.blynk_loop, 0.05)

    def blynk_loop(self, dt):
        self.blynk.run()

    def start(self):
        self.running = True
        Clock.schedule_interval(self.update, 1/15)

    def update(self, dt):

        if not self.running:
            return False

        frame = self.detector.get_frame()

        if frame is None:
            return True

        annotated, fall, conf = self.detector.detect(frame)

        frame_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        frame_rgb = cv2.flip(frame_rgb, 0)

        texture = Texture.create(size=(frame_rgb.shape[1], frame_rgb.shape[0]))
        texture.blit_buffer(frame_rgb.tobytes(), colorfmt="rgb", bufferfmt="ubyte")

        self.video.texture = texture

        if fall:

            self.status.text = "FALL DETECTED"

            if not self.alert_sent:
                self.blynk.send_virtual(1)
                self.blynk.send_event()
                self.alert_sent = True

        else:

            self.status.text = "Monitoring"
            self.alert_sent = False