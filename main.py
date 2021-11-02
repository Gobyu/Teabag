from replit import db
import discord
import os
import random
import json
import requests


client = discord.Client()


poker_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
poker_suits = ["♤", "♡", "♧", "♢"]

profanity_list = []
profanity_warning = "watch yo profanity"

profanity_list = db["swears_list"]





## FUNC: rock_paper_scissors ##
def rock_paper_scissors(you):
  computer = random.randint(1,3)

  if computer == 1:
    if you.lower() == "rock":
      return "Computer: :rock:\nYou: :rock:\n`Result: Tie.` :no_mouth:"
    if you.lower() == "paper":
      return "Computer: :rock:\nYou: :roll_of_paper:\n`Result: You Win!` :slight_smile:"
    if you.lower() == "scissors":
      return "Computer: :rock:\nYou: :scissors:\n`Result: You Lose.` :slight_frown:"

  elif computer == 2:
    if you.lower() == "rock":
      return "Computer: :roll_of_paper:\nYou: :rock:\n`Result: You Lose.` :slight_frown:"
    if you.lower() == "paper":
      return "Computer: :roll_of_paper:\nYou: :roll_of_paper:\n`Result: Tie.` :no_mouth:"
    if you.lower() == "scissors":
      return "Computer: :roll_of_paper:\nYou: :scissors:\n`Result: You Win!` :slight_smile:"

  elif computer == 3:
    if you.lower() == "rock":
      return "Computer: :scissors:\nYou: :rock:\n`Result: You Win!` :slight_smile:"
    if you.lower() == "paper":
      return "Computer: :scissors:\nYou: :roll_of_paper:\n`Result: You Lose.` :slight_frown:"
    if you.lower() == "scissors":
      return "Computer: :scissors:\nYou: :scissors:\n`Result: Tie.` :no_mouth:"

## FUNC: coin_flip ##
def coin_flip():
  flip = random.randint(0,1)
  if flip == 0:
    return "Tails"
  elif flip == 1:
    return "Heads"

## FUNC: get_city_time ##
def get_city_time(region,city):
  response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=F3CIUVZMCEIP&format=json&by=zone&zone=" + region + "/" + city)
  json_data = json.loads(response.text)
  format_time_date = json_data['formatted']
  if format_time_date == "":
    return False
  else:
    return format_time_date

## FUNC: generate_profanity_list ##
def generate_profanity_string(list):
  sorted_list = []
  profanity_string = ""
  for v in range(len(list)):
    sorted_list.append(list[v])
    sorted_list.sort()
  for v in range(len(sorted_list)):
    profanity_string = profanity_string + sorted_list[v] + " | "
  return profanity_string

## FUNC: rng ##
def rng(v):
  return random.randint(1,v)

## FUNC: add_profanity ##
def add_profanity(profanity_list,profanity_word):
  if profanity_list.count(profanity_word) == 0:
    return profanity_list.append(profanity_word)
  else:
    return False

## FUNC: del_profanity ##
def del_profanity(profanity_list,profanity_word):
  if profanity_list.count(profanity_word) > 0:
    return profanity_list.remove(profanity_word)
  else:
    return False

## FUNC: clr_profanity ##
def clr_profanity(profanity_list):
  return profanity_list.clear()

## FUNC rate_something ##
def rate_something():
  rating = round(random.uniform(1,10),1)
  return str(rating)






@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg_lower = msg.lower()
    msg_lower_split = msg_lower.split(" ")

    ## CMD: !help ##
    if msg_lower.startswith("!help"):
      await message.channel.send(':small_orange_diamond::small_blue_diamond:**__List of commands__**:small_blue_diamond::small_orange_diamond:\n\n:o: **1. !addprofanity**\nFunction: add a term to the profanity list\nSyntax: !addprofanity {term}\n\n:x: **2. !removeprofanity**\nFunction: remove a term from the profanity list\nSyntax: !removeprofanity {term}\n\n:closed_book: **3. !profanitylist**\nFunction: Shows the profanity list\n\n:diamonds: **4. !poker**\nFunction: Sends a random poker card\n\n:game_die: **5. !rng**\nFunction: generates a random number from 0 to N\nSyntax: !rng N\n\n:1234: **6. !rate**\nFunction: rates a term\nSyntax: !rate {term}\n\n:clock1030: **7. !get_city_time**\nFunction: Sends the time and date of a supported city\nSyntax: !get_city_time {region} {city}\n`use !get_regions for a list of regions. Please use _ instead of spaces for cities with more than one word (e.g. Los Angeles --> Los_Angeles)`\n\n:map: **8. !get_regions**\nFunction: Sends a list of supported regions for !get_city_time\n\n**:coin: 9. !coin_flip**\nFunction: Flip a coin\n\n**:question: 10. !rps**\nFunction: Play Rock Paper Scissors with the computer\nSyntax: !rps {rock,paper,or scissors}')

    ## CMD: !addprofanity ##
    if msg_lower.startswith("!addprofanity"):
      new_profanity = msg_lower.split("!addprofanity ",1)[1]
      if add_profanity(profanity_list, new_profanity) != False:
        db["swears_list"] = profanity_list
        await message.channel.send(message.author.mention + ' added **"' + new_profanity + '"**' + " to the profanity list.")
      else:
        await message.channel.send('**"' + new_profanity + '"**' + " already exists in the profanity list")
    else:

      ## CMD: !removeprofanity ##
      if msg_lower.startswith("!removeprofanity"):
        new_profanity = msg_lower.split("removeprofanity ",1)[1]
        if del_profanity(profanity_list, new_profanity) != False:
          db["swears_list"] = profanity_list
          await message.channel.send(message.author.mention + ' deleted **"' + new_profanity + '"**' + " from the profanity list.")
        else:
          await message.channel.send('**"' + new_profanity + '"**' + " does not exist in the profanity list")
      else:
        if any(word in msg_lower_split for word in profanity_list):
          await message.delete()
          await message.channel.send(message.author.mention + " " + profanity_warning)

    ## CMD: !poker ##  
    if msg_lower.startswith('!poker'):
      await message.channel.send("`" + random.choice(poker_cards) + random.choice(poker_suits) + "`")

    ## CMD: !rng ##
    if msg_lower.startswith('!rng'):
      rng_range = msg_lower.split("rng ",1)[1]
      if rng_range.isdigit() == False:
        await message.channel.send("cannot pick a random number between 1 and a non number")
      elif int(rng_range) < 1:
        await message.channel.send("cannot pick a random number between 1 and " + str(rng_range))
      else:
        result_number = rng(int(rng_range))
        await message.channel.send(":game_die:`random number from 1 to " + str(rng_range) + ":` " + "**" + str(result_number) + "**")
    
    ## CMD: !profanitylist ##
    if msg_lower.startswith('!profanitylist'):
      await message.channel.send(":closed_book: **Profanity List: **" + "` " + generate_profanity_string(profanity_list) + "`")

    ## CMD: !clearprofanity ##
    if msg_lower.startswith('!clearprofanity'):
      clr_profanity(profanity_list)
      db["swears_list"] = profanity_list
      await message.channel.send(message.author.mention + " cleared the profanity list.")

    ## CMD: !rate ##
    if msg_lower.startswith('!rate'):
      ratee = msg_lower.split("!rate ",1)[1]
      rating = rate_something()
      if float(rating) < 3:
        await message.channel.send(":clown: BOO! " + ratee + "'s rating is **" + rating + "/10**")
      elif float(rating) < 7:
        await message.channel.send(":man_shrugging: " + ratee + "'s rating is **" + rating + "/10**")
      elif float(rating) <10 :
        await message.channel.send(":star_struck: SHEEESH! " + ratee + "'s rating is **" + rating + "/10**")
      elif float(rating) == 10:
        await message.channel.send(ratee + " is a KING! :crown: **" + rating + "/10**")

    ## CMD: !get_city_time ##
    if msg_lower.startswith('!get_city_time'):
      region_city = msg_lower.split("!get_city_time ",1)[1]
      region = region_city.split(" ",1)[0]
      city = region_city.split(" ",1)[1]
      if get_city_time(region,city) != False:
        await message.channel.send("The time and date for " + city + ":\n`" + get_city_time(region,city) + "`")
      else:
        await message.channel.send("Either the Region/City is not supported or command format incorrect. Use !help for formatting help")

    ## CMD: !get_regions ##
    if msg_lower.startswith('!get_regions'):
      await message.channel.send("Africa, America, Antartica, Asia, Atlantic, Australia, Europe, Indian, Pacific")

    ## CMD: !coin_flip ##
    if msg_lower.startswith('!coin_flip'):
      await message.channel.send(":coin: Coin Flip: " + coin_flip())

    ## CMD: !RPS ##
    if msg_lower.startswith('!rps'):
      your_RPS = msg_lower.split("!rps ",1)[1]
      await message.channel.send(rock_paper_scissors(your_RPS))




client.run(os.getenv('TOKEN'))