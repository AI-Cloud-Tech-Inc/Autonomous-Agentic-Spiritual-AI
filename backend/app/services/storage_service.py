"""
Storage Service for Cloud File Management
"""
import boto3
from typing import BinaryIO
import os
from app.core.config import settings


class StorageService:
    """Service for managing file uploads to cloud storage"""
    
    def __init__(self):
        # Initialize S3 client (can be extended for Azure Blob Storage)
        self.use_s3 = hasattr(settings, 'AWS_ACCESS_KEY_ID')
        
        if self.use_s3:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=getattr(settings, 'AWS_ACCESS_KEY_ID', None),
                aws_secret_access_key=getattr(settings, 'AWS_SECRET_ACCESS_KEY', None),
                region_name=getattr(settings, 'AWS_REGION', 'us-east-1')
            )
            self.bucket_name = getattr(settings, 'S3_BUCKET_NAME', 'ai-film-studio')
        else:
            # Fallback to local storage
            self.local_storage_path = "media"
            os.makedirs(self.local_storage_path, exist_ok=True)
    
    async def upload_file(self, file: BinaryIO, filename: str, folder: str = "uploads") -> str:
        """Upload file to cloud storage and return URL"""
        object_key = f"{folder}/{filename}"
        
        if self.use_s3:
            try:
                self.s3_client.upload_fileobj(file, self.bucket_name, object_key)
                url = f"https://{self.bucket_name}.s3.amazonaws.com/{object_key}"
                return url
            except Exception as e:
                raise Exception(f"S3 upload failed: {str(e)}")
        else:
            # Local storage fallback
            local_path = os.path.join(self.local_storage_path, folder)
            os.makedirs(local_path, exist_ok=True)
            file_path = os.path.join(local_path, filename)
            
            with open(file_path, 'wb') as f:
                f.write(file.read())
            
            return f"/media/{folder}/{filename}"
    
    async def delete_file(self, file_url: str):
        """Delete file from cloud storage"""
        if self.use_s3:
            # Extract object key from URL
            object_key = file_url.split(f"{self.bucket_name}.s3.amazonaws.com/")[1]
            try:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_key)
            except Exception as e:
                raise Exception(f"S3 deletion failed: {str(e)}")
        else:
            # Local storage deletion
            if os.path.exists(file_url):
                os.remove(file_url)
    
    async def get_presigned_url(self, object_key: str, expiration: int = 3600) -> str:
        """Generate presigned URL for temporary access"""
        if self.use_s3:
            try:
                url = self.s3_client.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': self.bucket_name, 'Key': object_key},
                    ExpiresIn=expiration
                )
                return url
            except Exception as e:
                raise Exception(f"Presigned URL generation failed: {str(e)}")
        else:
            return object_key  # Return local path for local storage


storage_service = StorageService()
