from __future__ import annotations

from pydantic import BaseModel

from .settings import settings


class PixelLabClient(BaseModel):
    secret: str
    base_url: str = "https://api.pixellab.ai/v1"

    @classmethod
    def from_env(cls) -> PixelLabClient:
        return cls(**settings(env_file=None).model_dump(exclude_none=True))

    @classmethod
    def from_env_file(cls, env_file: str) -> PixelLabClient:
        return cls(**settings(env_file=env_file).model_dump(exclude_none=True))

    def auth_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token()}",
        }

    def headers(self):
        return {"Authorization": f"Bearer {self.secret}"}

    from .animate_with_skeleton import animate_with_skeleton
    from .generate_image_bitforge import generate_image_bitforge
    from .generate_image_pixflux import generate_image_pixflux
    from .inpaint import inpaint
    from .rotate import rotate
    from .get_balance import get_balance
