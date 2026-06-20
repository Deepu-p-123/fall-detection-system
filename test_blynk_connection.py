import blynklib
import time

BLYNK_AUTH = "v6r5GR0SJDMKykbrSJzeI-V0i4gPtCnF"

blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    time.sleep(0.05)