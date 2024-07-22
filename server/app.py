import asyncio
from asyncio import sleep
import itertools
from typing import AsyncGenerator, Dict
from litestar.config.cors import CORSConfig
from uuid import uuid4

from litestar import Litestar, MediaType, Request, Response, get
from litestar.response import ServerSentEvent, ServerSentEventMessage
from litestar.types import SSEData


import json

async def result_notifier() -> AsyncGenerator[SSEData, None]:
    # keep state per client, re-render template fragment
    count = 0

    while count < 10:
        await sleep(1)
        count += 1
        print(count)
        yield ServerSentEventMessage(event="progress", data=count)

        if count == 7:
            # close connection
            yield ServerSentEventMessage(
                event="result", data=json.dumps({"msg": "yeee"})
            )
            yield ServerSentEventMessage(event="close")
            return


@get("/")
async def get_hello_world() -> Dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}


@get("/progress", sync_to_thread=False)
async def get_progress(request: Request) -> ServerSentEvent:
    """Handler function that returns a greeting dictionary."""    

    sseEvent = ServerSentEvent(result_notifier())
    return sseEvent


cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(route_handlers=[get_hello_world, get_progress], cors_config=cors_config)
