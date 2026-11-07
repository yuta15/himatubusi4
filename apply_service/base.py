from abc import ABC, abstractmethod

from .common import Provider, Request, Result


class Applier(ABC):
    def _print(
        self,
        provider: Provider,
        resource_type: str,
        **fields: object,
    ) -> None:
        """リソースの見出しと、項目名を揃えた詳細を出力する。"""
        width = max((len(key) for key in fields), default=0)
        lines = [f"[{provider}/{resource_type}]"]
        lines.extend(f"  {key:<{width}} : {value}" for key, value in fields.items())
        print("\n".join(lines))

    @abstractmethod
    def apply(self) -> Result: ...


class Builder(ABC):
    @abstractmethod
    def build(self, request: Request) -> Applier: ...
