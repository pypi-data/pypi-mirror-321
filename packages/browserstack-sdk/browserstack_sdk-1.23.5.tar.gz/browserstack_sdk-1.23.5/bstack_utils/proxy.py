# coding: UTF-8
import sys
bstack11lllll_opy_ = sys.version_info [0] == 2
bstack1l1l1_opy_ = 2048
bstack11ll11_opy_ = 7
def bstack11111_opy_ (bstack11l1lll_opy_):
    global bstack11l1l11_opy_
    bstack1ll1ll_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lllll1l_opy_ = bstack11l1lll_opy_ [:-1]
    bstack1l11_opy_ = bstack1ll1ll_opy_ % len (bstack1lllll1l_opy_)
    bstack1lllll1_opy_ = bstack1lllll1l_opy_ [:bstack1l11_opy_] + bstack1lllll1l_opy_ [bstack1l11_opy_:]
    if bstack11lllll_opy_:
        bstack11lll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    else:
        bstack11lll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1_opy_ - (bstack11111l_opy_ + bstack1ll1ll_opy_) % bstack11ll11_opy_) for bstack11111l_opy_, char in enumerate (bstack1lllll1_opy_)])
    return eval (bstack11lll1l_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l1ll111_opy_
bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
def bstack1ll1l1111ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1ll1l111l1l_opy_(bstack1ll1l111lll_opy_, bstack1ll1l111ll1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1ll1l111lll_opy_):
        with open(bstack1ll1l111lll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1ll1l1111ll_opy_(bstack1ll1l111lll_opy_):
        pac = get_pac(url=bstack1ll1l111lll_opy_)
    else:
        raise Exception(bstack11111_opy_ (u"ࠧࡑࡣࡦࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠧᚈ").format(bstack1ll1l111lll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11111_opy_ (u"ࠣ࠺࠱࠼࠳࠾࠮࠹ࠤᚉ"), 80))
        bstack1ll1l111l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1ll1l111l11_opy_ = bstack11111_opy_ (u"ࠩ࠳࠲࠵࠴࠰࠯࠲ࠪᚊ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1ll1l111ll1_opy_, bstack1ll1l111l11_opy_)
    return proxy_url
def bstack1lll11ll11_opy_(config):
    return bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᚋ") in config or bstack11111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᚌ") in config
def bstack1llll111ll_opy_(config):
    if not bstack1lll11ll11_opy_(config):
        return
    if config.get(bstack11111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᚍ")):
        return config.get(bstack11111_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᚎ"))
    if config.get(bstack11111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᚏ")):
        return config.get(bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᚐ"))
def bstack1llll1llll_opy_(config, bstack1ll1l111ll1_opy_):
    proxy = bstack1llll111ll_opy_(config)
    proxies = {}
    if config.get(bstack11111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᚑ")) or config.get(bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᚒ")):
        if proxy.endswith(bstack11111_opy_ (u"ࠫ࠳ࡶࡡࡤࠩᚓ")):
            proxies = bstack11ll11l1ll_opy_(proxy, bstack1ll1l111ll1_opy_)
        else:
            proxies = {
                bstack11111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᚔ"): proxy
            }
    bstack1llllll1l1_opy_.bstack1l1111llll_opy_(bstack11111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ᚕ"), proxies)
    return proxies
def bstack11ll11l1ll_opy_(bstack1ll1l111lll_opy_, bstack1ll1l111ll1_opy_):
    proxies = {}
    global bstack1ll1l11l11l_opy_
    if bstack11111_opy_ (u"ࠧࡑࡃࡆࡣࡕࡘࡏ࡙࡛ࠪᚖ") in globals():
        return bstack1ll1l11l11l_opy_
    try:
        proxy = bstack1ll1l111l1l_opy_(bstack1ll1l111lll_opy_, bstack1ll1l111ll1_opy_)
        if bstack11111_opy_ (u"ࠣࡆࡌࡖࡊࡉࡔࠣᚗ") in proxy:
            proxies = {}
        elif bstack11111_opy_ (u"ࠤࡋࡘ࡙ࡖࠢᚘ") in proxy or bstack11111_opy_ (u"ࠥࡌ࡙࡚ࡐࡔࠤᚙ") in proxy or bstack11111_opy_ (u"ࠦࡘࡕࡃࡌࡕࠥᚚ") in proxy:
            bstack1ll1l11l111_opy_ = proxy.split(bstack11111_opy_ (u"ࠧࠦࠢ᚛"))
            if bstack11111_opy_ (u"ࠨ࠺࠰࠱ࠥ᚜") in bstack11111_opy_ (u"ࠢࠣ᚝").join(bstack1ll1l11l111_opy_[1:]):
                proxies = {
                    bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧ᚞"): bstack11111_opy_ (u"ࠤࠥ᚟").join(bstack1ll1l11l111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᚠ"): str(bstack1ll1l11l111_opy_[0]).lower() + bstack11111_opy_ (u"ࠦ࠿࠵࠯ࠣᚡ") + bstack11111_opy_ (u"ࠧࠨᚢ").join(bstack1ll1l11l111_opy_[1:])
                }
        elif bstack11111_opy_ (u"ࠨࡐࡓࡑ࡛࡝ࠧᚣ") in proxy:
            bstack1ll1l11l111_opy_ = proxy.split(bstack11111_opy_ (u"ࠢࠡࠤᚤ"))
            if bstack11111_opy_ (u"ࠣ࠼࠲࠳ࠧᚥ") in bstack11111_opy_ (u"ࠤࠥᚦ").join(bstack1ll1l11l111_opy_[1:]):
                proxies = {
                    bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᚧ"): bstack11111_opy_ (u"ࠦࠧᚨ").join(bstack1ll1l11l111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᚩ"): bstack11111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᚪ") + bstack11111_opy_ (u"ࠢࠣᚫ").join(bstack1ll1l11l111_opy_[1:])
                }
        else:
            proxies = {
                bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᚬ"): proxy
            }
    except Exception as e:
        print(bstack11111_opy_ (u"ࠤࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨᚭ"), bstack111l1ll111_opy_.format(bstack1ll1l111lll_opy_, str(e)))
    bstack1ll1l11l11l_opy_ = proxies
    return proxies