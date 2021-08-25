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
        'EXCELSAVEFILENAME': r'logo_uae_sipsi_{}_v{}'.format(GC.SW['PROJECT'],GC.SW['VERSION']),
        'SYSTEMREQ': testsystemreq, 
        'VERSION': GC.SW['VERSION'], 
        'PROJECT': GC.SW['PROJECT'],
        'REGION': GC.SW['REGION'], 
        'COUNTRY': GC.DUT['COUNTRY'],
        'SETUPPIN':[8,8,8,8] # change accordingly
        }

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 1:UAEDigitalTuningLCNCheck
# ----------------------------------------------------------------------------------------
UAEDigitalTuningLCNCheck = {    'IMAGENAME1': r'LOGO_UAE_TC1_VCN_BANNER_100.png', 'IMAGENAME2': r'LOGO_UAE_TC1_VCN_BANNER_101.png',
                                'IMAGENAME3': r'LOGO_UAE_TC1_VCN_BANNER_102.png', 'IMAGENAME4': r'LOGO_UAE_TC1_VCN_BANNER_103.png',
                                'IMAGENAME5': r'LOGO_UAE_TC1_VCN_BANNER_104.png', 'IMAGENAME6': r'LOGO_UAE_TC1_VCN_BANNER_105.png',
                                'IMAGENAME7': r'LOGO_UAE_TC1_VCN_BANNER_107.png',
                              
                                'CONFIGJSON1': r'LOGO_UAE_TESTCASE1_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE1_REF_VCN_image6.json',
                                'CONFIGJSON3': r'LOGO_UAE_TESTCASE1_REF_VCN_image11.json','CONFIGJSON4': r'LOGO_UAE_TESTCASE1_REF_VCN_image16.json',
                                'CONFIGJSON5': r'LOGO_UAE_TESTCASE1_REF_VCN_image21.json','CONFIGJSON6': r'LOGO_UAE_TESTCASE1_REF_VCN_image26.json',
                                'CONFIGJSON7': r'LOGO_UAE_TESTCASE1_REF_VCN_image31.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 2:UAEDigitalEventInformation
# ----------------------------------------------------------------------------------------
UAEDigitalEventInformation = {'IMAGENAME1': r'LOGO_UAE_TC2_VCN_DISPLAY_BANNER_100.png', 'IMAGENAME2': r'LOGO_UAE_TC2_VCN_DISPLAY_EPG_100.png',
                              'IMAGENAME3': r'LOGO_UAE_TC2_VCN_DISPLAY_EI_100.png', 'IMAGENAME4': r'LOGO_UAE_TC2_VCN_EPG_NEXT_EVENT.png',
                              'IMAGENAME5': r'LOGO_UAE_TC2_VCN_EPG_SELECT_NEXT_EVENT.png', 'IMAGENAME6': r'LOGO_UAE_TC2_VCN_BANNER_NEXT_BUTTON.png',
                              'IMAGENAME7': r'LOGO_UAE_TC2_VCN_DISPLAY_BANNER_101.png', 'IMAGENAME8': r'LOGO_UAE_TC2_VCN_DISPLAY_EPG_101.png',
                              'IMAGENAME9': r'LOGO_UAE_TC2_VCN_DISPLAY_EI_101.png', 'IMAGENAME10': r'LOGO_UAE_TC2_VCN_DISPLAY_BANNER_102.png',
                              'IMAGENAME11': r'LOGO_UAE_TC2_VCN_DISPLAY_EPG_102.png', 'IMAGENAME12': r'LOGO_UAE_TC2_VCN_DISPLAY_EI_102.png',
                              'IMAGENAME13': r'LOGO_UAE_TC2_VCN_DISPLAY_BANNER_103.png', 'IMAGENAME14': r'LOGO_UAE_TC2_VCN_DISPLAY_EPG_103.png',
                              'IMAGENAME15': r'LOGO_UAE_TC2_VCN_DISPLAY_EI_103.png', 'IMAGENAME16': r'LOGO_UAE_TC2_VCN_DISPLAY_BANNER_104.png',
                              'IMAGENAME17': r'LOGO_UAE_TC2_VCN_DISPLAY_EPG_104.png', 'IMAGENAME18': r'LOGO_UAE_TC2_VCN_DISPLAY_EI_104.png', 

                              'CONFIGJSON1': r'LOGO_UAE_TESTCASE2_REF_VCN_image1.json', 'CONFIGJSON2': r'LOGO_UAE_TESTCASE2_REF_VCN_image6.json',
                              'CONFIGJSON3': r'LOGO_UAE_TESTCASE2_REF_VCN_image7.json', 'CONFIGJSON4': r'LOGO_UAE_TESTCASE2_REF_VCN_image8.json',
                              'CONFIGJSON5': r'LOGO_UAE_TESTCASE2_REF_VCN_image9.json', 'CONFIGJSON6': r'LOGO_UAE_TESTCASE2_REF_VCN_image10.json',
                              'CONFIGJSON7': r'LOGO_UAE_TESTCASE2_REF_VCN_image15.json', 'CONFIGJSON8': r'LOGO_UAE_TESTCASE2_REF_VCN_image20.json',
                              'CONFIGJSON9': r'LOGO_UAE_TESTCASE2_REF_VCN_image21.json', 'CONFIGJSON10': r'LOGO_UAE_TESTCASE2_REF_VCN_image22.json',
                              'CONFIGJSON11': r'LOGO_UAE_TESTCASE2_REF_VCN_image27.json', 'CONFIGJSON12': r'LOGO_UAE_TESTCASE2_REF_VCN_image28.json',
                              'CONFIGJSON13': r'LOGO_UAE_TESTCASE2_REF_VCN_image29.json', 'CONFIGJSON14': r'LOGO_UAE_TESTCASE2_REF_VCN_image34.json',
                              'CONFIGJSON15': r'LOGO_UAE_TESTCASE2_REF_VCN_image35.json', 'CONFIGJSON16': r'LOGO_UAE_TESTCASE2_REF_VCN_image36.json',
                              'CONFIGJSON17': r'LOGO_UAE_TESTCASE2_REF_VCN_image41.json', 'CONFIGJSON18': r'LOGO_UAE_TESTCASE2_REF_VCN_image42.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 3:UAECodecInformation
# ----------------------------------------------------------------------------------------
UAECodecInformation = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 4:UAEAudSubtitle
# ----------------------------------------------------------------------------------------
UAEAudSubtitle = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 5:UAEParentalLock
# ----------------------------------------------------------------------------------------
UAEParentalLock = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 6:UAEBroadcastMixedAudio
# ----------------------------------------------------------------------------------------
UAEBroadcastMixedAudio = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 7:UAELCNV1Descriptors
# ----------------------------------------------------------------------------------------
UAELCNV1Descriptors = {'IMAGENAME1': r'LOGO_UAE_TC7_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC7_VCN_DownButon.png',
            
                              'CONFIGJSON1': r'LOGO_UAE_TESTCASE7_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE7_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 8:UAELCNZeroDescriptors
# ----------------------------------------------------------------------------------------
UAELCNZeroDescriptors = {'IMAGENAME1': r'LOGO_UAE_TC8_VCN_OpenEPG.png',
            
                    'CONFIGJSON1': r'LOGO_UAE_TESTCASE8_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 9:UAEAddDelLCNCheck
# ----------------------------------------------------------------------------------------
UAEAddDelLCNCheck = { 'IMAGENAME1': r'LOGO_UAE_TC9_VCN_OpenEPG.png',
            
                      'CONFIGJSON1': r'LOGO_UAE_TESTCASE9_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 10:UAEAddDelAddService
# ----------------------------------------------------------------------------------------
UAEAddDelAddService = { 'IMAGENAME1': r'LOGO_UAE_TC10_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC10_VCN_OpenEPG_After_Interval.png',
                        'IMAGENAME3': r'LOGO_UAE_TC10_VCN_Down_6_Times_CHLCheck.png',
                        
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE10_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE10_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_UAE_TESTCASE10_REF_VCN_image3.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 11:UAEAddDelNormalService
# ----------------------------------------------------------------------------------------
UAEAddDelNormalService = {'IMAGENAME1': r'LOGO_UAE_TC11_VCN_OpenEPG.png',
            
                          'CONFIGJSON1': r'LOGO_UAE_TESTCASE11_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 12:UAEAddDelDeleteService
# ----------------------------------------------------------------------------------------
UAEAddDelDeleteService = {'IMAGENAME1': r'LOGO_UAE_TC12_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC12_VCN_OpenEPG_AfterInterval.png',
            
                          'CONFIGJSON1': r'LOGO_UAE_TESTCASE12_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE12_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 13:UAEClashLCNSimultaneous
# ----------------------------------------------------------------------------------------
UAEClashLCNSimultaneous = {'IMAGENAME1': r'LOGO_UAE_TC13_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC13_VCN_CheckCHL_EPG.png',
            
                           'CONFIGJSON1': r'LOGO_UAE_TESTCASE13_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE13_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 14:UAEClashLCNMuxInitial
# ----------------------------------------------------------------------------------------
UAEClashLCNMuxInitial = { 'IMAGENAME1': r'LOGO_UAE_TC14_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC14_VCN_CheckCHL_EPG.png',
                        'IMAGENAME3': r'LOGO_UAE_TC14_VCN_Down_1_Time.png',
                        
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE14_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE14_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_UAE_TESTCASE14_REF_VCN_image3.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 15:UAEClashLCNMuxAfter
# ----------------------------------------------------------------------------------------
UAEClashLCNMuxAfter = {'IMAGENAME1': r'LOGO_UAE_TC15_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC15_VCN_CheckCHL_EPG.png',
            
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE15_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE15_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 16:UAEMuxAddDelInitial
# ----------------------------------------------------------------------------------------
UAEMuxAddDelInitial = {'IMAGENAME1': r'LOGO_UAE_TC16_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC16_VCN_CheckCHL_EPG.png',
            
                       'CONFIGJSON1': r'LOGO_UAE_TESTCASE16_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE16_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 17:UAEMuxAddDelSimultaneous
# ----------------------------------------------------------------------------------------
UAEMuxAddDelSimultaneous = {'IMAGENAME1': r'LOGO_UAE_TC17_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC17_VCN_CheckCHL_EPG.png',
            
                            'CONFIGJSON1': r'LOGO_UAE_TESTCASE17_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE17_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 18s:UAEMuxAddDelChlDel474
# ----------------------------------------------------------------------------------------
UAEMuxAddDelChlDel474 = {'IMAGENAME1': r'LOGO_UAE_TC18_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC18_VCN_CheckCHL_EPG.png',
            
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE18_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE18_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 19:UAEMuxAddDelChlDel858
# ----------------------------------------------------------------------------------------
UAEMuxAddDelChlDel858 = { 'IMAGENAME1': r'LOGO_UAE_TC19_VCN_OpenEPG.png','IMAGENAME2': r'LOGO_UAE_TC19_VCN_CheckCHL_EPG.png',
            
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE19_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE19_REF_VCN_image2.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 20:UAEServiceLCNUpdate
# ----------------------------------------------------------------------------------------
UAEServiceLCNUpdate = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 21:UAEServiceEventUpdate120
# ----------------------------------------------------------------------------------------
UAEServiceEventUpdate120 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 22:UAEServiceEventUpdate131
# ----------------------------------------------------------------------------------------
UAEServiceEventUpdate131 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 23:UAEServiceEventUpdate555
# ----------------------------------------------------------------------------------------
UAEServiceEventUpdate555 = {}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 24:UAECharEventPF
# ----------------------------------------------------------------------------------------
UAECharEventPF = { 'IMAGENAME1': r'LOGO_UAE_TC24_VCN_CHARACTER_EVENT_TS_OPEN_EPG.png','IMAGENAME2': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME3': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME4': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_EI.png',
                        'IMAGENAME5': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EVENT.png', 'IMAGENAME6': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI.png',
                        'IMAGENAME7': r'LOGO_UAE_TC24_VCN_LCN100_CHARACTER_DISPLAY_NEXT_EI_BANNER.png', 'IMAGENAME8': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME9': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME10': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_EPG_INFO.png',
                        'IMAGENAME11': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG.png', 'IMAGENAME12': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_NEXT_EPG_INFO.png',
                        'IMAGENAME13': r'LOGO_UAE_TC24_VCN_LCN101_CHARACTER_DISPLAY_NEXT_BANNER.png', 'IMAGENAME14': r'LOGO_UAE_TC24_VCN_LCN102_CHARACTER_DISPLAY_BANNER.png',
                        'IMAGENAME15': r'LOGO_UAE_TC24_VCN_LCN102_CHARACTER_DISPLAY_EPG.png', 'IMAGENAME16': r'LOGO_UAE_TC24_VCN_LCN102_CHARACTER_DISPLAY_EPG_INFO.png',
                              
                        'CONFIGJSON1': r'LOGO_UAE_TESTCASE24_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE24_REF_VCN_image2.json',
                        'CONFIGJSON3': r'LOGO_UAE_TESTCASE24_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_UAE_TESTCASE24_REF_VCN_image8.json',
                        'CONFIGJSON5': r'LOGO_UAE_TESTCASE24_REF_VCN_image9.json','CONFIGJSON6': r'LOGO_UAE_TESTCASE24_REF_VCN_image10.json',
                        'CONFIGJSON7': r'LOGO_UAE_TESTCASE24_REF_VCN_image11.json','CONFIGJSON8': r'LOGO_UAE_TESTCASE24_REF_VCN_image16.json',
                        'CONFIGJSON9': r'LOGO_UAE_TESTCASE24_REF_VCN_image21.json','CONFIGJSON10': r'LOGO_UAE_TESTCASE24_REF_VCN_image22.json',
                        'CONFIGJSON11': r'LOGO_UAE_TESTCASE24_REF_VCN_image23.json','CONFIGJSON12': r'LOGO_UAE_TESTCASE24_REF_VCN_image24.json',
                        'CONFIGJSON13': r'LOGO_UAE_TESTCASE24_REF_VCN_image25.json','CONFIGJSON14': r'LOGO_UAE_TESTCASE24_REF_VCN_image30.json',
                        'CONFIGJSON15': r'LOGO_UAE_TESTCASE24_REF_VCN_image35.json','CONFIGJSON16': r'LOGO_UAE_TESTCASE24_REF_VCN_image36.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 25:UAECharEventSchedule
# ----------------------------------------------------------------------------------------
UAECharEventSchedule = {'IMAGENAME1': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_EPG.png','IMAGENAME2': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_3_EPG.png',
                                'IMAGENAME3': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_3_EPG_EI.png', 'IMAGENAME4': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_4_EPG.png',
                                'IMAGENAME5': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_4_EPG_EI.png', 'IMAGENAME6': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_5_EPG.png',
                                'IMAGENAME7': r'LOGO_UAE_TC25_VCN_EVENTSCHEDULE_5_EPG_EI.png', 
                                
                                'CONFIGJSON1': r'LOGO_UAE_TESTCASE25_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE25_REF_VCN_image2.json',
                                'CONFIGJSON3': r'LOGO_UAE_TESTCASE25_REF_VCN_image3.json','CONFIGJSON4': r'LOGO_UAE_TESTCASE25_REF_VCN_image4.json',
                                'CONFIGJSON5': r'LOGO_UAE_TESTCASE25_REF_VCN_image5.json','CONFIGJSON6': r'LOGO_UAE_TESTCASE25_REF_VCN_image6.json',
                                'CONFIGJSON7': r'LOGO_UAE_TESTCASE25_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 26:UAENoTableDefinition
# ----------------------------------------------------------------------------------------
UAENoTableDefinition = {'IMAGENAME1': r'LOGO_UAE_TC26_VCN_BANNER.png','IMAGENAME2': r'LOGO_UAE_TC26_VCN_EPG.png',
                                'IMAGENAME3': r'LOGO_UAE_TC26_VCN_EI.png', 

                                'CONFIGJSON1': r'LOGO_UAE_TESTCASE26_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE26_REF_VCN_image6.json',
                                'CONFIGJSON3': r'LOGO_UAE_TESTCASE26_REF_VCN_image7.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 27:UAELatinTable1
# ----------------------------------------------------------------------------------------
UAELatinTable1 = {'IMAGENAME1': r'LOGO_UAE_TC27_VCN_ISO_BANNER.png','IMAGENAME2': r'LOGO_UAE_TC27_VCN_ISO_EPG.png',
                   'IMAGENAME3': r'LOGO_UAE_TC27_VCN_ISO_EI.png',
                              
                   'CONFIGJSON1': r'LOGO_UAE_TESTCASE27_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE27_REF_VCN_image1.json',
                   'CONFIGJSON3': r'LOGO_UAE_TESTCASE27_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 28:UAELatinTable2
# ----------------------------------------------------------------------------------------
UAELatinTable2 = {'IMAGENAME1': r'LOGO_UAE_TC28_VCN_ISO_BANNER.png','IMAGENAME2': r'LOGO_UAE_TC28_VCN_ISO_EPG.png',
                   'IMAGENAME3': r'LOGO_UAE_TC28_VCN_ISO_EI.png',
                              
                   'CONFIGJSON1': r'LOGO_UAE_TESTCASE28_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE28_REF_VCN_image1.json',
                   'CONFIGJSON3': r'LOGO_UAE_TESTCASE28_REF_VCN_image1.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Test Case 29:UAEAFDTest
# ----------------------------------------------------------------------------------------
UAEAFDTest = { 'IMAGENAME1': r'LOGO_UAE_TC29_VCN_EPG.png','IMAGENAME2': r'LOGO_UAE_TC29_VCN_BANNER_111.png',
                              'IMAGENAME3': r'LOGO_UAE_TC29_VCN_BANNER_222.png', 'IMAGENAME4': r'LOGO_UAE_TC29_VCN_BANNER_333.png',
                              'IMAGENAME5': r'LOGO_UAE_TC29_VCN_BANNER_444.png',

                              'CONFIGJSON1': r'LOGO_UAE_TESTCASE29_REF_VCN_image1.json','CONFIGJSON2': r'LOGO_UAE_TESTCASE29_REF_VCN_image2.json',
                              'CONFIGJSON3': r'LOGO_UAE_TESTCASE29_REF_VCN_image7.json','CONFIGJSON4': r'LOGO_UAE_TESTCASE29_REF_VCN_image12.json',
                              'CONFIGJSON5': r'LOGO_UAE_TESTCASE29_REF_VCN_image17.json'}
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------