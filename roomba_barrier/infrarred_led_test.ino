
int led_pin = 7;

void setup() {
  pinMode(led_pin, OUTPUT);

}

void loop() {

  //1
  tone(led_pin, 38000, 3);
  delay(4);

  //0
  tone(led_pin, 38000, 1);
  delay(4);

  //1
  tone(led_pin, 38000, 3);
  delay(4);

  //0
  tone(led_pin, 38000, 1);
  delay(4);

  //0
  tone(led_pin, 38000, 1);
  delay(4);

  //0
  tone(led_pin, 38000, 1);
  delay(4);

  //1
  tone(led_pin, 38000, 3);
  delay(4);

  //0
  tone(led_pin, 38000, 1);
  delay(4);

  delay(20);

}
