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
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
    bstack11111ll111_opy_,
    bstack111l1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from browserstack_sdk.sdk_cli.bstack11111l1l11_opy_ import bstack1111llll11_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
import weakref
class bstack1111lll1ll_opy_(bstack111ll1l111_opy_):
    bstack1111ll111l_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack111l1llll1_opy_]]
    def __init__(self, bstack1111ll111l_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.bstack11111l1ll1_opy_ = dict()
        self.bstack1111ll111l_opy_ = bstack1111ll111l_opy_
        self.frameworks = frameworks
        if any(bstack111l111ll1_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack111l111ll1_opy_.bstack111l1ll111_opy_(
                (bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.PRE), self.__11111ll1l1_opy_
            )
            bstack111l111ll1_opy_.bstack111l1ll111_opy_(
                (bstack111ll1ll11_opy_.QUIT, bstack111ll11111_opy_.POST), self.__11111l11l1_opy_
            )
    def __11111ll1l1_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, self.bstack1111ll111l_opy_, False):
            return
        if not f.bstack11111ll11l_opy_(f.hub_url(driver)):
            self.bstack11111l1ll1_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack11111ll111_opy_.bstack111l1ll11l_opy_(instance, self.bstack1111ll111l_opy_, True)
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨက") + str(instance.ref()) + bstack1l1_opy_ (u"ࠤࠥခ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack11111ll111_opy_.bstack111l1ll11l_opy_(instance, self.bstack1111ll111l_opy_, True)
        self.logger.debug(bstack1l1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧဂ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠦࠧဃ"))
    def __11111l11l1_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack11111l11ll_opy_(instance)
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡷࡵࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢင") + str(instance.ref()) + bstack1l1_opy_ (u"ࠨࠢစ"))
    def bstack11111lll1l_opy_(self, context: bstack1111llll11_opy_, reverse=True) -> List[Tuple[Callable, bstack111l1llll1_opy_]]:
        matches = []
        for data in self.drivers.values():
            if (
                bstack111l111ll1_opy_.bstack1111lllll1_opy_(data[1])
                and data[1].bstack11111l1l1l_opy_(context)
                and getattr(data[0](), bstack1l1_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦဆ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack11111l1lll_opy_, reverse=reverse)
    def bstack1111l11ll1_opy_(self, context: bstack1111llll11_opy_, reverse=True) -> List[Tuple[Callable, bstack111l1llll1_opy_]]:
        matches = []
        for data in self.bstack11111l1ll1_opy_.values():
            if (
                data[1].bstack11111l1l1l_opy_(context)
                and getattr(data[0](), bstack1l1_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧဇ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack11111l1lll_opy_, reverse=reverse)
    def bstack11111l111l_opy_(self, instance: bstack111l1llll1_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack11111l11ll_opy_(self, instance: bstack111l1llll1_opy_) -> bool:
        if self.bstack11111l111l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack11111ll111_opy_.bstack111l1ll11l_opy_(instance, self.bstack1111ll111l_opy_, False)
            return True
        return False