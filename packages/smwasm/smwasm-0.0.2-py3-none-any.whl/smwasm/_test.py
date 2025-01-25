import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
print("--- current directory --- ", current_dir)
sys.path.append(os.path.join(current_dir, ".."))


import smh
import smu

# ------------------------------------------------------------

SM_DOMAIN = "test"


def _sm_get_text(dt):
    ret = {"text": dt["text"] + "--abc123"}
    return ret


def book():
    itdef_get_text = {"$usage": SM_DOMAIN + ".get.text", "text": ""}
    smh.register(itdef_get_text, "", _sm_get_text)

# ------------------------------------------------------------


def test():
    current = smu.current()
    print("--- start --- {0} ---".format(current))
    smh.log("--- log something ---")

    dt = smh.call({"$usage": "test.get.text", "text": "abc"})
    print("--- {0} ---".format(dt))


if __name__ == "__main__":

    book()
    test()
