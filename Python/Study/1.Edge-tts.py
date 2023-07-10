import edge_tts
import asyncio
TEXT = '''
小马过河

马棚里住着一匹老马和一匹小马。

有一天，老马对小马说：你已经长大了，能帮妈妈做点儿事吗？
小马连蹦带跳地说：怎么不能？我很愿意帮您做事。老马高兴地说：那好啊，你把这半口袋麦子驮到磨坊去吧。

小马驮起口袋，飞快地往磨坊跑去。跑着跑着，一条小河挡住了去路，河水哗哗地流着。小马为难了，心想：我能不能过去呢？如果妈妈在身边，问问她该怎么办，那多好啊！可是他离家已经很远了。

'''
# with open('G:\\CodesProjects\\Python\\Study\\1.Edge-tts.txt', 'rb')as f:
#     data = f.read()
#     TEXT = data.decode('utf-8')
# print(TEXT)
voice = 'zh-CN-XiaoxiaoNeural'
output = 'G:\\CodesProjects\\Python\\Study\\1.Edge-tts.mp3'
rate = '+10%'
volume = '+10%'


async def my_function():
    tts = edge_tts.Communicate(
        text=TEXT, voice=voice, rate=rate, volume=volume)
    await tts.save(output)
if __name__ == '__main__':
    asyncio.run(my_function())



'''

Name: en-AU-NatashaNeural
Gender: Female

Name: en-AU-WilliamNeural
Gender: Male

Name: en-CA-ClaraNeural
Gender: Female

Name: en-CA-LiamNeural
Gender: Male

Name: en-GB-LibbyNeural
Gender: Female

Name: en-GB-MaisieNeural
Gender: Female

Name: en-GB-RyanNeural
Gender: Male

Name: en-GB-SoniaNeural
Gender: Female

Name: en-GB-ThomasNeural
Gender: Male

Name: en-HK-SamNeural
Gender: Male

Name: en-HK-YanNeural
Gender: Female

Name: en-IE-ConnorNeural
Gender: Male

Name: en-IE-EmilyNeural
Gender: Female

Name: en-IN-NeerjaExpressiveNeural
Gender: Female

Name: en-IN-NeerjaNeural
Gender: Female

Name: en-IN-PrabhatNeural
Gender: Male

Name: en-KE-AsiliaNeural
Gender: Female

Name: en-KE-ChilembaNeural
Gender: Male

Name: en-NG-AbeoNeural
Gender: Male

Name: en-NG-EzinneNeural
Gender: Female

Name: en-NZ-MitchellNeural
Gender: Male

Name: en-NZ-MollyNeural
Gender: Female

Name: en-PH-JamesNeural
Gender: Male

Name: en-PH-RosaNeural
Gender: Female

Name: en-SG-LunaNeural
Gender: Female

Name: en-SG-WayneNeural
Gender: Male

Name: en-TZ-ElimuNeural
Gender: Male

Name: en-TZ-ImaniNeural
Gender: Female

Name: en-US-AnaNeural
Gender: Female

Name: en-US-AriaNeural
Gender: Female

Name: en-US-ChristopherNeural
Gender: Male

Name: en-US-EricNeural
Gender: Male

Name: en-US-GuyNeural
Gender: Male

Name: en-US-JennyNeural
Gender: Female

Name: en-US-MichelleNeural
Gender: Female

Name: en-US-RogerNeural
Gender: Male

Name: en-US-SteffanNeural
Gender: Male

Name: en-ZA-LeahNeural
Gender: Female

Name: en-ZA-LukeNeural
Gender: Male
'''
'''
Name: zh-CN-XiaoxiaoNeural
Gender: Female

Name: zh-CN-XiaoyiNeural
Gender: Female

Name: zh-CN-YunjianNeural
Gender: Male

Name: zh-CN-YunxiNeural
Gender: Male

Name: zh-CN-YunxiaNeural
Gender: Male

Name: zh-CN-YunyangNeural
Gender: Male

Name: zh-CN-liaoning-XiaobeiNeural
Gender: Female

Name: zh-CN-shaanxi-XiaoniNeural
Gender: Female

Name: zh-HK-HiuGaaiNeural
Gender: Female

Name: zh-HK-HiuMaanNeural
Gender: Female

Name: zh-HK-WanLungNeural
Gender: Male

Name: zh-TW-HsiaoChenNeural
Gender: Female

Name: zh-TW-HsiaoYuNeural
Gender: Female

Name: zh-TW-YunJheNeural
Gender: Male
'''
