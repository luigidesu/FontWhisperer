import discord
from discord.ext import commands
import random
from fuzzywuzzy import fuzz
import asyncio

TOKEN = '' #Add yo token here.
SCANLATOR_ROLE = 'Scanlator'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# This the font lists, the font is the name and the link is... the link, the image is the image link, which will get embed.
font_lists = {
    'Dialogue': [
        {'font': 'Joe Kubert', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847154566733627423', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847154508442107914/bl017i-2T.png'},
        {'font': 'Wall Scrawler', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847156673366065192', 'image': 'https://media.discordapp.net/attachments/846430804418625536/847156613503516772/bl020i-2T.png'},
        {'font': 'Hedge Backwards', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847156531995607070', 'image': 'https://media.discordapp.net/attachments/846430804418625536/847156505445662770/bl019i-2T.png'},
        {'font': 'Soothsayer', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086717225064485005', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086717224548581506/Soothsayer1.png'},
        {'font': 'Soliloquous', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086717021514891316', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086717021376499762/Soliloquous1.png'},
        {'font': 'Monologous', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086714587782590597', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086714587191197696/Monologous1.png'},
        {'font': 'Ladronn', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086714049795981352', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086714049275891903/Ladronn1.png'},
        {'font': 'Kiss And Tell', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086713783558357002', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086713782983725167/Kiss_And_Tell1.png'},
        {'font': 'Jim Lee', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086712856122237009', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086712855648272495/Jim_Lee1.png'},
        {'font': 'Face Front', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086710747062616146', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086710746710286407/Face_Front1.png'},
        {'font': 'Cutthroat', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086707786408284294', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086707785892376587/Cutthroat.png'},
        {'font': 'Cutthroat Lower', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086708075957858364', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086708075190288414/Cutthroat_Lower1.png'},
        {'font': 'Comicrazy', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086707104204734555', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086707103722373200/Comicrazy1.png'},
        {'font': 'Clean Cut Kid', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086706565224079360', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086706564691406858/Clean_Cut_Kid1.png'},
        {'font': 'Kickback', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086304553672122419', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1086304520285470801/bl036i-2T.png'},
        {'font': 'Chatterbox', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1086303486012043395', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/1086303485781348553/bl029i-2T.png'},
        {'font': 'Wascally Wabbit', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1084262142045335552', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1084262141441343548/WASCALLY_WABBIT.png'},
        {'font': 'Fontropolis', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1050390256874180618', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1050390256140177459/IMG_9755.png'},
        {'font': 'Mighty Mouth', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/1050051531459788900', 'image': 'https://media.discordapp.net/attachments/846430804418625536/1050051530801299496/bl072-2T.png'},
        {'font': 'Mike Kunkel', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/903268357447512085', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/903268312484565083/unknown.png'},
        {'font': 'Wild Words Lower', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/886310742268207175', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/886310645702733854/unknown.png'},
        {'font': 'Joe Mad', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/886289032580038666', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/886288933179252817/unknown.png'},
        {'font': 'Totally Awesome', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/858824830308581396', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/858824790181150770/unknown.png'},
        {'font': 'Mild Mannered', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/855499879680573450', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/855499829014822974/unknown.png'},
        {'font': 'Richard Starkings', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847518991428616263', 'image': 'https://media.discordapp.net/attachments/846430804418625536/847518892134105148/bl049i-2T.png'},
        {'font': 'Hush Hush', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847517692961488906', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847517457732337694/bl022i-2T.png'},
        {'font': 'Tall Tales', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847517239309369374', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847517142987702332/bl074-2T.png'},
        {'font': 'Origin Story', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847516867676471336', 'image': 'https://media.discordapp.net/attachments/846430804418625536/847516805533925376/bl073-'},
        {'font': 'Plot Holes', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/1055577687093162115', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/1055577686870867978/FkluKnWXkAEc24U.jpg'},
        {'font': 'Out of Line Pro', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/1041472795089051718', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/1041472794355052667/unknown.png'},
        {'font': 'Nerves of Steel', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/1027447533028524032', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/1027447532357423114/unknown.png'},
        {'font': 'Hometown Hero', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/965130297513476167', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/965130232107507742/Ht_H.png'},
        {'font': 'Hired Goons', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/965126121970597911', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/965126055369248798/3328.png'},
        {'font': 'Ready for Anything', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/910618603865399298', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/910618561305772032/295571.png'},
        {'font': 'Ready for More', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/910617321310126153', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/910617206684008519/tYt452HmyAIrfsllZZulk8rk_543ab0925de8c1d3facae7db055ba361.png'},
        {'font': 'Collect Em\' Now', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/877783924900786206', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/877783904172531772/flag_cen1.png'},
        {'font': 'Sunday Comics', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/872184756413030470', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/872184714985889812/flag_sundaycomics_720x.jpg'},
        {'font': 'Super Strong', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/872184197', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/872184136960475156/flag_superstrong_720x.jpg'},
        {'font': 'Tokyo Robot', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/872179992015011840', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/872179960754868274/7009_0.jpg'},
        {'font': 'Unmasked', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/872173562511884339', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/872173522510823545/flag_unmasked_720x.jpg'},
        {'font': 'Evil Genius', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/871043122321326110', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/871043099147763762/flag_evilgenius_300x300.png'},
        {'font': 'Elevations', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/871042787259322418', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/871042776723255337/flag_elevations_300x300.png'},
        {'font': 'Duty Calls', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/871040468841033778', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/871040460590813224/flag_dutycalls_300x300.png'},
        {'font': 'Web Letterer', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/870703409840402513', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/870703371395432468/flag_webletterer_720x.jpg'},
        {'font': 'Web Letterer PRO', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/870703808177647617', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/870703769548095488/flag_weblettererpro_720x.jpg'},
        {'font': 'Wickenden Cafe NDP', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/870700444803039283', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/870700417871380550/b45489926170a23850c88871dc9cce7a.png'},
        {'font': 'Zud Juice', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/870690867898359909', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/870690819907141652/zud-juice-font-2-big.png'},
        {'font': 'Silver Age', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/865038615934140436', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/865038593248591872/flag_silverage.png'},
        {'font': 'Tight Spot', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/862641315762536469', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/862641190055051284/flag_tightspot1_lg.png'},
        {'font': 'Manga Master', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/861523281499652116', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/861523242207805440/flag_mangamaster.png'},
        {'font': 'Crime Fighter', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/860342261890809876', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/860342252685099048/flag_crimefighter_300x300.png'},
        {'font': 'Cloud Splitter', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/860337971735298048', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/860337916899360778/flag_cloudsplitter_300x300.png'},
        {'font': 'Blambot Classic', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/860234216221704222', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/860234200006393856/flag_bbclassic_300x300.png'},
        {'font': 'Blambot Casual', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/860234048042565634', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/860234028312821820/flag_bbcasual_300x300.png'},
        {'font': 'Blambastic', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/860233876819673098', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/860233846564978698/flag_blambastic1-2_300x300.png'},
        {'font': 'Back Issues', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/859925285172543558', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/859925182025170974/flag_backissues_300x300.png'},
        {'font': 'Action Figure', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/858469293405896724', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/858469242374062080/flag_actionfigure_300x300.png'},
        {'font': '10 Cent Comics', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/858468507594260520', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/858468291555098664/flag_10centcomics_300x300.png'},
        {'font': 'Heavy Mettle', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/855888010204938241', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/855887953003675668/flag_heavymettle.png'},
        {'font': 'EuroComic', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854297720617697280', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854297686232006716/flag_eurocomic.png'},
        {'font': 'Lint McCree', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854217750838378497', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854217677333987358/flag_LM.png'},
        {'font': 'Bottle Rocket', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854216013032718386', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854215923464405002/flag_bottlerocket.png'},
        {'font': 'San Diego 2005', 'link': 'https://discord.com/channels/846402995252232232/846599363111157760/948969660940959784', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854208998554861568/font_sd2005.jpg'},
        {'font': 'San Diego 2004', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854208930767044628', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854208891914682368/font_sd2004.jpg'},
        {'font': 'San Diego 2003', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854208781691650088', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854208737992376340/font_sd2003.jpg'},
        {'font': 'San Diego 2002', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854201510286852096', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854201478134759444/font_sd2002.jpg'},
        {'font': 'LetterOMatic!', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854101644370116628', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854101555027771432/sletteromatic-0.png'},
        {'font': 'Enchilada', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854098519173890079', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854098449111580702/enchilada-741x415-d578a9d5f4.png'},
        {'font': 'Edible Pet', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/854097970012880916', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/854097906935791646/unknown.png'},
        {'font': 'Victory Speech Lower', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847511894910959656', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847511795858014208/bl066i-2T.png'},
        {'font': 'Victory Speech', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847511726018920478', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847511694439350312/bl064i-2T.png'},
        {'font': 'Meanwhile', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847508285858250812', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847508182532358174/bl012i-2T.png'},
        {'font': 'Wild Words [I\'m getting pointed to my head with a gun right now.]', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847506994239504444', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847506919533969458/bl003i-2T.png'},
        {'font': 'Blah Blah Upper', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847439886893449256', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847439710858248212/bl069-2T.png'},
        {'font': 'Blah Blah Blah', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847439647998476368', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847439590188515338/bl026i-2T.png'},
        {'font': 'A Likely Story', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847412604033171458', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847412520566128661/bl065i-2T.png'},
        {'font': 'J. Scott Campbell Lower', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847402730011099176', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847402591281610772/bl063i-2T.png'},
        {'font': 'The Sculptor', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847399569544446012', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847399517502177280/bl061i-2T.png'},
        {'font': 'Colleen Doran', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847393922501312532', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847393863718273074/bl055i-2T.png'},
        {'font': 'Code Monkey Variable', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847373162849107998', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847373110847209472/bl050i-2T.png'},
        {'font': 'Rick Veitch', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847369709199949844', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847369634184298526/bl046i-2T.png'},
        {'font': 'Marian Churchland', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847346711265673226', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847346618902642718/bl042i-2T.png'},
        {'font': 'Holier Than Thou', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847160760000839690', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847160697690521671/cl328i-2T.png'},
        {'font': 'Scott McCloud', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847160601646202950', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847160496142155786/bl034i-2T.png'},
        {'font': 'Astronauts in Trouble', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847158372880875540', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847158216810299433/bl031i-2T.png'},
        {'font': 'Adam Kubert', 'link': 'https://discord.com/channels/846402995252232232/846430804418625536/847154961677811762', 'image': 'https://cdn.discordapp.com/attachments/846430804418625536/847154874209927248/bl018i-1.png'}
    ],
    'Narration': [
        {'font': 'Duty Calls', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/871040468841033778', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/871040460590813224/flag_dutycalls_300x300.png'}
    ],
    'Aside': [
    {'font': 'The Sculptor', 'link': 'https://discord.com/channels/846402995252232232/846430825934487602/871040468841033778', 'image': 'https://cdn.discordapp.com/attachments/846430825934487602/871040460590813224/flag_dutycalls_300x300.png'}
    ]
}


# Console nerd stuff
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

def find_closest_match(input_name, available_names):
    matches = []
    for name in available_names:
        similarity_score = fuzz.ratio(input_name, name)
        matches.append((name, similarity_score))

    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[0][0]

@bot.command()
async def suggest(ctx, font_type: str = None):
    if font_type is None: #If you send just /suggest without any font, it'll show you the font lists, kinda like a help command.
        available_lists = '\n* '.join(font_lists.keys())
        preview_message = f"Hey, I'm the font suggestor. Here are my font lists: \n* {available_lists}\nTo get a suggestion, just type ***/suggest + The list you want to get a suggestion from.***"
        await ctx.send(preview_message)
        return

    if font_type.lower() == "set": #This command gives a set of fonts, getting one font from every list, but without an image, to avoid having 50 embeds.
        suggestion_message = "I suggest using this font set:\n"
        for font_list, suggestions in font_lists.items():
            suggestion = random.choice(suggestions)
            font_name = suggestion['font']
            link = suggestion['link']
            suggestion_message += f"{font_list} - ***{font_name}*** - {link}\n"
        
        await ctx.send(suggestion_message)
        return
    
    member = ctx.author
    scanlator_role = discord.utils.get(member.guild.roles, name=SCANLATOR_ROLE)
    
    font_type = font_type.lower() #Lowercase protection.
    
    closest_match = find_closest_match(font_type, font_lists.keys()) #Anti-Typo errors measure, so you can send something like "DaILoGeU" and still get a font from the "Dialogue" font list.
    
    if closest_match in font_lists: 
        suggestions = font_lists[closest_match]
        suggestion = random.choice(suggestions)
        font_name = suggestion['font']
        link = suggestion['link']
        image_link = suggestion['image']
        
        message = f'I suggest using ***{font_name}*** for {closest_match}.\n{link}' #This is the default message, a suggestion from a list.
        
        if scanlator_role is not None and scanlator_role not in member.roles:
            message += f'\n\nCan\'t access the link? Make sure you have the {SCANLATOR_ROLE} role.\nYou can ask for it on https://discord.com/channels/846402995252232232/951959937746083870' #This is the message sent if the user doesn't have the scanlator role.
        
        await ctx.send(message)
        await ctx.send(image_link)  # Sends the image as a separate message, so it can get embed correctly.
    else:
        await ctx.send(f'Sorry, I don\'t have any suggestions for "{font_type}".') #This error appears if you make a typo, even though we got a protection for that, this can appear.

bot.run(TOKEN)
