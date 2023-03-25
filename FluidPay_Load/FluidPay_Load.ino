#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);

byte cardData[16] = {};  // 16-byte buffer to store card data
String name = "Fasina Oreoluwa";  // Name to be stored on the card
byte cardID[4] = {0x12, 0x34, 0x56, 0x78};  // Card unique ID
int bvn = 22339731679;  // BVN to be stored on the card
byte amount = 100;       // Amount to be stored on the card

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  SPI.begin();         // Initialize SPI communication
  mfrc522.PCD_Init();  // Initialize RC522 module0.0
}

void loop() {0.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {  // Check if a new card is present
    return;
  }

  if ( ! mfrc522.PICC_ReadCardSerial()) {    // Select and read the card
    return;
  }

  for (byte i = 0; i < 16; i++) {            // Store card data in buffer
    cardData[i] = mfrc522.uid.uidByte[i];
  }

  mfrc522.PICC_HaltA();  // Stop communication with the card
  mfrc522.PCD_StopCrypto1();

  // Write card data, name, card ID, BVN, and amount to serial monitor
  Serial.print("Card Data: ");
  for (byte i = 0; i < 16; i++) {
    Serial.print(cardData[i], HEX);
    Serial.print(" ");
  }
  Serial.println();

  Serial.print("Name: ");
  Serial.println(name);

  Serial.print("Card ID: ");
  for (byte i = 0; i < 4; i++) {
    Serial.print(cardID[i], HEX);
    Serial.print(" ");
  }
  Serial.println();

  Serial.print("BVN: ");
  Serial.println(bvn);

  Serial.print("Amount: ");
  Serial.println(amount);

  delay(1000);  // Wait for 1 second before reading the next card
}
