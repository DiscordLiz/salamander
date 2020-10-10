#   Copyright 2020 Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import annotations

from discord.ext import commands

from ..bot import Salamander, SalamanderContext


class Meta(commands.Cog):
    def __init__(self, bot: Salamander):
        self.bot: Salamander = bot

    @commands.is_owner()
    @commands.command()
    async def shutdown(self, ctx: SalamanderContext):
        """ Shuts down the bot """
        await self.bot.logout()
