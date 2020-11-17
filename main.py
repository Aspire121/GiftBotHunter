import discord
from discord.ext import commands

# TODO: Obvious todo
intents = discord.Intents.default()
intents.members = True
intents.presences = False

description = '''GiftBot Hunter'''
bot = commands.Bot(command_prefix=">", description=description, case_insensitive=False, intents=intents)
bot.remove_command("help")

# Update the sharedBot so other modules can use it
import utils.keys as keys
import utils.checks as checks
from ScamBotProtectionCog import ScamBotProtection

@bot.event
async def on_ready():
    print("GiftBotHunter 1.9 is ready!")
    print("The bot is currently protecting {} servers".format(len(bot.guilds)))
    for guild in bot.guilds:

        owner = bot.get_user(int(guild.owner_id))
        print("Guild name: {} | Owner: {}".format(guild, owner ))
    pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown) or isinstance(ctx.channel, discord.DMChannel):
        pass


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)

##########################
#       COMMANDS         #
##########################
@bot.command()
@commands.check(checks.is_mod)
async def help_ctx(ctx):
    help(ctx)

bot.add_cog(ScamBotProtection(bot))

bot.run(keys.Bot_token)
