class AbstractWowApiSearchRequest:
    orderBy = "id"
    _page = 1

    def __init__(self, orderBy, page):
        self.orderBy = orderBy
        self._page = page