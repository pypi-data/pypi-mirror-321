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
    bstack111l1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack111l111l1l_opy_ import bstack111l111ll1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l1ll1ll_opy_ import bstack111ll1l111_opy_
import traceback
import os
import time
class bstack1lll1l111ll_opy_(bstack111ll1l111_opy_):
    bstack1lll11lll11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack111l111ll1_opy_.bstack111l1ll111_opy_((bstack111ll1ll11_opy_.bstack111ll1l1l1_opy_, bstack111ll11111_opy_.PRE), self.bstack111lll1111_opy_)
    def is_enabled(self) -> bool:
        return True
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
        hub_url = f.hub_url(driver)
        if f.bstack11111ll11l_opy_(hub_url):
            if not bstack1lll1l111ll_opy_.bstack1lll11lll11_opy_:
                self.logger.warning(bstack1l1_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࠡࡵࡨࡰ࡫࠳ࡨࡦࡣ࡯ࠤ࡫ࡲ࡯ࡸࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥႰ") + str(hub_url) + bstack1l1_opy_ (u"ࠥࠦႱ"))
                bstack1lll1l111ll_opy_.bstack1lll11lll11_opy_ = True
            return
        bstack1lll11lllll_opy_ = f.bstack1lll1l11l1l_opy_(*args)
        bstack1lll1l1111l_opy_ = f.bstack1lll1l11lll_opy_(*args)
        if bstack1lll11lllll_opy_ and bstack1lll11lllll_opy_.lower() == bstack1l1_opy_ (u"ࠦ࡫࡯࡮ࡥࡧ࡯ࡩࡲ࡫࡮ࡵࠤႲ") and bstack1lll1l1111l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1lll1l1111l_opy_.get(bstack1l1_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦႳ"), None), bstack1lll1l1111l_opy_.get(bstack1l1_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧႴ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l1_opy_ (u"ࠢࡼࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࡽ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡺࡹࡩ࡯ࡩࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡼࡡ࡭ࡷࡨࡁࠧႵ") + str(locator_value) + bstack1l1_opy_ (u"ࠣࠤႶ"))
                return
            def bstack1lll1l11111_opy_(driver, bstack1lll1l1l111_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1lll1l1l111_opy_(driver, *args, **kwargs)
                    response = self.bstack1lll1l11l11_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l1_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧႷ") + str(locator_value) + bstack1l1_opy_ (u"ࠥࠦႸ"))
                    else:
                        self.logger.warning(bstack1l1_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢႹ") + str(response) + bstack1l1_opy_ (u"ࠧࠨႺ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1lll11llll1_opy_(
                        driver, bstack1lll1l1l111_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1lll1l11111_opy_.__name__ = bstack1lll11lllll_opy_
            return bstack1lll1l11111_opy_
    def __1lll11llll1_opy_(
        self,
        driver,
        bstack1lll1l1l111_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1lll1l11l11_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡶࡵ࡭࡬࡭ࡥࡳࡧࡧ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨႻ") + str(locator_value) + bstack1l1_opy_ (u"ࠢࠣႼ"))
                bstack1lll1l11ll1_opy_ = self.bstack1lll11lll1l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡨࡦࡣ࡯࡭ࡳ࡭࡟ࡳࡧࡶࡹࡱࡺ࠽ࠣႽ") + str(bstack1lll1l11ll1_opy_) + bstack1l1_opy_ (u"ࠤࠥႾ"))
                if bstack1lll1l11ll1_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l1_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤႿ"): bstack1lll1l11ll1_opy_.locator_type,
                            bstack1l1_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥჀ"): bstack1lll1l11ll1_opy_.locator_value,
                        }
                    )
                    return bstack1lll1l1l111_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡏ࡟ࡅࡇࡅ࡙ࡌࠨჁ"), False):
                    self.logger.info(bstack1lll1l111l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠮࡯࡬ࡷࡸ࡯࡮ࡨ࠼ࠣࡷࡱ࡫ࡥࡱࠪ࠶࠴࠮ࠦ࡬ࡦࡶࡷ࡭ࡳ࡭ࠠࡺࡱࡸࠤ࡮ࡴࡳࡱࡧࡦࡸࠥࡺࡨࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠦ࡬ࡰࡩࡶࠦჂ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥჃ") + str(response) + bstack1l1_opy_ (u"ࠣࠤჄ"))
        except Exception as err:
            self.logger.warning(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨჅ") + str(err) + bstack1l1_opy_ (u"ࠥࠦ჆"))
        raise exception
    def bstack1lll1l11l11_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l1_opy_ (u"ࠦ࠵ࠨჇ"),
    ):
        self.bstack111l1lllll_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l1_opy_ (u"ࠧࠨ჈")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack111ll1l11l_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣ჉") + str(r) + bstack1l1_opy_ (u"ࠢࠣ჊"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ჋") + str(e) + bstack1l1_opy_ (u"ࠤࠥ჌"))
            traceback.print_exc()
            raise e
    def bstack1lll11lll1l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l1_opy_ (u"ࠥ࠴ࠧჍ")):
        self.bstack111l1lllll_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack111ll1l11l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨ჎") + str(r) + bstack1l1_opy_ (u"ࠧࠨ჏"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦა") + str(e) + bstack1l1_opy_ (u"ࠢࠣბ"))
            traceback.print_exc()
            raise e