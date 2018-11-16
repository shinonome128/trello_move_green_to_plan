  
# README.md  
  
## 目的  
  
plan の効率化  
trello で緑ラベルが付いているものだけを Plan リストに移動  
  
## 参照  
  
このドキュメントのコード管理  
https://github.com/shinonome128/trello_move_green_to_plan  
  
緑ラベルをクリップに移動  
https://github.com/shinonome128/trello_move_green_to_clip  
  
Trello API ガイド 、 /cards/{id} パラメータ説明  
https://developers.trello.com/reference/#cardsid-1  
  
## やること  
  
レポジトリの作成  
Trello クライアントから緑ラベルのカードを取得  
取得したカードを Plan リストに移動  
  
## レポジトリの作成  
  
レポジトリ名  
```  
trello_move_green_to_plan  
```  
  
ディレクトリ  
```  
mkdir C:\Users\shino\doc\trello_move_green_to_plan  
```  
  
README 作成  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
echo # hoge>> README.md  
```  
内容をコピー  
  
.gitignore 作成  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
echo # .gitignore>> .gitignore  
echo *.swp>> .gitignore  
```  
  
github に登録  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
git init  
git config --local user.email shinonome128@gmail.com  
git config --local user.name "shinonome128"  
git add .gitignore  
git add README.md  
git commit -m "first commit"  
git remote add origin https://github.com/shinonome128/trello_move_green_to_plan.git  
git push -u origin master  
```  
  
## Trello クライアントから緑ラベルのカードを取得  
  
クリップボードへ移動するときのコードを流用  
  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
copy .gitignore C:\Users\shino\doc\trello_move_green_to_plan  
copy conf.txt C:\Users\shino\doc\trello_move_green_to_plan  
copy conf_sample.txt C:\Users\shino\doc\trello_move_green_to_plan  
copy get_card.py C:\Users\shino\doc\trello_move_green_to_plan  
copy get_green.bat C:\Users\shino\doc\trello_move_green_to_plan  
xcopy py-trello C:\Users\shino\doc\trello_move_green_to_plan\py-trello /s/e/i  
```  
  
先に .gitignore だけ同期  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
git add .gitignore  
git commit -m "first commit"  
git push  
```  
  
のこりを同期  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
git add *  
git commit -m "first commit"  
git push  
```  
  
ファイル名変更  
```  
cd C:\Users\shino\doc\trello_move_green_to_plan  
move get_card.py move_card.py  
git add *  
git commit -m "first commit"  
git push  
```  
  
## 取得したカードを Plan リストに移動  
  
カード名を渡して指定のリストに渡す方法を調査  
  
card.py で定義されていそう  
```  
    def change_list(self, list_id):  
        self.client.fetch_json(  
            '/cards/' + self.id + '/idList',  
            http_method='PUT',  
            post_args={'value': list_id})  
```  
  
API ガイドでパラメータを調査  
カード ID と 宛先リスト ID を渡せば、 PUT で対応していそう  
```  
id  
The ID of the card to update  
idList  
The ID of the list the card should be in  
```  
  
デバッグで実装  
  
ここから再開  
  
EOF  
