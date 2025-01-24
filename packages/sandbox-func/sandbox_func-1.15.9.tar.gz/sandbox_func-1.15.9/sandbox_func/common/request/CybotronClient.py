import logging
import contextvars
import httpx

from sandbox_func.common.config.LoginConfig import DefaultLoginConfig
from sandbox_func.common.config.BaseURLConfig import DefaultURLConfig

logger = logging.getLogger(__name__)
ENV = DefaultLoginConfig.get_env()
TENANT_ID = contextvars.ContextVar('Id of tenant')
TRACE_ID = contextvars.ContextVar('Trace id')


def get_base_url() -> str:
    if DefaultLoginConfig.unit_test:
        return DefaultURLConfig.get_api_base_url(ENV)
    else:
        return 'http://localhost:{}'.format(9000 if DefaultLoginConfig.is_online else 8081)  # 区分沙盒边车和CLI边车端口


class CybotronClient:
    Client = httpx.AsyncClient(base_url=get_base_url(), timeout=httpx.Timeout(30.0))

    def __init__(self, throw_exception: bool = True):
        self.throw_exception = throw_exception
        self.client = CybotronClient.Client

    @staticmethod
    def __get_headers(method, url) -> dict:
        # 单元测试时从配置文件中获取
        if DefaultLoginConfig.unit_test:
            headers = {
                'X-API-KEY': DefaultLoginConfig.get_api_key(),
                'X-TENANT-ID': DefaultLoginConfig.get_tenant_id()
            }
        else:
            headers = {
                'X-TENANT-ID': TENANT_ID.get(),
                'Original-Request': '{}__{}'.format(method, url),
                'traceId': TRACE_ID.get()
            }
        return headers

    async def get(self, url, params=None):
        return await self.send(url, method="get", params=params)

    async def send(self, url, method, data=None, files=None, json=None, params=None):
        headers = CybotronClient.__get_headers(method, url)
        # 除单元测试外，全部进行转发
        if not DefaultLoginConfig.unit_test:
            method, url = 'post', '/forward-request'
        logging.info('发送业务请求: method({}), url({})'.format(method, str(self.client.base_url) + url))
        logging.info('请求参数: data({}), json({}), params({})'.format(data, json, params))
        request = self.client.build_request(method=method, url=url, data=data, json=json, files=files,
                                            params=params, headers=headers)
        response = await self.client.send(request)
        response_json = response.json()

        if self.throw_exception:
            if response_json.get("errorMessage"):
                raise Exception(response_json.get("errorMessage"))
            if not response_json.get("success"):
                msg = f"code: {response_json.get('code')}, msg: {response_json.get('message')}"
                raise Exception(msg)
        return response_json

    async def post(self, url, data=None, files=None, json=None):
        return await self.send(url, method="post", data=data, files=files, json=json)
