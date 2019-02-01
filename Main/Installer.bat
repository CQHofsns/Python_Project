@echo off
cd ..
cd "%cd%\Font"

start NotoSans-Black.ttf
start NotoSansCJKjp-Black.otf
start NotoSansCJKkr-Black.otf
start NotoSansCJKsc-Black.otf
start NotoSansCJKtc-Black.otf

cd ..
cd "%cd%\source"

@echo python %cd%\source.py > Start-Program.bat
@echo pause >> Start-Program.bat

exit