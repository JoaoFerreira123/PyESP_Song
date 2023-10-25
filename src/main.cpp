#include <Arduino.h>

void setup(){
  Serial.begin(115200);
  pinMode(4, INPUT);
}


void loop(){
  //Serial.println(touchRead(4));
  if(touchRead(4) < 60){
    Serial.println('1');
  }else{
    Serial.println('0');
  }
  delay(100);
}