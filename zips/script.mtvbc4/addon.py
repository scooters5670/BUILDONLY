import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Channel 4 Links[/COLOR][/B]', [
    '[B][COLOR=green]      Channel 4 Link 1[/COLOR][/B]' ,
    '[B][COLOR=green]      Channel 4 Link 2[/COLOR][/B]' ,
    '[B][COLOR=green]      Channel 4 Link 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.livehub2%5cicon.png&mode=10&name=%5bCOLOR%20white%5dChannel%204%5b%2fCOLOR%5d&url=mpd%3a%2f%2fe77d2afa4363dad35c713745802d7bee.m3u8",return)')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.216.192:7071/routernew/Channel4/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DChannel+4%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F51044_ch41.jpg&description=Channel+4+Channel+4+Channel+4+Channel+4+Channel+4")')
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaakchenl-4%2FStrm%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+4+UK&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Ffootball.jpg&description=")')


menuoptions()