import hassapi as hass
import datetime

class SleepWell(hass.Hass):

  def initialize(self):
    bed_time = datetime.time(21, 0, 0)
    wake_up_time = datetime.time(8, 30, 0)
    self.run_daily(self.on_going_to_bed_cb, bed_time)
    self.run_daily(self.on_waking_up_cb, wake_up_time)

  def on_going_to_bed_cb(self, kwargs):
    self.turn_on("scene.salon_de_ambiente")

  def on_waking_up_cb(self, kwargs):
    self.turn_off("switch.enchufe_3_on_off")

