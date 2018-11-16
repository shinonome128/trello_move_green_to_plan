
"""
必要モジュールロード
"""
from trello import TrelloClient
import configparser
import codecs
import pyperclip

"""
主処理
"""
def main():

        # 設定ファイルの読込
        conf_file = 'conf.txt'
        config = configparser.ConfigParser()

        # 気持ち程度のエラー処理
        try:
            # configのファイルを開く
            config.readfp(codecs.open(conf_file, "r", "utf8"))
         
            # パラメータの読み込み
            API_Key = config.get('API', 'API_Key')
            API_SECRET = config.get('API', 'API_SECRET')
            OAUTH_TOKEN = config.get('API', 'OAUTH_TOKEN')
            OAUTH_TOKEN_SECRET = config.get('API', 'OAUTH_TOKEN_SECRET')
            BOARD_NAME = config.get('ENV', 'BOARD_NAME')
            TAG_NAME = config.get('ENV', 'TAG_NAME')
            DST_LIST_NAME = config.get('ENV', 'DST_LIST_NAME')

        # 失敗した時はエラーとだけ伝える
        except:
            print("Error occured")
            exit()

        # クライアントを作成
        client = TrelloClient(API_Key, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        # 緑ラベルカードの配列を呼び出し
        green_cards = get_green_cards(client, BOARD_NAME, TAG_NAME)

        # 宛先リスト ID を取得
        dst_list_id = get_dst_list_id(client, BOARD_NAME, DST_LIST_NAME)

        # 緑ラベルカードを宛先リストへ移動
        move_cards(green_cards, dst_list_id)

"""
緑ラベルカードの配列を取得
"""
def get_green_cards(client, BOARD_NAME, TAG_NAME):

        # 緑ラベルカードの空配列を作成
        green_cards = []

        # ボードリスト取得
        board_list = client.list_boards()

        # ボード名を取得してループ処理
        for board in board_list:

            # ボード名が一致するものを処理
            if board.name == BOARD_NAME:

                # リスト名を取得してループ処理
                for list in board.list_lists('open'):

                    # カード名を取得してループ処理
                    for card in list.list_cards():

                        # ラベルがついたものを処理
                        if len(card.labels) > 0:

                            # ラベル名が一致するものを処理
                            if card.labels[0].name == TAG_NAME:

                                # 緑ラベルのカードを配列に追加
                                green_cards.append(card)

        return green_cards

"""
宛先リストの ID を取得
"""
def get_dst_list_id(client, BOARD_NAME, DST_LIST_NAME):

        # ボードリストを取得
        board_list = client.list_boards()

        # ボード名を取得してループ処理
        for board in board_list:

            # ボード名が一致するものを処理
            if board.name == BOARD_NAME:

                # リスト名を取得してループ処理
                for list in board.list_lists('open'):

                    # リスト名が一致するものを処理
                    if list.name == DST_LIST_NAME:

                        # リスト ID を取得
                        dst_list_id = list.id

        return dst_list_id

"""
カードリストを宛先リストに移動
"""
def move_cards(green_cards, dst_list_id):

        # カード名を取得してループ処理
        for card in green_cards:

            # カードを宛先リストに移動
            card.change_list(dst_list_id)

        return

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
