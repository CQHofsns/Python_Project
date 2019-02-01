echo Checking python version
python3 --version

if (( $? )); then
	echo Not found Python
else
	echo Checking done.
fi


echo Install required packages:
echo
echo Installing Pillow package:
echo
python3 -m pip install Pillow
if (( $? ));then
	echo Failed to install Pillow package.
	echo
else
	echo Pillow was installed successfully.
	echo
fi

echo
echo Installing Numpy package:
echo
python3 -m pip install numpy
if (( $? ));then
	echo Failed to install Numpy package.
	echo
else
	echo Numpy was installed successfully.
	echo
fi

echo
echo Installing ReGex package:
echo
python3 -m pip install regex
if (( $? ));then
	echo Failed to install ReGex package.
	echo
else
	echo ReGex was installed successfully.
	echo
fi

echo
echo Installing OpenCV-Python package:
echo
python3 -m pip install opencv-python
if (( $? ));then
	echo Failed to install OpenCV-Python package.
	echo
else
	echo OpenCV-Python was installed successfully.
	echo
fi

echo
echo Installing Font packages:

cd ..
cd $PWD/Font
xdg-open NotoSans-Black.ttf
xdg-open NotoSansCJKjp-Black.otf
xdg-open NotoSansCJKkr-Black.otf
xdg-open NotoSansCJKsc-Black.otf
xdg-open NotoSansCJKtc-Black.otf

cd ..
cd $PWD/Main
echo Generating Executable script
cat >Run.sh<<EOF
python3 source_Linux.py
read -p "Press Enter to continue"
EOF
chmod +x Run.sh


read -p "Press Enter to continute"
