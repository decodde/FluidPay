#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup()
{
    Serial.begin(9600); // Initialize serial communication
    SPI.begin();        // Initialize SPI bus
    mfrc522.PCD_Init(); // Initialize MFRC522
    Serial.println("FLUID PAY");
}

void loop()
{
    String message = "";
    if (Serial.available() > 0)
    {
        //message = serial.readStringUntil('\n');
         message = Serial.readString();

        if (message.startsWith("COMMAND_WITH_DATA:") || message.startsWith("COMMAND:"))
        {
           processCommand(message);
        }
        else if (message.startsWith("buzzer="))
        {
           
        }

        message = "";
    }
    CheckForRfid();
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();
}

void processCommand(String message){
    String command = "";
    if(message.startsWith("COMMAND:")){
      command = message.substring(8);
    }
    else if (message.startsWith(("COMMAND_WITH_DATA:"))){
      String t = message.substring(18,message.length());
      int dataSeperatorPosition = t.indexOf(":");
      command = t.substring(0,dataSeperatorPosition);
      String data = t.substring(dataSeperatorPosition + 1, message.length());
      Serial.print(data);
    }
    
    Serial.print(command);
    //Serial.print(message);
}
void CheckForRfid()
{
    // Look for new RFID tags
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())
    {
        // Get the ID of the tag as a string
        String tagId = "";
        for (byte i = 0; i < mfrc522.uid.size; i++)
        {
            tagId.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
            tagId.concat(String(mfrc522.uid.uidByte[i], HEX));
        }
        Serial.println("RFID tag detected: " + tagId);
        // Send the tag ID over serial
        Serial.print("RFID_TAG:");
        Serial.println(tagId);
    }
}