#include <Arduino.h>

void setup(){
  Serial.begin(115200);
  pinMode(32, INPUT);
  pinMode(33, INPUT);
  pinMode(27, INPUT);
  pinMode(14, INPUT);
  pinMode(12, INPUT);
}


void loop(){
  Serial.println(touchRead(32));
  Serial.println(touchRead(33));
  Serial.println(touchRead(27));
  Serial.println(touchRead(14));
  Serial.println(touchRead(12));

  delay(100);
}

//Código feito anteriormente, pensando em identificar cada planta. Porém não há necessidade.
/*  int plantaA = touchRead(32);
  String sendA = "A"+String(plantaA);
  Serial.println(sendA); //talvez de ruim pq ele vai mandar constantemente... Talvez tenha que colocar um attachInterrupt ou um if aqui pra só mandar se tiver variacao

  int plantaB = touchRead(33);
  String sendB = "B"+String(plantaB);
  Serial.println(sendB);

  int plantaC = touchRead(27);
  String sendC = "C"+String(plantaC);
  Serial.println(sendC);

  int plantaD = touchRead(14);
  String sendD = "D"+String(plantaD);
  Serial.println(sendD);

  int plantaE = touchRead(12);
  String sendE = "E"+String(plantaE);
  Serial.println(sendE);*/