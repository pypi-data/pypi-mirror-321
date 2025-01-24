import requests
import asyncio
from datetime import datetime
import secrets

class Bitmoro:
    BASE_URL = "https://www.bitmoro.com/api/message"
    
    def __init__(self,token:str):
        self.token =token
        self.headers ={
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json",
        }
        
    async def _make_request(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            await asyncio.sleep(0)
            response = requests.post(url=url, headers=self.headers, json=data)
            if response.status_code >= 400:
                await asyncio.sleep(0)
                raise Exception(f"Error: {response.reason}. Response: {response.text}")
            await asyncio.sleep(0)
            return response.json()
        except Exception as e:
            print("error:", e)

    async def send_bulk_message(
        self,
        message:str,
        numbers:list[str],
        sender_id:str=None,
        scheduled_date:int=None,
        callback_url:str=None  
    )->dict:
        """Send bulk messages to multiple recipients."""
        data={
            "message": message,
            "number": numbers,
            "senderId": sender_id,
            "scheduledDate": scheduled_date,
            "callbackUrl": callback_url,
        }
        
        data = {key: value for key , value in data.items() if value is not None}
        response = await self._make_request("bulk-api",data)
        return response

    async def send_dynamic_message(
        self,
        message:str,
        contacts:list[dict],
        sender_id:str=None,
        scheduled_date:int=None,
        default_value:dict=None,
        callback_url:str=None  
        )->dict:
        """Send dynamic messages with templates."""
        
        data={
            "contacts":contacts,
            "message":message,
            "senderId":sender_id,
            "scheduledDate":scheduled_date,
            "callbackUrl":callback_url,
            "defaultValues":default_value
        }
        data={key: value for key , value in data.items() if value is not None}
        response = await self._make_request("dynamic-api",data)
        return response
    
    async def get_otp_manager(
        self,
        expiry_seconds: int = 300,
        otp_length: int = 4,
        max_attempts: int = 3
    ):
        return OtpManager(self.token,expiry_seconds,otp_length,max_attempts)
        
class OtpManager:
    """Manage OTP generation, verification, and sending."""
    BASE_URL = "https://bitmoro.com/api/message/api"
    
    def __init__(
        self,
        token,
        expiry_seconds: int = 300,
        otp_length: int = 4,
        max_attempts: int = 3
    ):
        self.expiry_seconds = expiry_seconds
        self.otp_length = otp_length
        self.max_attempts = max_attempts 
        self.token = token
        self._otps: dict[str, dict] = {}
        self.headers ={
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json",
        }
        
    
    def generate_otp(self, id: str) -> str:
        """Generate new OTP for a user."""
        otp = "".join(secrets.choice("0123456789") for _ in range(self.otp_length+1))
        self._otps[id] = {
           "otp": otp,
           "created_at": datetime.now(),
           "attempts": 0
        }
        
        asyncio.create_task(self._cleanup_otp(id)) 
        
        return otp
    
    def verify_otp(self, id: str, otp: str) -> bool:
        """Verify OTP for a user."""
        if id not in self._otps:
            raise Exception("No active OTP found for this user.")
        otp_data = self._otps[id]
        
        if self._is_expired(otp_data["created_at"]):
            del self._otps[id]
            raise Exception("Otp has expired.")
        if otp_data["attempts"] >= self.max_attempts:
            raise Exception("Maximum verification attempts exceeded.")
        otp_data["attempts"] += 1
        if otp_data["otp"] == otp:
            del self._otps[id]
            return True
        return False

    async def send_otp(self, phone_number: str, message_template: str, sender_id: str=None):
        """Send OTP via SMS."""  
        data = {
            "message": message_template,
            "number": [phone_number],
            "senderId": sender_id 
        }
        data = {key: value for key, value in data.items() if value is not None}
        response = await self._request_otp(data)
        return response
        
    async def _request_otp(self, data):
        try:
            await asyncio.sleep(0)
            response = requests.post(url=self.BASE_URL, headers=self.headers, json=data)
            if response.status_code >= 400:
                await asyncio.sleep(0)
                raise Exception(f"Error: {response.reason}. Response: {response.text}")
            await asyncio.sleep(0)
            return response.json()
        except Exception as e:
            print("error:", e)
        
    def _is_expired(self, created_at: datetime) -> bool:
        """Check if OTP is expired."""
        elapsed = (datetime.now() - created_at).total_seconds()
        return elapsed > self.expiry_seconds
   
    async def _cleanup_otp(self, user_id: str):
        """Clean up expired OTP."""
        await asyncio.sleep(self.expiry_seconds)
        self._otps.pop(user_id, None)
        
    def _is_rate_limited(self, user_id: str) -> bool:
        """Check if user is rate limited for OTP generation."""
        if user_id in self._otps:
            elapsed = (datetime.now() - self._otps[user_id]["created_at"]).total_seconds()
            return elapsed < 60
        return False
