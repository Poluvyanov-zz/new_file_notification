# new_file_notification
A small script that checks the folder for updates that have appeared and, if there are any, sends them to the telegram

# Usage

  - An example of using this script. If you are engaged in 3D visualization and leave images for rendering overnight, then you can 
configure this script so that it checks for updates in the folder every hour and sends a new rendered image to your telegram channel

- Launching this can be problematic, because the code was written for yourself, but below I am attaching a launch instruction, maybe it will be useful to someone.

### Installation

```
Create .env file with 2 lines:
bot<you_bot_id>
-<you_chat_id>
```

```
1. Install <a href="https://www.python.org/downloads/">python</a>
2. Run command: pip install -r requirements.txt
3. Open windows terminal, go to folder with script and run: python main.py
4. You need set folder for parsing created images (for example): set_folder C:\work\images
5. Then you need set minutes interval for check updates (by default 30 minutes): set_time_interval 60
6. You can see you settings: show_settings
7. Run command to start script: job
```
