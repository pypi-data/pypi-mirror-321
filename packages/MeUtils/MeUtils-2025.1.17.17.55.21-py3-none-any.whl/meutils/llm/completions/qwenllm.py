#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : qwen
# @Time         : 2025/1/17 16:45
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.llm.clients import AsyncOpenAI
from meutils.llm.openai_utils import to_openai_params

from meutils.config_utils.lark_utils import get_next_token_for_polling
from meutils.schemas.openai_types import chat_completion, chat_completion_chunk, ChatCompletionRequest, CompletionUsage

FEISHU_URL = "https://xchatllm.feishu.cn/sheets/Bmjtst2f6hfMqFttbhLcdfRJnNf?sheet=PP1PGr"

base_url = "https://chat.qwenlm.ai/api"


async def create(request: ChatCompletionRequest):
    token = await get_next_token_for_polling(feishu_url=FEISHU_URL)

    client = AsyncOpenAI(base_url=base_url, api_key=token)
    data = to_openai_params(request)

    if request.stream:
        _chunk = ""
        async for chunk in await client.chat.completions.create(**data):
            chunk = chunk.choices[0].delta.content or ""
            yield chunk.removeprefix(_chunk)
            _chunk = chunk

    else:
        response = await client.chat.completions.create(**data)
        yield response.choices[0].message.content


if __name__ == '__main__':
    request = ChatCompletionRequest(
        # model="qwen-turbo-2024-11-01",
        # model="claude-3-5-sonnet-20241022",
        model="qwen-plus-latest",

        messages=[
            {
                'role': 'user',
                'content': 'hi'
            },

        ],
        stream=False,
    )
    arun(create(request))
