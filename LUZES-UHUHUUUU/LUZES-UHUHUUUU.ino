const int pinoLed1=8;
const int pinoLed2=9;
const int pinoLed3=10;
const int pinoLed4=11;
const int pinoLed5=12;
//OBS:SE FOR FAZER COM MAIS OU MENOS LEDS RETIRE/ADICIONE COM CUIDADO UIUI

void setup() {
  pinMode(pinoLed1,OUTPUT);
  pinMode(pinoLed2,OUTPUT);
  pinMode(pinoLed3,OUTPUT);
  pinMode(pinoLed4,OUTPUT);
  pinMode(pinoLed5,OUTPUT);
}

void loop() {
  //PISCADAS RÁPIDAS
   for (int i = 0; i < 3; i++) {
    digitalWrite(pinoLed1, HIGH);
    digitalWrite(pinoLed2, HIGH);
    digitalWrite(pinoLed3, HIGH);
    digitalWrite(pinoLed4, HIGH);
    digitalWrite(pinoLed5,HIGH);
    delay(150);
    digitalWrite(pinoLed1, LOW);
    digitalWrite(pinoLed2, LOW);
    digitalWrite(pinoLed3, LOW);
    digitalWrite(pinoLed4, LOW);
    digitalWrite(pinoLed5, LOW);
    delay(150);
  }
  
  // PISCADA SEQUENCIAL
  for (int i = 0; i < 2; i++) {
    digitalWrite(pinoLed1, HIGH);
    delay(400);
    digitalWrite(pinoLed1, LOW);
    
    digitalWrite(pinoLed2, HIGH);
    delay(400);
    digitalWrite(pinoLed2, LOW);
    
    digitalWrite(pinoLed3, HIGH);
    delay(400);
    digitalWrite(pinoLed3, LOW);
    
    digitalWrite(pinoLed4, HIGH);
    delay(400);
    digitalWrite(pinoLed4, LOW);
    
    digitalWrite(pinoLed5, HIGH);
    delay(400);
    digitalWrite(pinoLed5, LOW);
  }

  //ONDINHAS 
  for (int i = 0; i < 2; i++) {
    digitalWrite(pinoLed1, HIGH);
    delay(400);
    digitalWrite(pinoLed1, LOW);
    
    digitalWrite(pinoLed2, HIGH);
    delay(800);
    digitalWrite(pinoLed2, LOW);
    
    digitalWrite(pinoLed3, HIGH);
    delay(1200);
    digitalWrite(pinoLed3, LOW);
    
    digitalWrite(pinoLed4, HIGH);
    delay(800);
    digitalWrite(pinoLed4, LOW);
    
    digitalWrite(pinoLed5,HIGH);
    delay(800);
    digitalWrite(pinoLed5,LOW);
  }

  //INVERTENDO
  for (int i = 0; i < 3; i++) {
    digitalWrite(pinoLed1, HIGH);
    digitalWrite(pinoLed4, HIGH);
    delay(300);
    digitalWrite(pinoLed1, LOW);
    digitalWrite(pinoLed4, LOW);
    
    digitalWrite(pinoLed2, HIGH);
    digitalWrite(pinoLed3, HIGH);
    delay(300);
    digitalWrite(pinoLed2, LOW);
    digitalWrite(pinoLed3, LOW);
    
    digitalWrite(pinoLed4,LOW);
    digitalWrite(pinoLed5,HIGH);
    delay(300);
    digitalWrite(pinoLed4,LOW);
    digitalWrite(pinoLed5,LOW);
  }

//TEMPO PARA COMEÇAR DNV
  delay(1000);

}
