# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack11111l1_opy_ = 2048
bstack11l1lll_opy_ = 7
def bstack1l1_opy_ (bstack111l_opy_):
    global bstack11ll1_opy_
    bstack1111ll1_opy_ = ord (bstack111l_opy_ [-1])
    bstack11l11ll_opy_ = bstack111l_opy_ [:-1]
    bstack111lll_opy_ = bstack1111ll1_opy_ % len (bstack11l11ll_opy_)
    bstack1l111l_opy_ = bstack11l11ll_opy_ [:bstack111lll_opy_] + bstack11l11ll_opy_ [bstack111lll_opy_:]
    if bstack1llll11_opy_:
        bstack11l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l1_opy_ - (bstack11lllll_opy_ + bstack1111ll1_opy_) % bstack11l1lll_opy_) for bstack11lllll_opy_, char in enumerate (bstack1l111l_opy_)])
    else:
        bstack11l1_opy_ = str () .join ([chr (ord (char) - bstack11111l1_opy_ - (bstack11lllll_opy_ + bstack1111ll1_opy_) % bstack11l1lll_opy_) for bstack11lllll_opy_, char in enumerate (bstack1l111l_opy_)])
    return eval (bstack11l1_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l1ll111lll_opy_
bstack111l11ll_opy_ = Config.bstack11l111ll_opy_()
def bstack1l1ll111ll1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1l1ll11ll1l_opy_(bstack1l1ll11l111_opy_, bstack1l1ll11ll11_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1l1ll11l111_opy_):
        with open(bstack1l1ll11l111_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1l1ll111ll1_opy_(bstack1l1ll11l111_opy_):
        pac = get_pac(url=bstack1l1ll11l111_opy_)
    else:
        raise Exception(bstack1l1_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫᎦ").format(bstack1l1ll11l111_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l1_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨᎧ"), 80))
        bstack1l1ll11l11l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1l1ll11l11l_opy_ = bstack1l1_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧᎨ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1l1ll11ll11_opy_, bstack1l1ll11l11l_opy_)
    return proxy_url
def bstack11l11l11ll_opy_(config):
    return bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᎩ") in config or bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᎪ") in config
def bstack1l1ll11lll_opy_(config):
    if not bstack11l11l11ll_opy_(config):
        return
    if config.get(bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᎫ")):
        return config.get(bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ꭼ"))
    if config.get(bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᎭ")):
        return config.get(bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᎮ"))
def bstack1lll1l1lll_opy_(config, bstack1l1ll11ll11_opy_):
    proxy = bstack1l1ll11lll_opy_(config)
    proxies = {}
    if config.get(bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᎯ")) or config.get(bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᎰ")):
        if proxy.endswith(bstack1l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭Ꮁ")):
            proxies = bstack1ll1111l1l_opy_(proxy, bstack1l1ll11ll11_opy_)
        else:
            proxies = {
                bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᎲ"): proxy
            }
    bstack111l11ll_opy_.set_property(bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᎳ"), proxies)
    return proxies
def bstack1ll1111l1l_opy_(bstack1l1ll11l111_opy_, bstack1l1ll11ll11_opy_):
    proxies = {}
    global bstack1l1ll11l1l1_opy_
    if bstack1l1_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᎴ") in globals():
        return bstack1l1ll11l1l1_opy_
    try:
        proxy = bstack1l1ll11ll1l_opy_(bstack1l1ll11l111_opy_, bstack1l1ll11ll11_opy_)
        if bstack1l1_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᎵ") in proxy:
            proxies = {}
        elif bstack1l1_opy_ (u"ࠨࡈࡕࡖࡓࠦᎶ") in proxy or bstack1l1_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᎷ") in proxy or bstack1l1_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᎸ") in proxy:
            bstack1l1ll11l1ll_opy_ = proxy.split(bstack1l1_opy_ (u"ࠤࠣࠦᎹ"))
            if bstack1l1_opy_ (u"ࠥ࠾࠴࠵ࠢᎺ") in bstack1l1_opy_ (u"ࠦࠧᎻ").join(bstack1l1ll11l1ll_opy_[1:]):
                proxies = {
                    bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᎼ"): bstack1l1_opy_ (u"ࠨࠢᎽ").join(bstack1l1ll11l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭Ꮎ"): str(bstack1l1ll11l1ll_opy_[0]).lower() + bstack1l1_opy_ (u"ࠣ࠼࠲࠳ࠧᎿ") + bstack1l1_opy_ (u"ࠤࠥᏀ").join(bstack1l1ll11l1ll_opy_[1:])
                }
        elif bstack1l1_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᏁ") in proxy:
            bstack1l1ll11l1ll_opy_ = proxy.split(bstack1l1_opy_ (u"ࠦࠥࠨᏂ"))
            if bstack1l1_opy_ (u"ࠧࡀ࠯࠰ࠤᏃ") in bstack1l1_opy_ (u"ࠨࠢᏄ").join(bstack1l1ll11l1ll_opy_[1:]):
                proxies = {
                    bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭Ꮕ"): bstack1l1_opy_ (u"ࠣࠤᏆ").join(bstack1l1ll11l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᏇ"): bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᏈ") + bstack1l1_opy_ (u"ࠦࠧᏉ").join(bstack1l1ll11l1ll_opy_[1:])
                }
        else:
            proxies = {
                bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᏊ"): proxy
            }
    except Exception as e:
        print(bstack1l1_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᏋ"), bstack1l1ll111lll_opy_.format(bstack1l1ll11l111_opy_, str(e)))
    bstack1l1ll11l1l1_opy_ = proxies
    return proxies