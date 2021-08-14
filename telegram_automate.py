from telethon import TelegramClient
import pandas as pd

api_id = 'YOUR_TELEGRAM_API_ID'
api_hash = 'YOUR_TELEGRAM_API_HASH'
csv_path = 'YOUR_CSV_PATH'
message = 'YOUR_MESSAGE'
image_file = 'YOUR_IMAGE_FILE'


class telegram_automate():

    def __init__(self, api_id, api_hash, csv_path, message='No message inserted'):
        self.api_hash = api_hash
        self.api_id = api_id
        self.csv_path = csv_path

        if message == 'No message inserted':
            self.message = input(
                "Insert your message (write \\n for new line)\n")
        else:
            self.message = message

        self.client = TelegramClient('some_name', api_id, api_hash)
        with self.client:
            self.client.loop.run_until_complete(self.__main())

    def __make_list(self):
        name_list = []
        name_csv = pd.read_csv(csv_path)
        for name in name_csv:
            if name == '' or name == '.':  # removing invalid tags
                continue
            else:
                if(name[0] == '@'):  # removing the @ symbol
                    name = name[1:]
                name_list.append(name)
        return name_list

    async def __main(self):

        users = self.__make_list()
        for username in users:
            # message = await self.client.send_message(
            #     name,
            #     self.message_eng,
            #     link_preview=False
            # )
            image = await self.client.send_file(
                entity=username,
                file=image_file,
                caption=self.message, # file caption
                link_preview=False
            )


if __name__ == '__main__':
    telegram_automate(api_id, api_hash, csv_path, message)
