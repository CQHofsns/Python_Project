@echo off

echo Checking Python version:
python --version
if errorlevel 1 echo Python is not found.

echo(
echo Install required packages:

echo(
echo Installing "Pillow" package:
python -m pip install Pillow
if errorlevel 1 (
	echo Failed to install numpy package.
	pause)else echo Install successfully !

echo(
echo Installing "ReGex" package:
python -m pip install regex
if errorlevel 1 (
	echo Failed to install numpy package.
	pause)else echo Install successfully !

echo(
echo Installing "Numpy" package:
python -m pip install numpy
if errorlevel 1 (
	echo Failed to install numpy package.
	pause)else echo Install successfully !

echo(
echo Installing "Opencv-python" package:
python -m pip install opencv-python
if errorlevel 1 (
	echo Failed to install numpy package.
	pause)else echo Install successfully !

cd ..
cd "%cd%\Font"

start NotoSans-Black.ttf
start NotoSansCJKjp-Black.otf
start NotoSansCJKkr-Black.otf
start NotoSansCJKsc-Black.otf
start NotoSansCJKtc-Black.otf

cd ..
cd "%cd%\Main"

@echo python %cd%\source.py > Run.bat
@echo echo %cd% >> Run.bat
@echo pause >> Run.bat

exit