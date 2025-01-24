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
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1ll1ll1lll_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11ll111l1l_opy_, bstack1l1llll1ll_opy_, update, bstack111lll11_opy_,
                                       bstack1lll1l1l11_opy_, bstack1ll1l1111l_opy_, bstack1l11ll1lll_opy_, bstack1l11111lll_opy_,
                                       bstack1ll1l1l1l1_opy_, bstack1llll11lll_opy_, bstack1lll11111l_opy_, bstack111l1l1l1_opy_,
                                       bstack1lllll11_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11ll11l1_opy_)
from browserstack_sdk.bstack1l1llll111_opy_ import bstack1l111ll11_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11l1l11ll_opy_
from bstack_utils.capture import bstack11l1ll111l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1l1llll11_opy_, bstack1lll1ll11_opy_, bstack1ll111lll1_opy_, \
    bstack1ll1lll1_opy_
from bstack_utils.helper import bstack1l11lll1ll_opy_, bstack1llll11llll_opy_, bstack11l11l1ll1_opy_, bstack11l11l111_opy_, bstack1llll1l1111_opy_, bstack1l1l11lll_opy_, \
    bstack1lll11l11ll_opy_, \
    bstack1llll1111ll_opy_, bstack11ll1l1l1_opy_, bstack1llll1l11_opy_, bstack1lll1l111l1_opy_, bstack1ll1l1l1ll_opy_, Notset, \
    bstack1lll11l1ll_opy_, bstack1lll1ll1lll_opy_, bstack1llll111l1l_opy_, Result, bstack1lll1111lll_opy_, bstack1llll111l11_opy_, bstack11l11ll11l_opy_, \
    bstack1ll11lll1l_opy_, bstack1l1l1111l_opy_, bstack1llll1lll1_opy_, bstack1lll111lll1_opy_
from bstack_utils.bstack1ll1lllll11_opy_ import bstack1ll1lll11ll_opy_
from bstack_utils.messages import bstack1l111111ll_opy_, bstack11111ll11_opy_, bstack1lll1l1ll1_opy_, bstack1l1l11l11l_opy_, bstack1ll1l111l_opy_, \
    bstack1l1111l1ll_opy_, bstack1ll1l111_opy_, bstack11ll1llll_opy_, bstack1l111lll11_opy_, bstack111llll1_opy_, \
    bstack11ll11l1l_opy_, bstack1llll1l111_opy_
from bstack_utils.proxy import bstack1llll111ll_opy_, bstack11ll11l1ll_opy_
from bstack_utils.bstack1l1l11l11_opy_ import bstack1ll11lll11l_opy_, bstack1ll1l11111l_opy_, bstack1ll11llll1l_opy_, bstack1ll11llllll_opy_, \
    bstack1ll11lll1l1_opy_, bstack1ll11lllll1_opy_, bstack1ll11lll111_opy_, bstack1llll1ll11_opy_, bstack1ll11lll1ll_opy_
from bstack_utils.bstack1l11l1l11_opy_ import bstack1l1lll111_opy_
from bstack_utils.bstack1ll11l1lll_opy_ import bstack1ll1l1llll_opy_, bstack1l1l1lllll_opy_, bstack1lll1ll11l_opy_, \
    bstack1ll11l1111_opy_, bstack11llll11ll_opy_
from bstack_utils.bstack11l1l11ll1_opy_ import bstack11l1l1l1ll_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack1l1l11l1l1_opy_
import bstack_utils.bstack111ll1111l_opy_ as bstack1l1lll1l1_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack1lll11llll_opy_
from bstack_utils.bstack1l11l1lll1_opy_ import bstack1l11l1lll1_opy_
from browserstack_sdk.__init__ import bstack1lllll111_opy_
bstack11ll11ll1l_opy_ = None
bstack1l11lllll1_opy_ = None
bstack1111ll1l1_opy_ = None
bstack11lllll1l1_opy_ = None
bstack1l11l1ll1_opy_ = None
bstack1l111l11l1_opy_ = None
bstack11lllll11_opy_ = None
bstack1lllll111l_opy_ = None
bstack1lllll1lll_opy_ = None
bstack11l1lll1l_opy_ = None
bstack1l11ll1l1l_opy_ = None
bstack11llll11l_opy_ = None
bstack1lllllll1l_opy_ = None
bstack1ll111l1l1_opy_ = bstack11111_opy_ (u"ࠫࠬ᢮")
CONFIG = {}
bstack1lll111111_opy_ = False
bstack1l1111lll_opy_ = bstack11111_opy_ (u"ࠬ࠭᢯")
bstack1ll1l1ll_opy_ = bstack11111_opy_ (u"࠭ࠧᢰ")
bstack1l1l11ll_opy_ = False
bstack1ll1lll11l_opy_ = []
bstack11ll1l1ll1_opy_ = bstack1l1llll11_opy_
bstack1l1ll1ll1ll_opy_ = bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᢱ")
bstack1l1lllllll_opy_ = {}
bstack1l1lllll11_opy_ = None
bstack11l1111ll_opy_ = False
logger = bstack11l1l11ll_opy_.get_logger(__name__, bstack11ll1l1ll1_opy_)
store = {
    bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᢲ"): []
}
bstack1l1ll11ll1l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11l11l1111_opy_ = {}
current_test_uuid = None
def bstack1llll11ll1_opy_(page, bstack1l1ll1l111_opy_):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᢳ"),
                      bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧᢴ") + json.dumps(
                          bstack1l1ll1l111_opy_) + bstack11111_opy_ (u"ࠦࢂࢃࠢᢵ"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥᢶ"), e)
def bstack1ll11l11_opy_(page, message, level):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᢷ"), bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬᢸ") + json.dumps(
            message) + bstack11111_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫᢹ") + json.dumps(level) + bstack11111_opy_ (u"ࠩࢀࢁࠬᢺ"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨᢻ"), e)
def pytest_configure(config):
    bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
    config.args = bstack1l1l11l1l1_opy_.bstack1l1lll11111_opy_(config.args)
    bstack1llllll1l1_opy_.bstack11111l1ll_opy_(bstack1llll1lll1_opy_(config.getoption(bstack11111_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᢼ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1l1ll11llll_opy_ = item.config.getoption(bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᢽ"))
    plugins = item.config.getoption(bstack11111_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢᢾ"))
    report = outcome.get_result()
    bstack1l1ll1l1ll1_opy_(item, call, report)
    if bstack11111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧᢿ") not in plugins or bstack1ll1l1l1ll_opy_():
        return
    summary = []
    driver = getattr(item, bstack11111_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤᣀ"), None)
    page = getattr(item, bstack11111_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣᣁ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1l1ll11l11l_opy_(item, report, summary, bstack1l1ll11llll_opy_)
    if (page is not None):
        bstack1l1ll1lll11_opy_(item, report, summary, bstack1l1ll11llll_opy_)
def bstack1l1ll11l11l_opy_(item, report, summary, bstack1l1ll11llll_opy_):
    if report.when == bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᣂ") and report.skipped:
        bstack1ll11lll1ll_opy_(report)
    if report.when in [bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᣃ"), bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᣄ")]:
        return
    if not bstack1llll1l1111_opy_():
        return
    try:
        if (str(bstack1l1ll11llll_opy_).lower() != bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫᣅ")):
            item._driver.execute_script(
                bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬᣆ") + json.dumps(
                    report.nodeid) + bstack11111_opy_ (u"ࠨࡿࢀࠫᣇ"))
        os.environ[bstack11111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᣈ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥᣉ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᣊ")))
    bstack1l1111111l_opy_ = bstack11111_opy_ (u"ࠧࠨᣋ")
    bstack1ll11lll1ll_opy_(report)
    if not passed:
        try:
            bstack1l1111111l_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11111_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᣌ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1111111l_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᣍ")))
        bstack1l1111111l_opy_ = bstack11111_opy_ (u"ࠣࠤᣎ")
        if not passed:
            try:
                bstack1l1111111l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᣏ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1111111l_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧᣐ")
                    + json.dumps(bstack11111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧᣑ"))
                    + bstack11111_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᣒ")
                )
            else:
                item._driver.execute_script(
                    bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᣓ")
                    + json.dumps(str(bstack1l1111111l_opy_))
                    + bstack11111_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥᣔ")
                )
        except Exception as e:
            summary.append(bstack11111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨᣕ").format(e))
def bstack1l1ll1l1l11_opy_(test_name, error_message):
    try:
        bstack1l1ll111l11_opy_ = []
        bstack111l11111_opy_ = os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᣖ"), bstack11111_opy_ (u"ࠪ࠴ࠬᣗ"))
        bstack11111l11_opy_ = {bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᣘ"): test_name, bstack11111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᣙ"): error_message, bstack11111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᣚ"): bstack111l11111_opy_}
        bstack1l1ll11l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᣛ"))
        if os.path.exists(bstack1l1ll11l1ll_opy_):
            with open(bstack1l1ll11l1ll_opy_) as f:
                bstack1l1ll111l11_opy_ = json.load(f)
        bstack1l1ll111l11_opy_.append(bstack11111l11_opy_)
        with open(bstack1l1ll11l1ll_opy_, bstack11111_opy_ (u"ࠨࡹࠪᣜ")) as f:
            json.dump(bstack1l1ll111l11_opy_, f)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧᣝ") + str(e))
def bstack1l1ll1lll11_opy_(item, report, summary, bstack1l1ll11llll_opy_):
    if report.when in [bstack11111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᣞ"), bstack11111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᣟ")]:
        return
    if (str(bstack1l1ll11llll_opy_).lower() != bstack11111_opy_ (u"ࠬࡺࡲࡶࡧࠪᣠ")):
        bstack1llll11ll1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᣡ")))
    bstack1l1111111l_opy_ = bstack11111_opy_ (u"ࠢࠣᣢ")
    bstack1ll11lll1ll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1111111l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᣣ").format(e)
                )
        try:
            if passed:
                bstack11llll11ll_opy_(getattr(item, bstack11111_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᣤ"), None), bstack11111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᣥ"))
            else:
                error_message = bstack11111_opy_ (u"ࠫࠬᣦ")
                if bstack1l1111111l_opy_:
                    bstack1ll11l11_opy_(item._page, str(bstack1l1111111l_opy_), bstack11111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦᣧ"))
                    bstack11llll11ll_opy_(getattr(item, bstack11111_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᣨ"), None), bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᣩ"), str(bstack1l1111111l_opy_))
                    error_message = str(bstack1l1111111l_opy_)
                else:
                    bstack11llll11ll_opy_(getattr(item, bstack11111_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᣪ"), None), bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᣫ"))
                bstack1l1ll1l1l11_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢᣬ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11111_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᣭ"), default=bstack11111_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᣮ"), help=bstack11111_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧᣯ"))
    parser.addoption(bstack11111_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᣰ"), default=bstack11111_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢᣱ"), help=bstack11111_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣᣲ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11111_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧᣳ"), action=bstack11111_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥᣴ"), default=bstack11111_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧᣵ"),
                         help=bstack11111_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧ᣶"))
def bstack11l1l1ll11_opy_(log):
    if not (log[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᣷")] and log[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᣸")].strip()):
        return
    active = bstack11l1ll1lll_opy_()
    log = {
        bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ᣹"): log[bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ᣺")],
        bstack11111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ᣻"): bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"ࠬࡠࠧ᣼"),
        bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᣽"): log[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᣾")],
    }
    if active:
        if active[bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭᣿")] == bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᤀ"):
            log[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᤁ")] = active[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᤂ")]
        elif active[bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪᤃ")] == bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࠫᤄ"):
            log[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᤅ")] = active[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᤆ")]
    bstack1lll11llll_opy_.bstack11lll1l111_opy_([log])
def bstack11l1ll1lll_opy_():
    if len(store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᤇ")]) > 0 and store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᤈ")][-1]:
        return {
            bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩᤉ"): bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᤊ"),
            bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᤋ"): store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᤌ")][-1]
        }
    if store.get(bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᤍ"), None):
        return {
            bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᤎ"): bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࠨᤏ"),
            bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᤐ"): store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᤑ")]
        }
    return None
bstack11l1ll1l1l_opy_ = bstack11l1ll111l_opy_(bstack11l1l1ll11_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        item._1l1ll11111l_opy_ = True
        bstack1lll1l11l_opy_ = bstack1l1lll1l1_opy_.bstack1l1lll11l_opy_(bstack1llll1111ll_opy_(item.own_markers))
        item._a11y_test_case = bstack1lll1l11l_opy_
        if bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᤒ"), None):
            driver = getattr(item, bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᤓ"), None)
            item._a11y_started = bstack1l1lll1l1_opy_.bstack1l1lll1ll1_opy_(driver, bstack1lll1l11l_opy_)
        if not bstack1lll11llll_opy_.on() or bstack1l1ll1ll1ll_opy_ != bstack11111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᤔ"):
            return
        global current_test_uuid, bstack11l1ll1l1l_opy_
        bstack11l1ll1l1l_opy_.start()
        bstack11l11l11ll_opy_ = {
            bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᤕ"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᤖ"): bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭ᤗ")
        }
        current_test_uuid = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪᤘ")]
        store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᤙ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᤚ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11l11l1111_opy_[item.nodeid] = {**_11l11l1111_opy_[item.nodeid], **bstack11l11l11ll_opy_}
        bstack1l1ll1111ll_opy_(item, _11l11l1111_opy_[item.nodeid], bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᤛ"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡦࡥࡱࡲ࠺ࠡࡽࢀࠫᤜ"), str(err))
def pytest_runtest_setup(item):
    global bstack1l1ll11ll1l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1lll1l111l1_opy_():
        atexit.register(bstack11ll1l1111_opy_)
        if not bstack1l1ll11ll1l_opy_:
            try:
                bstack1l1ll11l1l1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1lll111lll1_opy_():
                    bstack1l1ll11l1l1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1l1ll11l1l1_opy_:
                    signal.signal(s, bstack1l1ll1l1lll_opy_)
                bstack1l1ll11ll1l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡨ࡫ࡶࡸࡪࡸࠠࡴ࡫ࡪࡲࡦࡲࠠࡩࡣࡱࡨࡱ࡫ࡲࡴ࠼ࠣࠦᤝ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1ll11lll11l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᤞ")
    try:
        if not bstack1lll11llll_opy_.on():
            return
        bstack11l1ll1l1l_opy_.start()
        uuid = uuid4().__str__()
        bstack11l11l11ll_opy_ = {
            bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ᤟"): uuid,
            bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᤠ"): bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩᤡ"),
            bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᤢ"): bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᤣ"),
            bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᤤ"): bstack11111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᤥ"),
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨᤦ"): bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᤧ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᤨ")] = item
        store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᤩ")] = [uuid]
        if not _11l11l1111_opy_.get(item.nodeid, None):
            _11l11l1111_opy_[item.nodeid] = {bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᤪ"): [], bstack11111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᤫ"): []}
        _11l11l1111_opy_[item.nodeid][bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ᤬")].append(bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ᤭")])
        _11l11l1111_opy_[item.nodeid + bstack11111_opy_ (u"࠭࠭ࡴࡧࡷࡹࡵ࠭᤮")] = bstack11l11l11ll_opy_
        bstack1l1ll111lll_opy_(item, bstack11l11l11ll_opy_, bstack11111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ᤯"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫᤰ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1l1lllllll_opy_
        bstack111l11111_opy_ = 0
        if bstack1l1l11ll_opy_ is True:
            bstack111l11111_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᤱ")))
        if bstack1ll111l11l_opy_.bstack1111llll_opy_() == bstack11111_opy_ (u"ࠥࡸࡷࡻࡥࠣᤲ"):
            if bstack1ll111l11l_opy_.bstack111l1111l_opy_() == bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᤳ"):
                bstack1l1ll11lll1_opy_ = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᤴ"), None)
                bstack11111l11l_opy_ = bstack1l1ll11lll1_opy_ + bstack11111_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᤵ")
                driver = getattr(item, bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᤶ"), None)
                bstack1l11l1111l_opy_ = getattr(item, bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᤷ"), None)
                bstack1l1l1lll1l_opy_ = getattr(item, bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᤸ"), None)
                PercySDK.screenshot(driver, bstack11111l11l_opy_, bstack1l11l1111l_opy_=bstack1l11l1111l_opy_, bstack1l1l1lll1l_opy_=bstack1l1l1lll1l_opy_, bstack11l111l1_opy_=bstack111l11111_opy_)
        if getattr(item, bstack11111_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡦࡸࡴࡦࡦ᤹ࠪ"), False):
            bstack1l111ll11_opy_.bstack11111ll1_opy_(getattr(item, bstack11111_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ᤺"), None), bstack1l1lllllll_opy_, logger, item)
        if not bstack1lll11llll_opy_.on():
            return
        bstack11l11l11ll_opy_ = {
            bstack11111_opy_ (u"ࠬࡻࡵࡪࡦ᤻ࠪ"): uuid4().__str__(),
            bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ᤼"): bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩ᤽"),
            bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭᤾"): bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ᤿"),
            bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭᥀"): bstack11111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨ᥁"),
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ᥂"): bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᥃")
        }
        _11l11l1111_opy_[item.nodeid + bstack11111_opy_ (u"ࠧ࠮ࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ᥄")] = bstack11l11l11ll_opy_
        bstack1l1ll111lll_opy_(item, bstack11l11l11ll_opy_, bstack11111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ᥅"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱ࠾ࠥࢁࡽࠨ᥆"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1lll11llll_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1ll11llllll_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩ᥇")] = request.node
    elif bstack1ll11lll1l1_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ᥈")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ᥉"): fixturedef.argname,
            bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᥊"): bstack1lll11l11ll_opy_(outcome),
            bstack11111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ᥋"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ᥌")]
        if not _11l11l1111_opy_.get(current_test_item.nodeid, None):
            _11l11l1111_opy_[current_test_item.nodeid] = {bstack11111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ᥍"): []}
        _11l11l1111_opy_[current_test_item.nodeid][bstack11111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ᥎")].append(fixture)
    except Exception as err:
        logger.debug(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧ᥏"), str(err))
if bstack1ll1l1l1ll_opy_() and bstack1lll11llll_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11l11l1111_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᥐ")].bstack1ll111l1ll_opy_(id(step))
        except Exception as err:
            print(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶ࠺ࠡࡽࢀࠫᥑ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11l11l1111_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᥒ")].bstack11l1l1l1l1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬᥓ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11l1l11ll1_opy_: bstack11l1l1l1ll_opy_ = _11l11l1111_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᥔ")]
            bstack11l1l11ll1_opy_.bstack11l1l1l1l1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧᥕ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1l1ll1ll1ll_opy_
        try:
            if not bstack1lll11llll_opy_.on() or bstack1l1ll1ll1ll_opy_ != bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᥖ"):
                return
            global bstack11l1ll1l1l_opy_
            bstack11l1ll1l1l_opy_.start()
            driver = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫᥗ"), None)
            if not _11l11l1111_opy_.get(request.node.nodeid, None):
                _11l11l1111_opy_[request.node.nodeid] = {}
            bstack11l1l11ll1_opy_ = bstack11l1l1l1ll_opy_.bstack1ll111l1111_opy_(
                scenario, feature, request.node,
                name=bstack1ll11lllll1_opy_(request.node, scenario),
                bstack11l1lll11l_opy_=bstack1l1l11lll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨᥘ"),
                tags=bstack1ll11lll111_opy_(feature, scenario),
                bstack11l1l1l11l_opy_=bstack1lll11llll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {}
            )
            _11l11l1111_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᥙ")] = bstack11l1l11ll1_opy_
            bstack1l1ll1l1111_opy_(bstack11l1l11ll1_opy_.uuid)
            bstack1lll11llll_opy_.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᥚ"), bstack11l1l11ll1_opy_)
        except Exception as err:
            print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫᥛ"), str(err))
def bstack1l1ll11ll11_opy_(bstack11l1lll1l1_opy_):
    if bstack11l1lll1l1_opy_ in store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᥜ")]:
        store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᥝ")].remove(bstack11l1lll1l1_opy_)
def bstack1l1ll1l1111_opy_(bstack11l1l1l111_opy_):
    store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᥞ")] = bstack11l1l1l111_opy_
    threading.current_thread().current_test_uuid = bstack11l1l1l111_opy_
@bstack1lll11llll_opy_.bstack1ll111111l1_opy_
def bstack1l1ll1l1ll1_opy_(item, call, report):
    logger.debug(bstack11111_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡸࡴࠨᥟ"))
    global bstack1l1ll1ll1ll_opy_
    bstack1l11l111l_opy_ = bstack1l1l11lll_opy_()
    if hasattr(report, bstack11111_opy_ (u"ࠧࡴࡶࡲࡴࠬᥠ")):
        bstack1l11l111l_opy_ = bstack1lll1111lll_opy_(report.stop)
    elif hasattr(report, bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࠧᥡ")):
        bstack1l11l111l_opy_ = bstack1lll1111lll_opy_(report.start)
    try:
        if getattr(report, bstack11111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᥢ"), bstack11111_opy_ (u"ࠪࠫᥣ")) == bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᥤ"):
            bstack11l1ll1l1l_opy_.reset()
        if getattr(report, bstack11111_opy_ (u"ࠬࡽࡨࡦࡰࠪᥥ"), bstack11111_opy_ (u"࠭ࠧᥦ")) == bstack11111_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᥧ"):
            logger.debug(bstack11111_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡵࡧࠣ࠱ࠥࢁࡽ࠭ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࠳ࠠࡼࡿࠪᥨ").format(getattr(report, bstack11111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᥩ"), bstack11111_opy_ (u"ࠪࠫᥪ")).__str__(), bstack1l1ll1ll1ll_opy_))
            if bstack1l1ll1ll1ll_opy_ == bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᥫ"):
                _11l11l1111_opy_[item.nodeid][bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᥬ")] = bstack1l11l111l_opy_
                bstack1l1ll1111ll_opy_(item, _11l11l1111_opy_[item.nodeid], bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᥭ"), report, call)
                store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᥮")] = None
            elif bstack1l1ll1ll1ll_opy_ == bstack11111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ᥯"):
                bstack11l1l11ll1_opy_ = _11l11l1111_opy_[item.nodeid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᥰ")]
                bstack11l1l11ll1_opy_.set(hooks=_11l11l1111_opy_[item.nodeid].get(bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᥱ"), []))
                exception, bstack11l1llll11_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11l1llll11_opy_ = [call.excinfo.exconly(), getattr(report, bstack11111_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪᥲ"), bstack11111_opy_ (u"ࠬ࠭ᥳ"))]
                bstack11l1l11ll1_opy_.stop(time=bstack1l11l111l_opy_, result=Result(result=getattr(report, bstack11111_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᥴ"), bstack11111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᥵")), exception=exception, bstack11l1llll11_opy_=bstack11l1llll11_opy_))
                bstack1lll11llll_opy_.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᥶"), _11l11l1111_opy_[item.nodeid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ᥷")])
        elif getattr(report, bstack11111_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ᥸"), bstack11111_opy_ (u"ࠫࠬ᥹")) in [bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᥺"), bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᥻")]:
            logger.debug(bstack11111_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡴࡦࠢ࠰ࠤࢀࢃࠬࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࠲ࠦࡻࡾࠩ᥼").format(getattr(report, bstack11111_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭᥽"), bstack11111_opy_ (u"ࠩࠪ᥾")).__str__(), bstack1l1ll1ll1ll_opy_))
            bstack11l1l11l1l_opy_ = item.nodeid + bstack11111_opy_ (u"ࠪ࠱ࠬ᥿") + getattr(report, bstack11111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᦀ"), bstack11111_opy_ (u"ࠬ࠭ᦁ"))
            if getattr(report, bstack11111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᦂ"), False):
                hook_type = bstack11111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᦃ") if getattr(report, bstack11111_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᦄ"), bstack11111_opy_ (u"ࠩࠪᦅ")) == bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᦆ") else bstack11111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᦇ")
                _11l11l1111_opy_[bstack11l1l11l1l_opy_] = {
                    bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪᦈ"): uuid4().__str__(),
                    bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᦉ"): bstack1l11l111l_opy_,
                    bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᦊ"): hook_type
                }
            _11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᦋ")] = bstack1l11l111l_opy_
            bstack1l1ll11ll11_opy_(_11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᦌ")])
            bstack1l1ll111lll_opy_(item, _11l11l1111_opy_[bstack11l1l11l1l_opy_], bstack11111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᦍ"), report, call)
            if getattr(report, bstack11111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᦎ"), bstack11111_opy_ (u"ࠬ࠭ᦏ")) == bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᦐ"):
                if getattr(report, bstack11111_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨᦑ"), bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᦒ")) == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᦓ"):
                    bstack11l11l11ll_opy_ = {
                        bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᦔ"): uuid4().__str__(),
                        bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᦕ"): bstack1l1l11lll_opy_(),
                        bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᦖ"): bstack1l1l11lll_opy_()
                    }
                    _11l11l1111_opy_[item.nodeid] = {**_11l11l1111_opy_[item.nodeid], **bstack11l11l11ll_opy_}
                    bstack1l1ll1111ll_opy_(item, _11l11l1111_opy_[item.nodeid], bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᦗ"))
                    bstack1l1ll1111ll_opy_(item, _11l11l1111_opy_[item.nodeid], bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᦘ"), report, call)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡿࢂ࠭ᦙ"), str(err))
def bstack1l1ll1ll111_opy_(test, bstack11l11l11ll_opy_, result=None, call=None, bstack1ll1llll11_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l1l11ll1_opy_ = {
        bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᦚ"): bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᦛ")],
        bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩᦜ"): bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࠪᦝ"),
        bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᦞ"): test.name,
        bstack11111_opy_ (u"ࠧࡣࡱࡧࡽࠬᦟ"): {
            bstack11111_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᦠ"): bstack11111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᦡ"),
            bstack11111_opy_ (u"ࠪࡧࡴࡪࡥࠨᦢ"): inspect.getsource(test.obj)
        },
        bstack11111_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᦣ"): test.name,
        bstack11111_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫᦤ"): test.name,
        bstack11111_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ᦥ"): bstack1l1l11l1l1_opy_.bstack111llll111_opy_(test),
        bstack11111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᦦ"): file_path,
        bstack11111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᦧ"): file_path,
        bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᦨ"): bstack11111_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᦩ"),
        bstack11111_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᦪ"): file_path,
        bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᦫ"): bstack11l11l11ll_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ᦬")],
        bstack11111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ᦭"): bstack11111_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ᦮"),
        bstack11111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬ᦯"): {
            bstack11111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧᦰ"): test.nodeid
        },
        bstack11111_opy_ (u"ࠫࡹࡧࡧࡴࠩᦱ"): bstack1llll1111ll_opy_(test.own_markers)
    }
    if bstack1ll1llll11_opy_ in [bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᦲ"), bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᦳ")]:
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠧ࡮ࡧࡷࡥࠬᦴ")] = {
            bstack11111_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᦵ"): bstack11l11l11ll_opy_.get(bstack11111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᦶ"), [])
        }
    if bstack1ll1llll11_opy_ == bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᦷ"):
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᦸ")] = bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᦹ")
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᦺ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᦻ")]
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᦼ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᦽ")]
    if result:
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᦾ")] = result.outcome
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᦿ")] = result.duration * 1000
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᧀ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᧁ")]
        if result.failed:
            bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ᧂ")] = bstack1lll11llll_opy_.bstack111l1ll1ll_opy_(call.excinfo.typename)
            bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᧃ")] = bstack1lll11llll_opy_.bstack1l1llll1111_opy_(call.excinfo, result)
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᧄ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᧅ")]
    if outcome:
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᧆ")] = bstack1lll11l11ll_opy_(outcome)
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᧇ")] = 0
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᧈ")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᧉ")]
        if bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᧊")] == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᧋"):
            bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ᧌")] = bstack11111_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬ᧍")  # bstack1l1ll111111_opy_
            bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭᧎")] = [{bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ᧏"): [bstack11111_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫ᧐")]}]
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᧑")] = bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ᧒")]
    return bstack11l1l11ll1_opy_
def bstack1l1ll1l1l1l_opy_(test, bstack111llll1ll_opy_, bstack1ll1llll11_opy_, result, call, outcome, bstack1l1ll1l11ll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭᧓")]
    hook_name = bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ᧔")]
    hook_data = {
        bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ᧕"): bstack111llll1ll_opy_[bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ᧖")],
        bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬ᧗"): bstack11111_opy_ (u"ࠨࡪࡲࡳࡰ࠭᧘"),
        bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᧙"): bstack11111_opy_ (u"ࠪࡿࢂ࠭᧚").format(bstack1ll1l11111l_opy_(hook_name)),
        bstack11111_opy_ (u"ࠫࡧࡵࡤࡺࠩ᧛"): {
            bstack11111_opy_ (u"ࠬࡲࡡ࡯ࡩࠪ᧜"): bstack11111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭᧝"),
            bstack11111_opy_ (u"ࠧࡤࡱࡧࡩࠬ᧞"): None
        },
        bstack11111_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧ᧟"): test.name,
        bstack11111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩ᧠"): bstack1l1l11l1l1_opy_.bstack111llll111_opy_(test, hook_name),
        bstack11111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭᧡"): file_path,
        bstack11111_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭᧢"): file_path,
        bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᧣"): bstack11111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ᧤"),
        bstack11111_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬ᧥"): file_path,
        bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ᧦"): bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᧧")],
        bstack11111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᧨"): bstack11111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭᧩") if bstack1l1ll1ll1ll_opy_ == bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ᧪") else bstack11111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭᧫"),
        bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ᧬"): hook_type
    }
    bstack1ll111l11ll_opy_ = bstack111lll1l11_opy_(_11l11l1111_opy_.get(test.nodeid, None))
    if bstack1ll111l11ll_opy_:
        hook_data[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭᧭")] = bstack1ll111l11ll_opy_
    if result:
        hook_data[bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᧮")] = result.outcome
        hook_data[bstack11111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ᧯")] = result.duration * 1000
        hook_data[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᧰")] = bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᧱")]
        if result.failed:
            hook_data[bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ᧲")] = bstack1lll11llll_opy_.bstack111l1ll1ll_opy_(call.excinfo.typename)
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ᧳")] = bstack1lll11llll_opy_.bstack1l1llll1111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᧴")] = bstack1lll11l11ll_opy_(outcome)
        hook_data[bstack11111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ᧵")] = 100
        hook_data[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᧶")] = bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᧷")]
        if hook_data[bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᧸")] == bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᧹"):
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭᧺")] = bstack11111_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩ᧻")  # bstack1l1ll111111_opy_
            hook_data[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ᧼")] = [{bstack11111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭᧽"): [bstack11111_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨ᧾")]}]
    if bstack1l1ll1l11ll_opy_:
        hook_data[bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᧿")] = bstack1l1ll1l11ll_opy_.result
        hook_data[bstack11111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᨀ")] = bstack1lll1ll1lll_opy_(bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᨁ")], bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᨂ")])
        hook_data[bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᨃ")] = bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᨄ")]
        if hook_data[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᨅ")] == bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᨆ"):
            hook_data[bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᨇ")] = bstack1lll11llll_opy_.bstack111l1ll1ll_opy_(bstack1l1ll1l11ll_opy_.exception_type)
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᨈ")] = [{bstack11111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᨉ"): bstack1llll111l1l_opy_(bstack1l1ll1l11ll_opy_.exception)}]
    return hook_data
def bstack1l1ll1111ll_opy_(test, bstack11l11l11ll_opy_, bstack1ll1llll11_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11111_opy_ (u"ࠩࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡨࡺࡪࡴࡴ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠡ࠯ࠣࡿࢂ࠭ᨊ").format(bstack1ll1llll11_opy_))
    bstack11l1l11ll1_opy_ = bstack1l1ll1ll111_opy_(test, bstack11l11l11ll_opy_, result, call, bstack1ll1llll11_opy_, outcome)
    driver = getattr(test, bstack11111_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᨋ"), None)
    if bstack1ll1llll11_opy_ == bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᨌ") and driver:
        bstack11l1l11ll1_opy_[bstack11111_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫᨍ")] = bstack1lll11llll_opy_.bstack11l1ll1ll1_opy_(driver)
    if bstack1ll1llll11_opy_ == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᨎ"):
        bstack1ll1llll11_opy_ = bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᨏ")
    bstack111lll11ll_opy_ = {
        bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᨐ"): bstack1ll1llll11_opy_,
        bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᨑ"): bstack11l1l11ll1_opy_
    }
    bstack1lll11llll_opy_.bstack1l11l1l1l1_opy_(bstack111lll11ll_opy_)
    if bstack1ll1llll11_opy_ == bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᨒ"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᨓ"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᨔ")}
    elif bstack1ll1llll11_opy_ == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᨕ"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᨖ"): getattr(result, bstack11111_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩᨗ"), bstack11111_opy_ (u"ᨘࠩࠪ"))}
def bstack1l1ll111lll_opy_(test, bstack11l11l11ll_opy_, bstack1ll1llll11_opy_, result=None, call=None, outcome=None, bstack1l1ll1l11ll_opy_=None):
    logger.debug(bstack11111_opy_ (u"ࠪࡷࡪࡴࡤࡠࡪࡲࡳࡰࡥࡲࡶࡰࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥ࡮࡯ࡰ࡭ࠣࡨࡦࡺࡡ࠭ࠢࡨࡺࡪࡴࡴࡕࡻࡳࡩࠥ࠳ࠠࡼࡿࠪᨙ").format(bstack1ll1llll11_opy_))
    hook_data = bstack1l1ll1l1l1l_opy_(test, bstack11l11l11ll_opy_, bstack1ll1llll11_opy_, result, call, outcome, bstack1l1ll1l11ll_opy_)
    bstack111lll11ll_opy_ = {
        bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᨚ"): bstack1ll1llll11_opy_,
        bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᨛ"): hook_data
    }
    bstack1lll11llll_opy_.bstack1l11l1l1l1_opy_(bstack111lll11ll_opy_)
def bstack111lll1l11_opy_(bstack11l11l11ll_opy_):
    if not bstack11l11l11ll_opy_:
        return None
    if bstack11l11l11ll_opy_.get(bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ᨜"), None):
        return getattr(bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ᨝")], bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭᨞"), None)
    return bstack11l11l11ll_opy_.get(bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᨟"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1lll11llll_opy_.on():
            return
        places = [bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᨠ"), bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᨡ"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᨢ")]
        bstack11l111l11l_opy_ = []
        for bstack1l1ll1ll11l_opy_ in places:
            records = caplog.get_records(bstack1l1ll1ll11l_opy_)
            bstack1l1ll1ll1l1_opy_ = bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᨣ") if bstack1l1ll1ll11l_opy_ == bstack11111_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᨤ") else bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᨥ")
            bstack1l1ll1l111l_opy_ = request.node.nodeid + (bstack11111_opy_ (u"ࠩࠪᨦ") if bstack1l1ll1ll11l_opy_ == bstack11111_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᨧ") else bstack11111_opy_ (u"ࠫ࠲࠭ᨨ") + bstack1l1ll1ll11l_opy_)
            bstack11l1l1l111_opy_ = bstack111lll1l11_opy_(_11l11l1111_opy_.get(bstack1l1ll1l111l_opy_, None))
            if not bstack11l1l1l111_opy_:
                continue
            for record in records:
                if bstack1llll111l11_opy_(record.message):
                    continue
                bstack11l111l11l_opy_.append({
                    bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᨩ"): bstack1llll11llll_opy_(record.created).isoformat() + bstack11111_opy_ (u"࡚࠭ࠨᨪ"),
                    bstack11111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᨫ"): record.levelname,
                    bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᨬ"): record.message,
                    bstack1l1ll1ll1l1_opy_: bstack11l1l1l111_opy_
                })
        if len(bstack11l111l11l_opy_) > 0:
            bstack1lll11llll_opy_.bstack11lll1l111_opy_(bstack11l111l11l_opy_)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ᨭ"), str(err))
def bstack1ll11ll1l_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1111ll_opy_
    bstack11ll1l11l1_opy_ = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧᨮ"), None) and bstack1l11lll1ll_opy_(
            threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᨯ"), None)
    bstack11ll11l1l1_opy_ = getattr(driver, bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬᨰ"), None) != None and getattr(driver, bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ᨱ"), None) == True
    if sequence == bstack11111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧᨲ") and driver != None:
      if not bstack11l1111ll_opy_ and bstack1llll1l1111_opy_() and bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᨳ") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᨴ")] == True and bstack1l11l1lll1_opy_.bstack11111llll_opy_(driver_command) and (bstack11ll11l1l1_opy_ or bstack11ll1l11l1_opy_) and not bstack11ll11l1_opy_(args):
        try:
          bstack11l1111ll_opy_ = True
          logger.debug(bstack11111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬᨵ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩᨶ").format(str(err)))
        bstack11l1111ll_opy_ = False
    if sequence == bstack11111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᨷ"):
        if driver_command == bstack11111_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪᨸ"):
            bstack1lll11llll_opy_.bstack11lll1l1ll_opy_({
                bstack11111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ᨹ"): response[bstack11111_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧᨺ")],
                bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᨻ"): store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᨼ")]
            })
def bstack11ll1l1111_opy_():
    global bstack1ll1lll11l_opy_
    bstack11l1l11ll_opy_.bstack1l111ll11l_opy_()
    logging.shutdown()
    bstack1lll11llll_opy_.bstack11l11l11l1_opy_()
    for driver in bstack1ll1lll11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1ll1l1lll_opy_(*args):
    global bstack1ll1lll11l_opy_
    bstack1lll11llll_opy_.bstack11l11l11l1_opy_()
    for driver in bstack1ll1lll11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll111llll_opy_, stage=STAGE.SINGLE, bstack1111l111l_opy_=bstack1l1lllll11_opy_)
def bstack1l1l11l1_opy_(self, *args, **kwargs):
    bstack1lllll1l1l_opy_ = bstack11ll11ll1l_opy_(self, *args, **kwargs)
    bstack1ll11ll1_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬᨽ"), None)
    if bstack1ll11ll1_opy_ and bstack1ll11ll1_opy_.get(bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᨾ"), bstack11111_opy_ (u"࠭ࠧᨿ")) == bstack11111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᩀ"):
        bstack1lll11llll_opy_.bstack1l1lll11_opy_(self)
    return bstack1lllll1l1l_opy_
@measure(event_name=EVENTS.bstack111ll1ll_opy_, stage=STAGE.bstack111ll1l1l_opy_, bstack1111l111l_opy_=bstack1l1lllll11_opy_)
def bstack1l1llll1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
    if bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬᩁ")):
        return
    bstack1llllll1l1_opy_.bstack1l1111llll_opy_(bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭ᩂ"), True)
    global bstack1ll111l1l1_opy_
    global bstack1lll11lll_opy_
    bstack1ll111l1l1_opy_ = framework_name
    logger.info(bstack1llll1l111_opy_.format(bstack1ll111l1l1_opy_.split(bstack11111_opy_ (u"ࠪ࠱ࠬᩃ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1llll1l1111_opy_():
            Service.start = bstack1l11ll1lll_opy_
            Service.stop = bstack1l11111lll_opy_
            webdriver.Remote.__init__ = bstack1l11l1l1ll_opy_
            webdriver.Remote.get = bstack1ll11111ll_opy_
            if not isinstance(os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬᩄ")), str):
                return
            WebDriver.close = bstack1ll1l1l1l1_opy_
            WebDriver.quit = bstack1l111l1l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack1llll1l1111_opy_() and bstack1lll11llll_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l11l1_opy_
        bstack1lll11lll_opy_ = True
    except Exception as e:
        pass
    bstack11ll1111ll_opy_()
    if os.environ.get(bstack11111_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪᩅ")):
        bstack1lll11lll_opy_ = eval(os.environ.get(bstack11111_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫᩆ")))
    if not bstack1lll11lll_opy_:
        bstack1lll11111l_opy_(bstack11111_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤᩇ"), bstack11ll11l1l_opy_)
    if bstack11ll11l11l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._11ll11l111_opy_ = bstack1ll111111l_opy_
        except Exception as e:
            logger.error(bstack1l1111l1ll_opy_.format(str(e)))
    if bstack11111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᩈ") in str(framework_name).lower():
        if not bstack1llll1l1111_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1lll1l1l11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l1111l_opy_
            Config.getoption = bstack11ll1l1l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1l111l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1l1lll11_opy_, stage=STAGE.SINGLE, bstack1111l111l_opy_=bstack1l1lllll11_opy_)
def bstack1l111l1l_opy_(self):
    global bstack1ll111l1l1_opy_
    global bstack111lllll_opy_
    global bstack1l11lllll1_opy_
    try:
        if bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᩉ") in bstack1ll111l1l1_opy_ and self.session_id != None and bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᩊ"), bstack11111_opy_ (u"ࠫࠬᩋ")) != bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᩌ"):
            bstack1l11l1l11l_opy_ = bstack11111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᩍ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᩎ")
            bstack1l1l1111l_opy_(logger, True)
            if self != None:
                bstack1ll11l1111_opy_(self, bstack1l11l1l11l_opy_, bstack11111_opy_ (u"ࠨ࠮ࠣࠫᩏ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᩐ"), None)
        if item is not None and bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᩑ"), None):
            bstack1l111ll11_opy_.bstack11111ll1_opy_(self, bstack1l1lllllll_opy_, logger, item)
        threading.current_thread().testStatus = bstack11111_opy_ (u"ࠫࠬᩒ")
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨᩓ") + str(e))
    bstack1l11lllll1_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1l1l1ll111_opy_, stage=STAGE.SINGLE, bstack1111l111l_opy_=bstack1l1lllll11_opy_)
def bstack1l11l1l1ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack111lllll_opy_
    global bstack1l1lllll11_opy_
    global bstack1l1l11ll_opy_
    global bstack1ll111l1l1_opy_
    global bstack11ll11ll1l_opy_
    global bstack1ll1lll11l_opy_
    global bstack1l1111lll_opy_
    global bstack1ll1l1ll_opy_
    global bstack1l1lllllll_opy_
    CONFIG[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᩔ")] = str(bstack1ll111l1l1_opy_) + str(__version__)
    command_executor = bstack1llll1l11_opy_(bstack1l1111lll_opy_, CONFIG)
    logger.debug(bstack1l1l11l11l_opy_.format(command_executor))
    proxy = bstack1lllll11_opy_(CONFIG, proxy)
    bstack111l11111_opy_ = 0
    try:
        if bstack1l1l11ll_opy_ is True:
            bstack111l11111_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᩕ")))
    except:
        bstack111l11111_opy_ = 0
    bstack1ll11llll1_opy_ = bstack11ll111l1l_opy_(CONFIG, bstack111l11111_opy_)
    logger.debug(bstack11ll1llll_opy_.format(str(bstack1ll11llll1_opy_)))
    bstack1l1lllllll_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᩖ"))[bstack111l11111_opy_]
    if bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᩗ") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᩘ")]:
        bstack1lll1ll11l_opy_(bstack1ll11llll1_opy_, bstack1ll1l1ll_opy_)
    if bstack1l1lll1l1_opy_.bstack11ll11llll_opy_(CONFIG, bstack111l11111_opy_) and bstack1l1lll1l1_opy_.bstack1l1l1l111l_opy_(bstack1ll11llll1_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        bstack1l1lll1l1_opy_.set_capabilities(bstack1ll11llll1_opy_, CONFIG)
    if desired_capabilities:
        bstack1l1111ll1l_opy_ = bstack1l1llll1ll_opy_(desired_capabilities)
        bstack1l1111ll1l_opy_[bstack11111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᩙ")] = bstack1lll11l1ll_opy_(CONFIG)
        bstack1ll11l11l1_opy_ = bstack11ll111l1l_opy_(bstack1l1111ll1l_opy_)
        if bstack1ll11l11l1_opy_:
            bstack1ll11llll1_opy_ = update(bstack1ll11l11l1_opy_, bstack1ll11llll1_opy_)
        desired_capabilities = None
    if options:
        bstack1llll11lll_opy_(options, bstack1ll11llll1_opy_)
    if not options:
        options = bstack111lll11_opy_(bstack1ll11llll1_opy_)
    if proxy and bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬᩚ")):
        options.proxy(proxy)
    if options and bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᩛ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11ll1l1l1_opy_() < version.parse(bstack11111_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᩜ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1ll11llll1_opy_)
    logger.info(bstack1lll1l1ll1_opy_)
    bstack1ll1ll1lll_opy_.end(EVENTS.bstack111ll1ll_opy_.value, EVENTS.bstack111ll1ll_opy_.value + bstack11111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᩝ"),
                               EVENTS.bstack111ll1ll_opy_.value + bstack11111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᩞ"), True, None)
    if bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ᩟")):
        bstack11ll11ll1l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠫ࠸࠴࠸࠯࠲᩠ࠪ")):
        bstack11ll11ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬᩡ")):
        bstack11ll11ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11ll11ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l1l11ll1_opy_ = bstack11111_opy_ (u"࠭ࠧᩢ")
        if bstack11ll1l1l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨᩣ")):
            bstack1l1l11ll1_opy_ = self.caps.get(bstack11111_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣᩤ"))
        else:
            bstack1l1l11ll1_opy_ = self.capabilities.get(bstack11111_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤᩥ"))
        if bstack1l1l11ll1_opy_:
            bstack1ll11lll1l_opy_(bstack1l1l11ll1_opy_)
            if bstack11ll1l1l1_opy_() <= version.parse(bstack11111_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪᩦ")):
                self.command_executor._url = bstack11111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᩧ") + bstack1l1111lll_opy_ + bstack11111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤᩨ")
            else:
                self.command_executor._url = bstack11111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᩩ") + bstack1l1l11ll1_opy_ + bstack11111_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣᩪ")
            logger.debug(bstack11111ll11_opy_.format(bstack1l1l11ll1_opy_))
        else:
            logger.debug(bstack1l111111ll_opy_.format(bstack11111_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤᩫ")))
    except Exception as e:
        logger.debug(bstack1l111111ll_opy_.format(e))
    bstack111lllll_opy_ = self.session_id
    if bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᩬ") in bstack1ll111l1l1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᩭ"), None)
        if item:
            bstack1l1l1lllll1_opy_ = getattr(item, bstack11111_opy_ (u"ࠫࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࡠࡵࡷࡥࡷࡺࡥࡥࠩᩮ"), False)
            if not getattr(item, bstack11111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᩯ"), None) and bstack1l1l1lllll1_opy_:
                setattr(store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᩰ")], bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᩱ"), self)
        bstack1ll11ll1_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩᩲ"), None)
        if bstack1ll11ll1_opy_ and bstack1ll11ll1_opy_.get(bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᩳ"), bstack11111_opy_ (u"ࠪࠫᩴ")) == bstack11111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ᩵"):
            bstack1lll11llll_opy_.bstack1l1lll11_opy_(self)
    bstack1ll1lll11l_opy_.append(self)
    if bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᩶") in CONFIG and bstack11111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᩷") in CONFIG[bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᩸")][bstack111l11111_opy_]:
        bstack1l1lllll11_opy_ = CONFIG[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᩹")][bstack111l11111_opy_][bstack11111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᩺")]
    logger.debug(bstack111llll1_opy_.format(bstack111lllll_opy_))
@measure(event_name=EVENTS.bstack11lll1l1l_opy_, stage=STAGE.SINGLE, bstack1111l111l_opy_=bstack1l1lllll11_opy_)
def bstack1ll11111ll_opy_(self, url):
    global bstack1lllll1lll_opy_
    global CONFIG
    try:
        bstack1l1l1lllll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l111lll11_opy_.format(str(err)))
    try:
        bstack1lllll1lll_opy_(self, url)
    except Exception as e:
        try:
            bstack1ll11l1l1_opy_ = str(e)
            if any(err_msg in bstack1ll11l1l1_opy_ for err_msg in bstack1ll111lll1_opy_):
                bstack1l1l1lllll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l111lll11_opy_.format(str(err)))
        raise e
def bstack1ll1lll1l1_opy_(item, when):
    global bstack11llll11l_opy_
    try:
        bstack11llll11l_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1l111l_opy_(item, call, rep):
    global bstack1lllllll1l_opy_
    global bstack1ll1lll11l_opy_
    name = bstack11111_opy_ (u"ࠪࠫ᩻")
    try:
        if rep.when == bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ᩼"):
            bstack111lllll_opy_ = threading.current_thread().bstackSessionId
            bstack1l1ll11llll_opy_ = item.config.getoption(bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᩽"))
            try:
                if (str(bstack1l1ll11llll_opy_).lower() != bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫ᩾")):
                    name = str(rep.nodeid)
                    bstack111111111_opy_ = bstack1ll1l1llll_opy_(bstack11111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ᩿"), name, bstack11111_opy_ (u"ࠨࠩ᪀"), bstack11111_opy_ (u"ࠩࠪ᪁"), bstack11111_opy_ (u"ࠪࠫ᪂"), bstack11111_opy_ (u"ࠫࠬ᪃"))
                    os.environ[bstack11111_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ᪄")] = name
                    for driver in bstack1ll1lll11l_opy_:
                        if bstack111lllll_opy_ == driver.session_id:
                            driver.execute_script(bstack111111111_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭᪅").format(str(e)))
            try:
                bstack1llll1ll11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᪆"):
                    status = bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᪇") if rep.outcome.lower() == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᪈") else bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᪉")
                    reason = bstack11111_opy_ (u"ࠫࠬ᪊")
                    if status == bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᪋"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11111_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ᪌") if status == bstack11111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᪍") else bstack11111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᪎")
                    data = name + bstack11111_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ᪏") if status == bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᪐") else name + bstack11111_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧ᪑") + reason
                    bstack1ll1l1ll1l_opy_ = bstack1ll1l1llll_opy_(bstack11111_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ᪒"), bstack11111_opy_ (u"࠭ࠧ᪓"), bstack11111_opy_ (u"ࠧࠨ᪔"), bstack11111_opy_ (u"ࠨࠩ᪕"), level, data)
                    for driver in bstack1ll1lll11l_opy_:
                        if bstack111lllll_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll1l1ll1l_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭᪖").format(str(e)))
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧ᪗").format(str(e)))
    bstack1lllllll1l_opy_(item, call, rep)
notset = Notset()
def bstack11ll1l1l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l11ll1l1l_opy_
    if str(name).lower() == bstack11111_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫ᪘"):
        return bstack11111_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ᪙")
    else:
        return bstack1l11ll1l1l_opy_(self, name, default, skip)
def bstack1ll111111l_opy_(self):
    global CONFIG
    global bstack11lllll11_opy_
    try:
        proxy = bstack1llll111ll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11111_opy_ (u"࠭࠮ࡱࡣࡦࠫ᪚")):
                proxies = bstack11ll11l1ll_opy_(proxy, bstack1llll1l11_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1l111l_opy_ = proxies.popitem()
                    if bstack11111_opy_ (u"ࠢ࠻࠱࠲ࠦ᪛") in bstack1l1l111l_opy_:
                        return bstack1l1l111l_opy_
                    else:
                        return bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ᪜") + bstack1l1l111l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨ᪝").format(str(e)))
    return bstack11lllll11_opy_(self)
def bstack11ll11l11l_opy_():
    return (bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᪞") in CONFIG or bstack11111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᪟") in CONFIG) and bstack11l11l111_opy_() and bstack11ll1l1l1_opy_() >= version.parse(
        bstack1lll1ll11_opy_)
def bstack1ll1llllll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1lllll11_opy_
    global bstack1l1l11ll_opy_
    global bstack1ll111l1l1_opy_
    CONFIG[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᪠")] = str(bstack1ll111l1l1_opy_) + str(__version__)
    bstack111l11111_opy_ = 0
    try:
        if bstack1l1l11ll_opy_ is True:
            bstack111l11111_opy_ = int(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭᪡")))
    except:
        bstack111l11111_opy_ = 0
    CONFIG[bstack11111_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ᪢")] = True
    bstack1ll11llll1_opy_ = bstack11ll111l1l_opy_(CONFIG, bstack111l11111_opy_)
    logger.debug(bstack11ll1llll_opy_.format(str(bstack1ll11llll1_opy_)))
    if CONFIG.get(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ᪣")):
        bstack1lll1ll11l_opy_(bstack1ll11llll1_opy_, bstack1ll1l1ll_opy_)
    if bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᪤") in CONFIG and bstack11111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ᪥") in CONFIG[bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᪦")][bstack111l11111_opy_]:
        bstack1l1lllll11_opy_ = CONFIG[bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᪧ")][bstack111l11111_opy_][bstack11111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᪨")]
    import urllib
    import json
    if bstack11111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ᪩") in CONFIG and str(CONFIG[bstack11111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ᪪")]).lower() != bstack11111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ᪫"):
        bstack1ll11l1l1l_opy_ = bstack1lllll111_opy_()
        bstack1l111l111l_opy_ = bstack1ll11l1l1l_opy_ + urllib.parse.quote(json.dumps(bstack1ll11llll1_opy_))
    else:
        bstack1l111l111l_opy_ = bstack11111_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ᪬") + urllib.parse.quote(json.dumps(bstack1ll11llll1_opy_))
    browser = self.connect(bstack1l111l111l_opy_)
    return browser
def bstack11ll1111ll_opy_():
    global bstack1lll11lll_opy_
    global bstack1ll111l1l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l11lll111_opy_
        if not bstack1llll1l1111_opy_():
            global bstack11l111l1l_opy_
            if not bstack11l111l1l_opy_:
                from bstack_utils.helper import bstack11ll1lllll_opy_, bstack11111ll1l_opy_
                bstack11l111l1l_opy_ = bstack11ll1lllll_opy_()
                bstack11111ll1l_opy_(bstack1ll111l1l1_opy_)
            BrowserType.connect = bstack1l11lll111_opy_
            return
        BrowserType.launch = bstack1ll1llllll_opy_
        bstack1lll11lll_opy_ = True
    except Exception as e:
        pass
def bstack1l1ll1111l1_opy_():
    global CONFIG
    global bstack1lll111111_opy_
    global bstack1l1111lll_opy_
    global bstack1ll1l1ll_opy_
    global bstack1l1l11ll_opy_
    global bstack11ll1l1ll1_opy_
    CONFIG = json.loads(os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪ᪭")))
    bstack1lll111111_opy_ = eval(os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭᪮")))
    bstack1l1111lll_opy_ = os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭᪯"))
    bstack111l1l1l1_opy_(CONFIG, bstack1lll111111_opy_)
    bstack11ll1l1ll1_opy_ = bstack11l1l11ll_opy_.bstack1l11l11l11_opy_(CONFIG, bstack11ll1l1ll1_opy_)
    global bstack11ll11ll1l_opy_
    global bstack1l11lllll1_opy_
    global bstack1111ll1l1_opy_
    global bstack11lllll1l1_opy_
    global bstack1l11l1ll1_opy_
    global bstack1l111l11l1_opy_
    global bstack1lllll111l_opy_
    global bstack1lllll1lll_opy_
    global bstack11lllll11_opy_
    global bstack1l11ll1l1l_opy_
    global bstack11llll11l_opy_
    global bstack1lllllll1l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11ll11ll1l_opy_ = webdriver.Remote.__init__
        bstack1l11lllll1_opy_ = WebDriver.quit
        bstack1lllll111l_opy_ = WebDriver.close
        bstack1lllll1lll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᪰") in CONFIG or bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᪱") in CONFIG) and bstack11l11l111_opy_():
        if bstack11ll1l1l1_opy_() < version.parse(bstack1lll1ll11_opy_):
            logger.error(bstack1ll1l111_opy_.format(bstack11ll1l1l1_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack11lllll11_opy_ = RemoteConnection._11ll11l111_opy_
            except Exception as e:
                logger.error(bstack1l1111l1ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l11ll1l1l_opy_ = Config.getoption
        from _pytest import runner
        bstack11llll11l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1ll1l111l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1lllllll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ᪲"))
    bstack1ll1l1ll_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ᪳"), {}).get(bstack11111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᪴"))
    bstack1l1l11ll_opy_ = True
    bstack1l1llll1_opy_(bstack1ll1lll1_opy_)
if (bstack1lll1l111l1_opy_()):
    bstack1l1ll1111l1_opy_()
@bstack11l11ll11l_opy_(class_method=False)
def bstack1l1ll111ll1_opy_(hook_name, event, bstack1l1ll111l1l_opy_=None):
    if hook_name not in [bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ᪵࠭"), bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰ᪶ࠪ"), bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ᪷࠭"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧ᪸ࠪ"), bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹ᪹ࠧ"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶ᪺ࠫ"), bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪ᪻"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᪼")]:
        return
    node = store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯᪽ࠪ")]
    if hook_name in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭᪾"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧᪿࠪ")]:
        node = store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨᫀ")]
    elif hook_name in [bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ᫁"), bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ᫂")]:
        node = store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯᫃ࠪ")]
    if event == bstack11111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ᫄࠭"):
        hook_type = bstack1ll11llll1l_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack111llll1ll_opy_ = {
            bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ᫅"): uuid,
            bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ᫆"): bstack1l1l11lll_opy_(),
            bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ᫇"): bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ᫈"),
            bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ᫉"): hook_type,
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ᫊"): hook_name
        }
        store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᫋")].append(uuid)
        bstack1l1ll1l11l1_opy_ = node.nodeid
        if hook_type == bstack11111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᫌ"):
            if not _11l11l1111_opy_.get(bstack1l1ll1l11l1_opy_, None):
                _11l11l1111_opy_[bstack1l1ll1l11l1_opy_] = {bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᫍ"): []}
            _11l11l1111_opy_[bstack1l1ll1l11l1_opy_][bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᫎ")].append(bstack111llll1ll_opy_[bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᫏")])
        _11l11l1111_opy_[bstack1l1ll1l11l1_opy_ + bstack11111_opy_ (u"ࠫ࠲࠭᫐") + hook_name] = bstack111llll1ll_opy_
        bstack1l1ll111lll_opy_(node, bstack111llll1ll_opy_, bstack11111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭᫑"))
    elif event == bstack11111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ᫒"):
        bstack11l1l11l1l_opy_ = node.nodeid + bstack11111_opy_ (u"ࠧ࠮ࠩ᫓") + hook_name
        _11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᫔")] = bstack1l1l11lll_opy_()
        bstack1l1ll11ll11_opy_(_11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᫕")])
        bstack1l1ll111lll_opy_(node, _11l11l1111_opy_[bstack11l1l11l1l_opy_], bstack11111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᫖"), bstack1l1ll1l11ll_opy_=bstack1l1ll111l1l_opy_)
def bstack1l1l1llllll_opy_():
    global bstack1l1ll1ll1ll_opy_
    if bstack1ll1l1l1ll_opy_():
        bstack1l1ll1ll1ll_opy_ = bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨ᫗")
    else:
        bstack1l1ll1ll1ll_opy_ = bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᫘")
@bstack1lll11llll_opy_.bstack1ll111111l1_opy_
def bstack1l1ll11l111_opy_():
    bstack1l1l1llllll_opy_()
    if bstack11l11l111_opy_():
        bstack1llllll1l1_opy_ = Config.bstack11lll111l_opy_()
        if bstack1llllll1l1_opy_.get_property(bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ᫙")):
            return
        bstack1l1lll111_opy_(bstack1ll11ll1l_opy_)
    try:
        bstack1ll1lll11ll_opy_(bstack1l1ll111ll1_opy_)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡷࠥࡶࡡࡵࡥ࡫࠾ࠥࢁࡽࠣ᫚").format(e))
bstack1l1ll11l111_opy_()