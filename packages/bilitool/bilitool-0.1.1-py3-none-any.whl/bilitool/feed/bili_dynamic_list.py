# Copyright (c) 2025 bilitool

from bilitool.authenticate.wbi_sign import WbiSign
import random
import requests

class BiliDynamicList:
    def __init__(self, headers):
        self.headers = headers

    def get_dm_img(self, params):
        """Get the url params
        https://github.com/SocialSisterYi/bilibili-API-collect/issues/868#issuecomment-1916892809
        """

        dm_rand = 'ABCDEFGHIJK'
        params['dm_img_list'] ='[]'
        params['dm_img_str'] =''.join(random.sample(dm_rand, 2))
        params['dm_cover_img_str'] =''.join(random.sample(dm_rand, 2))
        params['dm_img_inter'] ='{"ds":[],"wh":[0,0,0],"of":[0,0,0]}'
        return params

    def get_dynamic_list(self, host_mid, offset='') -> dict:
        """Get the dynamic list of the user
        More details: https://socialsisteryi.github.io/bilibili-API-collect/docs/dynamic/space.html
        """

        params = {
            'host_mid': host_mid,
            'offset': offset,
        }
        params = WbiSign().get_wbi_signed_params(self.get_dm_img(params))
        response_json = requests.get('https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space',
                            headers=self.headers, params=params).json()
        if response_json.get('code') == -352:
            raise Exception("The interface is suspended")
        return response_json['data']