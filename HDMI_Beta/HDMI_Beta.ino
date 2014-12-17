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
#define uno  0x20DF8877
#define dos  0x20DF48B7
#define tres  0x20DFC837
#define cuatro 0x20DF28D7
#define cinco  0x20DFA857
#define seis  0x20DF6897
#define siete  0x20DFE817
#define ocho  0x20DF18E7
#define nueve 0x20DF9867
#define cero 0x20DF08F7
#define salir 0x20DFDA25
#define right 0x20DF609F
#define left 0x20DFE01F



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
	
		case 's':
			probarHDMI();
                        cargando();
		break;	
		case 'r':
			regresoHDMI();
                        cargando();
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
			paso(up,indicadorA);
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
			paso(input,indicadorA);
		break;

                case '1':
			paso(uno,indicadorB);
		break;		
		case '2':
			paso(dos,indicadorA);
		break;	
		case '3':
			paso(tres,indicadorB);
		break;		
		case '4':
			paso(cuatro,indicadorA);
		break;
    		case '5':
			paso(cinco,indicadorB);
		break;
		case '6':
			paso(seis,indicadorA);
		break;	
		case '7':
			paso(siete,indicadorB);
		break;		
		case '8':
			paso(ocho,indicadorA);
		break;
    		case '9':
			paso(nueve,indicadorB);
		break;
                case '0':
			paso(cero,indicadorA);
		break;  
               case 'x':
			paso(salir,indicadorA);
		break;
               case 'L':
			paso(left,indicadorB);
		break;
               case 'R':
			paso(right,indicadorA);
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

void cargando(){
  digitalWrite(indicadorA,HIGH);
  digitalWrite(indicadorB,HIGH);
  delay(4000);
  digitalWrite(indicadorA,LOW);
  digitalWrite(indicadorB,LOW);
}
