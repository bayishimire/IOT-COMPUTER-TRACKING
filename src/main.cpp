#include <Arduino.h>
#include <WiFi.h>

const char* ssid="SOGO7";
const char* password="eze12345";

WiFiServer server(80);

void setup() {
Serial.begin(115200);

Serial.println("connect to wifi");
Serial.println(ssid);
WiFi.begin(ssid,password);

while (WiFi.status() !=WL_CONNECTED){
delay(500);
Serial.print(".");
}
Serial.println("");
Serial.println("wifi connectd");
Serial.println("esp32 ip address:");
Serial.println(WiFi.localIP());

//dealing with server connection
server.begin();

}

void loop() {
  // put your main code here, to run repeatedly:


WiFiClient client = server.available();

if(client){

  String currentline = "";
  while(client.connected()){
    if(client.available()){
      char d;
      d = client.read();
      Serial.write(d);


    if(d=='\n'&&currentline.length()==0){
      client.println("HTTP/1.1 200 OK");
      client.println("Content-type: text/html");
      // client.println("Connection: close");
      client.println();  // Important: blank line to end header


      //html files
      client.println("<!DOCTYPE html>");
      client.println("<html>");
      client.println("<head>");
      client.println("<title>GROUP 5 </title>");
      client.println("</head>");
      client.println("<body>");
      client.println("<h1>GROUP FIVE</h1>");
      client.println("</body>");
      client.println("</html>");

      break;
    }
    else if(d!='\r'){
      currentline = currentline + d;
    }
    else{
      currentline ="";
    }
    }
  }
}

client.stop();

}
