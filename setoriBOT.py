#coding:utf-8

# インストールした discord.py を読み込む
import discord


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
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


    #リストに追加
    if message.content.startswith('$in'):
        await message.channel.send('OKにゃ')

        temp  = message.author.name
        temp2 = temp.encode('utf-8')

        list.append(temp2) 
        print (list)
        num+=1


    #リストから削除
    if message.content.startswith('$out'):       
        if num > 0:
            list.pop(0) 
            print (list)
            num-=1
            await message.channel.send('OK、お疲れ様にゃ')

        else:
            await message.channel.send('誰もいないにゃ！')


    #リスト出力
    if message.content.startswith('$list'):

        if num > 0:
            s="now-".encode('utf-8')+list[0]
            print (s)
            await message.channel.send(s)

        if num > 1:
            s="   1   -".encode('utf-8')+list[1]
            print (s)
            await message.channel.send(s)

        if num > 2:
            s="   2   -".encode('utf-8')+list[2]
            print (s)
            await message.channel.send(s)

        if num > 3:
            s="   3   -".encode('utf-8')+list[3]
            print (s)
            await message.channel.send(s)

        if num > 4:
            s="   4   -".encode('utf-8')+list[4]
            print (s)
            await message.channel.send(s)

        if num > 5:
            s="   5   -".encode('utf-8')+list[5]
            print (s)
            await message.channel.send(s)

        else:

            print ("error")




# Botの起動とDiscordサーバーへの接続
client.run('NzMyMTc1ODYyNjUyMjA3MTg1.Xwwx6A.C88CWOQslC9uUXovFtx3tZ49gxY')