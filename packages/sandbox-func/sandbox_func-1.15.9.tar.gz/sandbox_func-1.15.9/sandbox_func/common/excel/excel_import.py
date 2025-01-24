import logging
import functools
import os
import time
import urllib.parse

from sandbox_func.common.file.LTFileManager import LTFileManager
from sandbox_func.request.SFRequest import SFRequest
from sandbox_func.request.SFResponse import SFResponse
from sandbox_func.service.SandboxFuncService import SandboxFuncService
from sandbox_func.common.excel.utils import clear_directory, get_request_tmp_path

logger = logging.getLogger(__name__)

file_ins = LTFileManager(None, None)


def excel_import(func):
    """
    导入装饰器，实现导出方法通用逻辑
    执行前：模板下载
    执行后：文件上传
    :param func:
    :return:
    """
    @functools.wraps(func)
    async def wrapper(request: SFRequest, response: SFResponse):
        local_file_path, original_file = None, None
        try:
            local_file_path = await parse_input(request.input, request.request_id)
            original_file = request.input["file_url"]
            request.input["local_file_path"] = local_file_path

            start_time = time.time()
            logger.debug(f"开始执行导入方法：{func}")
            await SandboxFuncService.update_async_job(request.job_id, status="PROCESSING", progress=40,
                                                      loading_message='准备处理导入数据')
            result = await func(request, response)
            await SandboxFuncService.update_async_job(request.job_id, status="PROCESSING", progress=80,
                                                      loading_message='导入数据处理完成')
            elapsed_time = round(time.time() - start_time, 4)
            logger.debug(f"导入方法执行完成: {result}")
            logger.debug(f"导入耗时：{elapsed_time}")

            res = await parse_output(result, original_file)
            return res
        except Exception as e:
            logger.exception(e)
            error_msg = str(e)
            logger.debug(f"导入方法执行失败：{error_msg}")
            return {"originalFile": original_file, "output": None, "fileKey": None,
                    "successCount": 0, "errorCount": 0, "errorMessage": error_msg}
        finally:
            clear_directory(local_file_path)

    return wrapper


async def parse_input(params, request_id):
    required_params = ["app_id", "table_id", "file_url"]
    if params is None or any(_p not in params for _p in required_params):
        raise Exception("导入方法缺少必要输入参数：应用，数据表，导入文件")

    logger.debug("开始下载导入文件...")
    tmp_path = get_request_tmp_path(request_id)
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    import_file_path = await file_ins.download_file(params["file_url"], tmp_path)
    logger.debug(f"下载导入文件完成: {import_file_path}")
    return import_file_path


async def parse_output(result, original_file):
    _local_path = None
    required_params = ["output", "successCount", "errorCount"]
    try:
        if isinstance(result, dict):
            if any(_p not in result for _p in required_params):
                raise Exception(
                    "导入方法输出参数需要包含导入结果文件地址、成功数量、失败数量，"
                    "例如：{'output': '/mnt/import_result.xlsx', 'successCount': 10, 'errorCount': 1}'}")
            cloud_path = None
            _local_path = result['output']
            if not os.path.exists(result["output"]):
                _local_path = None
                raise Exception(f"当前返回导入结果文件地址错误，未找到相关文件：{_local_path}")
            if result['errorCount'] > 0:
                logger.debug("存在导入错误的行，开始上传导入结果文件...")
                cloud_path = await file_ins.upload_file(_local_path)
                logger.debug(f"上传导入结果文件完成: {cloud_path}")
            else:
                logger.debug(f"导入全部成功，跳过上传结果文件")
            return {"originalFile": original_file, "output": cloud_path,
                    "fileKey": urllib.parse.unquote(os.path.basename(cloud_path)) if cloud_path else None,
                    "successCount": result['successCount'], "errorCount": result['errorCount'], "errorMessage": None}
        else:
            raise Exception("导入方法输出参数应为字典，需要包含导入结果文件地址、成功数量、失败数量，例如：{'output': "
                            "'/tmp/import_result.xlsx', 'successCount': 10, 'errorCount': 1}'}")
    finally:
        if _local_path and os.path.exists(_local_path):
            logger.debug(f"删除本地导入结果文件：{result['output']}")
            os.remove(result["output"])
