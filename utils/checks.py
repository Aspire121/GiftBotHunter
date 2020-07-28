from discord.ext import commands
import discord.utils



def is_admin(ctx:discord.message.Message):
    member = ctx.author # type: discord.Member
    if (member.guild_permissions.administrator):
        return True

    return False

def is_mod(ctx:discord.message.Message):
    member = ctx.author # type: discord.Member
    if (member.guild_permissions.manage_messages):
        return True

    return False
