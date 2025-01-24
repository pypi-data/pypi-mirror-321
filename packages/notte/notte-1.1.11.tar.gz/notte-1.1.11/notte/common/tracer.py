import datetime as dt
import json
from pathlib import Path
from typing import Any, ClassVar, Protocol

from typing_extensions import override


class Tracer(Protocol):
    """Protocol for database clients that handle LLM usage logging."""

    def trace(self, *args: Any, **kwargs: Any) -> None:
        """Log LLM usage to the database."""
        pass


class LlmTracer(Tracer):

    @override
    def trace(
        self,
        timestamp: str,
        model: str,
        messages: list[dict[str, str]],
        completion: str,
        usage: dict[str, int],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Log LLM usage to the database."""
        raise NotImplementedError


class LlmUsageFileTracer(LlmTracer):

    file_path: ClassVar[Path] = Path(__file__).parent.parent.parent / "llm_usage.jsonl"

    @override
    def trace(
        self,
        timestamp: str,
        model: str,
        messages: list[dict[str, str]],
        completion: str,
        usage: dict[str, int],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Log LLM usage to a file."""
        with open(self.file_path, "a") as f:
            json.dump(
                {
                    "timestamp": timestamp,
                    "model": model,
                    "messages": messages,
                    "completion": completion,
                    "usage": usage,
                },
                f,
            )
            _ = f.write("\n")


class LlmParsingErrorFileTracer(Tracer):

    file_path: ClassVar[Path] = Path(__file__).parent.parent.parent / "llm_parsing_error.jsonl"

    @override
    def trace(
        self,
        status: str,
        pipe_name: str,
        nb_retries: int,
        error_msgs: list[str],
    ) -> None:
        """Log LLM parsing errors to a file."""
        with open(self.file_path, "a") as f:
            json.dump(
                {
                    "timestamp": dt.datetime.now().isoformat(),
                    "status": status,
                    "pipe_name": pipe_name,
                    "nb_retries": nb_retries,
                    "error_msgs": error_msgs,
                },
                f,
            )
            _ = f.write("\n")
