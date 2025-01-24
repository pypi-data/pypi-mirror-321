from typing import List, Optional, Union
from pydantic import BaseModel

from foundationallm.models.orchestration import (
    AnalysisResult,
    ContentArtifact,
    OpenAIImageFileMessageContentItem,
    OpenAITextMessageContentItem
)

class CompletionResponse(BaseModel):
    """
    Response from a language model.
    """
    id: Optional[str] = None
    operation_id: str
    user_prompt: str
    user_prompt_rewrite: Optional[str] = None
    full_prompt: Optional[str] = None
    content: Optional[
        List[
            Union[
                OpenAIImageFileMessageContentItem,
                OpenAITextMessageContentItem
            ]
        ]
    ] = None
    analysis_results: Optional[List[AnalysisResult]] = []
    content_artifacts: Optional[List[ContentArtifact]] = []
    user_prompt_embedding: Optional[List[float]] = []
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    total_cost: float = 0.0
    errors: Optional[List[str]] = []
