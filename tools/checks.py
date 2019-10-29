from discord.ext import commands


# Checks
def in_channel(channel_name):
    ''' Checks if command is sent from a specific channel '''
    def predicate(ctx):
        return ctx.channel.name == channel_name
    return commands.check(predicate)


def in_channels(channel_list):
    ''' Checks if command is sent from a channel in a list '''
    def predicate(ctx):
        return ctx.channel.name in channel_list
    return commands.check(predicate)
