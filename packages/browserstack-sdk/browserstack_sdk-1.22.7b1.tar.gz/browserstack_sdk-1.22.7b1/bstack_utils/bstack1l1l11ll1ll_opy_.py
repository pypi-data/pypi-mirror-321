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
import threading
bstack1l11lll111l_opy_ = 1000
bstack1l11lll11l1_opy_ = 5
bstack1l11ll1ll1l_opy_ = 30
bstack1l11lll1l1l_opy_ = 2
class bstack1l11lll1l11_opy_:
    def __init__(self, handler, bstack1l11lll11ll_opy_=bstack1l11lll111l_opy_, bstack1l11ll1l1ll_opy_=bstack1l11lll11l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1l11lll11ll_opy_ = bstack1l11lll11ll_opy_
        self.bstack1l11ll1l1ll_opy_ = bstack1l11ll1l1ll_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1l11lll1111_opy_()
    def bstack1l11lll1111_opy_(self):
        self.timer = threading.Timer(self.bstack1l11ll1l1ll_opy_, self.bstack1l11ll1llll_opy_)
        self.timer.start()
    def bstack1l11ll1ll11_opy_(self):
        self.timer.cancel()
    def bstack1l11ll1lll1_opy_(self):
        self.bstack1l11ll1ll11_opy_()
        self.bstack1l11lll1111_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1l11lll11ll_opy_:
                t = threading.Thread(target=self.bstack1l11ll1llll_opy_)
                t.start()
                self.bstack1l11ll1lll1_opy_()
    def bstack1l11ll1llll_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1l11lll11ll_opy_]
        del self.queue[:self.bstack1l11lll11ll_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1l11ll1ll11_opy_()
        while len(self.queue) > 0:
            self.bstack1l11ll1llll_opy_()