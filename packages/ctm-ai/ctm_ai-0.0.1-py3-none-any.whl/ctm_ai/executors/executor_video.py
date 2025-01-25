import os
from typing import Any, Union

from openai import OpenAI
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from ctm_ai.utils.loader import load_image

from ..messengers import Message
from ..utils import message_exponential_backoff
from .executor_base import BaseExecutor


@BaseExecutor.register_executor('video_executor')
class VideoExecutor(BaseExecutor):
    def init_model(self, *args: Any, **kwargs: Any) -> None:
        self.model = OpenAI()

    def convert_message_to_param(
        self, message: Message
    ) -> Union[
        ChatCompletionAssistantMessageParam,
        ChatCompletionSystemMessageParam,
        ChatCompletionUserMessageParam,
    ]:
        if message.content is None:
            raise ValueError('Message content cannot be None')
        if message.role == 'system':
            return ChatCompletionSystemMessageParam(
                role='system', content=message.content
            )
        elif message.role == 'user':
            return ChatCompletionUserMessageParam(role='user', content=message.content)
        elif message.role == 'assistant':
            return ChatCompletionAssistantMessageParam(
                role='assistant', content=message.content
            )
        else:
            raise ValueError(f'Unsupported message role: {message.role}')

    @message_exponential_backoff()
    def ask(
        self,
        messages: list[Message],
        max_token: int = 300,
        return_num: int = 5,
        *args: Any,
        **kwargs: Any,
    ) -> Message:
        model_messages = [
            self.convert_message_to_param(message) for message in messages
        ]

        video_frames_path = kwargs.get('video_frames_path')
        if not video_frames_path:
            raise ValueError(f'No video frames provided in kwargs, kwargs: {kwargs}')

        if not all(os.path.exists(path) for path in video_frames_path):
            missing_files = [
                path for path in video_frames_path if not os.path.exists(path)
            ]
            raise FileNotFoundError(f'Some video frames not found: {missing_files}')

        for path in video_frames_path:
            video_message = {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': 'Here is the relevant image frames of the video:',
                    },
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/jpeg;base64,{load_image(path)}'
                        },
                    },
                ],
            }
            model_messages.append(video_message)  # type: ignore[arg-type]

        response = self.model.chat.completions.create(
            model='gpt-4o',
            messages=model_messages,
            max_tokens=max_token,
            n=return_num,
        )

        gists = [response.choices[i].message.content for i in range(return_num)]
        return Message(
            role='assistant',
            content=gists[0],
            gist=gists[0],
            gists=gists,
        )
