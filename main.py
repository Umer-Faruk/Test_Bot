import discord
import os
import requests
from server import keep_alive

client = discord.Client()
my_secret = os.environ['Bot_token']


@client.event
async def on_redy():
  print('hello i logged in to discored as str {0.user}'.format(client))


@client.event
async def on_message(message):
  try:
    if message.author == client.user:
        return
    # print(message)
    # print(message.type)
    print(message.content)
    if message.content.startswith('$hello'):
      await message.channel.send("hello Sir")

    if message.content.startswith('$sum'):
      l = message.content.split()
      # print(l)
      a = int(l[1])
      b = int(l[2])
    
      await message.channel.send("sum = "+str(a+b) )
      
       
    if message.content.startswith('$sub'):
      l = message.content.split()
      # print(l)
      a = int(l[1])
      b = int(l[2])
      await message.channel.send("sub = "+str(a-b) )

    if message.content.startswith('$git_user'):
      l = message.content.split()
      user_name = l[1]
      username = user_name
      url = f"https://api.github.com/users/{username}"
      user_data = requests.get(url).json()
      # print(user_data)
      # print(user_data['bio'])
      # print(user_data['name'])
      # print(user_data['public_repos'])
      # print(user_data['public_gists'])
      # print(user_data['followers'])
      # print(user_data['following'])
      await message.channel.send("user name = "+str(user_data['name'])+"\n bio = "+str(user_data['bio'])+"\n public_repos = "+str(user_data['public_repos'])+"\n public_gists = "+str(user_data['public_gists'])+"\n followers = "+str(user_data['followers'])+"\n following = "+str(user_data['following']))

  except:
     await message.channel.send("this is rong formet    use formets given below \n $sum num1 num2 \n $sub num1 num2 \n $git_user github id")


def git_user():
  username = "Umer-Faruk"
  url = f"https://api.github.com/users/{username}"
  user_data = requests.get(url).json()
  print(user_data)
  print(user_data['bio'])
  print(user_data['name'])
  print(user_data['public_repos'])
  print(user_data['public_gists'])
  print(user_data['followers'])
  print(user_data['following'])


  # followers_url = user_data['followers_url']
  # followers_data = requests.get(followers_url).json()
  # for i in followers_data:
  #   print(i['name'])

 
# git_user()

    
keep_alive()
client.run(my_secret)
 

 
