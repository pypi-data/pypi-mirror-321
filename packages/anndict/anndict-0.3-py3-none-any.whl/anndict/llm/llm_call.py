# llm_call
"""
A module for managing interactions with Large Language Models (LLMs) across providers.
Provides configuration, initialization, and retry mechanisms for making LLM calls
through a unified interface that works with OpenAI, Google, Anthropic and others.
"""
from typing import Any, Dict, List, Optional
from .llm_manager import LLMManager  # type: ignore

# Global instance management
_llm_instance: Optional[Any] = None
_llm_config: Optional[Dict[str, Any]] = None


def configure_llm_backend(provider: str, model: str, **kwargs) -> None:
    """
    Configures the LLM backend by setting environment variables.

    Args:
        provider (str): The LLM provider name
        model (str): The model name
        **kwargs: Additional configuration parameters

    Examples:
        # General (for most providers)
        configure_llm_backend('your-provider-name',
        'your-provider-model-name',
        api_key='your-provider-api-key')

        # For general example (OpenAI), works the same for providers google and anthropic.
        configure_llm_backend('openai', 'gpt-3.5-turbo', api_key='your-openai-api-key')
        configure_llm_backend('anthropic','claude-3-5-sonnet-20240620',
            api_key='your-anthropic-api-key'
        )

        # For AzureML Endpoint
        configure_llm_backend('azureml_endpoint','llama-2',
            endpoint_name='your-endpoint-name',region='your-region',api_key='your-api-key'
            )

        # For Bedrock
        configure_llm_backend('bedrock','anthropic.claude-v2',
        region_name='us-west-2',aws_access_key_id='your-access-key-id',
        aws_secret_access_key='your-secret-access-key'
        )
    """
    LLMManager.configure_llm_backend(provider, model, **kwargs)
    global _llm_instance, _llm_config
    _llm_instance = None
    _llm_config = None


def get_llm(**kwargs) -> Any:
    """Dynamically retrieves the appropriate LLM based on the configuration."""
    global _llm_instance, _llm_config
    return LLMManager.get_llm(_llm_instance, _llm_config, **kwargs)


def call_llm(messages: List[Dict[str, str]], **kwargs) -> str:
    """Calls the configured LLM provider with the given parameters."""
    return LLMManager.call_llm(messages, **kwargs)


def retry_call_llm(
    messages: List[Dict[str, str]],
    process_response,
    failure_handler,
    max_attempts: int = 5,
    call_llm_kwargs: Optional[Dict[str, Any]] = None,
    process_response_kwargs: Optional[Dict[str, Any]] = None,
    failure_handler_kwargs: Optional[Dict[str, Any]] = None,
) -> Any:
    """
    A generic wrapper for LLM calls that implements retry logic with custom processing
    and failure handling.
    """
    return LLMManager.retry_call_llm(
        messages=messages,
        process_response=process_response,
        failure_handler=failure_handler,
        max_attempts=max_attempts,
        call_llm_kwargs=call_llm_kwargs,
        process_response_kwargs=process_response_kwargs,
        failure_handler_kwargs=failure_handler_kwargs,
    )