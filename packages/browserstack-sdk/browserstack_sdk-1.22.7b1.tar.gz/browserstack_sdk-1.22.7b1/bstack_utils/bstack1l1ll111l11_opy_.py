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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack1l1ll1111l1_opy_
from browserstack_sdk.bstack1111llll_opy_ import bstack11l11111_opy_
def _1l1l1ll1l1l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1l1l1llllll_opy_:
    def __init__(self, handler):
        self._1l1ll111111_opy_ = {}
        self._1l1l1lllll1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11l11111_opy_.version()
        if bstack1l1ll1111l1_opy_(pytest_version, bstack1l1_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨᏌ")) >= 0:
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᏍ")] = Module._register_setup_function_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᏎ")] = Module._register_setup_module_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᏏ")] = Class._register_setup_class_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᏐ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᏑ"))
            Module._register_setup_module_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᏒ"))
            Class._register_setup_class_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᏓ"))
            Class._register_setup_method_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᏔ"))
        else:
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᏕ")] = Module._inject_setup_function_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᏖ")] = Module._inject_setup_module_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᏗ")] = Class._inject_setup_class_fixture
            self._1l1ll111111_opy_[bstack1l1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ꮨ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᏙ"))
            Module._inject_setup_module_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᏚ"))
            Class._inject_setup_class_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᏛ"))
            Class._inject_setup_method_fixture = self.bstack1l1ll11111l_opy_(bstack1l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᏜ"))
    def bstack1l1l1llll1l_opy_(self, bstack1l1l1ll1lll_opy_, hook_type):
        bstack1l1ll111l1l_opy_ = id(bstack1l1l1ll1lll_opy_.__class__)
        if (bstack1l1ll111l1l_opy_, hook_type) in self._1l1l1lllll1_opy_:
            return
        meth = getattr(bstack1l1l1ll1lll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1l1l1lllll1_opy_[(bstack1l1ll111l1l_opy_, hook_type)] = meth
            setattr(bstack1l1l1ll1lll_opy_, hook_type, self.bstack1l1l1ll1ll1_opy_(hook_type, bstack1l1ll111l1l_opy_))
    def bstack1l1l1lll1l1_opy_(self, instance, bstack1l1ll1111ll_opy_):
        if bstack1l1ll1111ll_opy_ == bstack1l1_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᏝ"):
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧᏞ"))
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤᏟ"))
        if bstack1l1ll1111ll_opy_ == bstack1l1_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᏠ"):
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨᏡ"))
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥᏢ"))
        if bstack1l1ll1111ll_opy_ == bstack1l1_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤᏣ"):
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣᏤ"))
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧᏥ"))
        if bstack1l1ll1111ll_opy_ == bstack1l1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᏦ"):
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧᏧ"))
            self.bstack1l1l1llll1l_opy_(instance.obj, bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤᏨ"))
    @staticmethod
    def bstack1l1l1lll11l_opy_(hook_type, func, args):
        if hook_type in [bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᏩ"), bstack1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᏪ")]:
            _1l1l1ll1l1l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1l1l1ll1ll1_opy_(self, hook_type, bstack1l1ll111l1l_opy_):
        def bstack1l1l1llll11_opy_(arg=None):
            self.handler(hook_type, bstack1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᏫ"))
            result = None
            try:
                bstack1l1llll1lll_opy_ = self._1l1l1lllll1_opy_[(bstack1l1ll111l1l_opy_, hook_type)]
                self.bstack1l1l1lll11l_opy_(hook_type, bstack1l1llll1lll_opy_, (arg,))
                result = Result(result=bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᏬ"))
            except Exception as e:
                result = Result(result=bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᏭ"), exception=e)
                self.handler(hook_type, bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᏮ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭Ꮿ"), result)
        def bstack1l1l1lll1ll_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨᏰ"))
            result = None
            exception = None
            try:
                self.bstack1l1l1lll11l_opy_(hook_type, self._1l1l1lllll1_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᏱ"))
            except Exception as e:
                result = Result(result=bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᏲ"), exception=e)
                self.handler(hook_type, bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᏳ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᏴ"), result)
        if hook_type in [bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬᏵ"), bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ᏶")]:
            return bstack1l1l1lll1ll_opy_
        return bstack1l1l1llll11_opy_
    def bstack1l1ll11111l_opy_(self, bstack1l1ll1111ll_opy_):
        def bstack1l1l1lll111_opy_(this, *args, **kwargs):
            self.bstack1l1l1lll1l1_opy_(this, bstack1l1ll1111ll_opy_)
            self._1l1ll111111_opy_[bstack1l1ll1111ll_opy_](this, *args, **kwargs)
        return bstack1l1l1lll111_opy_