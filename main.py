
import asyncio
import random
from keep_alive import keep_alive
import gtts



import discord
import os

def generateGrats():
  congrats_list = ['best wishes', 'compliments', 'felicitations', 'commendation', 'kudos', 'a pat on the back']
  big_list = ['colossal', 'substantial', 'remarkable', 'momentous', 'considerable', 'immense', 'enormous', 'gargantuan', 'great', 'massive', 'significant', 'consequential', 'stupendous', 'gigantic', 'monumental', 'mighty', 'giant', 'tremendous', 'humongous', 'astronomical']

  achievement_list = ['attainment', 'acquirement', 'procurement', 'accomplishment', 'success', 'triumph', 'effort', 'deed', 'undertaking', 'fulfilment', 'performance']

  random.shuffle(congrats_list)
  random.shuffle(big_list)
  random.shuffle(achievement_list)

  congratulations = congrats_list[0]
  big = big_list[0]
  achievement = achievement_list[0]

  
  output_string = f"{congratulations} on your {big} {achievement}"
  return output_string


intents = discord.Intents().default()
intents.guilds = True
intents.members = True
intents.emojis = True

client = discord.Client(intents=intents)


enabledReacts = False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_reaction_add(reaction, user):
  #print("sensed a reaction")
  #print(reaction.emoji.id)
  if user == client.user:
      return



@client.event
async def on_message(message):
  global enabledReacts

  if message.author == client.user:
    return

  if True:
    sender = message.author.name
    if message.content.startswith('$'):
      await message.channel.send("Hello -w-, u summoned me ^w^")

    if message.content.startswith('$piplup'):
      print("vc sensed from me")
      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        print("already connected to vc!")
        print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      vc.play(discord.FFmpegPCMAudio('pip.wav'))

    if message.content.startswith('$squirtle'):
      print("rubyree sensed")
      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        print("already connected to vc!")
        print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      vc.play(discord.FFmpegPCMAudio('squirtle.wav'))

        

      #await asyncio.sleep(10)
      #await vc.disconnect()

      ##vc.play(discord.FFmpegAudio(source="pip.wav"))

    if message.content.startswith('$dc'):

      vc = client.voice_clients[0]
      await message.channel.send("disconnecting from all voice chats ^w^")

      await vc.disconnect()


    if message.content.startswith('$say'):
      print("say sensed from me")
      saywhat = message.content[5:]
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='com')
      tts.save("saywhat.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        print("already connected to vc!")
        print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))


  if message.content.startswith('$jiang'):
      print("jiang sensed from me")
      jiang = message.content[7:]
      print(jiang)

      if "fuck" in jiang:
        jiang = jiang.replace("fuck" ,"fish")

      if "penis" in jiang:
        jiang = jiang.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " jiang " + jiang, lang='zh-CN')
      tts.save("jiang.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        print("already connected to vc!")
        print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender}在<#{vc.channel.id}>讲：{jiang}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('jiang.mp3'), volume=2.5))

  if message.content.startswith('$play'):
      print("play sensed")
      skill = message.content[6:]
      print(skill)
      skill_list = ['agility', 'attack', 'cooking', 'crafting', 'defence', 'farming', 'fishing', 'fletching', 'fm', 'herblore', 'hp', 'mage1', 'magic', 'mining', 'prayer', 'ranged', 'rc', 'slayer', 'smithing', 'strength', 'thieving', 'waow', 'wc', 'disaster', 'theyalldead', 'questionable', 'sad', 'charge', 'crybaby', 'ayayayaya', 'nextlevelplay', 'lakadmatatag', 'absolutelyperfect', 'failedexperiment', '-w-', 'ss2', 'icebarrage', 'clue', 'dead', 'problem', 'power', 'scientist', 'emeraldstart', 'ludipq', 'diamondstart', 'diamondroute101', 'diamondpokecenter', 'p', 'scary', 'emeraldprestart', 'gbstart', 'gb1']
      wav_list = ['diamondstart', 'diamondroute101', 'diamondpokecenter', 'p', 'scary']

      if skill not in skill_list:
        await message.channel.send(f"i do not recognise that sound :( \n available sound list: {skill_list}")
        return


      myvc = message.author.voice.channel.id
      print(myvc)


      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        print("already connected to vc!")
        print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      await message.channel.send(f"{sender} is playing in <#{vc.channel.id}> the sound: {skill}")
      if skill not in wav_list:
        vc.play(discord.FFmpegPCMAudio(f'rs skills/{skill}.mp3'))
      else:
        vc.play(discord.FFmpegPCMAudio(f'rs skills/{skill}.wav'))

  if message.content.startswith('$grats'):
    output_string = generateGrats()

    await message.channel.send(output_string)


    




  if message.content.startswith('$') and message.guild == client.get_guild(260389250225143808) and message.channel.id == 443978416618864640 and message.author.id != 386535807986565132:
    #await message.channel.send("i am disabled in this server for everyone except my owner :/")
    return

  if message.guild == client.get_guild(260389250225143808) and message.author.id != 386535807986565132:
    return

    #print(message.author.name, " name\n", message.author.id, " id")
    
    #print("message sensed")

  if message.author.id == 386535807986565132: #if me

          

    if message.content.startswith('$var_dump'):
      await message.channel.send("current channel id: "+ str(message.channel.id) + "\ncurrent guild id: " + str(message.channel.guild.id))

      #await message.channel.send(message.channel.guild.get_member_named("rubiak"))
      
      return
    if message.content.startswith('$getuser'):

      #print(str(message.guild.default_role.members))
      
      
      
      myinput = message.content[9:]
      users = message.raw_mentions

      await message.channel.send(str(users))

      

      #member = message.guild.get_member_named(myinput)

      #await message.channel.send("member id: " + str(member.id) + "\nmember: " + str(member.name))

      

      return

      #current channel id: 443978416618864640 bot commands
      #current guild id: 260389250225143808 sga
  
  if message.content.startswith("$") and message.channel.guild.id == 260389250225143808 and message.channel.id != 443978416618864640:
    await message.add_reaction(client.get_emoji(823183587678355476))
    return 

  if 'fuck' in message.content.lower():

    await message.channel.send("hello!! " + str(message.author.mention) + " please mind your language!! -w-")

    return 

  
  if message.content.startswith('$react'):
    #if message.author.id != 386535807986565132:
      #await message.channel.send("haha u are not a valid user to use this right now")
      #return
    #enabledReacts = True
    return



  if message.content.startswith('$help'):
      myoutput = 'last updated: 3/2/2022 \n current available commands! \n $help \n $play (type for available sounds) \n $say something \n $jiang something (chinese accent) \n $dc (disconnect from all voice chats) \n '
      await message.channel.send(myoutput)
      return





  if message.content.startswith('$user'):
    mentionedusers = message.raw_mentions

    for mentioneduserid in mentionedusers:
      mentioneduser = await client.fetch_user(mentioneduserid)
      display_name = mentioneduser.display_name
      avatar_url = mentioneduser.avatar_url
      await message.channel.send("user id: " + str(mentioneduserid))
      await message.channel.send(avatar_url)
    

      member = message.channel.guild.get_member(mentioneduserid)
      #await message.channel.send(member)
      joindate = member.joined_at.strftime("%d/%m/%Y")
      await message.channel.send("display name: "+display_name+"\nserver join date: "+joindate)
      return


  if enabledReacts and "piplup" in message.content.lower():

    emojiids = [819177264187965511, 817266435394633739, 817268340748714034, 816303563202494464, 817270302508974091, 816297120100909066, 823183587678355476, 822152761533661276, 817061884133507142, 816279779266789388, 816279779266789388, 817263062540222506, 817264343359029248,817258762976362529,817263188307083284,817264137872080947,817258786884288532,816294959899607060,828689493598797914,828687940359684116,817260016411213836,817255977371828264,817256130832891904,817060892390064168,819153083355365417,828695708584116306,828696077808435250,816296571528020038,822110333115695164]

    random.shuffle(emojiids)

    emojiids = emojiids[:20]
    #piplup emojiids = (817061884133507142, 816279779266789388, 816279779266789388, 817263062540222506, 817264343359029248,817258762976362529,817263188307083284,817264137872080947,817258786884288532,816294959899607060,828689493598797914,828687940359684116,817260016411213836,817255977371828264,817256130832891904,817060892390064168,819153083355365417,828695708584116306,828696077808435250,816296571528020038,822110333115695164)

    #remaining piplup emoji ids: ()

    for emoji in emojiids:
        Emoji = client.get_emoji(emoji)
        await message.add_reaction(Emoji)








my_secret = os.environ['TOKEN']

keep_alive()
client.run(my_secret)







