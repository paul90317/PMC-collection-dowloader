import re

class parser:
    collection=lambda u :re.compile(r'^https://www.planetminecraft.com/collection/[0-9]+(/.*)?').fullmatch(u)!=None
    datapack=lambda u:re.compile(r'^https://www.planetminecraft.com/data-pack/[^/]+/?').fullmatch(u)!=None
    texturepack=lambda u:re.compile(r'^https://www.planetminecraft.com/texture-pack/[^/]+/?').fullmatch(u)!=None
    curseforge=lambda u:re.compile(r'^https://www.curseforge.com/minecraft/texture-packs/[^/]+/download/[0-9]+/?').fullmatch(u)!=None
    adfoc=lambda u:re.compile(r'^http://adfoc.us/[0-9]+').fullmatch(u)!=None
    mediafire=lambda u:re.compile(r'^https://www.mediafire.com/file/.*').fullmatch(u)!=None
    mirror=lambda u:re.compile(r'^https://www.planetminecraft.com/[^/]+/[^/]+/download/(mirror|website)/[0-9]+/?').fullmatch(u)!=None
    ignore=lambda u:re.compile(r'^https://(www.)?((youtube.com|youtu.be|discord.gg|discord.com)(/.*)?|github.com/[^/]+/[^/]+(/?|/tree/.*))').fullmatch(u)!=None

if __name__=='__main__':
    print(parser.mirror('https://www.planetminecraft.com/data-pack/mlik-bottle/download/file/652319'))
    pass