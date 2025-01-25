import copy

USAGE = "$usage"

_g_funcs = {}
_g_paths = {}
_g_usages = {}
_g_logger = None


def register(itdef, path, func):
    name = itdef[USAGE]
    _g_usages[name] = itdef
    _g_funcs[name] = func
    _g_paths[name] = path


def load_wasm(wasm_path, page_num):
    from smwasm.wasm import load

    load.load_wasm(wasm_path, page_num)


def call(dt):
    usage = dt.get(USAGE)
    func = _g_funcs.get(usage)
    dtRet = func(dt)
    return dtRet


def info():
    ret = {"function": _g_paths}
    return ret


def log(text):
    if _g_logger:
        _g_logger.info(text)
    else:
        print(text)


def set_logger(logger):
    global _g_logger
    _g_logger = logger
