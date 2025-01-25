# llm_manager.py
"""
A manager class for configuring and interacting with
Language Learning Models (LLMs) through a unified interface.
Handles provider configuration, initialization, and message passing using environment variables.
"""
import os
import importlib
from typing import Any, Dict, List, Optional, Tuple
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from .llm_providers import LLMProviders  # type: ignore


class LLMManager:
    """Internal manager class for LLM operations"""

    @staticmethod
    def configure_llm_backend(provider: str, model: str, **kwargs) -> None:
        """
        sets the environment variables necessary for a given LLM.
        """
        providers = LLMProviders.get_providers()
        if provider.lower() not in providers:
            raise ValueError(f"Unsupported provider: {provider}")

        # Clean up old LLM_ environment variables
        for key in list(os.environ.keys()):
            if key.startswith("LLM_"):
                del os.environ[key]

        os.environ["LLM_PROVIDER"] = provider.lower()
        os.environ["LLM_MODEL"] = model

        for key, value in kwargs.items():
            os.environ[f"LLM_{key.upper()}"] = str(value)

    @staticmethod
    def get_llm_config() -> Dict[str, Any]:
        """Retrieves the LLM configuration from environment variables."""
        provider = os.getenv("LLM_PROVIDER")
        model = os.getenv("LLM_MODEL")
        providers = LLMProviders.get_providers()

        if provider not in providers:
            raise ValueError(f"Unsupported provider: {provider}")

        provider_config = providers[provider]
        config = {
            "provider": provider,
            "model": model,
            "class": provider_config.class_name,
            "module": provider_config.module_path,
        }

        # Add all LLM_ prefixed environment variables to the config
        for key, value in os.environ.items():
            if key.startswith("LLM_") and key not in ["LLM_PROVIDER", "LLM_MODEL"]:
                config[key[4:].lower()] = value

        return config

    @staticmethod
    def get_llm(
        instance: Optional[Any], config: Optional[Dict[str, Any]], **kwargs
    ) -> Tuple[Any, Dict[str, Any]]:
        """Dynamically retrieves the appropriate LLM based on the configuration."""
        current_config = LLMManager.get_llm_config()

        # Check if instance exists and config hasn't changed
        if instance is not None and config == current_config:
            return instance, config

        try:
            module = importlib.import_module(current_config["module"])
            llm_class = getattr(module, current_config["class"])

            # Remove 'class' and 'module' from config before passing to constructor
            constructor_args = {
                k: v
                for k, v in current_config.items()
                if k not in ["class", "module", "provider"]
            }

            # Get provider config and initialize
            providers = LLMProviders.get_providers()
            provider_config = providers[current_config["provider"]]
            initializer = provider_config.init_class(provider_config)

            constructor_args, kwargs = initializer.initialize(
                constructor_args, **kwargs
            )

            instance = llm_class(**constructor_args)
            return instance, current_config

        except (ImportError, AttributeError) as e:
            raise ValueError(
                f"Error initializing provider {current_config['provider']}: {str(e)}"
            ) from e

    @staticmethod
    def call_llm(messages: List[Dict[str, str]], **kwargs) -> str:
        """Calls the configured LLM provider with the given parameters."""
        config = LLMManager.get_llm_config()
        llm, _ = LLMManager.get_llm(None, None, **kwargs)

        # Get provider config and initialize
        providers = LLMProviders.get_providers()
        provider_config = providers[config["provider"]]
        initializer = provider_config.init_class(provider_config)

        # Get additional kwargs from initializer
        _, kwargs = initializer.initialize({}, **kwargs)

        # Check if this model doesn't support system messages
        supports_system_messages = kwargs.pop("supports_system_messages", True)

        message_types = {
            "system": (
                SystemMessage if supports_system_messages is not False else HumanMessage
            ),
            "user": HumanMessage,
            "assistant": AIMessage,
        }

        langchain_messages = [
            message_types.get(msg["role"], HumanMessage)(content=msg["content"])
            for msg in messages
        ]

        response = llm(langchain_messages, **kwargs)

        # Write the response to a file
        with open(
            os.getenv("RESPONSE_PATH", "response.txt"), "a", encoding="utf-8"
        ) as f:
            f.write(f"{response}\n")

        return response.content.strip()

    @staticmethod
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
        A retry wrapper for call_llm.
        Implements custom retry behaviour, response processing, and failure handling.
        """
        call_llm_kwargs = call_llm_kwargs or {}
        process_response_kwargs = process_response_kwargs or {}
        failure_handler_kwargs = failure_handler_kwargs or {}

        for attempt in range(1, max_attempts + 1):
            # Adjust temperature if it's in call_llm_kwargs
            if "temperature" in call_llm_kwargs:
                call_llm_kwargs["temperature"] = (
                    0 if attempt <= 2 else (attempt - 2) * 0.025
                )

            # Call the LLM
            response = LLMManager.call_llm(messages=messages, **call_llm_kwargs)

            # Attempt to process the response
            try:
                processed_result = process_response(response, **process_response_kwargs)
                return processed_result
            except Exception as e:
                print(f"Attempt {attempt} failed: {str(e)}. Retrying...")
                print(f"Response from failed attempt:\n{response}")

        # If we've exhausted all attempts, call the failure handler
        print(f"All {max_attempts} attempts failed. Calling failure handler.")
        return failure_handler(**failure_handler_kwargs)
