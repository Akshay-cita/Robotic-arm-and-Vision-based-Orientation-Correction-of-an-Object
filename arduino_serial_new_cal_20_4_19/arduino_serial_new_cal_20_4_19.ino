#include <Servo.h>

Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;
Servo Servo5;
Servo Servo6;

int pos = 0;
String Control_sig = "90";  
volatile int rot ;

void setup() {
  Serial.begin(115200);
  Serial.flush();
  Servo1.attach(3);
  Servo2.attach(5);
  Servo3.attach(6);
  Servo4.attach(9);
  Servo5.attach(10);
  Servo6.attach(11);

  Servo1.write(50);
  Servo2.write(100);
  Servo3.write(80);
  Servo4.write(170);
  Servo5.write(0);
  Servo6.write(100); 
}

void loop() {
  if (Serial.available() > 0) {
    Control_sig = Serial.readString(); //Rotates 180 degree after picking the object if control_sig is 180
    Serial.println(Control_sig);
    //Serial.println(Control_sig);
    if (Control_sig == "180") {
      pick(180);
    }
    else if (Control_sig == "0" )
    {
      pick(0);
    }
    else {
      servo_calib();
    }
  }
}

void pick(int rot) {
 for (pos = 50; pos <= 120; pos += 1) { 
    Servo1.write(pos); 
    Serial.println(pos);            
    delay(40);     
  }
  for (pos = 100; pos >= 48; pos -= 1) { 
    Servo2.write(pos); 
    Serial.println(pos);             
    Servo3.write(180 - pos);
    delay(55);                       
  }
  delay(200);
  for (pos = 150; pos >= 180; pos += 1) { 
    Servo4.write(pos); 
    Serial.println(pos);            
    delay(55);                      
  }
  delay(800);
  Servo6.write(60);
  delay(800);
  
for (pos = 180; pos <= 150; pos -= 1) { 
    Servo4.write(pos); 
    Serial.println(pos);            
    delay(55);                      
  }
    for (pos = 48; pos <= 100; pos += 1) { 
    Servo2.write(pos);
    Serial.println(pos);              
    Servo3.write(180 - pos);
    delay(55);                      
  }
  //------------------------------------------------------
  for (pos = 0; pos <= rot; pos += 1) {
    Servo5.write(pos);
    delay(10);
  }
  //------------------------------------------------------
for (pos = 120; pos >= 50; pos -= 1) {
    Servo1.write(pos);  
    Serial.println(pos);            
    delay(40);                      
  } 
  //______________________________________________________________________
    for (pos = 100; pos >= 48; pos -= 1) { 
    Servo2.write(pos); 
    Serial.println(pos);             
    Servo3.write(180 - pos);
    delay(55);                       
  }
  for (pos = 150; pos >= 180; pos += 1) { 
    Servo4.write(pos); 
    Serial.println(pos);            
    delay(55);                      
  }
  delay(800);
  Servo6.write(100);
  delay(800);
   for (pos = 180; pos <= 150; pos -= 1) { 
    Servo4.write(pos); 
    Serial.println(pos);            
    delay(55);                      
  }
    for (pos = 48; pos <= 100; pos += 1) { 
    Servo2.write(pos);
    Serial.println(pos);              
    Servo3.write(180 - pos);
    delay(55);                      
  }
  //-------------------------------------------------------
  for (pos = rot; pos >= 0; pos -= 1) {
    Servo5.write(pos);
    delay(10);
  }
  //-------------------------------------------------------
  Control_sig = "90" ;
}

void servo_calib() {
  Servo1.write(45);
  Servo2.write(100);
  Servo3.write(80);
  Servo4.write(170);
  Servo5.write(0);
  Servo6.write(100); 
}


