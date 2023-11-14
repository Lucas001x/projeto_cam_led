#define ledazul 13
#define ledvermelho 12
#define ledamarelo 14

void setup(){
  Serial.begin(115200);

  pinMode(ledazul, OUTPUT);
  pinMode(ledvermelho, OUTPUT);
  pinMode(ledamarelo, OUTPUT);

}

void loop() {


  char controlSignal;

  

  while(!Serial.available());
  controlSignal = Serial.read();
  //verifica se recebeu algum serial

  Serial.println(controlSignal);

    if (controlSignal == '1'){
      digitalWrite(ledazul, 0);
    };

    if (controlSignal == '2'){
      digitalWrite(ledvermelho, 0);
    };

    if (controlSignal == '3'){
      digitalWrite(ledamarelo, 0);
    };

    if (controlSignal == '4'){
      digitalWrite(ledvermelho, LOW);
      digitalWrite(ledamarelo, LOW);
      digitalWrite(ledazul, LOW);
    };

    if (controlSignal == '5'){
      digitalWrite(ledazul, 1);
    };

    if (controlSignal == '6'){
      digitalWrite(ledvermelho, 1);
    };
    if(controlSignal == '7'){
      digitalWrite(ledamarelo, 1);
    };


}