import discord
import os
from dotenv import load_dotenv
import time
import datetime
import wikipedia
import smtplib


client = discord.Client()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('EmAIL ID HERE', 'PASSWORD')
    server.sendmail('EMAIL ID HERE', to, content)
    server.close()

@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.idle, activity=discord.Game('help!| Im just a prototype'))
     print('We have logged in as {0.user}'.format(client))

def check(msg):
        return msg.author == message.author and msg.channel == message.channel
def check1(msg):
        return msg.author == message.author and msg.channel != message.channel
@client.event
async def on_message(message):
    def check(msg):
        return msg.author == message.author and msg.channel == message.channel
    def check1(msg):
        return msg.author == message.author and msg.channel != message.channel
    if message.author == client.user:
        return
    elif message.content.startswith('help!'):
         await message.author.send("``` !search (query) makes me search the net```")
         await message.author.send("``` !time- makes me tell you the time```")
         await message.author.send("```% (role name) to get a role in the server```")
         await message.author.send("```#(role name) to remove a role from yourself```")
         await message.author.send("```send mail   - to send emails```")
         await message.author.send("```search music(query) searches the internet for a song```")
         await message.author.send("```$$servers - tells you the number of servers i am in```")
    elif message.content.startswith('!search'):
        que = message.content.replace("!search", "")
        results = wikipedia.summary(que, sentences=5)
        await message.channel.send(results)
    elif message.content.startswith('!time'):
        strTime = datetime.datetime.now().strftime("%H hrs %M min %S sec")    
        tim=await message.channel.send(strTime)
        await message.author.send('buy a watch!') 
    elif message.content.startswith('search music '):
        mus=message.content.replace('search music ','')
        await message.channel.send('results for ' + mus)
        finmus=mus.replace(' ','+')
        await message.channel.send('https://music.youtube.com/search?q=' + finmus)
    elif message.content.startswith('$$servers'):
        r=len(client.guilds)
        await message.channel.send(r)
    elif message.content.startswith('%'):
        x=message.content.replace("%","")
        await message.delete()
        try:
            Role = discord.utils.get(message.author.guild.roles, name=x)
            await message.author.add_roles(Role)
            await message.author.send('role added sucessfully.....')
        except:
            await message.author.send('i could not give you that role! try rechecking the role name')
    elif message.content.startswith('#'):
        x=message.content.replace("#","")
        await message.delete()
        try:
            Role = discord.utils.get(message.author.guild.roles, name=x)
            await message.author.remove_roles(Role)
            await message.author.send('role removed sucessfully.....')
        except:
            await message.author.send('i could not remove the role from you! recheck role name')
    elif message.content.startswith('send email'):
        try:
            await message.channel.send('what should i say in the email?')
            msg = await client.wait_for("message", check=check)
            content=msg.content
            content=content + '   -message sent by via manobot discord'
            await message.channel.send('who should i send this mail to')
            add = await client.wait_for("message", check=check)
            to = add.content
            sendEmail(to, content)
            await message.channel.send("Email has been sent!")
        except Exception as e:
            raise(e)
            await message.channel.send("Sorry I am not able to send this email")   
            

client.run('BOT TOKEN')
