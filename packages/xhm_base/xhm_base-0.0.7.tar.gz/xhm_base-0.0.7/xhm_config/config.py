import os
from dynaconf import Dynaconf

# 使用 try-except 判断是否安装了 Redis
try:
    from redis.connection import ConnectionPool
    from xhm_redis import XHMRedis

    REDIS_ENABLED = True
except ImportError:
    REDIS_ENABLED = False


class CacheConfig:
    root_path: str = None

    def get_pool(self):
        if REDIS_ENABLED:
            return ConnectionPool(
                host=self.settings.xhm_config_redis.host,
                port=self.settings.xhm_config_redis.port,
                password=self.settings.xhm_config_redis.password,
                db=self.settings.xhm_config_redis.db,
                encoding="utf-8",
                decode_responses=True,
            )
        return None

    def __init__(self):
        # 加载系统文件配置
        self.sys_settings = Dynaconf(settings_files=self._get_sys_settings(),
                                     envvar_prefix="xhm",
                                     environments=False,
                                     load_dotenv=False,
                                     redis_enabled=False
                                     )

        self.env = self.sys_settings.get("xhm.activate", "")

        # 加载配置
        self.settings = Dynaconf(
            settings_files=self._get_settings_files(),
            environments=True,  # 启用分层配置
            load_dotenv=False,  # 不加载环境变量
            redis_enabled=False,  # 启用 Redis 后端
        )

        # 初始化redis
        if self.settings.cache_mode and REDIS_ENABLED:
            self._cache = XHMRedis(connection_pool=self.get_pool())
        else:
            self._cache = None

    def _get_settings_files(self):
        # 获取项目配置文件路径
        project_files = self._get_project_path()  # 这里返回的是一个列表

        # 获取 SDK 配置文件路径
        sdk_settings_file = os.path.join(os.path.dirname(__file__), 'sdk_settings.toml')
        sdk_secrets_file = os.path.join(os.path.dirname(__file__), 'sdk_secrets.toml')

        # 定义所有文件路径（按优先级顺序）
        files = [sdk_settings_file, sdk_secrets_file] + project_files

        # 加载存在的文件
        return [file for file in files if os.path.exists(file)]

    def _get_sys_settings(self):
        # 获取项目配置文件路径
        project_application_file = os.path.join(os.getcwd(), 'application.toml')

        # 获取 SDK 配置文件路径
        sdk_application_file = os.path.join(os.path.dirname(__file__), 'application.toml')

        # 定义所有文件路径（按优先级顺序）
        files = [sdk_application_file, project_application_file]

        # 加载存在的文件
        return [file for file in files if os.path.exists(file)]

    def get(self, key: str):
        return self._get_width_cache_mode(key) or self.settings.get(key, None)

    def set(self, key: str, value: any):
        if self._cache:
            self._cache.set(key, value)
        else:
            raise Exception("只允许对缓存中的值进行变更，不允许对配置文件进行变更")

    def _get_width_cache_mode(self, key: str):
        # 缓存模式
        if self.settings.cache_mode == "all" or self.settings.cache_mode == "preferred" and self.settings.get(
                f"{key}_cache", False):
            return self._cache.get(key) if self._cache else None
        return None

    def all(self):
        return self.settings.as_dict()

    def info(self):
        project_settings_file, project_secrets_file = self._get_project_path()
        return {
            "env": self.env,
            "root_path": self.get_root_path(),
            "project_settings": project_settings_file,
            "project_secrets": project_secrets_file}

    def _get_project_path(self):
        base_path = os.getcwd()
        if not self.env:
            file_names = [f'application.toml', '.secrets.toml']
        else:
            file_names = [f'application_{self.env}.toml', f'.secrets_{self.env}.toml']
        return [os.path.join(base_path, file_name) for file_name in file_names]

    def get_root_path(self):
        return self.root_path if self.root_path else os.getcwd()

    def set_root_path(self, root_path: str):
        self.root_path = root_path


conf = CacheConfig()
