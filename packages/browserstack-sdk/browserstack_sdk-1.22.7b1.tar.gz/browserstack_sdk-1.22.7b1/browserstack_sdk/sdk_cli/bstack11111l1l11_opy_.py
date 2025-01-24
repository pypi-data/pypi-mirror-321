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
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1111llll11_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack111111llll_opy_:
    bstack111111ll1l_opy_ = bstack1l1_opy_ (u"ࠤࡥࡩࡳࡩࡨ࡮ࡣࡵ࡯ࠧဈ")
    context: bstack1111llll11_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1111llll11_opy_):
        self.context = context
        self.data = dict({bstack111111llll_opy_.bstack111111ll1l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪဉ"), bstack1l1_opy_ (u"ࠫ࠵࠭ည")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack111111lll1_opy_(self, target: object):
        return bstack111111llll_opy_.create_context(target) == self.context
    def bstack11111l1l1l_opy_(self, context: bstack1111llll11_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack11l1ll11ll_opy_(self, key: str, value: timedelta):
        self.data[bstack111111llll_opy_.bstack111111ll1l_opy_][key] += value
    def bstack11111l1111_opy_(self) -> dict:
        return self.data[bstack111111llll_opy_.bstack111111ll1l_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1111llll11_opy_(
            id=id(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=type(target),
        )