import asyncio
from bitmoro import Bitmoro
import time

async def get_user_input():
    return input("Enter the OTP you received: ")

async def main():
    token = "<TOKEN>"
    client = Bitmoro(token)
    
    ## OTP MESSAGE
    # otp_manager = await client.get_otp_manager()
    # phone_number = "98xxxxxxxx"
    # otp = otp_manager.generate_otp(phone_number)
    # print(f"Generated OTP for {phone_number}: {otp}")
    # otp_send_response = await otp_manager.send_otp(
    #     phone_number=phone_number,
    #     message_template="Your OTP is:" + otp,
    # )
    # print("OTP send response:", otp_send_response)
    # entered_otp = await get_user_input()
    # otp_verification_response = otp_manager.verify_otp(phone_number, entered_otp)
    # if otp_verification_response:
    #     print(f"OTP for {phone_number} verified successfully.")
    # else:
    #     print(f"OTP verification failed for {phone_number}.")
    
    # BULK MESSAGE 
    
    # bulk_response = await client.send_bulk_message(
    # message="ranodm ",
    # numbers=["98XXXXXXXX"],
    # callback_url="https://demo.requestcatcher.com/test"
    # )
    # print("Bulk message response:", bulk_response)
    
    ## Callback Url response 
    # {"messageId":"Z89IXMreLNwgeBfZehQp","message":"ranodm","status":"sent","report":[{"number":"98XXXXXXXX","status":"success","message":"Sent.","creditCount":1}],"failed":0,"senderId":"BIT_MORE","deliveredDate":"2025-01-16T03:53:22.188Z","refunded":0}
    
    # Send a dynamic message
    # dynamic_response = await client.send_dynamic_message(
    #     message="Hello, ${name}!",
    #     contacts=[
    #         {"number": "98XXXXXXXX", "name": "ramu"},
    #         # {"number": "98XXXXXXXX"}
    #     ],
    #     sender_id="BIT_MORE",
    #     scheduled_date=int(time.time())+60,  # Optional
    #     default_value={"name": "User"},
    #     # callback_url=None  # Optional
    # )
    # print("Dynamic message response:", dynamic_response)

asyncio.run(main())
