"""
Video Generation Service
Integrates with Stable Diffusion, RunwayML for video generation
"""
from typing import Dict, Any, List, Optional
import logging
import base64
import io
from pathlib import Path
import replicate
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from app.core.config import settings

logger = logging.getLogger(__name__)


class VideoGenerator:
    """Video generation using Stable Diffusion and RunwayML"""
    
    def __init__(self):
        """Initialize video generation services"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.sd_pipeline = None
        self.replicate_client = None
        
        if settings.REPLICATE_API_KEY:
            self.replicate_client = replicate.Client(api_token=settings.REPLICATE_API_KEY)
            logger.info("Replicate client initialized")
    
    async def generate_video_from_text(
        self,
        prompt: str,
        duration: int = 3,
        fps: int = 24,
        width: int = 1024,
        height: int = 576,
        style: str = "cinematic"
    ) -> Dict[str, Any]:
        """
        Generate video from text prompt
        
        Args:
            prompt: Description of the video scene
            duration: Video duration in seconds
            fps: Frames per second
            width: Video width
            height: Video height
            style: Visual style
            
        Returns:
            Video generation result with URL/path
        """
        try:
            # Use RunwayML Gen-2 via Replicate
            if self.replicate_client:
                return await self._generate_runway_video(
                    prompt, duration, width, height, style
                )
            else:
                # Fallback to image sequence generation
                return await self._generate_image_sequence(
                    prompt, duration, fps, width, height, style
                )
        except Exception as e:
            logger.error(f"Error generating video: {str(e)}")
            return {"error": str(e), "status": "failed"}
    
    async def _generate_runway_video(
        self,
        prompt: str,
        duration: int,
        width: int,
        height: int,
        style: str
    ) -> Dict[str, Any]:
        """Generate video using RunwayML Gen-2"""
        enhanced_prompt = f"{style} style: {prompt}"
        
        output = await self.replicate_client.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={
                "cond_aug": 0.02,
                "decoding_t": 7,
                "input_image": None,  # Text-to-video
                "video_length": "14_frames_with_svd",
                "sizing_strategy": "maintain_aspect_ratio",
                "motion_bucket_id": 127,
                "frames_per_second": 6,
                "prompt": enhanced_prompt
            }
        )
        
        return {
            "status": "success",
            "video_url": output,
            "prompt": enhanced_prompt,
            "duration": duration,
            "method": "runway_ml"
        }
    
    async def _generate_image_sequence(
        self,
        prompt: str,
        duration: int,
        fps: int,
        width: int,
        height: int,
        style: str
    ) -> Dict[str, Any]:
        """Generate video as sequence of AI-generated images"""
        num_frames = duration * fps
        
        # Generate keyframes (every second)
        keyframes = duration
        images = []
        
        for i in range(keyframes):
            image = await self._generate_image(
                f"{style} style, frame {i}: {prompt}",
                width,
                height
            )
            images.append(image)
        
        # In production, interpolate between keyframes and create video
        return {
            "status": "success",
            "keyframes": len(images),
            "total_frames": num_frames,
            "fps": fps,
            "method": "image_sequence",
            "images": images
        }
    
    async def _generate_image(
        self,
        prompt: str,
        width: int,
        height: int
    ) -> str:
        """Generate single image using Stable Diffusion"""
        if not self.sd_pipeline:
            logger.info("Loading Stable Diffusion pipeline...")
            self.sd_pipeline = StableDiffusionPipeline.from_pretrained(
                "stabilityai/stable-diffusion-2-1",
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            )
            self.sd_pipeline.to(self.device)
        
        image = self.sd_pipeline(
            prompt,
            height=height,
            width=width,
            num_inference_steps=30
        ).images[0]
        
        # Convert to base64 for easy transport
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{image_base64}"
    
    async def generate_image_from_text(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 576,
        num_images: int = 1
    ) -> List[str]:
        """
        Generate images from text prompt
        
        Args:
            prompt: Image description
            width: Image width
            height: Image height
            num_images: Number of images to generate
            
        Returns:
            List of image URLs/base64
        """
        images = []
        for _ in range(num_images):
            image = await self._generate_image(prompt, width, height)
            images.append(image)
        
        return images


# Global instance
video_generator = VideoGenerator()
