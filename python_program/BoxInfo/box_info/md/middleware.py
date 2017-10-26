#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
from django.shortcuts import HttpResponse


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Access_permission(MiddlewareMixin):
    def process_request(self, request):
        client_ip = request.META['REMOTE_ADDR']
        print(client_ip)
        url_path = ['/suntv/index/', "/login/", "/suntv/BoxInfo/", "/logout/", "/admin/"]
        if request.path_info in url_path:
            if request.path_info == "/suntv/BoxInfo/":
                client_ip = request.META['REMOTE_ADDR']
                code = re.findall("127.0.0", client_ip)
                print(client_ip)
                if not code:
                   return HttpResponse('403')
            else:
                return None
        else:
            return HttpResponse("404")

    def process_response(self, request, response):
        return response