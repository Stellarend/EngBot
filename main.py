import discord
import asyncio
import os

VALUE_DICT = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
              "8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
              0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",
              8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

client = discord.Client()
disFormat = "__**engbot:**__\n```{}```"
helpText = """#### Syntax ####
    !engbot,command[,params]
    command: The command to be used, see list of commands below
    params: The parameters to pass to the command

#### List of Commands ####
    help: Shows this help menu
    
    convertBase: Converts a number from one base to another
        startBase: The base of the number you pass through
        targetBase: The base that you want to convert to
        number: The number you want to convert

#### Examples ####
    !engbot,help
    Shows the help menu

    !engbot,convertBase,16,2,A23482
    Converts the number A23482 to binary(base 2)
"""
errorText= """There was an error with the parameters you gave"""
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("---------")

@client.event
async def on_message(message):
    text = message.content.replace(" ", "")
    if text.startswith("!engbot"):
        parsedText = text.split(',')
        if len(parsedText)>2: params = parsedText[2:len(parsedText)]
        command = parsedText[1]
        if command == "help":
            await client.send_message(message.channel, disFormat.format(helpText))
        elif command == "convertBase":
            try:
                output = base_to_base(*params)
                await client.send_message(message.channel, disFormat.format(output))
            except:
                await client.send_message(message.channel, disFormat.format(errorText))
            
def base_to_dec(startBase, numberStr):
    startBase = int(startBase)
    numberStr = str(numberStr).upper()
    positive = 1
    if numberStr[0] == '-':
        positive = -1
        numberStr = numberStr[1:len(numberStr)]
    numberStr = numberStr[::-1] 
    decValue = 0
    for i, digit in enumerate(numberStr):
        decValue += startBase**i * VALUE_DICT[digit]
    return decValue * positive

def dec_to_base(targetBase, number):
    targetBase = int(targetBase)
    number = int(number)
    outString = ""
    if number < 0: outString += '-'
    number = abs(number)
    exponent = int(16/targetBase * 14)
    while targetBase ** exponent > number:
        exponent -= 1
    while number > 0:
        expValue = targetBase ** exponent
        if expValue <= number:
            digit = number // expValue
            outString += VALUE_DICT[digit]
            number -= expValue * digit
        else:
            outString += '0'
        exponent -= 1
    return outString
    
def base_to_base(startBase, targetBase, number):
    return(dec_to_base(targetBase, base_to_dec(startBase, number)))

username = input("username(email):")
password = input("password:")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
else:
    pass
print("Trying to log in, please wait")
client.run(username, password)
