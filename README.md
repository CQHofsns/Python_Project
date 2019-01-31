# Python Project Text To Image
**_This is my very first post and project on GitHub Community._**	

## Summary:
Python_Project_Text_To_Image is a program that convert the content that you wrote on text file (.txt) into image format (.bmp, .png, .jpg). Not only just convert text, you can adjust font color and background right in your text, like this:

> <edit c:"**_font color here_**", b:"**_background color here_**">"**_Text content here_**"<@edit>

For example, I have put a example text in Text Folder. And here is its content: 

> <edit: c=red, b=white>My na<@edit><edit: c=yellow, b=blue>me is <@edit><edit: c=black, b=yellow>Chu Quang Huy<@edit>

And here is the result:

![example](https://github.com/CQHofsns/Python_Project_Text_To_Image/blob/master/For%20README.md/result.png)

**WARNING: My program currently just can convert 1 line text file, which mean 2 line above text file will not work !! (Sorry I still working on it  :sweat: )**

## How to run this program:
**Note: _Before running this program, make sure you have Python ver3 in your computer, or a Python IDE (such as Pycharm,..). Also, this 4 packages have been installed: `Pillow`, `opencv-python`, `regex` and `numpy`_.**

1. Open `Font` Folder and install all fonts.
2. Make a text (.txt) file with above format and save it with **UTF-8 charater code**.
3. Open `source` folder which contain 2 file: `source.py` and `source.pyc`: While the `source.py` is used for running on Command Line, the `source.pyc` is used for running on Python Virtual Machine.
4. For both source file you will see the same window:


