import os
import http.client
import json
from abc import ABC

from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class SourceTypeEnum(str, Enum):
    BLOOMBERG = "bloomberg"
    SCHWAB_NETWORK = "schwab_network"
    YAHOO_FINANCE = "yahoo_finance"

    def __str__(self):
        return str(self.name)


class Script(BaseModel):
    source_type: SourceTypeEnum
    start: datetime
    end: datetime
    content: str

    @classmethod
    def from_response(cls, response: dict):
        return cls(
            source_type=SourceTypeEnum(response["source_type"]),
            start=datetime.fromisoformat(response["start_time"]),
            end=datetime.fromisoformat(response["end_time"]),
            content=response["content"],
        )


class __BaseYoutubeScriptClient(ABC):
    __token: str
    __host: str = "youtube-stt-collector.vaquum.quantit.io"

    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)

    def __init__(self):
        # 환경변수에서 토큰을 가져옵니다.
        self.__token = os.getenv("FINTER_API_KEY", None)
        if self.__token is None:
            raise ValueError(
                "토큰이 필요합니다.\n환경변수에 FINTER_API_KEY를 설정해주세요"
            )

    @property
    def __headers(self):
        return {
            "Authorization": self.__token,
            "Content-Type": "application/json",
        }

    @staticmethod
    def data_serializer(obj):
        if isinstance(obj, datetime):
            # datetime을 ISO 8601 형식으로 변환
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} is not serializable")

    def _get_script(self, **kwargs):
        conn = http.client.HTTPSConnection(self.__host)
        try:
            # 요청 전송
            conn.request(
                method="GET",
                url="/script/",
                body=json.dumps(kwargs, cls=self.JSONEncoder),
                headers=self.__headers,
            )

            # 응답 수신
            response = conn.getresponse()
            response_data = response.read().decode("utf-8")
        finally:
            # 연결 닫기
            conn.close()

        if response.status != 200:
            raise Exception(f"Error: {response_data}")

        return Script.from_response(json.loads(response_data))


class YoutubeScriptClient(__BaseYoutubeScriptClient):
    def __init__(self):
        super().__init__()

    def get_script(
        self,
        start: datetime,
        end: datetime,
        source_type: SourceTypeEnum,
    ) -> Script:
        return self._get_script(
            source_type=source_type.name,
            start_time=start.isoformat(),
            end_time=end.isoformat(),
        )

    @staticmethod
    def bloomberg() -> "BloombergScriptClient":
        """blomberg source type을 사용하는 YoutubeScriptClient를 반환합니다."""
        return BloombergScriptClient()

    @staticmethod
    def schwab_network() -> "SchwabNetworkScriptClient":
        """schwab_network source type을 사용하는 YoutubeScriptClient를 반환합니다."""
        return SchwabNetworkScriptClient()

    @staticmethod
    def yahoo_finance() -> "YahooFinanceScriptClient":
        """yahoo_finance source type을 사용하는 YoutubeScriptClient를 반환합니다."""
        return YahooFinanceScriptClient()


class __YoutubeScriptClient(__BaseYoutubeScriptClient):
    source_type: SourceTypeEnum

    def __init__(self, source_type: SourceTypeEnum):
        super().__init__()
        self.source_type = source_type

    def get_script(self, start: datetime, end: datetime):
        return self._get_script(
            source_type=self.source_type.name,
            start_time=start,
            end_time=end,
        )


class BloombergScriptClient(__YoutubeScriptClient):
    def __init__(self):
        super().__init__(source_type=SourceTypeEnum.BLOOMBERG)


class SchwabNetworkScriptClient(__YoutubeScriptClient):
    def __init__(self):
        super().__init__(source_type=SourceTypeEnum.SCHWAB_NETWORK)


class YahooFinanceScriptClient(__YoutubeScriptClient):
    def __init__(self):
        super().__init__(source_type=SourceTypeEnum.YAHOO_FINANCE)
