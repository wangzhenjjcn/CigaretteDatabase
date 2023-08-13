import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import json
from io import BytesIO
import re
import time
import csv

# 如果Tesseract的路径不在您的系统PATH中，请取消以下行的注释，并指定正确的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image_from_url(img_url):
    urlstr=str(img_url)
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/6d4/edc/6d4edc2fb3a94a707d2d38f529f80ace.png","0.1mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/a25/57f/a2557ffb8eb6d306aa94a5d648b6f35a.png","0.2mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d52/573/d52573c9d4cf1eb50005d5592d82fc1c.png","0.3mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f0a/d4d/f0ad4db43c9ed066fb15f2ff20ad1b6a.png","0.4mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ae8/54c/ae854ca6390c8fef559360d057a46638.png","0.5mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/032/1bf/0321bf304f596d2ba2dc38e550cb8420.png","0.6mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/154/a5b/154a5b3d18f65092c738312a73461c05.png","0.7mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e9f/31e/e9f31eff2c370c2eddf50713ae53ab61.png","0.8mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/299/ec2/299ec2bb8ab6d3a4c41f9c6bf39411ff.png","0.9mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4d3/6eb/4d36ebb935332fd2c80e465e6a145a4b.png","1mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/fce/005/fce005075e99b885b79a90e3471f1855.png","1.0mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/207/b99/207b99d095a1a91017908c5bc8e03acf.png","1.1mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/1b3/727/1b3727e8c25203686f846a5a4dec3809.png","1.2mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/737/1e7/7371e7252b6e7c8b2f846cc1f5b2ec79.png","1.3mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/846/9e9/8469e9835d88d9bd3c4509160ed37a22.png","1.5mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/030/e02/030e02e9713fe60654393dc3d5798dbd.png","2mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4a5/ab2/4a5ab2d7e8eb5da25864bd8f8b78b465.png","3mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9c6/764/9c6764951c1b3e52561d864627aadbaa.png","4mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/775/3bd/7753bd386e520af95aad2afe01d29d6c.png","4.5mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/1c2/e01/1c2e01e6e28c2e7bfcfdf5ffb5c92b2f.png","5mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/586/565/586565cd1677763594d56f11743e97ce.png","6mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/323/3b4/3233b449b016de60019b6b184f047641.png","7mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4af/bb2/4afbb2d48718dffd6fb7b2952435e5bf.png","8mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/489/f78/489f78b6037e5f94d6409f61d2f99755.png","9mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/fd0/a5a/fd0a5a1127e03b734f91566c7e44f2a1.png","10mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/23c/208/23c208ccca6a91fcc39bfaf1494273a0.png","11mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/fed/b33/fedb33caeefd245d320c59dee3029131.png","12mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e20/8e8/e208e8ae7c03b8496a8a501aa1ef6f8f.png","13mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d0a/f5a/d0af5a1848bb82660c1a4997b6c15548.png","14mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/c28/188/c28188c11fc7ef0f157310c974f8337c.png","15mg") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/474/aa6/474aa69787195f07271e3b13c34c1f73.png","16mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ca6/274/ca6274c48d170f834ccccd13c2515881.png","17mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/301/fa3/301fa37cca3f344e551d722d89c9f236.png","17.5mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/eb7/62c/eb762c98f17984801e1927f9d0fa8492.png","18mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/844/20e/84420e4ea4386a35ec5277c6db4dd683.png","20mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/594/8a5/5948a5f85189ea2f0e8431c131bb7da7.png","25mg")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/24d/6a5/24d6a558da285f720a7dd70a914ad322.png","30mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/c0b/d34/c0bd34c3e86f8f1388bc2bc3f0dc4d8d.png","24mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/594/8a5/5948a5f85189ea2f0e8431c131bb7da7.png","25mm") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/cfe/1b5/cfe1b576b2e67877bd6ced7de05e411c.png","28mm") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/24d/6a5/24d6a558da285f720a7dd70a914ad322.png","30mm") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5bb/ded/5bbded2b064913e77ebf7e7b9ffea5ce.png","84mm") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/b31/de2/b31de2b0d6d24dd4174d0247371452ef.png","¥5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/1a5/10d/1a510dd86f10f17c703d65916c8d7270.png","¥10元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/210/f7f/210f7f3a101a84e98c64330a1e3e5bbb.png","¥15元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f4a/8f9/f4a8f96daf63733375c68d8f5d793c9e.png","¥17元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5a8/240/5a824059b1105bcaabd8a62189b42a22.png","¥20元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/b4f/b2a/b4fb2a7bf98f78a7459d74febf822a64.png","¥22元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ac2/ee6/ac2ee6a4ffa89754dd8bd02446d7b7fa.png","¥26元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/1ed/400/1ed400b70741947ed316ab019a68bee8.png","¥50元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f8e/7e7/f8e7e7b43752eebb3fa9192ed06f1906.png","¥65元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/038/66b/03866b230a4a495dcde8db04ac4f4671.png","¥100元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/333/2bc/3332bc33ba8ec28dfdb0021cd8134638.png","¥120元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d93/788/d93788fcdf4ce81bce11ec2143897d24.png","¥130元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/345/eb6/345eb60d1673e23f74696a6c8fa63d10.png","¥150元")   
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/359/6f6/3596f6f20f97178c41ca21d38077442e.png","¥170元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/1d6/84f/1d684fa11575457c6e4d991d3e365e46.png","¥220元")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/76e/67f/76e67f419db8fa8127a2e62335a36aba.png","¥260元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e24/802/e2480214b0edaa5578e543d07ad3cb98.png","¥650元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/cd7/2f8/cd72f88eb552cd485da7c95ba49d143b.png","¥850元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/74b/3f8/74b3f801c84ba385a9e378dcfbec05bd.png","¥1000元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/53e/bba/53ebba4b3b131c2d3a4ca1804190a680.png","¥1500元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ece/b17/eceb17ff573bfdf88c5be5613cb54efb.png","¥1330") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/3cc/8b0/3cc8b00412419ac29ff81b512b43e047.png","2") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/880/492/8804928ddab531c0b37e93ea7f166be1.png","4") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/a60/32f/a6032fdeb6bb5e90b2568bc942838b5a.png","5") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d04/dab/d04dabc2491d2fb911e65f4b14b3007e.png","10")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4e9/129/4e9129ca22c7cb87a00114718215cb22.png","16") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ff8/926/ff8926eedb22a35de01c15bcefac0f42.png","18")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/657/bd6/657bd60d1726ca788550516b7507a728.png","20")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/69c/c15/69cc15d32f64a7b3deb8619903575831.png","25")  
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f72/600/f72600c7eb96fa982c691a269ab0ce03.png","50") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/af5/b59/af5b59545dfbb6a41cab70a0be4b62aa.png","中") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9a2/b0e/9a2b0e6cab75c13f787f8e9a684698b9.png","¥200元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/285/7ef/2857ef1d14642e43d5c33daad7f475ef.png","¥23元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/73b/40f/73b40f9f787ddd7b8e0fcafb5ce90d6f.png","¥230元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ed8/b59/ed8b590d5f194f3f94e142e680666fce.png","¥30元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/52c/e72/52ce72526bb60b64a2dce268f6356b27.png","¥300元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/fb7/789/fb778986168a3a9b28e893e0a640156b.png","¥2元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/282/e72/282e72788c9a44b90a1585a2d7ba7719.png","¥8元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/46e/87f/46e87f55dd6184e91887cef461d61883.png","¥80元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ddb/fd7/ddbfd71a484540169adbae23e5db1739.png","¥12元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/811/965/811965460f49e843d0e30afbc34a82c7.png","¥33元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/8d8/c1c/8d8c1c1e7dd316b460c6bf3e67f1d53f.png","¥330元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5e7/59d/5e759d783289abd6f99192f59e63f6df.png","¥55元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/72a/37e/72a37e90de7281aacd033b30da3841c5.png","¥550元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/763/a41/763a416943457d4a435c278ec0c903eb.png","¥40元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/678/7ef/6787ef0f52ffc00348b5bd8a4e83c7d0.png","¥400元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/cf3/fd4/cf3fd440192debb9b7b5a6cff09ef6b6.png","¥60元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9ef/090/9ef09082627a6ab78d7222ed97f7d700.png","¥600元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/2cb/3b0/2cb3b0e21c114d3bc6b65d0344fd0223.png","¥4元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f5e/735/f5e73567dd93d13e6f5447dee77cb7d0.png","¥38元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/623/b6a/623b6a55c2a08bd8e9c65dfae4b37ff4.png","¥18元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4b8/265/4b82653d4bdf806d1b19e267397bb969.png","¥180元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e6a/70a/e6a70acb2165e551d00bf4b5754f9ced.png","¥25元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/024/b09/024b091068eef52a4037c10baf764fe8.png","¥250元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d2f/01e/d2f01ec2baaaa53ed8cf56577d938bd2.png","¥35元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ed5/8b1/ed58b14924ee809ce74335485162c70c.png","¥350元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/acd/527/acd5278149f4e7b7b8f5fbc6fce7b5d7.png","¥7元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/356/c9d/356c9daeac62d3a35bcb6875d18985a6.png","¥70元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/a97/e5b/a97e5baa657f558153a1108aab415249.png","¥11元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/dee/b58/deeb5847a8a7e00210c0656c994a6d89.png","¥110元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/272/24f/27224feae3f5838095bb774b2190b9c3.png","¥32元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4ce/84a/4ce84adafb84b18414147cabe14859df.png","¥320元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/0f1/697/0f16978c83b1222d61bb0c8a56ea09aa.png","¥9元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/724/f0f/724f0f5fa0dbcc4871529e6b90479093.png","¥90元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/db8/0fe/db80fe44b2ac2e94293fde4d4f4eeade.png","¥3元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/3b9/fe5/3b9fe5a4f1b8b4ed32b0514c124587f9.png","¥1元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e7e/1f9/e7e1f9f84b7524675af3f1b82e152df9.png","¥190元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/e20/fec/e20fec84697391c849d48e17f49f79a1.png","¥4.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f84/930/f849303eb846e69b42484c6aca969e4a.png","¥45元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/dd3/d9e/dd3d9e2b11bd0fb47795b01ad5e67d51.png","29mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5d7/1b3/5d71b3e25a0d2e4d2e3b3eff105590ae.png","¥16元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/102/3c4/1023c41d4d6e7115a086eb9895ab0ecb.png","¥160元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/3c2/5cd/3c25cd93fe253aa8492eb620e66592a2.png","94mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/3ce/847/3ce84753297763e850e96c512b3a5f47.png","23mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/f97/fb6/f97fb67bd7e5934a6487216bf8735bf9.png","22mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/2d5/bb8/2d5bb8c0db404d1bd8e3a12831b34aea.png","¥6元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/dc7/6e6/dc76e640ed0cb820e52f5a4cbe73330e.png","¥2.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/bba/4fc/bba4fc3dda247cab309accb8b650281e.png","19mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5b6/cb7/5b6cb7766521f54e2dd2f5489e26435a.png","¥15元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/225/186/22518639cabba8a936f4b91162ba3335.png","¥42元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d0e/8ec/d0e8ec24553db7d9f6743cb518cceb1e.png","¥420元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/b49/39c/b4939c8b08233ea3c030ac040635e28e.png","27mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/b03/60b/b0360bd0f275ef716631d70623d453b6.png","¥500元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/386/f5e/386f5e2fbb52a9de1b72360a316c5a1e.png","¥14元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/c5c/37a/c5c37a8d6bc3f1cf2f9f1cbade67ee18.png","¥140元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/8f2/0c4/8f20c4bea727b721b0673a9381a41ac3.png","¥800元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/602/f67/602f673a6a176a64d4d4f7fd5d65102e.png","100mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/590/e8a/590e8aa07050c28f44718efe9a1ba1d0.png","11.41mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/69a/547/69a5479d599f0709d3c8cc51dcf063c9.png","35mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/751/0fc/7510fceb6b7bb9969cc3223f8ae61fdc.png","28环")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/160/2ee/1602ee1fd5420e74fa0d5e9cd9f24c36.png","¥450元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4e3/3c4/4e33c460dc60ef573a2761995c9ed3cd.png","77332691")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d4e/d44/d4ed44cbb9900705d5ebce86d7594b56.png","34mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9ec/fe9/9ecfe98b98f93a401a6784a8e27de435.png","¥36元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/709/bf1/709bf1a022fc4ac96ae614908d97d4ef.png","¥360元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9e6/2c2/9e62c204af0c21fe8a78f210552f15bf.png","¥19元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/7f1/75e/7f175e0eb55a9bc31175852d6f99aa74.png","¥6.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/038/e3e/038e3edb7db0e83759ee42ba60dbfa21.png","¥13.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/fb4/691/fb469100074fbc4acd61ca47d029245b.png","¥135元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/26f/964/26f9644ad1e1d37e83415b6c97ac16c3.png","¥5.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/528/f88/528f881e1576897d2ac9d55cc33a3ae6.png","¥21元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/529/01a/52901a5daf26c2b2300520c0365e9066.png","¥210元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/491/880/49188074ef57ae2f5c98cdd560f3cd03.png","40")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/069/ba0/069ba0a0a94055070a84b40921a4ac33.png","¥530元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/0a6/435/0a6435c803c4d959f33f47e1cd973b53.png","¥380元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d8b/2f4/d8b2f4564ab0e3981aa6c6ce0505258f.png","¥7.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/767/b74/767b74ea682a558c0ed9c05ca5805362.png","¥75元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/47b/d2e/47bd2e3f822a21411cdd4801a7805d81.png","97mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/805/6fb/8056fb075c8af88c126ab857bd6031da.png","17mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5aa/445/5aa4450647e891145c989782b3a87dde.png","61600157")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/a18/256/a1825638aec7b9d3fd40f82433688590.png","46089953")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/03d/5d5/03d5d5c69acda4bab97666961f4a65fb.png","¥3.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/7de/60a/7de60ac9c7a03f7f066de36f843cf6cd.png","¥85元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ece/73d/ece73d16839ee3d97d776107d7b4d26b.png","¥47元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/338/884/338884896d73287e7d371d53fe41355a.png","¥470元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/72b/a60/72ba6030c0cab24504a74db6e699ddf0.png","¥43元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ea3/128/ea3128f80626eb5e5909fbc596e1bf45.png","¥700元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9c3/4a8/9c34a8e263481cefadac2946a2d68c86.png","32mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/3ee/087/3ee087a2668f89c474310ff310a2eba0.png","¥28元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/8e1/183/8e1183157093190b0d2cffd124aed172.png","¥280元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ca9/4eb/ca94eb118bf6f0af81bbce862aa7a463.png","92mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/c7b/dc8/c7bdc815775e18fef7e2c7635ef17f02.png","70mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/9aa/227/9aa227f182c49a0a2b4241a7b1b3825e.png","21mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/392/491/3924918689f3554b46450be583e60455.png","74mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/eeb/a16/eeba168812e5891ebf3fda0ef67b898a.png","¥24元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/389/935/3899354e2e5efbca06d9ada5a0d90951.png","¥240元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/48b/759/48b7590c5dcfb74a2c5b86ecfb77c967.png","50219711")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/0b2/be6/0b2be6e86736cfbf62421c93a64b6a47.png","15mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/879/755/8797551aa3e37562f95eb246d54cf9e5.png","¥750元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/064/178/0641780f24f6f0bd7f3fe5e2989d7b22.png","98mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/821/c98/821c9881adf13cd12456aa20e07e53ee.png","120mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/025/96a/02596a70e7151bb44cd782e1f20c207c.png","58mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/939/e82/939e8242298945e2fd85360c61da2600.png","¥990元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/76f/4ec/76f4ec10e3df582a6a2ced549dff780b.png","¥66元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/624/16a/62416aa1354bcefa1494b71e34b7cf57.png","¥660元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/779/932/77993235dc45a59d70a0361a6c94ec6f.png","80mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/606/8f4/6068f4ba1a2472efaa8abf0caa9be32d.png","¥9.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/088/67c/08867c70ba54fd804812216c9f96445c.png","¥95元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/c96/46a/c9646a5ef33e6dcde8e66005af27934a.png","¥900元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/348/197/3481973cb3b4a69e3e8ce31ef6f5fb09.png","¥2.3元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/b08/83c/b0883cdb65f0bfda921f7c18668a9a10.png","48741699")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ca5/346/ca53462428f23fb99184e7150cc0758d.png","87248883")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/ef4/f69/ef4f6941e1644c2d8586686241e9c41a.png","¥950元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/23a/a3e/23aa3e5dcf0b298029485dfb91de8ca9.png","49400397")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/324/48c/32448c793ec6ca6b56261a384caf2a2b.png","50219124")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/dc7/6d6/dc76d666fd5e849baf052af91883708a.png","14mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/03d/5d5/03d5d5c69acda4bab97666961f4a65fb.png","¥3.5元") 
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/359/80a/35980ad7adbce77641b38b37e64d0a5f.png","24.2mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d2a/ed8/d2aed8e744e992fa67f1824ec10daab5.png","1lmm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4cc/af0/4ccaf060c1928529f653690c55b473ea.png","34.5mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4b6/608/4b66086c0e860535c0b0cdf9d9c83294.png","130mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/7ac/dd7/7acdd71631ccf632e49bf62e24920647.png","47mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/bcd/116/bcd116a488d9c1fedc0d838c13ae242d.png","160mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/239/5d6/2395d6b70b82faed038010a9176bef36.png","17.5mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/02e/14b/02e14b8627050d4715d101076e6fde23.png","55mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/05d/3a7/05d3a7b934c9014c489b29404527f375.png","44环")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/25d/639/25d639483b2fef2a350936ed5ca70609.png","110mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/7c4/aa2/7c4aa23ea95bff2e7c8538f787a39cf1.png","143mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/6ef/ebb/6efebbcd318950458376f3df0d0cb096.png","45mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/938/462/9384622d0c62c67753394b2feafe7184.png","36环")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/125/61d/12561d143713db24c716cc3e583fbd3f.png","¥98元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/32a/2a3/32a2a3a43090fcaf184dadf97a98ee41.png","¥980元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/482/9b5/4829b5a5a1d3b1b8ac94e93d3f184a15.png","¥480元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/4e3/fac/4e3fac2dc7a218f74707225d7da883c4.png","20mg")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/d96/604/d9660495d9259d60f247b96b76544111.png","10.5mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/06f/d18/06fd18747456de94ac52cb4fa2c508ea.png","33mm")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/936/a2c/936a2c279924283a8d2daa42cc6ff379.png","¥8.5元")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/5b0/77d/5b077dc7ec8f3804d46989badba5d111.png","95509228")
    urlstr=urlstr.replace("https://res.yanyue.cn/thumb/genpic/760/b48/760b48b500f067049a314c415d2ac00b.png","02886925")



    if "http" not in urlstr:
        return urlstr.strip()

  
   
 
    try:
        # response = requests.get(img_url)
        # print(str(img_url))
        payload = {}
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':    'gzip, deflate, br',
        'Accept-Language':    'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", urlstr, headers=headers, data=payload)
        # response = requests.get(img_url)
        # print(response.status_code)
        # print(response.text)

        # 检查响应状态和内容类型
        if response.status_code != 200 or 'image' not in response.headers['Content-Type']:
            return f"Invalid image URL: {img_url}"
        
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        if text.strip()=="":
            text = pytesseract.image_to_string(image)
            if text.strip()=="":
                return "OCRERR:"+img_url
        if '¥' in text.strip() and str(text.strip()).endswith('70'):
            if urlstr not in imglist:
                imglist.append(urlstr)
                with open(code_file, "a", encoding="utf-8", newline="") as codeFile:
                    codeFile.write('urlstr=urlstr.replace("%s","%s")\n'%(urlstr,convert_currency(str(text.strip()).replace(' ',''))))
            print('urlstr=urlstr.replace("%s","%s") '%(urlstr,convert_currency(str(text.strip()).replace(' ',''))))
            return  convert_currency(str(text.strip()).replace(' ',''))
        if (urlstr not in imglist) and len(text.strip())<10:
            imglist.append(urlstr)
            with open(code_file, "a", encoding="utf-8", newline="") as codeFile:
                codeFile.write('urlstr=urlstr.replace("%s","%s")\n'%(urlstr,text.strip()))
        return text.strip()
    except Exception as e:
        print("OCRERR[%s]:%s"%(img_url,str(e)))
        return str(img_url)

def get_price_from_id(idstr):
    url = "https://www.yanyue.cn/product/ajax_areaprice"
    payload = 'productid=%s'%idstr
    headers = {
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return (response.text)



def extract_data_from_url(url):
    # response = requests.get(url)
    payload = {}
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':    'gzip, deflate, br',
    'Accept-Language':    'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if "你这不行呀，太快了，下次请久一点"in response.text:
        time.sleep(1)
        return extract_data_from_url(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # 获取edition_wrap中的第一个h3标签的内容
    edition_wrap = soup.find("div", class_="edition_wrap")
    h3_content = edition_wrap.find("h3").text if edition_wrap else ""
    if not( h3_content==None or h3_content==""):
        print("loading[%s]:%s          remain[%smin--[%s]]"%((url,h3_content,str(int((endnum-i)/30)),str(endnum-i))))

    # 从ul类为ul_1中提取li标签的键值对
    ul_1 = soup.find("ul", class_="ul_1")    
    if ul_1==None:
        print("ERR[%s] Code:[%s]"%(url,response.status_code))
        print(response.text) 
    info_titles = ul_1.find_all("li", class_="info_title")
    info_contents = ul_1.find_all("li", class_="info_content")

    data = {'名称': h3_content}
    div_t1 = soup.find("div", id="t1")
    if div_t1==None:
        print("ERR:%sTYPE:%s"%(h3_content,url))
        div_place = soup.find("div", class_="place")
        if div_place==None:
            return data
        else:
            links = div_place.find_all("a")
            extracted_info = [{"text": link.text} for link in links]
            data['香烟品类']=extracted_info[0]['text']
            data['烟弹设备']=extracted_info[1]['text']
            data['产品品牌']=extracted_info[2]['text']
    else:
        links = div_t1.find_all("a")
        extracted_info = [{"text": link.text} for link in links]
        data['香烟品类']=extracted_info[0]['text']
        data['香烟地域']=extracted_info[1]['text']
        data['香烟品牌']=extracted_info[2]['text']
    for title, content in zip(info_titles, info_contents):
        img_tag = content.find("img")
        if img_tag and img_tag.has_attr("src"):
            value = ocr_image_from_url(img_tag["src"])
        else:
            value = content.text.strip()
        data[title.text.strip()] = value

    return data

def save_to_json(data_list, json_path):
    with open(json_path, "w", encoding="utf-8") as jsonfile:
        json.dump(data_list, jsonfile, ensure_ascii=False, indent=4)

def convert_currency(input_str):
    # 使用正则表达式匹配并确保字符串末尾精确匹配70
    match = re.search(r'^¥(.+)70$', input_str)
    if match:
        value = match.group(1)
        return f'¥{value}元'
    else:
        return input_str


def save_to_csv(data, csv_path):
    with open(csv_path, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


if __name__ == "__main__":
    code_file='code2add'
    json_path = "output.json"
    csv_path = "data.csv"
    all_data = []
    imglist=[]
    headers=['ID', '香烟品类', '香烟地域', '香烟品牌', '名称', '品牌:', '类型:', '焦油:','焦油高低:', '烟碱:', '一氧化碳:', '长度:', '过滤嘴长:', '周长:', '包装形式:', '主颜色:', '副颜色:', '条装盒数:', '每盒数量:', '小盒价格:', '条装价格:', '小盒条码:', '条装条码:']
    with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
    endnum=5300
    for i in range(1, endnum):  
        try:
            newheader=False
            url = f"https://www.yanyue.cn/product/{i}"
            data = extract_data_from_url(url)
            data['ID']=str(i)
            all_data.append(data)
            row_data=[]
            for key in data:    
                if key not in headers:
                    headers.append(key)
                    print("NewKey:[%s]"%str(key))
                    print("Header:[%s]"%headers)
            for rkey in headers:
                if rkey in data:
                    row_data.append(data[rkey])
                else:
                    row_data.append("")
            if data['名称']==None or data['名称']=="":
                continue
            save_to_csv(row_data, csv_path) 
            time.sleep(2)
        except Exception as e:
            print("ERR[%s]:%s"%(str(i),str(e)))

    save_to_json(all_data, json_path)
 