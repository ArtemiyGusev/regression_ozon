import pydantic
from appium.options.android import UiAutomator2Options
from typing import Literal, Optional

from mobile_utils import assist

EnvContext = Literal['personal', 'test', 'stage', 'prod']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'personal'

    # --- Appium Capabilities ---
    platformName: str = 'android'
    platformVersion: str = '9.0'
    deviceName: str = 'Google Pixel 3'
    app: Optional[str] = None
    appName: Optional[str] = None

    # --- > BrowserStack Capabilities ---
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    # --- > > BrowserStack credentials---
    usrName: Optional[str] = None
    accessKey: Optional[str] = None
    browserStackUrl: Optional[str] = None
    browserStackApi: Optional[str] = None

    # --- Remote Driver ---
    remote_url: str = f'http://{usrName}:{accessKey}@{browserStackUrl}'  # it's a default appium server url

    # --- Selene ---
    timeout: float = 6.0

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        options.device_name = self.deviceName
        options.platform_name = self.platformName
        options.app = (
            assist.file.abs_path_from_project(self.app)
            if self.app.startswith('./') or self.app.startswith('../')
            else self.app
        )

        if 'hub-cloud.browserstack' in self.remote_url:
            options.load_capabilities(
                {
                    'platformVersion': self.platformVersion,
                    'bstack:options': {
                        'projectName': self.projectName,
                        'buildName': self.buildName,
                        'sessionName': self.sessionName,
                        'userName': self.usrName,
                        'accessKey': self.accessKey,
                    },
                }
            )

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        asked_or_current = env or cls().context
        return cls(
            _env_file=assist.file.abs_path_from_project(
                f'config.{asked_or_current}.env.browserstack.example'
            )
        )


settings = Settings.in_context()
