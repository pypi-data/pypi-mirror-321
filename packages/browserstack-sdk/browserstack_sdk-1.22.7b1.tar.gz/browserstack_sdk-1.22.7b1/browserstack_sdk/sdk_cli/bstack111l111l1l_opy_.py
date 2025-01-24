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
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack11111ll111_opy_,
    bstack111l1llll1_opy_,
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack111l111ll1_opy_(bstack11111ll111_opy_):
    bstack1l1ll1l1lll_opy_ = bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥዅ")
    NAME = bstack1l1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ዆")
    bstack1ll11l111ll_opy_ = bstack1l1_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨ዇")
    bstack1ll1l111l11_opy_ = bstack1l1_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨወ")
    bstack1l1lll111l1_opy_ = bstack1l1_opy_ (u"ࠢࡪࡰࡳࡹࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧዉ")
    bstack1ll111l1lll_opy_ = bstack1l1_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢዊ")
    bstack1ll11ll1l11_opy_ = bstack1l1_opy_ (u"ࠤ࡬ࡷࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡭ࡻࡢࠣዋ")
    bstack1l1ll1ll111_opy_ = bstack1l1_opy_ (u"ࠥࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢዌ")
    bstack1l1ll1llll1_opy_ = bstack1l1_opy_ (u"ࠦࡪࡴࡤࡦࡦࡢࡥࡹࠨው")
    bstack111l111l11_opy_ = bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨዎ")
    bstack111l1l111l_opy_ = bstack1l1_opy_ (u"ࠨ࡮ࡦࡹࡶࡩࡸࡹࡩࡰࡰࠥዏ")
    bstack1l1lll111ll_opy_ = bstack1l1_opy_ (u"ࠢࡨࡧࡷࠦዐ")
    bstack1ll11l11l1l_opy_ = bstack1l1_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧዑ")
    bstack1l1lll11111_opy_ = bstack1l1_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࠧዒ")
    bstack1l1ll1ll11l_opy_ = bstack1l1_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࡧࡳࡺࡰࡦࠦዓ")
    bstack1l1ll1lll11_opy_ = bstack1l1_opy_ (u"ࠦࡶࡻࡩࡵࠤዔ")
    bstack1l1llllllll_opy_: Dict[str, List[Callable]] = dict()
    bstack111l1lll1l_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack111l1l1lll_opy_: Any
    bstack1l1ll1lll1l_opy_: Dict
    def __init__(
        self,
        bstack111l1lll1l_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack111l1l1lll_opy_: Dict[str, Any],
        methods=[bstack1l1_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢዕ"), bstack1l1_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨዖ"), bstack1l1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣ዗"), bstack1l1_opy_ (u"ࠣࡳࡸ࡭ࡹࠨዘ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack111l1lll1l_opy_ = bstack111l1lll1l_opy_
        self.platform_index = platform_index
        self.bstack1l1lllll1ll_opy_(methods)
        self.bstack111l1l1lll_opy_ = bstack111l1l1lll_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack11111ll111_opy_.get_data(bstack111l111ll1_opy_.bstack1ll1l111l11_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack11111ll111_opy_.get_data(bstack111l111ll1_opy_.bstack1ll11l111ll_opy_, target, strict)
    @staticmethod
    def bstack1l1lll11l1l_opy_(target: object, strict=True):
        return bstack11111ll111_opy_.get_data(bstack111l111ll1_opy_.bstack1l1lll111l1_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack11111ll111_opy_.get_data(bstack111l111ll1_opy_.bstack1ll111l1lll_opy_, target, strict)
    @staticmethod
    def bstack1111lllll1_opy_(instance: bstack111l1llll1_opy_) -> bool:
        return bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack1ll11ll1l11_opy_, False)
    @staticmethod
    def bstack1ll1111ll1l_opy_(instance: bstack111l1llll1_opy_, default_value=None):
        return bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack1ll11l111ll_opy_, default_value)
    @staticmethod
    def bstack1ll111111ll_opy_(instance: bstack111l1llll1_opy_, default_value=None):
        return bstack11111ll111_opy_.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack1ll111l1lll_opy_, default_value)
    @staticmethod
    def bstack11111ll11l_opy_(hub_url: str, bstack1l1lll11l11_opy_=bstack1l1_opy_ (u"ࠤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨዙ")):
        try:
            bstack1l1ll1ll1ll_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack1l1ll1ll1ll_opy_.endswith(bstack1l1lll11l11_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1ll11l1l1l1_opy_(method_name: str):
        return method_name == bstack1l1_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦዚ")
    @staticmethod
    def bstack111l1lll11_opy_(method_name: str, *args):
        return (
            bstack111l111ll1_opy_.bstack1ll11l1l1l1_opy_(method_name)
            and bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args) == bstack111l111ll1_opy_.bstack111l1l111l_opy_
        )
    @staticmethod
    def bstack1ll111l1ll1_opy_(method_name: str, *args):
        if not bstack111l111ll1_opy_.bstack1ll11l1l1l1_opy_(method_name):
            return False
        if not bstack111l111ll1_opy_.bstack1l1lll11111_opy_ in bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args):
            return False
        bstack1lll1l1111l_opy_ = bstack111l111ll1_opy_.bstack1lll1l11lll_opy_(*args)
        return bstack1lll1l1111l_opy_ and bstack1l1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦዛ") in bstack1lll1l1111l_opy_ and bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨዜ") in bstack1lll1l1111l_opy_[bstack1l1_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨዝ")]
    @staticmethod
    def bstack1ll111ll11l_opy_(method_name: str, *args):
        if not bstack111l111ll1_opy_.bstack1ll11l1l1l1_opy_(method_name):
            return False
        if not bstack111l111ll1_opy_.bstack1l1lll11111_opy_ in bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args):
            return False
        bstack1lll1l1111l_opy_ = bstack111l111ll1_opy_.bstack1lll1l11lll_opy_(*args)
        return (
            bstack1lll1l1111l_opy_
            and bstack1l1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዞ") in bstack1lll1l1111l_opy_
            and bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸࡩࡲࡪࡲࡷࠦዟ") in bstack1lll1l1111l_opy_[bstack1l1_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤዠ")]
        )
    @staticmethod
    def bstack111ll1llll_opy_(*args):
        return str(bstack111l111ll1_opy_.bstack1lll1l11l1l_opy_(*args)).lower()
    @staticmethod
    def bstack1lll1l11l1l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1lll1l11lll_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1ll1ll11l1_opy_(driver):
        command_executor = getattr(driver, bstack1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨዡ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l1_opy_ (u"ࠦࡤࡻࡲ࡭ࠤዢ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l1_opy_ (u"ࠧࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬ࠨዣ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡥࡳࡦࡴࡹࡩࡷࡥࡡࡥࡦࡵࠦዤ"), None)
        return hub_url
    def bstack111ll1ll1l_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥዥ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦዦ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l1_opy_ (u"ࠤࡢࡹࡷࡲࠢዧ")):
                setattr(command_executor, bstack1l1_opy_ (u"ࠥࡣࡺࡸ࡬ࠣየ"), hub_url)
                result = True
        if result:
            self.bstack111l1lll1l_opy_ = hub_url
            bstack111l111ll1_opy_.bstack111l1ll11l_opy_(instance, bstack111l111ll1_opy_.bstack1ll11l111ll_opy_, hub_url)
            bstack111l111ll1_opy_.bstack111l1ll11l_opy_(
                instance, bstack111l111ll1_opy_.bstack1ll11ll1l11_opy_, bstack111l111ll1_opy_.bstack11111ll11l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1llllll1l_opy_(bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_]):
        return bstack1l1_opy_ (u"ࠦ࠿ࠨዩ").join((bstack111ll1ll11_opy_(bstack111ll111l1_opy_[0]).name, bstack111ll11111_opy_(bstack111ll111l1_opy_[1]).name))
    @staticmethod
    def bstack111l1ll111_opy_(bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_], callback: Callable):
        bstack1ll111111l1_opy_ = bstack111l111ll1_opy_.bstack1l1llllll1l_opy_(bstack111ll111l1_opy_)
        if not bstack1ll111111l1_opy_ in bstack111l111ll1_opy_.bstack1l1llllllll_opy_:
            bstack111l111ll1_opy_.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_] = []
        bstack111l111ll1_opy_.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_].append(callback)
    def bstack1l1lllll11l_opy_(self, instance: bstack111l1llll1_opy_, method_name: str, bstack1l1llll1ll1_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧዪ")):
            return
        cmd = args[0] if method_name == bstack1l1_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢያ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack1l1ll1ll1l1_opy_ = bstack1l1_opy_ (u"ࠢ࠻ࠤዬ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠤይ") + bstack1l1ll1ll1l1_opy_, bstack1l1llll1ll1_opy_)
    def bstack1l1llll1l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1111_opy_, bstack1l1ll1lllll_opy_ = bstack111ll111l1_opy_
        bstack1ll111111l1_opy_ = bstack111l111ll1_opy_.bstack1l1llllll1l_opy_(bstack111ll111l1_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠤࡲࡲࡤ࡮࡯ࡰ࡭࠽ࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤዮ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦዯ"))
        if bstack1l1llll1111_opy_ == bstack111ll1ll11_opy_.bstack111ll11l11_opy_:
            if bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.POST and not bstack111l111ll1_opy_.bstack1ll1l111l11_opy_ in instance.data:
                session_id = getattr(target, bstack1l1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣደ"), None)
                if session_id:
                    instance.data[bstack111l111ll1_opy_.bstack1ll1l111l11_opy_] = session_id
        elif (
            bstack1l1llll1111_opy_ == bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_
            and bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args) == bstack111l111ll1_opy_.bstack111l1l111l_opy_
        ):
            if bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.PRE:
                hub_url = bstack111l111ll1_opy_.bstack1ll1ll11l1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack111l111ll1_opy_.bstack1ll11l111ll_opy_: hub_url,
                            bstack111l111ll1_opy_.bstack1ll11ll1l11_opy_: bstack111l111ll1_opy_.bstack11111ll11l_opy_(hub_url),
                            bstack111l111ll1_opy_.bstack111l111l11_opy_: int(
                                os.environ.get(bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧዱ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1lll1l1111l_opy_ = bstack111l111ll1_opy_.bstack1lll1l11lll_opy_(*args)
                bstack1l1lll11l1l_opy_ = bstack1lll1l1111l_opy_.get(bstack1l1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧዲ"), None) if bstack1lll1l1111l_opy_ else None
                if isinstance(bstack1l1lll11l1l_opy_, dict):
                    instance.data[bstack111l111ll1_opy_.bstack1l1lll111l1_opy_] = copy.deepcopy(bstack1l1lll11l1l_opy_)
                    instance.data[bstack111l111ll1_opy_.bstack1ll111l1lll_opy_] = bstack1l1lll11l1l_opy_
            elif bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l1_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨዳ"), dict()).get(bstack1l1_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦዴ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack111l111ll1_opy_.bstack1ll1l111l11_opy_: framework_session_id,
                                bstack111l111ll1_opy_.bstack1l1ll1ll111_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1llll1111_opy_ == bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_
            and bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args) == bstack111l111ll1_opy_.bstack1l1ll1lll11_opy_
            and bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.POST
        ):
            instance.data[bstack111l111ll1_opy_.bstack1l1ll1llll1_opy_] = datetime.now(tz=timezone.utc)
        if bstack1ll111111l1_opy_ in bstack111l111ll1_opy_.bstack1l1llllllll_opy_:
            bstack1l1lll11ll1_opy_ = None
            for callback in bstack111l111ll1_opy_.bstack1l1llllllll_opy_[bstack1ll111111l1_opy_]:
                try:
                    bstack1l1lll1111l_opy_ = callback(self, target, exec, bstack111ll111l1_opy_, result, *args, **kwargs)
                    if bstack1l1lll11ll1_opy_ == None:
                        bstack1l1lll11ll1_opy_ = bstack1l1lll1111l_opy_
                except Exception as e:
                    self.logger.error(bstack1l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࠢድ") + str(e) + bstack1l1_opy_ (u"ࠥࠦዶ"))
                    traceback.print_exc()
            if bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.PRE and callable(bstack1l1lll11ll1_opy_):
                return bstack1l1lll11ll1_opy_
            elif bstack1l1ll1lllll_opy_ == bstack111ll11111_opy_.POST and bstack1l1lll11ll1_opy_:
                return bstack1l1lll11ll1_opy_
    def bstack1l1llll1l11_opy_(
        self, method_name, previous_state: bstack111ll1ll11_opy_, *args, **kwargs
    ) -> bstack111ll1ll11_opy_:
        if method_name == bstack1l1_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨዷ") or method_name == bstack1l1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧዸ"):
            return bstack111ll1ll11_opy_.bstack111ll11l11_opy_
        if method_name == bstack1l1_opy_ (u"ࠨࡱࡶ࡫ࡷࠦዹ"):
            return bstack111ll1ll11_opy_.QUIT
        if method_name == bstack1l1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣዺ"):
            if previous_state != bstack111ll1ll11_opy_.NONE:
                bstack1lll11lllll_opy_ = bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args)
                if bstack1lll11lllll_opy_ == bstack111l111ll1_opy_.bstack111l1l111l_opy_:
                    return bstack111ll1ll11_opy_.bstack111ll11l11_opy_
            return bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_
        return bstack111ll1ll11_opy_.NONE