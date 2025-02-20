


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
