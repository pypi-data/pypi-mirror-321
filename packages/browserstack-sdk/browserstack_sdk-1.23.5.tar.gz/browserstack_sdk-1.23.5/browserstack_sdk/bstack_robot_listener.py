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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11l1l1111l_opy_ import RobotHandler
from bstack_utils.capture import bstack11l1ll111l_opy_
from bstack_utils.bstack11l1l11ll1_opy_ import bstack11l11ll1l1_opy_, bstack11l1ll11l1_opy_, bstack11l1l1l1ll_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack1l1l11l1l1_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack1lll11llll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l11lll1ll_opy_, bstack1l1l11lll_opy_, Result, \
    bstack11l11ll11l_opy_, bstack11l11l1ll1_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪຮ"): [],
        bstack11111_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭ຯ"): [],
        bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬະ"): []
    }
    bstack11l1111l1l_opy_ = []
    bstack11l1111l11_opy_ = []
    @staticmethod
    def bstack11l1l1ll11_opy_(log):
        if not (log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪັ")] and log[bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫາ")].strip()):
            return
        active = bstack1l1l11l1l1_opy_.bstack11l1ll1lll_opy_()
        log = {
            bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪຳ"): log[bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫິ")],
            bstack11111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩີ"): bstack11l11l1ll1_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩຶ"),
            bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩື"): log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧຸࠪ")],
        }
        if active:
            if active[bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨູ")] == bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬຺ࠩ"):
                log[bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬົ")] = active[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ຼ")]
            elif active[bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬຽ")] == bstack11111_opy_ (u"ࠨࡶࡨࡷࡹ࠭຾"):
                log[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ຿")] = active[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪເ")]
        bstack1lll11llll_opy_.bstack11lll1l111_opy_([log])
    def __init__(self):
        self.messages = bstack11l111111l_opy_()
        self._11l11l1l11_opy_ = None
        self._111lll11l1_opy_ = None
        self._11l11l1111_opy_ = OrderedDict()
        self.bstack11l1ll1l1l_opy_ = bstack11l1ll111l_opy_(self.bstack11l1l1ll11_opy_)
    @bstack11l11ll11l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack111llll1l1_opy_()
        if not self._11l11l1111_opy_.get(attrs.get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧແ")), None):
            self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨໂ"))] = {}
        bstack11l111llll_opy_ = bstack11l1l1l1ll_opy_(
                bstack11l11111ll_opy_=attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩໃ")),
                name=name,
                bstack11l1lll11l_opy_=bstack1l1l11lll_opy_(),
                file_path=os.path.relpath(attrs[bstack11111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧໄ")], start=os.getcwd()) if attrs.get(bstack11111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໅")) != bstack11111_opy_ (u"ࠩࠪໆ") else bstack11111_opy_ (u"ࠪࠫ໇"),
                framework=bstack11111_opy_ (u"ࠫࡗࡵࡢࡰࡶ່ࠪ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨ້"), None)
        self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"࠭ࡩࡥ໊ࠩ"))][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣ໋ࠪ")] = bstack11l111llll_opy_
    @bstack11l11ll11l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11l11l1lll_opy_()
        self._11l11ll1ll_opy_(messages)
        for bstack111lllll11_opy_ in self.bstack11l1111l1l_opy_:
            bstack111lllll11_opy_[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ໌")][bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨໍ")].extend(self.store[bstack11111_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴࠩ໎")])
            bstack1lll11llll_opy_.bstack1l11l1l1l1_opy_(bstack111lllll11_opy_)
        self.bstack11l1111l1l_opy_ = []
        self.store[bstack11111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪ໏")] = []
    @bstack11l11ll11l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11l1ll1l1l_opy_.start()
        if not self._11l11l1111_opy_.get(attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨ໐")), None):
            self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩ໑"))] = {}
        driver = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭໒"), None)
        bstack11l1l11ll1_opy_ = bstack11l1l1l1ll_opy_(
            bstack11l11111ll_opy_=attrs.get(bstack11111_opy_ (u"ࠨ࡫ࡧࠫ໓")),
            name=name,
            bstack11l1lll11l_opy_=bstack1l1l11lll_opy_(),
            file_path=os.path.relpath(attrs[bstack11111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໔")], start=os.getcwd()),
            scope=RobotHandler.bstack111llll111_opy_(attrs.get(bstack11111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໕"), None)),
            framework=bstack11111_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪ໖"),
            tags=attrs[bstack11111_opy_ (u"ࠬࡺࡡࡨࡵࠪ໗")],
            hooks=self.store[bstack11111_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬ໘")],
            bstack11l1l1l11l_opy_=bstack1lll11llll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11111_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤ໙").format(bstack11111_opy_ (u"ࠣࠢࠥ໚").join(attrs[bstack11111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ໛")]), name) if attrs[bstack11111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨໜ")] else name
        )
        self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧໝ"))][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨໞ")] = bstack11l1l11ll1_opy_
        threading.current_thread().current_test_uuid = bstack11l1l11ll1_opy_.bstack111lllllll_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩໟ"), None)
        self.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ໠"), bstack11l1l11ll1_opy_)
    @bstack11l11ll11l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11l1ll1l1l_opy_.reset()
        bstack111lll1l1l_opy_ = bstack11l1111lll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ໡")), bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ໢"))
        self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"ࠪ࡭ࡩ࠭໣"))][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ໤")].stop(time=bstack1l1l11lll_opy_(), duration=int(attrs.get(bstack11111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪ໥"), bstack11111_opy_ (u"࠭࠰ࠨ໦"))), result=Result(result=bstack111lll1l1l_opy_, exception=attrs.get(bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ໧")), bstack11l1llll11_opy_=[attrs.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ໨"))]))
        self.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ໩"), self._11l11l1111_opy_[attrs.get(bstack11111_opy_ (u"ࠪ࡭ࡩ࠭໪"))][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ໫")], True)
        self.store[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩ໬")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11l11ll11l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack111llll1l1_opy_()
        current_test_id = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨ໭"), None)
        bstack111lll111l_opy_ = current_test_id if bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩ໮"), None) else bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫ໯"), None)
        if attrs.get(bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ໰"), bstack11111_opy_ (u"ࠪࠫ໱")).lower() in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ໲"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ໳")]:
            hook_type = bstack11l11lll1l_opy_(attrs.get(bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫ໴")), bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ໵"), None))
            hook_name = bstack11111_opy_ (u"ࠨࡽࢀࠫ໶").format(attrs.get(bstack11111_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩ໷"), bstack11111_opy_ (u"ࠪࠫ໸")))
            if hook_type in [bstack11111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨ໹"), bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ໺")]:
                hook_name = bstack11111_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧ໻").format(bstack111lllll1l_opy_.get(hook_type), attrs.get(bstack11111_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧ໼"), bstack11111_opy_ (u"ࠨࠩ໽")))
            bstack111llll1ll_opy_ = bstack11l1ll11l1_opy_(
                bstack11l11111ll_opy_=bstack111lll111l_opy_ + bstack11111_opy_ (u"ࠩ࠰ࠫ໾") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ໿"), bstack11111_opy_ (u"ࠫࠬༀ")).lower(),
                name=hook_name,
                bstack11l1lll11l_opy_=bstack1l1l11lll_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11111_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ༁")), start=os.getcwd()),
                framework=bstack11111_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ༂"),
                tags=attrs[bstack11111_opy_ (u"ࠧࡵࡣࡪࡷࠬ༃")],
                scope=RobotHandler.bstack111llll111_opy_(attrs.get(bstack11111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ༄"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack111llll1ll_opy_.bstack111lllllll_opy_()
            threading.current_thread().current_hook_id = bstack111lll111l_opy_ + bstack11111_opy_ (u"ࠩ࠰ࠫ༅") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ༆"), bstack11111_opy_ (u"ࠫࠬ༇")).lower()
            self.store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ༈")] = [bstack111llll1ll_opy_.bstack111lllllll_opy_()]
            if bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ༉"), None):
                self.store[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫ༊")].append(bstack111llll1ll_opy_.bstack111lllllll_opy_())
            else:
                self.store[bstack11111_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧ་")].append(bstack111llll1ll_opy_.bstack111lllllll_opy_())
            if bstack111lll111l_opy_:
                self._11l11l1111_opy_[bstack111lll111l_opy_ + bstack11111_opy_ (u"ࠩ࠰ࠫ༌") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ།"), bstack11111_opy_ (u"ࠫࠬ༎")).lower()] = { bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ༏"): bstack111llll1ll_opy_ }
            bstack1lll11llll_opy_.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ༐"), bstack111llll1ll_opy_)
        else:
            bstack11l1ll1l11_opy_ = {
                bstack11111_opy_ (u"ࠧࡪࡦࠪ༑"): uuid4().__str__(),
                bstack11111_opy_ (u"ࠨࡶࡨࡼࡹ࠭༒"): bstack11111_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨ༓").format(attrs.get(bstack11111_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ༔")), attrs.get(bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩ༕"), bstack11111_opy_ (u"ࠬ࠭༖"))) if attrs.get(bstack11111_opy_ (u"࠭ࡡࡳࡩࡶࠫ༗"), []) else attrs.get(bstack11111_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫༘ࠧ")),
                bstack11111_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨ༙"): attrs.get(bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ༚"), []),
                bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ༛"): bstack1l1l11lll_opy_(),
                bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ༜"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭༝"),
                bstack11111_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ༞"): attrs.get(bstack11111_opy_ (u"ࠧࡥࡱࡦࠫ༟"), bstack11111_opy_ (u"ࠨࠩ༠"))
            }
            if attrs.get(bstack11111_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪ༡"), bstack11111_opy_ (u"ࠪࠫ༢")) != bstack11111_opy_ (u"ࠫࠬ༣"):
                bstack11l1ll1l11_opy_[bstack11111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭༤")] = attrs.get(bstack11111_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࠧ༥"))
            if not self.bstack11l1111l11_opy_:
                self._11l11l1111_opy_[self._11l11l1l1l_opy_()][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ༦")].add_step(bstack11l1ll1l11_opy_)
                threading.current_thread().current_step_uuid = bstack11l1ll1l11_opy_[bstack11111_opy_ (u"ࠨ࡫ࡧࠫ༧")]
            self.bstack11l1111l11_opy_.append(bstack11l1ll1l11_opy_)
    @bstack11l11ll11l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11l11l1lll_opy_()
        self._11l11ll1ll_opy_(messages)
        current_test_id = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫ༨"), None)
        bstack111lll111l_opy_ = current_test_id if current_test_id else bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭༩"), None)
        bstack111lll1lll_opy_ = bstack11l1111lll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ༪")), bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭༫"))
        bstack11l11lllll_opy_ = attrs.get(bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ༬"))
        if bstack111lll1lll_opy_ != bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ༭") and not attrs.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ༮")) and self._11l11l1l11_opy_:
            bstack11l11lllll_opy_ = self._11l11l1l11_opy_
        bstack11l1l111ll_opy_ = Result(result=bstack111lll1lll_opy_, exception=bstack11l11lllll_opy_, bstack11l1llll11_opy_=[bstack11l11lllll_opy_])
        if attrs.get(bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ༯"), bstack11111_opy_ (u"ࠪࠫ༰")).lower() in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ༱"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ༲")]:
            bstack111lll111l_opy_ = current_test_id if current_test_id else bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩ༳"), None)
            if bstack111lll111l_opy_:
                bstack11l1l11l1l_opy_ = bstack111lll111l_opy_ + bstack11111_opy_ (u"ࠢ࠮ࠤ༴") + attrs.get(bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ༵࠭"), bstack11111_opy_ (u"ࠩࠪ༶")).lower()
                self._11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ༷࠭")].stop(time=bstack1l1l11lll_opy_(), duration=int(attrs.get(bstack11111_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩ༸"), bstack11111_opy_ (u"ࠬ࠶༹ࠧ"))), result=bstack11l1l111ll_opy_)
                bstack1lll11llll_opy_.bstack11l1l1lll1_opy_(bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ༺"), self._11l11l1111_opy_[bstack11l1l11l1l_opy_][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ༻")])
        else:
            bstack111lll111l_opy_ = current_test_id if current_test_id else bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪ༼"), None)
            if bstack111lll111l_opy_ and len(self.bstack11l1111l11_opy_) == 1:
                current_step_uuid = bstack1l11lll1ll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭༽"), None)
                self._11l11l1111_opy_[bstack111lll111l_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭༾")].bstack11l1l1l1l1_opy_(current_step_uuid, duration=int(attrs.get(bstack11111_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩ༿"), bstack11111_opy_ (u"ࠬ࠶ࠧཀ"))), result=bstack11l1l111ll_opy_)
            else:
                self.bstack11l11ll111_opy_(attrs)
            self.bstack11l1111l11_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11111_opy_ (u"࠭ࡨࡵ࡯࡯ࠫཁ"), bstack11111_opy_ (u"ࠧ࡯ࡱࠪག")) == bstack11111_opy_ (u"ࠨࡻࡨࡷࠬགྷ"):
                return
            self.messages.push(message)
            bstack11l111l11l_opy_ = []
            if bstack1l1l11l1l1_opy_.bstack11l1ll1lll_opy_():
                bstack11l111l11l_opy_.append({
                    bstack11111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬང"): bstack1l1l11lll_opy_(),
                    bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫཅ"): message.get(bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཆ")),
                    bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫཇ"): message.get(bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ཈")),
                    **bstack1l1l11l1l1_opy_.bstack11l1ll1lll_opy_()
                })
                if len(bstack11l111l11l_opy_) > 0:
                    bstack1lll11llll_opy_.bstack11lll1l111_opy_(bstack11l111l11l_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1lll11llll_opy_.bstack11l11l11l1_opy_()
    def bstack11l11ll111_opy_(self, bstack11l111l111_opy_):
        if not bstack1l1l11l1l1_opy_.bstack11l1ll1lll_opy_():
            return
        kwname = bstack11111_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭ཉ").format(bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨཊ")), bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧཋ"), bstack11111_opy_ (u"ࠪࠫཌ"))) if bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩཌྷ"), []) else bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬཎ"))
        error_message = bstack11111_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧཏ").format(kwname, bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧཐ")), str(bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩད"))))
        bstack11l11lll11_opy_ = bstack11111_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣདྷ").format(kwname, bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪན")))
        bstack11l11111l1_opy_ = error_message if bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཔ")) else bstack11l11lll11_opy_
        bstack11l11llll1_opy_ = {
            bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨཕ"): self.bstack11l1111l11_opy_[-1].get(bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪབ"), bstack1l1l11lll_opy_()),
            bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨབྷ"): bstack11l11111l1_opy_,
            bstack11111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧམ"): bstack11111_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨཙ") if bstack11l111l111_opy_.get(bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪཚ")) == bstack11111_opy_ (u"ࠫࡋࡇࡉࡍࠩཛ") else bstack11111_opy_ (u"ࠬࡏࡎࡇࡑࠪཛྷ"),
            **bstack1l1l11l1l1_opy_.bstack11l1ll1lll_opy_()
        }
        bstack1lll11llll_opy_.bstack11lll1l111_opy_([bstack11l11llll1_opy_])
    def _11l11l1l1l_opy_(self):
        for bstack11l11111ll_opy_ in reversed(self._11l11l1111_opy_):
            bstack11l111lll1_opy_ = bstack11l11111ll_opy_
            data = self._11l11l1111_opy_[bstack11l11111ll_opy_][bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཝ")]
            if isinstance(data, bstack11l1ll11l1_opy_):
                if not bstack11111_opy_ (u"ࠧࡆࡃࡆࡌࠬཞ") in data.bstack111llllll1_opy_():
                    return bstack11l111lll1_opy_
            else:
                return bstack11l111lll1_opy_
    def _11l11ll1ll_opy_(self, messages):
        try:
            bstack11l1111111_opy_ = BuiltIn().get_variable_value(bstack11111_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃࠢཟ")) in (bstack11l111ll11_opy_.DEBUG, bstack11l111ll11_opy_.TRACE)
            for message, bstack11l111l1l1_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪའ"))
                level = message.get(bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩཡ"))
                if level == bstack11l111ll11_opy_.FAIL:
                    self._11l11l1l11_opy_ = name or self._11l11l1l11_opy_
                    self._111lll11l1_opy_ = bstack11l111l1l1_opy_.get(bstack11111_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧར")) if bstack11l1111111_opy_ and bstack11l111l1l1_opy_ else self._111lll11l1_opy_
        except:
            pass
    @classmethod
    def bstack11l1l1lll1_opy_(self, event: str, bstack11l111l1ll_opy_: bstack11l11ll1l1_opy_, bstack11l1l11111_opy_=False):
        if event == bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧལ"):
            bstack11l111l1ll_opy_.set(hooks=self.store[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪཤ")])
        if event == bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨཥ"):
            event = bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪས")
        if bstack11l1l11111_opy_:
            bstack111lll11ll_opy_ = {
                bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ཧ"): event,
                bstack11l111l1ll_opy_.bstack111llll11l_opy_(): bstack11l111l1ll_opy_.bstack111lll1ll1_opy_(event)
            }
            self.bstack11l1111l1l_opy_.append(bstack111lll11ll_opy_)
        else:
            bstack1lll11llll_opy_.bstack11l1l1lll1_opy_(event, bstack11l111l1ll_opy_)
class bstack11l111111l_opy_:
    def __init__(self):
        self._11l1111ll1_opy_ = []
    def bstack111llll1l1_opy_(self):
        self._11l1111ll1_opy_.append([])
    def bstack11l11l1lll_opy_(self):
        return self._11l1111ll1_opy_.pop() if self._11l1111ll1_opy_ else list()
    def push(self, message):
        self._11l1111ll1_opy_[-1].append(message) if self._11l1111ll1_opy_ else self._11l1111ll1_opy_.append([message])
class bstack11l111ll11_opy_:
    FAIL = bstack11111_opy_ (u"ࠪࡊࡆࡏࡌࠨཨ")
    ERROR = bstack11111_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪཀྵ")
    WARNING = bstack11111_opy_ (u"ࠬ࡝ࡁࡓࡐࠪཪ")
    bstack11l111ll1l_opy_ = bstack11111_opy_ (u"࠭ࡉࡏࡈࡒࠫཫ")
    DEBUG = bstack11111_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭ཬ")
    TRACE = bstack11111_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧ཭")
    bstack11l11l111l_opy_ = [FAIL, ERROR]
def bstack111lll1l11_opy_(bstack11l11l11ll_opy_):
    if not bstack11l11l11ll_opy_:
        return None
    if bstack11l11l11ll_opy_.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ཮"), None):
        return getattr(bstack11l11l11ll_opy_[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭཯")], bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ཰"), None)
    return bstack11l11l11ll_opy_.get(bstack11111_opy_ (u"ࠬࡻࡵࡪࡦཱࠪ"), None)
def bstack11l11lll1l_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴིࠬ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ཱིࠩ")]:
        return
    if hook_type.lower() == bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶུࠧ"):
        if current_test_uuid is None:
            return bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑཱུ࠭")
        else:
            return bstack11111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨྲྀ")
    elif hook_type.lower() == bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ཷ"):
        if current_test_uuid is None:
            return bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨླྀ")
        else:
            return bstack11111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪཹ")