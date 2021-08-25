from Api.at import ConstantName as CN
from testscript import testconfig as GC

# Default minio credentials for Tanker & System API
testsystemreq = {
'minioaddr':CN.SAPIMINIOIPADDRESS,
'minioid': 'steve',
'miniopass': 'steve123',
'bucket': 'broadcast',
'gatewaykey':'729cfbd5-5934-4850-961b-e5ddf1a268ae' # change accordingly
}

Init = { 
        'EXCELSAVEFILENAME': r'logo_malaysia_sipsi_{}_v{}'.format(GC.SW['PROJECT'],GC.SW['VERSION']),
        'SYSTEMREQ': testsystemreq, 
        'VERSION': GC.SW['VERSION'],
        'PROJECT': GC.SW['PROJECT'],
        'REGION': GC.SW['REGION'],
        'COUNTRY': GC.DUT['COUNTRY'],
        'SETUPPIN':[8,8,8,8] # change accordingly
        }

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 1:MYSServiceInstallation
# ----------------------------------------------------------------------------------------
MYSServiceInstallation = {'IMAGENAME1': r'LOGO_MYS_TC1_VCN_BANNER208.png', 'IMAGENAME2': r'LOGO_MYS_TC1_VCN_BANNER209.png',
                        'IMAGENAME3': r'LOGO_MYS_TC1_VCN_BANNER210.png', 'IMAGENAME4': r'LOGO_MYS_TC1_VCN_BANNER211.png',
                        'IMAGENAME5': r'LOGO_MYS_TC1_VCN_BANNER212.png', 'IMAGENAME6': r'LOGO_MYS_TC1_VCN_BANNER213.png',
                        'IMAGENAME7': r'LOGO_MYS_TC1_VCN_Open_EPG.png', 'IMAGENAME8': r'LOGO_MYS_TC1_VCN_Check_Chl_EPG.png',
                        
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE1_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE1_REF_VCN_image6.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE1_REF_VCN_image11.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE1_REF_VCN_image16.json',
                        'CONFIGJSON5': r'LOGO_MYS_TESTCASE1_REF_VCN_image21.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE1_REF_VCN_image26.json',
                        'CONFIGJSON7': r'LOGO_MYS_TESTCASE1_REF_VCN_image31.json','CONFIGJSON8': r'LOGO_MYS_TESTCASE1_REF_VCN_image32.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 2:MYSEventInformation
# ----------------------------------------------------------------------------------------
MYSEventInformation = {'IMAGENAME1': r'LOGO_MYS_TC2_VCN_208_Display_Banner.png', 'IMAGENAME2': r'LOGO_MYS_TC2_VCN_208_Display_EPG.png',
                        'IMAGENAME3': r'LOGO_MYS_TC2_VCN_208_Display_EPG_Desc.png', 'IMAGENAME4': r'LOGO_MYS_TC2_VCN_208_Next_EPG.png',
                        'IMAGENAME5': r'LOGO_MYS_TC2_VCN_208_Next_EI.png', 'IMAGENAME6': r'LOGO_MYS_TC2_VCN_208_Next_Banner.png',
                        'IMAGENAME7': r'LOGO_MYS_TC2_VCN_209_Display_Banner.png', 'IMAGENAME8': r'LOGO_MYS_TC2_VCN_209_Display_EPG.png',
                        'IMAGENAME9': r'LOGO_MYS_TC2_VCN_209_EPG_Desc.png',
                              
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE2_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE2_REF_VCN_image6.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE2_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE2_REF_VCN_image8.json',
                        'CONFIGJSON5': r'LOGO_MYS_TESTCASE2_REF_VCN_image9.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE2_REF_VCN_image10.json',
                        'CONFIGJSON7': r'LOGO_MYS_TESTCASE2_REF_VCN_image15.json','CONFIGJSON8': r'LOGO_MYS_TESTCASE2_REF_VCN_image20.json',
                        'CONFIGJSON9': r'LOGO_MYS_TESTCASE2_REF_VCN_image21.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 3:MYSCodecInformation
# ----------------------------------------------------------------------------------------
MYSCodecInformation = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 4:MYSCodecInformationAudioAlternate
# ----------------------------------------------------------------------------------------
MYSCodecInformationAudioAlternate = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 5:MYSAudioSubsLanguage
# ----------------------------------------------------------------------------------------
MYSAudioSubsLanguage = { 'IMAGENAME1': r'LOGO_MYS_TC5_VCN_OpenAudioMenu.png', 'IMAGENAME2': r'LOGO_MYS_TC5_VCN_AllAudioAvailable.png',
                         'IMAGENAME3': r'LOGO_MYS_TC5_VCN_OpenSubMenu.png', 'IMAGENAME4': r'LOGO_MYS_TC5_VCN_OpenAudioLCN209.png',
                                        
                         'CONFIGJSON1': r'LOGO_MYS_TESTCASE5_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE5_REF_VCN_image2.json',
                         'CONFIGJSON3': r'LOGO_MYS_TESTCASE5_REF_VCN_image3.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE5_REF_VCN_image4.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 6:MYSLCNV1Descriptors
# ----------------------------------------------------------------------------------------
MYSLCNV1Descriptors = {'IMAGENAME1': r'LOGO_MYS_TC6_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC6_VCN_EPG_Chl_Check.png',
            
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE6_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE6_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 7:MYSLCNV2Descriptors
# ----------------------------------------------------------------------------------------
MYSLCNV2Descriptors = {'IMAGENAME1': r'LOGO_MYS_TC7_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC7_VCN_EPG_Chl_Check.png',
            
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE7_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE7_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 8:MYSForeignService
# ----------------------------------------------------------------------------------------
MYSForeignService = {   'IMAGENAME1': r'LOGO_MYS_TC8_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC8_VCN_EPG_Chl_Check.png',
                        'IMAGENAME3': r'LOGO_MYS_TC8_VCN_EPG_Down.png', 
                        
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE8_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE8_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE8_REF_VCN_image3.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 9:MYSNoLCNDescriptor
# ----------------------------------------------------------------------------------------
MYSNoLCNDescriptor = {  'IMAGENAME1': r'LOGO_MYS_TC9_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC9_VCN_EPG_Chl_Check.png',
                        'IMAGENAME3': r'LOGO_MYS_TC9_VCN_EPG_Down.png', 
            
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE9_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE9_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE9_REF_VCN_image3.json',}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 10:MYSRegionalBroadcastManagement
# ----------------------------------------------------------------------------------------
MYSRegionalBroadcastManagement = {'IMAGENAME1': r'LOGO_MYS_TC10_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC10_VCN_EPG_CHLCheck.png',
                                'IMAGENAME3': r'LOGO_MYS_TC10_VCN_LCN1_OpenEPG.png', 'IMAGENAME4': r'LOGO_MYS_TC10_VCN_LCN1_EPG_CHLCheck.png',
                                
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE10_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE10_REF_VCN_image2.json',
                                'CONFIGJSON3': r'LOGO_MYS_TESTCASE10_REF_VCN_image3.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE10_REF_VCN_image4.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 11:MYSServiceAddDelLCNCheck
# ----------------------------------------------------------------------------------------
MYSServiceAddDelLCNCheck = {'IMAGENAME1': r'LOGO_MYS_TC11_VCN_OpenEPG.png',
            
                            'CONFIGJSON1': r'LOGO_MYS_TESTCASE11_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 12:MYSServiceAddDelAddTS
# ----------------------------------------------------------------------------------------
MYSServiceAddDelAddTS = {'IMAGENAME1': r'LOGO_MYS_TC12_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC12_VCN_OpenEPG_AfterDelay.png',
                        'IMAGENAME3': r'LOGO_MYS_TC12_VCN_EPG_Chl_Check.png',
                        
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE12_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE12_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE12_REF_VCN_image3.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 13:MYSServiceAddDelLCNCheckAfterDel
# ----------------------------------------------------------------------------------------
MYSServiceAddDelLCNCheckAfterDel = { 'IMAGENAME1': r'LOGO_MYS_TC13_VCN_OpenEPG.png',
            
                                     'CONFIGJSON1': r'LOGO_MYS_TESTCASE13_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 14:MYSServiceAddDelTSDeletion
# ----------------------------------------------------------------------------------------
MYSServiceAddDelTSDeletion = {'IMAGENAME1': r'LOGO_MYS_TC14_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC14_VCN_OpenEPG_After_Deletion.png',
            
                              'CONFIGJSON1': r'LOGO_MYS_TESTCASE14_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE14_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 15:MYSClashLCNResolutionTSMux
# ----------------------------------------------------------------------------------------
MYSClashLCNResolutionTSMux = {'IMAGENAME1': r'LOGO_MYS_TC15_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC15_VCN_EPG_Chl_Check.png',
            
                              'CONFIGJSON1': r'LOGO_MYS_TESTCASE15_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE15_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 16:MYSClashLCNResolutionASU
# ----------------------------------------------------------------------------------------
MYSClashLCNResolutionASU = {    'IMAGENAME1': r'LOGO_MYS_TC16_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC16_VCN_EPG_Chl_Check.png',
                                'IMAGENAME3': r'LOGO_MYS_TC16_VCN_EPG_Chl_Check_Down.png',
                                
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE16_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE16_REF_VCN_image2.json',
                                'CONFIGJSON3': r'LOGO_MYS_TESTCASE16_REF_VCN_image3.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 17:MYSClashLCNResolutionASUDiffMhz
# ----------------------------------------------------------------------------------------
MYSClashLCNResolutionASUDiffMhz = { 'IMAGENAME1': r'LOGO_MYS_TC17_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC17_VCN_EPG_Chl_Check.png',
            
                                    'CONFIGJSON1': r'LOGO_MYS_TESTCASE17_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE17_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 18:MYSMultiplexAddDelStaticAdd
# ----------------------------------------------------------------------------------------
MYSMultiplexAddDelStaticAdd = {'IMAGENAME1': r'LOGO_MYS_TC18_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC18_VCN_EPG_Chl_Check.png',
            
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE18_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE18_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 19:MYSMultiplexAddDelSimultaneous
# ----------------------------------------------------------------------------------------
MYSMultiplexAddDelSimultaneous = {'IMAGENAME1': r'LOGO_MYS_TC19_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC19_VCN_EPG_Chl_Check.png',
            
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE19_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE19_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 20:MYSMultiplexAddDel474Mhz
# ----------------------------------------------------------------------------------------
MYSMultiplexAddDel474Mhz = {'IMAGENAME1': r'LOGO_MYS_TC20_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC20_VCN_EPG_Chl_Check.png',
            
                            'CONFIGJSON1': r'LOGO_MYS_TESTCASE20_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE20_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 21:MYSMultiplexAddDel858Mhz
# ----------------------------------------------------------------------------------------
MYSMultiplexAddDel858Mhz = { 'IMAGENAME1': r'LOGO_MYS_TC21_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_MYS_TC21_VCN_EPG_Chl_Check.png',
            
                             'CONFIGJSON1': r'LOGO_MYS_TESTCASE21_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE21_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 22:MYSServiceEventUpdateLCN120
# ----------------------------------------------------------------------------------------
MYSServiceEventUpdateLCN120 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 23:MYSServiceEventUpdateLCN131
# ----------------------------------------------------------------------------------------
MYSServiceEventUpdateLCN131 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 24:MYSServiceEventUpdateLCN555
# ----------------------------------------------------------------------------------------
MYSServiceEventUpdateLCN555 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 25:MYSCharEventPF
# ----------------------------------------------------------------------------------------
MYSCharEventPF = { 'IMAGENAME1': r'LOGO_MYS_TC25_VCN_CHARACTER_EVENT_TS_OPEN_EPG.png','IMAGENAME2': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME3': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME4': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_EI.png',
                        'IMAGENAME5': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EVENT.png', 'IMAGENAME6': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI.png',
                        'IMAGENAME7': r'LOGO_MYS_TC25_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI_BANNER.png', 'IMAGENAME8': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME9': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME10': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_EPG_INFO.png',
                        'IMAGENAME11': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG.png', 'IMAGENAME12': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG_INFO.png',
                        'IMAGENAME13': r'LOGO_MYS_TC25_VCN_LCN101_CHARACTER_DISPLAY_NEXT_BANNER.png', 'IMAGENAME14': r'LOGO_MYS_TC25_VCN_LCN102_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME15': r'LOGO_MYS_TC25_VCN_LCN102_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME16': r'LOGO_MYS_TC25_VCN_LCN102_CHARACTER_DISPLAY_EPG_INFO.png',
                              
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE25_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE25_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE25_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE25_REF_VCN_image8.json',
                        'CONFIGJSON5': r'LOGO_MYS_TESTCASE25_REF_VCN_image9.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE25_REF_VCN_image10.json',
                        'CONFIGJSON7': r'LOGO_MYS_TESTCASE25_REF_VCN_image11.json','CONFIGJSON8': r'LOGO_MYS_TESTCASE25_REF_VCN_image16.json',
                        'CONFIGJSON9': r'LOGO_MYS_TESTCASE25_REF_VCN_image21.json','CONFIGJSON10': r'LOGO_MYS_TESTCASE25_REF_VCN_image22.json',
                        'CONFIGJSON11': r'LOGO_MYS_TESTCASE25_REF_VCN_image23.json','CONFIGJSON12': r'LOGO_MYS_TESTCASE25_REF_VCN_image24.json',
                        'CONFIGJSON13': r'LOGO_MYS_TESTCASE25_REF_VCN_image25.json','CONFIGJSON14': r'LOGO_MYS_TESTCASE25_REF_VCN_image30.json',
                        'CONFIGJSON15': r'LOGO_MYS_TESTCASE25_REF_VCN_image35.json','CONFIGJSON16': r'LOGO_MYS_TESTCASE25_REF_VCN_image36.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 26:MYSCharEventSchedule
# ----------------------------------------------------------------------------------------
MYSCharEventSchedule = {        'IMAGENAME1': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_EPG.png','IMAGENAME2': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_3_EPG.png',
                                'IMAGENAME3': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_3_EPG_EI.png', 'IMAGENAME4': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_4_EPG.png',
                                'IMAGENAME5': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_4_EPG_EI.png', 'IMAGENAME6': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_5_EPG.png',
                                'IMAGENAME7': r'LOGO_MYS_TC26_VCN_EVENTSCHEDULE_5_EPG_EI.png', 
                                
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE26_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE26_REF_VCN_image2.json',
                                'CONFIGJSON3': r'LOGO_MYS_TESTCASE26_REF_VCN_image3.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE26_REF_VCN_image4.json',
                                'CONFIGJSON5': r'LOGO_MYS_TESTCASE26_REF_VCN_image5.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE26_REF_VCN_image6.json',
                                'CONFIGJSON7': r'LOGO_MYS_TESTCASE26_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 27:MYSCharEventPFHuffman
# ----------------------------------------------------------------------------------------
MYSCharEventPFHuffman = {'IMAGENAME1': r'LOGO_MYS_TC27_VCN_CHARACTER_EVENT_TS_OPEN_EPG.png','IMAGENAME2': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME3': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME4': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_EI.png',
                        'IMAGENAME5': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EVENT.png', 'IMAGENAME6': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI.png',
                        'IMAGENAME7': r'LOGO_MYS_TC27_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI_BANNER.png', 'IMAGENAME8': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME9': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME10': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_EPG_INFO.png',
                        'IMAGENAME11': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG.png', 'IMAGENAME12': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG_INFO.png',
                        'IMAGENAME13': r'LOGO_MYS_TC27_VCN_LCN101_CHARACTER_DISPLAY_NEXT_BANNER.png', 'IMAGENAME14': r'LOGO_MYS_TC27_VCN_LCN102_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME15': r'LOGO_MYS_TC27_VCN_LCN102_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME16': r'LOGO_MYS_TC27_VCN_LCN102_CHARACTER_DISPLAY_EPG_INFO.png',
                              
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE27_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE27_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE27_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE27_REF_VCN_image8.json',
                        'CONFIGJSON5': r'LOGO_MYS_TESTCASE27_REF_VCN_image9.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE27_REF_VCN_image10.json',
                        'CONFIGJSON7': r'LOGO_MYS_TESTCASE27_REF_VCN_image11.json','CONFIGJSON8': r'LOGO_MYS_TESTCASE27_REF_VCN_image16.json',
                        'CONFIGJSON9': r'LOGO_MYS_TESTCASE27_REF_VCN_image21.json','CONFIGJSON10': r'LOGO_MYS_TESTCASE27_REF_VCN_image22.json',
                        'CONFIGJSON11': r'LOGO_MYS_TESTCASE27_REF_VCN_image23.json','CONFIGJSON12': r'LOGO_MYS_TESTCASE27_REF_VCN_image24.json',
                        'CONFIGJSON13': r'LOGO_MYS_TESTCASE27_REF_VCN_image25.json','CONFIGJSON14': r'LOGO_MYS_TESTCASE27_REF_VCN_image30.json',
                        'CONFIGJSON15': r'LOGO_MYS_TESTCASE27_REF_VCN_image35.json','CONFIGJSON16': r'LOGO_MYS_TESTCASE27_REF_VCN_image36.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 28:MYSCharEventScheduleHuffman
# ----------------------------------------------------------------------------------------
MYSCharEventScheduleHuffman = {'IMAGENAME1': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_EPG.png','IMAGENAME2': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_3_EPG.png',
                                'IMAGENAME3': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_3_EPG_EI.png', 'IMAGENAME4': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_4_EPG.png',
                                'IMAGENAME5': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_4_EPG_EI.png', 'IMAGENAME6': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_5_EPG.png',
                                'IMAGENAME7': r'LOGO_MYS_TC28_VCN_EVENTSCHEDULE_5_EPG_EI.png', 
                                
                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE28_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE28_REF_VCN_image2.json',
                                'CONFIGJSON3': r'LOGO_MYS_TESTCASE28_REF_VCN_image3.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE28_REF_VCN_image4.json',
                                'CONFIGJSON5': r'LOGO_MYS_TESTCASE28_REF_VCN_image5.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE28_REF_VCN_image6.json',
                                'CONFIGJSON7': r'LOGO_MYS_TESTCASE28_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 29:MYSHuffmanMalay
# ----------------------------------------------------------------------------------------
MYSHuffmanMalay = {     'IMAGENAME1': r'LOGO_MYS_TC29_VCN_Display_Banner.png', 'IMAGENAME2': r'LOGO_MYS_TESTCASE29_REF_VCN_EPG.png',
                        'IMAGENAME3': r'LOGO_MYS_TESTCASE29_REF_VCN_EPG_EI.png',
                                        
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE29_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE29_REF_VCN_image6.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE29_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 30:MYSHuffmanESC
# ----------------------------------------------------------------------------------------
MYSHuffmanESC = {'IMAGENAME1': r'LOGO_MYS_TESTCASE30_REF_VCN_Display_Banner.png', 'IMAGENAME2': r'LOGO_MYS_TESTCASE30_REF_VCN_Open_EPG.png',
                'IMAGENAME3': r'LOGO_MYS_TESTCASE30_REF_VCN_EventInformation.png', 'IMAGENAME4': r'LOGO_MYS_TESTCASE30_REF_VCN_Next_EPG.png',
                'IMAGENAME5': r'LOGO_MYS_TESTCASE30_REF_VCN_EI_Next.png', 'IMAGENAME6': r'LOGO_MYS_TESTCASE30_REF_VCN_Next_Banner.png',
                              
                'CONFIGJSON1': r'LOGO_MYS_TESTCASE30_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE30_REF_VCN_image6.json',
                'CONFIGJSON3': r'LOGO_MYS_TESTCASE30_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE30_REF_VCN_image8.json',
                'CONFIGJSON5': r'LOGO_MYS_TESTCASE30_REF_VCN_image9.json','CONFIGJSON6': r'LOGO_MYS_TESTCASE30_REF_VCN_image10.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 31:MYSNoTableDefinition
# ----------------------------------------------------------------------------------------
MYSNoTableDefinition = {        'IMAGENAME1': r'LOGO_MYS_TC31_VCN_BANNER.png','IMAGENAME2': r'LOGO_MYS_TC31_VCN_EPG.png',
                                'IMAGENAME3': r'LOGO_MYS_TC31_VCN_EI.png', 

                                'CONFIGJSON1': r'LOGO_MYS_TESTCASE31_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE31_REF_VCN_image6.json',
                                'CONFIGJSON3': r'LOGO_MYS_TESTCASE31_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 32:MYSAFDTest 
# ----------------------------------------------------------------------------------------
MYSAFDTest = {    'IMAGENAME1': r'LOGO_MYS_TC32_VCN_OpenEPG.png', 'IMAGENAME2': r'LOGO_MYS_TC32_VCN_LCN100_Display_Banner.png',
                        'IMAGENAME3': r'LOGO_MYS_TC32_VCN_LCN200_Display_Banner.png', 'IMAGENAME4': r'LOGO_MYS_TC32_VCN_LCN300_Display_Banner.png',
                                        
                        'CONFIGJSON1': r'LOGO_MYS_TESTCASE32_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_MYS_TESTCASE32_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_MYS_TESTCASE32_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_MYS_TESTCASE32_REF_VCN_image12.json'}
# ----------------------------------------------------------------------------------------