FILE = "./main.py"

def test_accept():
    assert 1==1

def test_hours():
    astval = False
    fh = open(FILE,'r',encoding='utf-8')
    content = fh.read().split('\n')
    for line in content:
        if line.startswith("hours"):
            if 'input' in line: astval = True
    assert astval

def test_rate():
    astval = False
    fh = open(FILE,'r',encoding='utf-8')
    content = fh.read().split('\n')
    for line in content:
        if line.startswith("rate"):
            if 'input' in line: astval = True
    assert astval

def test_calculate():
    astval = False
    fh = open(FILE,'r',encoding='utf-8')
    content = fh.read().split('\n')
    for line in content:
        if line.startswith("price"):
            if ( 'hours' in line ) and ('rate' in line) and ( '*' in line): astval = True
    assert astval==True

def test_price(monkeypatch):
    import io
    monkeypatch.setattr('sys.stdin', io.StringIO('35\n2.75'))
    from main import price
    assert price==96.25
