from src.commonutils  import Execmd
grep=lambda keyword,file: Execmd("grep " + keyword + " " + file ).get(raiseError=False)


def pipe(*fs):
    if not fs: return None
    return fs[-1](pipe(fs[:-1]))





