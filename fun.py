# fun.py
import discord
from discord.ext import commands
import random

def setup_fun(bot):

    @bot.command(name='randnum', description="Generate a random number between x and y.")
    async def randnum(ctx, x: int=None, y: int=None):
        if x is None or y is None:
            await ctx.send("Please provide two numbers x and y.")
            return
        if x >= y:
            await ctx.send("Please ensure x < y for generating a range.")
            return
        number = random.randint(x, y)
        await ctx.send(f'Random number between {x} and {y}: {number}')

    @bot.command(name='flipcoin', description="Flip a coin.")
    async def flipcoin(ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'Coin flip result: {result}')

    @bot.command(name='joke', description="Tell a random joke.")
    async def joke(ctx):
        jokes = [
            "Why did the bicycle fall over? It was two-tired!",
            "What do you call fake spaghetti? An impasta!",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why don't some couples go to the gym? Because some relationships don't work out.",
            "How does a penguin build its house? Igloos it together!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "What did the grape do when he got stepped on? Nothing but let out a little wine!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why was the broom late? It swept in!",
            "Why don't some fish play piano? Because you can't tuna fish!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why are ghosts bad at lying? Because you can see right through them!",
            "Why did the chicken join a band? Because it had the drumsticks!",
            "What do you call a cow with no legs? Ground beef!",
            "Why did the coffee file a police report? It got mugged!",
            "Why did the cookie go to the hospital? Because it felt crummy!",
            "Why don't some calendars do well in school? Their days are numbered!",
            "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field!",
            "What do you call a magician's dog? A labracadabrador!",
            "Why did the banana go to the doctor? Because it wasn't peeling well!",
            "Why was the math book sad? It had too many problems.",
            "Why did the stadium get hot after the game? All the fans left!",
            "What kind of shoes do ninjas wear? Sneakers!",
            "Why did the skeleton go to the party alone? Because he had no body to go with him!",
            "What did one wall say to the other? I'll meet you at the corner!",
            "What do you call a snowman with a six-pack? An abdominal snowman!",
            "Why don't some music notes eat? Because they're too sharp or flat!",
            "Why did the horse chew with its mouth open? Because it had bad stable manners!",
            "Why was the big cat disqualified from the race? Because it was a cheetah!",
            "What do you call a fish without eyes? Fsh!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "What kind of tree fits in your hand? A palm tree!",
            "Why did the mushroom go to the party alone? Because he's a fungi!",
            "What do you call a boomerang that won't come back? A stick!",
            "Why did the dog sit in the shade? Because he didn't want to be a hot dog!",
            "Why did the frog take the bus to work today? His car got toad away!",
            "What do you get when you cross a snowman and a dog? Frostbite!",
            "Why do birds fly south for the winter? Because it's too far to walk!",
            "What do you call a cat that likes to bowl? An alley cat!",
            "Why did the chicken join the band? Because it had the drumsticks!"
        ]
        await ctx.send(random.choice(jokes))
    @bot.command(name='8ball', description="Ask the magic 8-ball a question.")
    async def eight_ball(ctx, *, question=None):
        if question is None:
            await ctx.send("Please ask a question for the 8-ball.")
            return
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Mostly not"
            "Reply hazy, try again."
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @randnum.error
    @eight_ball.error
    @flipcoin.error
    @joke.error
    async def error_handler(ctx, error):
        await ctx.send("An error occurred. Please try again or check your command format.")

# This function should be called in main.py to register the commands
