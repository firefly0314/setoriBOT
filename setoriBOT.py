#coding:utf-8

# インストールした discord.py を読み込む
import discord
import unicodedata

# 接続に必要なオブジェクトを生成


client = discord.Client()
num=0
list=[]


# 起動時に動作する処理
@client.event
async def on_ready():# 起動したらターミナルにログイン通知が表示される
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    global list
    global num
    
    if message.content.startswith('$h'):
        await message.channel.send('$をつけてから\nin 予約をする\nout 次の人に順番を回す\nlist 予約を確認する\n以上でよろしいですかにゃ？')


    #リストに追加
    if message.content.startswith('$in'):
        await message.channel.send('了解ですにゃ['+message.author.name+"]")

        temp  = message.author.name

        list.append(temp) 
        print (list)
        ##print (temp)
        num+=1


    #リストから削除
    if message.content.startswith('$out'):       
        if num > 0:
            list.pop(0) 
            print (list)
            num-=1
            await message.channel.send('OK、お疲れ様...にゃ...')

        else:
            await message.channel.send('誰もいないのに何を言ってるにゃ...')


    #リスト出力
    if message.content.startswith('$list'):
            
        global sa
        global sb
        global sc
        global sd
        global se
        global sf
        global snam
        
        sa=" "
        sb=" "
        sc=" "
        sd=" "
        se=" "
        sf=" "
        snam=0

        if num > 0:

            sa="now -[ " +list[0]+"]"
            snam=1

        if num > 1:

            sb="1       -[ " +list[1]+"]"
            snam=1

        if num > 2:

            sc="2       -[ " +list[2]+"]"
            snam=1

        if num > 3:

            sd="3       -[ " +list[3]+"]"
            snam=1

        if num > 4:

            se="4       -[ " +list[4]+"]"
            snam=1

        if num > 5:

            sf="5       -[ " +list[5]+"]"
            snam=1

        if snam == 1:

            s = sa + "\n" + sb + "\n"  +sc + "\n"  + sd + "\n"  + se + "\n"  + sf
            await message.channel.send(s)
            print ("Export") 

        else:
                print ("no_date")
                snam=0
                await message.channel.send('誰もいないのでリストが作成できないですにゃ...')

    if message.content.startswith('かわいい'):
        await message.channel.send('何を言ってるんですか？\nそんなこと無いですにゃ')
    if message.content.startswith('オルガ'):
        await message.channel.send('止まるんじゃねぇぞ…　\n　\n　\n 　n\n　 _H\n　巛 ｸ　 ノﾚzz\n　 F｜　幺 ﾐwｯﾐ\n　｜｜　ヽﾚvvｲ\n　｜ ￣⌒＼二ヽ＿\n　 ￣￣Ｙ　ミ　 /|\n　　　 ｜　 |　｜|\n　　　 /　　|　｜|\n　　　/　　 |　 L|\n　　　＼＿_/|＿/(ヽ\n　　　 ｜　　 ｜/ぐ)\n　　　 ｜　 ﾊ ∧＼≫\n　　　 ｜　/ Ｖ∧\n　　　 ｜ ｜　Ｖ｜')
    if message.content.startswith('カカポ'):
        await message.channel.send('https://forest.watch.impress.co.jp/img/wf/docs/1251/932/60fpsparrot.gif')

# Botの起動とDiscordサーバーへの接続
client.run('')
