import os
import logging
import shutil

from sandbox_func.common.util.pathutil import get_tmp_path

logger = logging.getLogger(__name__)


def clear_directory(template_file_path):
    try:
        if template_file_path:
            _dir = os.path.dirname(template_file_path)
            logger.debug(f"删除导出目录: {_dir}")
            shutil.rmtree(_dir)
    except Exception as e:
        logger.exception(e)
        logger.debug("删除导出目录失败")


def get_request_tmp_path(request_id: str) -> str:
    return os.path.join(get_tmp_path(), "excel", request_id)