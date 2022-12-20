from keep_alive import keep_alive
import gtts
from itertools import cycle
from discord.ext import tasks



import discord
import os



intents = discord.Intents().default()
intents.guilds = True
intents.members = True
intents.emojis = True

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    change_status.start()


status = cycle(['piplup','is', 'cute'])

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))



@client.event
async def on_message(message):

  if message.author == client.user:
    return



  if True:
    sender = message.author.name
    if message.content.startswith('$'):
      await message.channel.send("Hello -w-, u summoned me ^w^")

      if message.author.id == 168075629193854976:
        await message.channel.send(f"you are onyo. you are temporarily unbanned.")
        #return

    if message.content.startswith('$piplup'):
      #print("vc sensed from me")
      myvc = message.author.voice.channel.id
      #print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        #print("already connected to vc!")
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      vc.play(discord.FFmpegPCMAudio('pip.wav'))

    if message.content.startswith('$dc'):

      vc = client.voice_clients[0]
      await message.channel.send("disconnecting from all voice chats ^w^")

      await vc.disconnect()


    if message.content.startswith('$remotesay'):

      saywhat = message.content[11:]
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='com')
      tts.save("saywhat.mp3")


      try:
        #already connected!
        #print("already connected to vc!")
        
        await message.channel.send(f"remote say!!")

          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]
      except:
        pass

      vc = client.voice_clients[0]
      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} remote say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))


    if message.content.startswith('$joinandsay'):

      saychannel = int(message.content.split(" ")[1])
      saywhat = " ".join(message.content.split(" ")[2:])
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='com')
      tts.save("saywhat.mp3")


      try:
        #already connected!
        #print("already connected to vc!")
        
        await message.channel.send(f"join and say!!")
        

          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]
        if vc.channel.id != saychannel:
          errorpurposely = "1" + 1
          
      except:
        await message.channel.send("joining the vc!")
        vc = await client.get_channel(saychannel).connect()
        pass

      vc = client.voice_clients[0]
      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} remote say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))
    if message.content.startswith('$remotejiang'):

      saywhat = message.content[13:]
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " jiang " + saywhat, lang='zh-CN', tld='com')
      tts.save("jiang.mp3")


      try:
        #already connected!
        #print("already connected to vc!")
        
        await message.channel.send(f"remote jiang =|!!")

          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]
      except:
        pass

      vc = client.voice_clients[0]
      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} remote jiang in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('jiang.mp3'), volume=2.5))

    
    
    
    if message.content.startswith('$aussiesay'):
      print("say sensed from me")
      saywhat = " ".join(message.content.split(" ")[1:])
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='com.au')
      tts.save("saywhat.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))





  if message.content.startswith('$indiasay'):
      print("say sensed from me")
      saywhat = " ".join(message.content.split(" ")[1:])
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='co.in')
      tts.save("saywhat.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))



  if message.content.startswith('$tldsay'):
      print("say sensed from me")
      saywhat = " ".join(message.content.split(" ")[2:])
      tld = message.content.split(" ")[1]
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld=tld)
      tts.save("saywhat.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))


  if message.content.startswith('$briishsay'):
      print("say sensed from me")
      saywhat = " ".join(message.content.split(" ")[1:])
      print(saywhat)

      if "fuck" in saywhat:
        saywhat = saywhat.replace("fuck" ,"fish")

      
      if "penis" in saywhat:
        saywhat = saywhat.replace("penis", "pepes")

      tts = gtts.gTTS(sender + " said " + saywhat, lang='en', tld='co.uk')
      tts.save("saywhat.mp3")

      myvc = message.author.voice.channel.id
      print(myvc)

      try:
        vc = await client.get_channel(myvc).connect()
      except:
        #already connected!
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender} say in <#{vc.channel.id}>: {saywhat}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('saywhat.mp3'), volume=2.5))

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
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
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
        #print("already connected to vc!")
        if myvc != client.voice_clients[0].channel.id:
          await message.channel.send(f"currently in vc: <#{client.voice_clients[0].channel.id}>! moving to <#{myvc}>")
          vc = client.voice_clients[0]
          await vc.disconnect()
          vc = await client.get_channel(myvc).connect()
          
        #print(client.voice_clients[0].channel.id)
        vc = client.voice_clients[0]

      #vc = await client.get_channel(575368218009665541).connect() #connects to gossip girls

      await vc.guild.change_voice_state(channel=vc.channel, self_mute=False, self_deaf=True)

      vc.stop()
      
      await message.channel.send(f"{sender}在<#{vc.channel.id}>讲：{jiang}")
      vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio('jiang.mp3'), volume=2.5))

  if message.content.startswith('$play'):
      #print("play sensed")
      skill = message.content[6:]
      #print(skill)
      skill_list = ['agility', 'attack', 'cooking', 'crafting', 'defence', 'farming', 'fishing', 'fletching', 'fm', 'herblore', 'hp', 'mage1', 'magic', 'mining', 'prayer', 'ranged', 'rc', 'slayer', 'smithing', 'strength', 'thieving', 'waow', 'wc', 'disaster', 'theyalldead', 'questionable', 'sad', 'charge', 'crybaby', 'ayayayaya', 'nextlevelplay', 'lakadmatatag', 'absolutelyperfect', 'failedexperiment', '-w-', 'ss2', 'icebarrage', 'clue', 'dead', 'problem', 'power', 'scientist', 'emeraldstart', 'ludipq', 'diamondstart', 'diamondroute101', 'diamondpokecenter', 'p', 'scary', 'emeraldprestart', 'gbstart', 'gb1', 'fallabortown', 'verdanturf', 'xuemaojiao', 'xiulianaiqing', 'snowman', 'doorknock', 'outramparkstation', 'pleasemindthegap', 'pleasemindtheplatformgap', 'cicada']
      wav_list = ['diamondstart', 'diamondroute101', 'diamondpokecenter', 'p', 'scary']

      m4a_list = ['xiulianaiqing']

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
      if skill in wav_list:
        vc.play(discord.FFmpegPCMAudio(f'rs skills/{skill}.wav'))
      elif skill in m4a_list:
        vc.play(discord.PCMVolumeTransformer(original=discord.FFmpegPCMAudio(f'rs skills/{skill}.m4a'), volume=5))
        await message.channel.send(f"volume 5")
        
      else:
        vc.play(discord.FFmpegPCMAudio(f'rs skills/{skill}.mp3'))




    




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
      
      
      
      
      users = message.raw_mentions

      await message.channel.send(str(users))

      

      #member = message.guild.get_member_named(myinput)

      #await message.channel.send("member id: " + str(member.id) + "\nmember: " + str(member.name))

      

      return

      #current channel id: 443978416618864640 bot commands
      #current guild id: 260389250225143808 sga
  
 

  
  



  if message.content.startswith('$help'):
    myoutput = 'last updated: 16/3/2022 \n current available commands! \n $help \n $play (type for available sounds) \n $say something \n $jiang something (chinese accent) \n $dc (disconnect from all voice chats) \n $remotesay something \n '



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


  








my_secret = os.environ['TOKEN']

keep_alive()

client.run(my_secret)











