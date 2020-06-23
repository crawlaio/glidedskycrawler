# -*- coding: utf-8 -*-
class LoginCookiesMiddleware:
    def __init__(self, cookies):
        self.cookies = cookies

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(cookies=settings.get("LOGIN_COOKIES"))

    def process_request(self, request, spider):
        request.cookies = self.cookies
