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
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack111l11l1l1_opy_ import (
    bstack111ll1ll11_opy_,
    bstack111ll11111_opy_,
    bstack111l1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll11lll1_opy_
import threading
import os
class bstack111l1l1111_opy_(bstack111ll1l111_opy_):
    bstack111l1111ll_opy_ = bstack1l1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢྏ")
    bstack111l11llll_opy_ = bstack1l1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤྐ")
    bstack111l11l1ll_opy_ = bstack1l1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤྑ")
    def __init__(self):
        super().__init__()
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll11l11_opy_, bstack111ll11111_opy_.PRE), self.bstack111l11l111_opy_)
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.PRE), self.bstack111lll1111_opy_)
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.POST), self.bstack111ll11l1l_opy_)
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.QUIT, bstack111ll11111_opy_.POST), self.bstack111lll1l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack111l11l111_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧྒ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            self.bstack111l1l11ll_opy_(instance, f, kwargs)
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡦ࠯ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿ࠽ࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥྒྷ") + str(kwargs) + bstack1l1_opy_ (u"ࠧࠨྔ"))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack111lll1111_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.bstack111l11ll11_opy_(instance, bstack111l1l1111_opy_.bstack111l1111ll_opy_, False):
            return
        if not f.bstack111lll1l1l_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_):
            return
        platform_index = f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_)
        if f.bstack111l1lll11_opy_(method_name, *args) and len(args) > 1:
            bstack11l1l1ll11_opy_ = datetime.now()
            hub_url = bstack111l111ll1_opy_.hub_url(driver)
            self.logger.warning(bstack1l1_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣྕ") + str(hub_url) + bstack1l1_opy_ (u"ࠢࠣྖ"))
            bstack111l11lll1_opy_ = args[1][bstack1l1_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢྗ")] if isinstance(args[1], dict) and bstack1l1_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣ྘") in args[1] else None
            bstack111l111lll_opy_ = bstack1l1_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣྙ")
            if isinstance(bstack111l11lll1_opy_, dict):
                bstack11l1l1ll11_opy_ = datetime.now()
                r = self.bstack111l1l1l1l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤྚ"), datetime.now() - bstack11l1l1ll11_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢྛ") + str(r) + bstack1l1_opy_ (u"ࠨࠢྜ"))
                        return
                    if r.hub_url:
                        f.bstack111ll1ll1l_opy_(instance, driver, r.hub_url)
                        f.bstack111l1ll11l_opy_(instance, bstack111l1l1111_opy_.bstack111l1111ll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨྜྷ"), e)
    def bstack111ll11l1l_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack111l11ll11_opy_(instance, bstack111l1l1111_opy_.bstack111l11llll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack111l111ll1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧྞ") + str(hub_url) + bstack1l1_opy_ (u"ࠤࠥྟ"))
            return
        framework_session_id = bstack111l111ll1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨྠ") + str(framework_session_id) + bstack1l1_opy_ (u"ࠦࠧྡ"))
            return
        if bstack111l111ll1_opy_.bstack111ll1llll_opy_(*args) == bstack111l111ll1_opy_.bstack111l1l111l_opy_:
            bstack11l1l1ll11_opy_ = datetime.now()
            r = self.bstack111lll11l1_opy_(
                ref,
                f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷࠦྡྷ"), datetime.now() - bstack11l1l1ll11_opy_)
            f.bstack111l1ll11l_opy_(instance, bstack111l1l1111_opy_.bstack111l11llll_opy_, r.success)
    def bstack111lll1l11_opy_(
        self,
        f: bstack111l111ll1_opy_,
        driver: object,
        exec: Tuple[bstack111l1llll1_opy_, str],
        bstack111ll111l1_opy_: Tuple[bstack111ll1ll11_opy_, bstack111ll11111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack111l11ll11_opy_(instance, bstack111l1l1111_opy_.bstack111l11l1ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack111l111ll1_opy_.session_id(driver)
        hub_url = bstack111l111ll1_opy_.hub_url(driver)
        bstack11l1l1ll11_opy_ = datetime.now()
        r = self.bstack111ll111ll_opy_(
            ref,
            f.bstack111l11ll11_opy_(instance, bstack111l111ll1_opy_.bstack111l111l11_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11l1ll11ll_opy_(bstack1l1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳࠦྣ"), datetime.now() - bstack11l1l1ll11_opy_)
        f.bstack111l1ll11l_opy_(instance, bstack111l1l1111_opy_.bstack111l11l1ll_opy_, r.success)
    def bstack111ll1111l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡺࡩࡧࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧྤ") + str(req) + bstack1l1_opy_ (u"ࠣࠤྥ"))
        try:
            r = self.bstack111ll1l11l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧྦ") + str(r.success) + bstack1l1_opy_ (u"ࠥࠦྦྷ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤྨ") + str(e) + bstack1l1_opy_ (u"ࠧࠨྩ"))
            traceback.print_exc()
            raise e
    def bstack111l1l1l1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack111l1lllll_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣྪ") + str(req) + bstack1l1_opy_ (u"ࠢࠣྫ"))
        try:
            r = self.bstack111ll1l11l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦྫྷ") + str(r.success) + bstack1l1_opy_ (u"ࠤࠥྭ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣྮ") + str(e) + bstack1l1_opy_ (u"ࠦࠧྯ"))
            traceback.print_exc()
            raise e
    def bstack111lll11l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack111l1lllll_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࡀࠠࠣྰ") + str(req) + bstack1l1_opy_ (u"ࠨࠢྱ"))
        try:
            r = self.bstack111ll1l11l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤྲ") + str(r) + bstack1l1_opy_ (u"ࠣࠤླ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢྴ") + str(e) + bstack1l1_opy_ (u"ࠥࠦྵ"))
            traceback.print_exc()
            raise e
    def bstack111ll111ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack111l1lllll_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳ࠾ࠥࠨྶ") + str(req) + bstack1l1_opy_ (u"ࠧࠨྷ"))
        try:
            r = self.bstack111ll1l11l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣྸ") + str(r) + bstack1l1_opy_ (u"ࠢࠣྐྵ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨྺ") + str(e) + bstack1l1_opy_ (u"ࠤࠥྻ"))
            traceback.print_exc()
            raise e
    def bstack111l1l11ll_opy_(self, instance: bstack111l1llll1_opy_, f: bstack111l111ll1_opy_, kwargs):
        bstack111ll1lll1_opy_ = version.parse(f.framework_version)
        bstack111ll1l1ll_opy_ = kwargs.get(bstack1l1_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦྼ"))
        bstack111l1l11l1_opy_ = kwargs.get(bstack1l1_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦ྽"))
        bstack111l1l1l11_opy_ = {}
        bstack111l11l11l_opy_ = {}
        bstack111l11ll1l_opy_ = None
        bstack111ll11ll1_opy_ = {}
        if bstack111l1l11l1_opy_ is not None or bstack111ll1l1ll_opy_ is not None: # check top level caps
            if bstack111l1l11l1_opy_ is not None:
                bstack111ll11ll1_opy_[bstack1l1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ྾")] = bstack111l1l11l1_opy_
            if bstack111ll1l1ll_opy_ is not None and callable(getattr(bstack111ll1l1ll_opy_, bstack1l1_opy_ (u"ࠨࡴࡰࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣ྿"))):
                bstack111ll11ll1_opy_[bstack1l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࡠࡣࡶࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ࿀")] = bstack111ll1l1ll_opy_.to_capabilities()
        response = self.bstack111ll1111l_opy_(f.platform_index, instance.ref(), json.dumps(bstack111ll11ll1_opy_).encode(bstack1l1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ࿁")))
        if response is not None and response.capabilities:
            bstack111l1l1l11_opy_ = json.loads(response.capabilities.decode(bstack1l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣ࿂")))
            if not bstack111l1l1l11_opy_: # empty caps bstack111lll11ll_opy_ bstack111l1ll1l1_opy_ bstack111ll11lll_opy_ bstack111lll111l_opy_ or error in processing
                return
            bstack111l11ll1l_opy_ = f.bstack111l1l1lll_opy_[bstack1l1_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡢࡳࡵࡺࡩࡰࡰࡶࡣ࡫ࡸ࡯࡮ࡡࡦࡥࡵࡹࠢ࿃")](bstack111l1l1l11_opy_)
        if bstack111ll1l1ll_opy_ is not None and bstack111ll1lll1_opy_ >= version.parse(bstack1l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ࿄")):
            bstack111l11l11l_opy_ = None
        if (
                not bstack111ll1l1ll_opy_ and not bstack111l1l11l1_opy_
        ) or (
                bstack111ll1lll1_opy_ < version.parse(bstack1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ࿅"))
        ):
            bstack111l11l11l_opy_ = {}
            bstack111l11l11l_opy_.update(bstack111l1l1l11_opy_)
        self.logger.info(bstack1ll11lll1_opy_)
        if os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠤ࿆")).lower().__eq__(bstack1l1_opy_ (u"ࠢࡵࡴࡸࡩࠧ࿇")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦ࿈"): f.bstack111l1lll1l_opy_,
                }
            )
        if bstack111ll1lll1_opy_ >= version.parse(bstack1l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ࿉")):
            if bstack111l1l11l1_opy_ is not None:
                del kwargs[bstack1l1_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ࿊")]
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧ࿋"): bstack111l11ll1l_opy_,
                    bstack1l1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤ࿌"): True,
                    bstack1l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨ࿍"): None,
                }
            )
        elif bstack111ll1lll1_opy_ >= version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭࿎")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣ࿏"): bstack111l11l11l_opy_,
                    bstack1l1_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥ࿐"): bstack111l11ll1l_opy_,
                    bstack1l1_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢ࿑"): True,
                    bstack1l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦ࿒"): None,
                }
            )
        elif bstack111ll1lll1_opy_ >= version.parse(bstack1l1_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ࿓")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨ࿔"): bstack111l11l11l_opy_,
                    bstack1l1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦ࿕"): True,
                    bstack1l1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣ࿖"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤ࿗"): bstack111l11l11l_opy_,
                    bstack1l1_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢ࿘"): True,
                    bstack1l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦ࿙"): None,
                }
            )