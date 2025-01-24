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
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import threading
@dataclass
class bstack1l11l111ll_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11ll1111ll_opy_:
    pass
class Events:
    bstack1ll1lll1l1_opy_ = bstack1l1_opy_ (u"ࠧࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠣဋ")
    CONNECT = bstack1l1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢဌ")
    bstack1ll111l1l_opy_ = bstack1l1_opy_ (u"ࠢࡴࡪࡸࡸࡩࡵࡷ࡯ࠤဍ")
    CONFIG = bstack1l1_opy_ (u"ࠣࡥࡲࡲ࡫࡯ࡧࠣဎ")
    bstack1111111l11_opy_ = bstack1l1_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡸࠨဏ")
    bstack1l111llll_opy_ = bstack1l1_opy_ (u"ࠥࡩࡽ࡯ࡴࠣတ")
class bstack111111ll11_opy_:
    bstack111111l11l_opy_ = bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡷࡹࡧࡲࡵࡧࡧࠦထ")
    FINISHED = bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨဒ")
class bstack111111l1l1_opy_:
    bstack111111l11l_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡵࡷࡥࡷࡺࡥࡥࠤဓ")
    FINISHED = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦန")
class bstack111111l1ll_opy_:
    bstack111111l11l_opy_ = bstack1l1_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡶࡰࡢࡷࡹࡧࡲࡵࡧࡧࠦပ")
    FINISHED = bstack1l1_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨဖ")
class bstack1111111l1l_opy_:
    bstack111111l111_opy_ = bstack1l1_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤဗ")
class bstack1111111lll_opy_:
    _1111111ll1_opy_ = None
    def __new__(cls):
        if not cls._1111111ll1_opy_:
            cls._1111111ll1_opy_ = super(bstack1111111lll_opy_, cls).__new__(cls)
        return cls._1111111ll1_opy_
    def __init__(self):
        self._hooks = defaultdict(list)
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack1l1_opy_ (u"ࠦࡈࡧ࡬࡭ࡤࡤࡧࡰࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡨࡲࡶࠥࠨဘ") + event_name)
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠣࠦမ") + str(threading.get_ident()) + bstack1l1_opy_ (u"ࠨࠢယ"))
            self._hooks[event_name].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            callbacks = self._hooks.get(event_name, [])
            if not callbacks:
                return
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡤࡣ࡯ࡰࡧࡧࡣ࡬ࡵࠬࢁࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࠨရ") + str(event_name) + bstack1l1_opy_ (u"ࠣࠩࠥလ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1l1_opy_ (u"ࠤ࡬ࡲࡻࡵ࡫ࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࠥဝ") + str(threading.get_ident()) + bstack1l1_opy_ (u"ࠥࠦသ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪ࠾ࠥࠨဟ") + str(e) + bstack1l1_opy_ (u"ࠧࠨဠ"))
                    traceback.print_exc()
bstack1llll1l11l_opy_ = bstack1111111lll_opy_()