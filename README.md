# Demonstration-python-compile

This repository contains example material used by MegaGiga ASBL for the demonstration of the packing relatively compiling of a python script into a single executable file (including all dependencies).

## Language file: megagiga.py

The python script that will be used to pack relatively compile.

## Python PACK instructions (pyinstaller)

    python -m venv venv
    source venv/bin/activate
    pip install pyinstaller
    
    pyinstaller --onefile megagiga.py
    
    deactivate
    cp dist/megagiga megagiga.bin1
    rm -r build
    rm -r dist
    rm -r venv
    rm megagiga.spec

## Python COMPILE instructions (nuitka)

    python -m venv venv
    source venv/bin/activate
    pip install nuitka
    
    nuitka --standalone megagiga.py
    
    deactivate
    cp megagiga.dist/megagiga.bin megagiga.bin2
    rm -r megagiga.build
    rm -r megagiga.dist
    rm -r venv

## Run script, packed and compiled

    python3 megagiga.py
    ./megagiga.bin1
    ./megagiga.bin2
