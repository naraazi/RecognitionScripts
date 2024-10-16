// -- pino digital do buzzer
int buzzerPin = 12;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();

    if (receivedChar == 'm') {
      digitalWrite(buzzerPin, HIGH);
    } else if (receivedChar == 's') {
      digitalWrite(buzzerPin, LOW);
    }
  }
}
