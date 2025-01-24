from datetime import datetime
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable

from litellm import ModelResponse
from loguru import logger

from notte.common.tracer import LlmTracer

if TYPE_CHECKING:
    from notte.llms.engine import LLMEngine


def trace_llm_usage(
    tracer: LlmTracer | None = None,
) -> Callable[[Callable[..., ModelResponse]], Callable[..., ModelResponse]]:
    def decorator(func: Callable[..., ModelResponse]) -> Callable[..., ModelResponse]:
        @wraps(func)
        def wrapper(
            engine: "LLMEngine",
            messages: list[dict[str, str]],
            model: str,
            **kwargs: Any,
        ) -> ModelResponse:
            # Call the original function
            response: ModelResponse = func(engine, messages, model, **kwargs)

            # Only trace if tracer is provided
            if tracer is not None:
                try:
                    _completion: str | None = response.choices[0].message.content  # type: ignore
                    completion: str = _completion or ""

                    usage = getattr(response, "usage", None)
                    usage_dict = (
                        {
                            "prompt_tokens": getattr(usage, "prompt_tokens", 0),
                            "completion_tokens": getattr(usage, "completion_tokens", 0),
                            "total_tokens": getattr(usage, "total_tokens", 0),
                        }
                        if usage
                        else {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
                    )

                    tracer.trace(
                        timestamp=datetime.now().isoformat(),
                        model=model,
                        messages=messages,
                        completion=completion,
                        usage=usage_dict,
                        metadata=kwargs.get("metadata"),
                    )
                except Exception as e:
                    logger.error(f"Error logging LLM usage: {str(e)}")

            return response

        return wrapper

    return decorator
