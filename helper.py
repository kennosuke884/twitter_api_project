import os
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

Twitter_api = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class helper:
    def __init__(self,reply_partner_id, time, filename):
        """
        reply_partner_id : @username
        time : (end - start) with time.process_time()
        filename : os.path.basename(__file__)
        """
        self.reply_partner_id = str(reply_partner_id)
        self.time = str(time)
        self.filename = str(filename)

    def inform_done(self):
        reply_text = self.reply_partner_id + '\n'
        reply_text += '「' + self.filename + '」' +'の実行が完了しました！' + '\n'
        reply_text += '処理時間は、' + self.time + 'です'
        Twitter_api.update_status(status=reply_text, in_reply_to_status_id=self.reply_partner_id)

