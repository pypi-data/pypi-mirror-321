
import requests
import httpx
from typing import Union, Optional
from ..types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import json

class SendFunctions:
    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[str] = None,
        reply_markup: InlineKeyboardMarkup = None
    ):
        """
        Send a message via the Telegram Bot API.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel.
            text (str): Text of the message to be sent, 1-4096 characters after entities parsing.
            parse_mode (Optional[str]): Mode for parsing entities in the message text.
            reply_markup (Optional[Union[dict, str]]): Additional interface options.

        Returns:
            Message: On success, the sent Message is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        url = f"{self.client.api_url}sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text
        }

        # Add optional parameters if they are provided
        if parse_mode:
            payload["parse_mode"] = parse_mode
        if reply_markup:
            payload["reply_markup"] = json.dumps(reply_markup.to_dict())

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return Message(self.client, response.json()["result"])
        except Exception as e:
            print(e)

    def send_audio(self, chat_id, audio, filename=None, caption=None, parse_mode=None):
        """
        Send an audio file via the Telegram Bot API.

        Args:
            chat_id (int): The chat ID to send the audio to.
            audio (str or bytes): The audio to be sent. It can be:
                                  - File path (str)
                                  - Public URL (str)
                                  - File ID (str, already uploaded to Telegram)
            filename (str, optional): Name of the file to be sent if using a local file.
            caption (str, optional): Caption for the audio message.
            parse_mode (str, optional): Formatting style for the caption (e.g., 'Markdown').
        """
        url = self.client.api_url + "sendAudio"

        payload = {"chat_id": chat_id}
        if caption:
            payload["caption"] = caption
        if parse_mode:
            payload["parse_mode"] = parse_mode

        # Handle different types of `audio`
        files = None
        if isinstance(audio, str):
            if audio.startswith("http://") or audio.startswith("https://"):
                # Audio is a URL
                payload["audio"] = audio
            else:
                # Audio is a file path
                try:
                    files = {"audio": (filename or "audio.mp3", open(audio, "rb"))}
                except FileNotFoundError:
                    print(f"Error: File '{audio}' not found.")
                    return
        elif isinstance(audio, bytes):
            # Audio is raw file content
            files = {"audio": (filename or "audio.mp3", audio)}
        else:
            print("Invalid audio type. Must be a file path, URL, or file ID.")
            return

        # Send the request
        try:
            response = requests.post(url, data=payload, files=files)
            if response.status_code == 200:
                print("Audio sent successfully!")
            else:
                print(f"Failed to send audio: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the file if opened
            if files and "audio" in files:
                files["audio"][1].close()

