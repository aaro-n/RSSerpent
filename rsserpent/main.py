import os
from pathlib import Path

import arrow
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette.templating import Jinja2Templates, _TemplateResponse as TemplateResponse

from .models import Feed, Plugin
from .plugins import plugins
from .utils import fetch_data
from .utils.provider import ProviderFn


templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
templates.env.autoescape = True
templates.env.globals["arrow"] = arrow


async def index(request: Request) -> TemplateResponse:
    """Return the index HTML web page."""
    return templates.TemplateResponse("index.html.jinja", {"request": request})


routes = [Route("/", endpoint=index)]


for plugin in plugins:
    for path, provider in plugin.routers.items():

        async def endpoint(
            request: Request, plugin: Plugin = plugin, provider: ProviderFn = provider
        ) -> TemplateResponse:
            """Return an RSS feed of XML format."""
            data = await fetch_data(
                provider, request.path_params, dict(request.query_params)
            )
            return templates.TemplateResponse(
                "rss.xml.jinja",
                {"data": Feed(**data), "plugin": plugin, "request": request},
                media_type="application/xml",
            )

        routes.append(Route(path, endpoint=endpoint))


app = Starlette(debug=bool(os.environ.get("DEBUG")), routes=routes)
