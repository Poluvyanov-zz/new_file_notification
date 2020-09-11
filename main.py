import cmd
from os import listdir
from os.path import isfile, join
import schedule
import requests
import os


class UpdateFilesNotification(cmd.Cmd):
    def __init__(self):
        super(UpdateFilesNotification, self).__init__()
        self.folder = "D:\\"
        self.minutes = 1
        if not os.path.exists('logs.txt'):
            open('logs.txt', 'w').close()

    def do_set_folder(self, line):
        if not line:
            line = self.folder
        else:
            self.folder = line
        print("Set folder: ", self.folder)

    def do_set_time_interval(self, line):
        if not line:
            line = self.minutes
        else:
            self.minutes = line
        print("running script every - ", self.minutes, "minutes")

    def do_show_settings(self, line):
        print("Settings:\nFolder:", self.folder, "\nStart every:", self.minutes, 'minutes')

    def run(self):
        onlyfiles = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
        for file in onlyfiles:
            print(file)
            with open('logs.txt') as f:
                if file not in f.read():
                    file1 = open("logs.txt", "a")
                    file1.writelines(file)
                    file1.close()
                    print("file --", file)
                    self.sendToTelegram(file)

    def sendToTelegram(self, file_name):
        print('file_name', file_name)
        config = self.telegramConfig(1)
        file = self.folder + "\\" + file_name
        message = ('https://api.telegram.org/' + config.get('bot_token').strip() + '/sendPhoto?chat_id=' + config.get(
            'chat_id').strip())
        send = requests.post(message, files={
            'photo': open(file, 'rb')
        })
        print(send.status_code, send.reason, send.content)

    def do_job(self, line):
        schedule.every(self.minutes).minutes.do(self.run)
        while True:
            schedule.run_pending()

    def telegramConfig(self, line):
        telegramConfig = dict()
        file = open('.env', 'r')
        data = file.readlines()
        telegramConfig['bot_token'] = data[0]
        telegramConfig['chat_id'] = data[1]
        return telegramConfig


if __name__ == '__main__':
    UpdateFilesNotification().cmdloop()
