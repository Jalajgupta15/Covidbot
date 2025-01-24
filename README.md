
# Covidbot

A Python-based bot that fetches COVID-19 vaccination slots from the CoWIN API, checks for availability, and notifies users through Telegram. The bot checks for free vaccine slots for individuals aged 18 and above and sends a notification with the relevant details.

## Features

- **Check vaccination slots**: Fetches vaccination slot details from the CoWIN API based on the district ID.
- **Telegram notifications**: Sends a message with details of available slots via Telegram.
- **Sound alerts**: Plays a notification sound when slots are available.
- **Fetches data for multiple days**: The bot fetches slot details for the next 3 days and checks for availability.

## Setup

1. **Install dependencies**:
   Create a `requirements.txt` with the following:
   ```
   requests
   playsound
   ```
   Then, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Telegram bot**:
   - Create a Telegram bot by chatting with [BotFather](https://core.telegram.org/bots#botfather) and getting the `telegram_key`.
   - Find your `telegram_chat_id` by interacting with your bot or using an API call.

3. **Location**:
   - Save the `district_id` (your area’s district ID) in the `location.txt` file.

4. **Sound Notification**:
   - Place a `.wav` notification sound file named `jg@notifiactionsound.wav` in the same directory.

5. **Run the bot**:
   - Execute the script to check for available slots and get notifications:
   ```bash
   python chatbot.py
   ```

## File Structure

- `chatbot.py`: Main script to run the bot and send notifications.
- `requirements.txt`: List of required Python libraries.
- `location.txt`: Stores the district ID for fetching slots.
- `jg@notifiactionsound.wav`: Sound file for notifications.
- `set_location.py`: Script to update the district ID in `location.txt`.

## Future Work

- Improve error handling and logging.
- Add functionality to specify time slots or preferred vaccines.

