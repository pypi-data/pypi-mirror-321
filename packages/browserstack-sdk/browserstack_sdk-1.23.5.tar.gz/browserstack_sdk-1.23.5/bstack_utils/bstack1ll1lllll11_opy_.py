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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack1llll111ll1_opy_
from browserstack_sdk.bstack1l1llll111_opy_ import bstack1l111ll11_opy_
def _1ll1ll1ll11_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1ll1lll11ll_opy_:
    def __init__(self, handler):
        self._1ll1lll1lll_opy_ = {}
        self._1ll1ll1ll1l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1l111ll11_opy_.version()
        if bstack1llll111ll1_opy_(pytest_version, bstack11111_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢᘠ")) >= 0:
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᘡ")] = Module._register_setup_function_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘢ")] = Module._register_setup_module_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘣ")] = Class._register_setup_class_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᘤ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᘥ"))
            Module._register_setup_module_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᘦ"))
            Class._register_setup_class_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᘧ"))
            Class._register_setup_method_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᘨ"))
        else:
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᘩ")] = Module._inject_setup_function_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᘪ")] = Module._inject_setup_module_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᘫ")] = Class._inject_setup_class_fixture
            self._1ll1lll1lll_opy_[bstack11111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᘬ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᘭ"))
            Module._inject_setup_module_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᘮ"))
            Class._inject_setup_class_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᘯ"))
            Class._inject_setup_method_fixture = self.bstack1ll1lll1ll1_opy_(bstack11111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘰ"))
    def bstack1ll1lll1l11_opy_(self, bstack1ll1lll1l1l_opy_, hook_type):
        bstack1ll1lll111l_opy_ = id(bstack1ll1lll1l1l_opy_.__class__)
        if (bstack1ll1lll111l_opy_, hook_type) in self._1ll1ll1ll1l_opy_:
            return
        meth = getattr(bstack1ll1lll1l1l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1ll1ll1ll1l_opy_[(bstack1ll1lll111l_opy_, hook_type)] = meth
            setattr(bstack1ll1lll1l1l_opy_, hook_type, self.bstack1ll1ll1lll1_opy_(hook_type, bstack1ll1lll111l_opy_))
    def bstack1ll1llll1ll_opy_(self, instance, bstack1ll1llll11l_opy_):
        if bstack1ll1llll11l_opy_ == bstack11111_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᘱ"):
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᘲ"))
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥᘳ"))
        if bstack1ll1llll11l_opy_ == bstack11111_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᘴ"):
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢᘵ"))
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦᘶ"))
        if bstack1ll1llll11l_opy_ == bstack11111_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᘷ"):
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤᘸ"))
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨᘹ"))
        if bstack1ll1llll11l_opy_ == bstack11111_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᘺ"):
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨᘻ"))
            self.bstack1ll1lll1l11_opy_(instance.obj, bstack11111_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥᘼ"))
    @staticmethod
    def bstack1ll1llll111_opy_(hook_type, func, args):
        if hook_type in [bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᘽ"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᘾ")]:
            _1ll1ll1ll11_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1ll1ll1lll1_opy_(self, hook_type, bstack1ll1lll111l_opy_):
        def bstack1ll1lll1111_opy_(arg=None):
            self.handler(hook_type, bstack11111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᘿ"))
            result = None
            try:
                bstack1ll1lll11l1_opy_ = self._1ll1ll1ll1l_opy_[(bstack1ll1lll111l_opy_, hook_type)]
                self.bstack1ll1llll111_opy_(hook_type, bstack1ll1lll11l1_opy_, (arg,))
                result = Result(result=bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᙀ"))
            except Exception as e:
                result = Result(result=bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᙁ"), exception=e)
                self.handler(hook_type, bstack11111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᙂ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᙃ"), result)
        def bstack1ll1llll1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack11111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᙄ"))
            result = None
            exception = None
            try:
                self.bstack1ll1llll111_opy_(hook_type, self._1ll1ll1ll1l_opy_[hook_type], (this, arg))
                result = Result(result=bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᙅ"))
            except Exception as e:
                result = Result(result=bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᙆ"), exception=e)
                self.handler(hook_type, bstack11111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᙇ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᙈ"), result)
        if hook_type in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᙉ"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᙊ")]:
            return bstack1ll1llll1l1_opy_
        return bstack1ll1lll1111_opy_
    def bstack1ll1lll1ll1_opy_(self, bstack1ll1llll11l_opy_):
        def bstack1ll1ll1llll_opy_(this, *args, **kwargs):
            self.bstack1ll1llll1ll_opy_(this, bstack1ll1llll11l_opy_)
            self._1ll1lll1lll_opy_[bstack1ll1llll11l_opy_](this, *args, **kwargs)
        return bstack1ll1ll1llll_opy_