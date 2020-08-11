# TORA (Tigre / Tiger)
Most of the UI Automation framework still has detected the object by DOM object or WinAPI. This small project is for looking into technical feasibility of object detection by image. If you have an interest in a similar approach, you might have heard the framework called Sikuli, written by Java. 

The aim of this code fully implements by python.

Tora means Tiger in Japanese. its pronunciation seams like "Dora", Korean, it means working well.

# Descriptions
* The syntax of script is defined using pypep2, parser generator, internally it is using a regular expression. 
* The syntax is supporting 4 commands, Click / Wait / Press / Type.
* Click should have a parameter which set for file_name of image listed on Image(png) area.
* The screen of window would be store in tmp directory, which will be generated in the workspace directory. it will be the target of a screen for template matching.
* Press / Type are using pyautogui API internally. 
for supporting various parameters are supported by pyautogui, it needs to extend the syntax of the script.I am considering adding an option payload in each command. e.g Click(image, Option:{param1, param2} 

![ui_screen](https://github.com/kimtth/tora/blob/master/main_screen.PNG?raw=true)

**Preview**

![preview](https://github.com/kimtth/tora/blob/master/preview.gif?raw=true)
