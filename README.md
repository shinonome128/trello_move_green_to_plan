  
# README.md  
  
## 目的  
  
plan の効率化  
trello で緑ラベルが付いているものだけを Plan リストに移動  
  
## 参照  
  
このドキュメントのコード管理  
あとで  
  
緑ラベルをクリップに移動  
https://github.com/shinonome128/trello_move_green_to_clip  
  
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
  
クリップボードをコードを流用  
  
## 取得したカードを Plan リストに移動  
  
EOF  
