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
import threading
bstack1ll11ll11ll_opy_ = 1000
bstack1ll11l1l1ll_opy_ = 5
bstack1ll11ll11l1_opy_ = 30
bstack1ll11l1ll1l_opy_ = 2
class bstack1ll11l1ll11_opy_:
    def __init__(self, handler, bstack1ll11ll1111_opy_=bstack1ll11ll11ll_opy_, bstack1ll11l1lll1_opy_=bstack1ll11l1l1ll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1ll11ll1111_opy_ = bstack1ll11ll1111_opy_
        self.bstack1ll11l1lll1_opy_ = bstack1ll11l1lll1_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1ll11l1l11l_opy_()
    def bstack1ll11l1l11l_opy_(self):
        self.timer = threading.Timer(self.bstack1ll11l1lll1_opy_, self.bstack1ll11l1llll_opy_)
        self.timer.start()
    def bstack1ll11l1l1l1_opy_(self):
        self.timer.cancel()
    def bstack1ll11ll1l11_opy_(self):
        self.bstack1ll11l1l1l1_opy_()
        self.bstack1ll11l1l11l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1ll11ll1111_opy_:
                t = threading.Thread(target=self.bstack1ll11l1llll_opy_)
                t.start()
                self.bstack1ll11ll1l11_opy_()
    def bstack1ll11l1llll_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1ll11ll1111_opy_]
        del self.queue[:self.bstack1ll11ll1111_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1ll11l1l1l1_opy_()
        while len(self.queue) > 0:
            self.bstack1ll11l1llll_opy_()