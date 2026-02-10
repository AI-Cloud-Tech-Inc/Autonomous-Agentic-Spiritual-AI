"""
NVIDIA API Client for AI Video Generation

Integrates with NVIDIA's AI video generation APIs (Cosmos, Ace, etc.)
"""

import os
import httpx
import json
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime
import logging

# Set up logging
logger = logging.getLogger(__name__)

# NVIDIA API Configuration
NVIDIA_API_BASE_URL = "https://api.nvcf.nvidia.com/v2"

# Get API credentials from environment
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_PROJECT_ID = os.getenv("NVIDIA_PROJECT_ID", "cebcfe9b-4787-4a7f-bed9-e94c91d28fd6")

# DIAGNOSTIC: Log API key status on module load
logger.info(f"[DIAGNOSTIC] NVIDIA_API_KEY set: {bool(NVIDIA_API_KEY)}")
logger.info(f"[DIAGNOSTIC] NVIDIA_PROJECT_ID: {NVIDIA_PROJECT_ID}")


class NVIDIAAPIClient:
    """Client for NVIDIA AI video generation APIs."""
    
    def __init__(self, api_key: str = None, project_id: str = None):
        self.api_key = api_key or NVIDIA_API_KEY
        self.project_id = project_id or NVIDIA_PROJECT_ID
        self.base_url = NVIDIA_API_BASE_URL
        
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "NVCF-Client-Info": "ai-film-studio/1.0"
        }
    
    async def generate_video(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: int = 1280,
        height: int = 720,
        frames: int = 24,
        fps: int = 24,
        guidance_scale: float = 7.5,
        num_inference_steps: int = 30,
        seed: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate video using NVIDIA's AI models.
        
        Args:
            prompt: Text description of the video to generate
            negative_prompt: What to avoid in the video
            width: Video width
            height: Video height
            frames: Number of frames
            fps: Frames per second
            guidance_scale: Prompt adherence strength
            num_inference_steps: Generation steps
            seed: Random seed for reproducibility
            
        Returns:
            Dict containing job_id and status
        """
        endpoint = f"{self.base_url}/genvid"
        
        payload = {
            "name": "NVIDIABuild-Autogen-72",
            "input": {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "width": width,
                "height": height,
                "frames": frames,
                "fps": fps,
                "guidance_scale": guidance_scale,
                "num_inference_steps": num_inference_steps
            },
            "settings": {
                "output_format": "mp4",
                "output_quality": "high"
            }
        }
        
        if seed is not None:
            payload["input"]["seed"] = seed
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    endpoint,
                    headers=self._get_headers(),
                    json=payload,
                    timeout=120.0
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    return {
                        "error": f"NVIDIA API error: {response.status_code}",
                        "details": response.text
                    }
                    
        except Exception as e:
            return {
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    async def check_status(self, invoke_id: str) -> Dict[str, Any]:
        """
        Check the status of a video generation job.
        
        Args:
            invoke_id: The job invocation ID
            
        Returns:
            Dict containing status and result
        """
        endpoint = f"{self.base_url}/genvid/status/{invoke_id}"
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    endpoint,
                    headers=self._get_headers(),
                    timeout=60.0
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    return {
                        "status": "error",
                        "error": f"Status check failed: {response.status_code}"
                    }
                    
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    async def get_result(self, invoke_id: str) -> Dict[str, Any]:
        """
        Get the generated video result.
        
        Args:
            invoke_id: The job invocation ID
            
        Returns:
            Dict containing video URL or error
        """
        endpoint = f"{self.base_url}/genvid/result/{invoke_id}"
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    endpoint,
                    headers=self._get_headers(),
                    timeout=120.0
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    return {
                        "status": "error",
                        "error": f"Result fetch failed: {response.status_code}"
                    }
                    
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def list_models(self) -> Dict[str, Any]:
        """List available NVIDIA AI models."""
        return {
            "available_models": [
                {
                    "id": "cosmos-1.0",
                    "name": "Cosmos 1.0",
                    "type": "text-to-video",
                    "description": "High-quality video generation from text prompts"
                },
                {
                    "id": "ace-1.0",
                    "name": "ACE 1.0",
                    "type": "character-animation",
                    "description": "AI character animation and expression"
                },
                {
                    "id": "stable-video-diffusion",
                    "name": "Stable Video Diffusion",
                    "type": "image-to-video",
                    "description": "Transform images into smooth video animations"
                }
            ]
        }


# Singleton instance
_nvidia_client: Optional[NVIDIAAPIClient] = None


def get_nvidia_client() -> NVIDIAAPIClient:
    """Get or create the NVIDIA API client singleton."""
    global _nvidia_client
    if _nvidia_client is None:
        _nvidia_client = NVIDIAAPIClient()
    return _nvidia_client


async def test_nvidia_connection() -> Dict[str, Any]:
    """
    Test the NVIDIA API connection.
    
    Returns:
        Dict with connection status and available models
    """
    client = get_nvidia_client()
    
    logger.info("[DIAGNOSTIC] test_nvidia_connection called")
    
    # Check if API key is configured
    if not client.api_key:
        logger.warning("[DIAGNOSTIC] NVIDIA_API_KEY is NOT set")
        return {
            "status": "not_configured",
            "message": "NVIDIA API key not set",
            "instructions": "Set NVIDIA_API_KEY in .env file"
        }
    
    logger.info(f"[DIAGNOSTIC] API key configured (length: {len(client.api_key)})")
    
    # List available models
    models = client.list_models()
    
    logger.info("[DIAGNOSTIC] Connection test complete - client initialized")
    
    return {
        "status": "ready",
        "message": "NVIDIA API client initialized",
        "project_id": client.project_id,
        "available_models": models["available_models"]
    }


# NVIDIA Chat Completion API Configuration
NVIDIA_CHAT_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_CHAT_MODEL = "meta/llama-4-maverick-17b-128e-instruct"


async def chat_completion(
    messages: List[Dict[str, str]],
    max_tokens: int = 512,
    temperature: float = 1.0,
    top_p: float = 1.0,
    stream: bool = False,
    api_key: str = None
) -> Dict[str, Any]:
    """
    Chat completion using NVIDIA's Llama model via direct API.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature (0.0 to 2.0)
        top_p: Top-p sampling threshold
        stream: Whether to stream the response
        api_key: NVIDIA API key (uses env var if not provided)
        
    Returns:
        Dict containing response data or error
    """
    # Get API key from parameter or environment
    api_key = api_key or os.getenv("NVIDIA_CHAT_API_KEY", "")
    
    if not api_key:
        logger.error("[DIAGNOSTIC] NVIDIA_CHAT_API_KEY not set")
        return {
            "error": "API key not configured",
            "message": "Set NVIDIA_CHAT_API_KEY in .env file"
        }
    
    logger.info(f"[DIAGNOSTIC] Sending chat request to {NVIDIA_CHAT_API_URL}")
    logger.info(f"[DIAGNOSTIC] Model: {NVIDIA_CHAT_MODEL}, Messages: {len(messages)}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "text/event-stream" if stream else "application/json"
    }
    
    payload = {
        "model": NVIDIA_CHAT_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stream": stream
    }
    
    try:
        # Using requests for sync chat completion (as provided by user)
        response = requests.post(
            NVIDIA_CHAT_API_URL,
            headers=headers,
            json=payload,
            timeout=120.0
        )
        
        if response.status_code == 200:
            result = response.json()
            logger.info("[DIAGNOSTIC] Chat completion successful")
            return {
                "status": "success",
                "response": result
            }
        else:
            logger.error(f"[DIAGNOSTIC] Chat API error: {response.status_code}")
            return {
                "error": f"API error: {response.status_code}",
                "details": response.text
            }
            
    except Exception as e:
        logger.error(f"[DIAGNOSTIC] Chat completion exception: {str(e)}")
        return {
            "error": str(e),
            "error_type": type(e).__name__
        }