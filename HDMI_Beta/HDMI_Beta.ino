#include <IRremote.h>
//#include <NewTone.h>

#define input  0x20DFD02F
#define ok     0x20DF22DD
#define power  0x20DF10EF
#define menu   0x20DFC23D
#define up     0x20DF02FD
#define down   0x20DF827D
#define chUp     0x20DF00FF
#define chDown   0x20DF807F
#define volUp     0x20DF40BF
#define volDown   0x20DFC03F

IRsend irenviar;
int indicadorA = 2;
int indicadorB = 4;
int opcion;

void setup() {
  
  Serial.begin(9600);
  pinMode(indicadorA,OUTPUT);
  pinMode(indicadorB,OUTPUT);

}

void loop() {
  
  if(Serial.available() > 0)
  {
    opcion = Serial.read();
    switch(opcion)
	{
	
		case '1':
			probarHDMI();
		break;	
		case '2':
			regresoHDMI();
		break;	
		case 'p':
                        digitalWrite(indicadorB, HIGH);
			paso(power,indicadorA);
                        digitalWrite(indicadorB,LOW);
		break;
		case 'm':
			paso(menu,indicadorA);
		break;		
		case 'o':
			paso(ok,indicadorA);
		break;	
		case 'u':
			paso(up,indicadorB);
		break;		
		case 'd':
			paso(down,indicadorB);
		break;
		case 'A':
			paso(chUp,indicadorA);
		break;		
		case 'B':
			paso(chDown,indicadorB);
		break;	
		case 'a':
			paso(volUp,indicadorA);
		break;		
		case 'b':
			paso(volDown,indicadorB);
		break;
    		case 'i':
			paso(input,indicadorB);
		break;
	}
   }
}

void paso (int long codigo,int indicador){
  irenviar.sendNEC(codigo,32);
  Serial.print("Enviando Codigo: ");
  Serial.println(codigo);
  digitalWrite(indicador, HIGH);
  delay(800);
  digitalWrite(indicador,LOW);
  
}

void probarHDMI(){
    //input
     paso(input,indicadorA);
     //Abajo
     paso(down,indicadorA);
     //ok
     paso(ok,indicadorA);
}

void regresoHDMI(){
   //input
     paso(input,indicadorB);
     //arriba
     paso(up,indicadorB);
     //ok
     paso(ok,indicadorB);
}
