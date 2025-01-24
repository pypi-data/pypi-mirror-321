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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11l1l11ll_opy_ import get_logger
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llllllllll_opy_
bstack1ll1ll1lll_opy_ = bstack1llllllllll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1111l111l_opy_: Optional[str] = None):
    bstack11111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡅࡧࡦࡳࡷࡧࡴࡰࡴࠣࡸࡴࠦ࡬ࡰࡩࠣࡸ࡭࡫ࠠࡴࡶࡤࡶࡹࠦࡴࡪ࡯ࡨࠤࡴ࡬ࠠࡢࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࡦࡲ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺࠠ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡶࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᙳ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack111111l111_opy_: str = bstack1ll1ll1lll_opy_.bstack11111l11ll_opy_(label)
            start_mark: str = label + bstack11111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᙴ")
            end_mark: str = label + bstack11111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᙵ")
            result = None
            try:
                if stage.value == STAGE.bstack111ll1l1l_opy_.value:
                    bstack1ll1ll1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1111l111l_opy_)
                elif stage.value == STAGE.SINGLE.value:
                    start_mark: str = bstack111111l111_opy_ + bstack11111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᙶ")
                    end_mark: str = bstack111111l111_opy_ + bstack11111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᙷ")
                    bstack1ll1ll1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1111l111l_opy_)
            except Exception as e:
                bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1111l111l_opy_)
            return result
        return wrapper
    return decorator