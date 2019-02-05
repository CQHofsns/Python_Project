# Python Project Text To Image
**_This is my very first post and project on GitHub Community._**	

## Summary:
Python_Project_Text_To_Image is a program that convert the content that you wrote on text file (.txt) into image format (.bmp, .png, .jpg). Not only just convert text, you can adjust font color and background right in your text, like this:

> <edit c:"**_font color here_**", b:"**_background color here_**">"**_Text content here_**"<@edit>

For example, I have put a example text in Text Folder. And here is its content: 

> <edit: c=yellow, b=red>Bring <@edit><edit: c=red, b=yellow>me <@edit><edit: c=Blue, b=black>T<@edit><edit: c=orange, b=black>H<@edit><edit: c=red, b=black>A<@edit><edit: c=green, b=black>N<@edit><edit: c=purple, b=black>O<@edit><edit: c=yellow, b=black>S<@edit>

And here is the result:

![example](https://github.com/CQHofsns/Python_Project_Text_To_Image/blob/master/For%20README.md/result.png)

**WARNING: My program currently just can convert 1 line text file, which mean 2 line above text file will not work !! (Sorry I still working on it  :sweat: )**

## How to run this program:
**Note: _Before running this program, make sure you have Python ver3 in your computer._**

1. Open the "Main" Folder, click "Setup_Linux.sh" if you are using LinuxOS and "Setup_Windows.bat" if you are using WindowsOS. A Command Line Window/ Terminal Window will show up and start install required packages. After the installation has finished, you will see a Run.bat (WindowsOS)/ Run.sh (LinuxOS) is created.
2. Make a text (.txt) file with above format and the content you want, then save it with **UTF-8 charater code**.
3. Now click the Run.bat/ Run.sh file to run the program. For both Run file you will see the same window:

![working window](https://github.com/CQHofsns/Python_Project_Text_To_Image/blob/master/For%20README.md/working%20window.png)

4. After see "IMPORT SUCCESS" line, Congratulation !! My program has run correctly :satisfied: :satisfied: . Now lets get back and look for the "Complete Images" Folder , your image will be put in that. And if you want I have also created the "Pattern Images" Folder that store every single pattern images from every text block (<edit ???>???<@edit>) you have put in your text.

## Pros and Cons (Self Evaluation):
+Pros:
  1. Easy to convert text file to image with adjustable font color and background color .
  2. The text edit block is easy to edit.
  3. Supporting Vietnamese, English, Japanese, Korean, Chinese (both Traditional and Simplified are supproted).
 
+Cons:
  1. The edit block must be **kept in the same order** with format: **<edit c:???, b:???>**, even the **wrong space** will cause an error.
  2. Between 2 text block **must not have space** , if it had it will cause an error. :disappointed:	
  3. The Setup progress still not unified, may cause some uncomfortable for someone.
 
##   
