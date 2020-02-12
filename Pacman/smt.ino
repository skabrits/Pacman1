#include <OneWire.h>
#include <DallasTemperature.h>
#include <math.h>
OneWire Wire1(6);
OneWire Wire2(7);
DallasTemperature sensors1(&Wire1);
DallasTemperature sensors2(&Wire2);
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int i;
float K;


double getK(float T1, float T2, float I) { // вычисляет коэфициент по температурам и току
  float sig = 0.0043;
  float ro = 0.01673;
  float T0 = 20;
  ro = ro * (1 + (T2 - T0) * sig);
  float rad = 0.2;
//  return (pow(I, 2) * ro * (1 + (T1 - T2) * sig)) / (pow(rad, 3) / 125 * (T1 - T2) * pow(M_PI, 2));
  return I / pow(((T1 - T2) / (ro * (1 + (T1 - T2) * sig))), 0.5);
}

double getI(float T1, float T2, float K) { // вычисляет силу тока по коэфициенту и температурам
  float sig = 0.0043;
  float ro = 0.01673;
  float T0 = 20;
  ro = ro * (1 + (T2 - T0) * sig);
  float rad = 0.2;
//  return pow(((K * pow(M_PI, 2) * pow(rad, 3) / 125 * (T1 - T2)) / (ro * (1 + (T1 - T2) * sig))), 0.5);
  return K*pow(((T1 - T2) / (ro * (1 + (T1 - T2) * sig))), 0.5);
}

void setup() {
  Serial.begin(9600);
  sensors1.begin();
  sensors2.begin();
  lcd.begin(16, 2);
  int i = 1;
}
void loop() {
  float d1 = sensors1.getTempCByIndex(0);
  float d2 = sensors2.getTempCByIndex(0);

  sensors1.requestTemperatures();
  Serial.print(" Температура 1 датчик: ");
  Serial.print(sensors1.getTempCByIndex(0));
  sensors2.requestTemperatures();
  Serial.print(" 2 датчик: ");
  Serial.print(sensors2.getTempCByIndex(0));
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("T1= " + String(sensors1.getTempCByIndex(0))); // выводит температуру окружающей среды
  lcd.setCursor(9, 0);
  lcd.print("T2= " + String(sensors2.getTempCByIndex(0))); // выводит температуру проводника
  lcd.setCursor(0, 1);
  lcd.print("I = " + String(getI(d2,d1,0.052985)) + " Ампер"); // - выводит ток I, если указать коэфициент
//  lcd.setCursor(5, 1);
//  lcd.print("*1000 " + String(getK(d2,d1,I)*1000)); - выводит коэфициент, если указать ток I
  delay(1000);
// 2.24 (просто пометка)
}