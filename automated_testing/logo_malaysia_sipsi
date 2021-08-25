# Import Python built in modules
import time

# Import AKIRA modules - do not modify
from Api.uistructure.uistructurelibrary import UIConstant as UIC
from Api.at import ConstantName as CN
from Api.at import Utility
from lib.script.moduleinit import TestScriptInit, TestExecution

STATION_INFO = Utility.get_test_station_info()

# Test Script Config import - can be modified
# Change path & module name accordingly if not default
from testscript.broadcast import logo_malaysia_sipsi_config as TC

#  Common Module import - can be modified
from lib.broadcast import broadcastlib as BL
from lib.common import navigation as NV
from lib.common import common as CM

class ScriptInitialise(TestScriptInit):

    def __init__(self,**optional):
        # Do-not change this
        super().__init__(
                        systemreq= TC.Init['SYSTEMREQ'],
                        excelsavefilename= TC.Init['EXCELSAVEFILENAME'],
                        **optional)


        # Common module init here
        # Navigation & CommonUtility module are higly recommended
        # Uncomment to use
        self.navi = NV.Navigation(project=self.projectname,
                                  remote=self.remote, 
                                  tracking=self.tracking, 
                                  system=self.system, 
                                  capture=self.capture)
        self.navi.start_from_home()

        self.brctfx = BL.BroadcastFunctions(serial=self.serial,
                                            remote=self.remote,
                                            projectname=self.projectname,
                                            region=self.region,
                                            country=self.country,
                                            system=self.system,
                                            datetime=self.datetime,
                                            navigation = self.navi
                                            )
        self.common = CM.CommonUtility(project=self.projectname,
                                       remote=self.remote,
                                       serial=self.serial,
                                       tracker=self.tracking,
                                       capture=self.capture
                                       )
        # Additional Common module init here

class DefaultTestCase(ScriptInitialise):
    def __init__(self, **optional):
        # Script test case database. Change the value of the dictionary with test case class name
        self.testcasedb_all = {
                        'TestCase1': MYSServiceInstallation,
                        'TestCase2': MYSEventInformation,
                        'TestCase3': MYSCodecInformation,
                        'TestCase4': MYSCodecInformationAudioAlternate, # Passed
                        'TestCase5': MYSAudioSubsLanguage,
                        'TestCase6': MYSLCNV1Descriptors,
                        'TestCase7': MYSLCNV2Descriptors,
                        'TestCase8': MYSForeignService,
                        'TestCase9': MYSNoLCNDescriptor,
                        'TestCase10': MYSRegionalBroadcastManagement,
                        'TestCase11': MYSServiceAddDelLCNCheck,
                        'TestCase12': MYSServiceAddDelAddTS,
                        'TestCase13': MYSServiceAddDelLCNCheckAfterDel,
                        'TestCase14': MYSServiceAddDelTSDeletion,
                        'TestCase15': MYSClashLCNResolutionTSMux,
                        'TestCase16': MYSClashLCNResolutionASU,
                        'TestCase17': MYSClashLCNResolutionASUDiffMhz,
                        'TestCase18': MYSMultiplexAddDelStaticAdd,
                        'TestCase19': MYSMultiplexAddDelSimultaneous,
                        'TestCase20': MYSMultiplexAddDel474Mhz,
                        'TestCase21': MYSMultiplexAddDel858Mhz,
                        'TestCase22': MYSServiceEventUpdateLCN120,
                        'TestCase23': MYSServiceEventUpdateLCN131,
                        'TestCase24': MYSServiceEventUpdateLCN555,
                        'TestCase25': MYSCharEventPF,
                        'TestCase26': MYSCharEventSchedule,
                        'TestCase27': MYSCharEventPFHuffman,
                        'TestCase28': MYSCharEventScheduleHuffman,
                        'TestCase29': MYSHuffmanMalay,
                        'TestCase30': MYSHuffmanESC,
                        'TestCase31': MYSNoTableDefinition,
                        'TestCase32': MYSAFDTest
        }
        super().__init__(**optional)
        self.name = __name__

# Add helper function here if any
##################  video judgment initialisation ###############
        run_time_para = Utility.get_run_time_para_data()
        # self.debugmode = TestConfig.Init['DEBUGMODE']
        self.debugmode = False
 
        if run_time_para['TEAM']['NAME'] is None:
            self.team = 'default'
        else:
            self.team = run_time_para['TEAM']['NAME']
 
###################################################################
    def video_hlink_gen(self,vidname):
        """
        To add hyperlink to your excel report so that boleh kebulan
        
        Args:
            vidname (string): exclude extension from naming
 
        Returns:
            [string]: Excel formula so that it can execute video from clicking it =p
        """
        if self.debugmode:
            tmptestvideoname = vidname
        else:
            tmptestvideoname = '{}_{}_{}'.format(self.datetime, self.team, vidname)
        fileformula = r'=HYPERLINK(LEFT(CELL("filename",A1),FIND("[",CELL("filename",A1))-1)&"{}.mp4")'.format(tmptestvideoname)
 
        return fileformula

    def test_preconditions(self):
            """
            Precondition(s) when test script is executed.
            Will be called by common module, after common precondition.
            Common precondition can be skipped by passing 'use_common = False' at the execution below.
            Operations:
                [1] Perform factory reset for local execution
                [2] Disconnect to network if connected for common pool
            """
            debug = False
            if STATION_INFO['env'] == 'dev':
                if not debug:
                    self.brctfx.return_to_ootb_condition(country=UIC.UI_FMALAYSIA)
            try:
                self.ac_netswitch.off()
            except:
                self.SYS_LOG.debug('No network found')


###----------- Test Case Classes Starts -------------###

class MYSServiceInstallation(DefaultTestCase):
    """
    1.1.1 & 1.1.2

    Play out MYS_SIPSI_1a.ts

    Perform full scan and observe the information as in expectation.

    Enter each service and ensure that all of them are accessible via numerical keys. Confirm the correct service name and LCN numbering in each service. 

    Steps:
        [1] Stop MYS_SIPSI_1a.ts 
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Observe the Service Name and LCN Numbering for each service in the service list and ensure that they are correctly arranged in an ascending order as below:

            LCN 208 : TV1_SD
            LCN 209 : TV2_HD
            LCN 210 : TV3_HD
            LCN 211 : TV4_SD
            LCN 212: TV5_Radio
            LCN 213: TV6_Radio

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all']
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_1a.ts)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp(pincode=TC.Init['SETUPPIN'])

        # Enter LCN 208
        self.brctfx.numeric_keys(208)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME1'], TC.MYSServiceInstallation['CONFIGJSON1'], 
        testdesc='Check for Service Installation: LCN208')
        
        # Enter LCN 209
        self.brctfx.numeric_keys(209)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME2'], TC.MYSServiceInstallation['CONFIGJSON2'], 
        testdesc='Check for Service Installation: LCN209')
        
        # Enter LCN 210
        self.brctfx.numeric_keys(210)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME3'], TC.MYSServiceInstallation['CONFIGJSON3'], 
        testdesc='Check for Service Installation: LCN210')
        
        # Enter LCN 211
        self.brctfx.numeric_keys(211)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME4'], TC.MYSServiceInstallation['CONFIGJSON4'], 
        testdesc='Check for Service Installation: LCN211')
        
        # Enter LCN 212
        self.brctfx.numeric_keys(212)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME5'], TC.MYSServiceInstallation['CONFIGJSON5'], 
        testdesc='Check for Service Installation: LCN212')
        
        # Enter LCN 213
        self.brctfx.numeric_keys(213)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME6'], TC.MYSServiceInstallation['CONFIGJSON6'], 
        testdesc='Check for Service Installation: LCN213')

        # Enter LCN 208
        self.brctfx.numeric_keys(208)
        
        self.dektec1.StopVideo(),time.sleep(2)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME7'], TC.MYSServiceInstallation['CONFIGJSON7'], 
        testdesc='Check for Service Installation: Open EPG')
        self.remote.RCDown(repetition = 9, delay = 2)
        self.capture.CapturePhoto(TC.MYSServiceInstallation['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceInstallation['IMAGENAME8'], TC.MYSServiceInstallation['CONFIGJSON8'], 
        testdesc='Check for Service Installation: Check CHL in EPG')
        self.remote.RCBack(delay = 2)

        videoname1 = 'LOGO_MYS_VCN_MYSServiceInstallation_Button_Test_video'
        testdescription1 = 'Check for Button Test.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCEPG(delay = 2)
        self.remote.RCDown(delay = 2)
        self.remote.RCSelect(delay = 2)
        self.remote.RCEPG(delay = 2)
        self.remote.RCChannelUp(delay = 3)
        self.remote.RCChannelDown(delay = 3)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSEventInformation(DefaultTestCase):
    """
    1.2.1 - 1.2.15
    Check the event information after accesing lcn banner such as rating

    Steps:
        [1] Enter LCN and access banner
        [2] Capture image for banner, epg, epg information, next event
        [3] Make picture judgement for each item
        [4] Record video to do lcn check 

    Expectation:
        [1] Service Name
            Event start and end time
            Event name
            Short Event Description
            Extended Event Description
            Rating

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_1a.ts)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp()

        # Enter LCN 208
        self.brctfx.numeric_keys(208)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME1'], TC.MYSEventInformation['CONFIGJSON1'], 
        testdesc='Check for Event Information:(208) Display Banner')
        self.dektec1.StopVideo(),time.sleep(2)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME2'], TC.MYSEventInformation['CONFIGJSON2'], 
        testdesc='Check for Event Information:(208) Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME3'], TC.MYSEventInformation['CONFIGJSON3'], 
        testdesc='Check for Event Information:(208) Display EPG Desc')
        self.remote.RCBack(delay = 2)
        self.remote.RCRight(delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME4'], TC.MYSEventInformation['CONFIGJSON4'], 
        testdesc='Check for Event Information:(208) Display Next EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME5'], TC.MYSEventInformation['CONFIGJSON5'], 
        testdesc='Check for Event Information:(208) Display Next EI')
        self.remote.RCEPG(delay = 2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME6'], TC.MYSEventInformation['CONFIGJSON6'], 
        testdesc='Check for Event Information:(208) Display Next Banner') 

        self.brctfx.numeric_keys(209)
        
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME7'], TC.MYSEventInformation['CONFIGJSON7'], 
        testdesc='Check for Event Information:(209) Display Banner') 
        time.sleep(2)
        self.dektec1.StopVideo(),time.sleep(2)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME8'], TC.MYSEventInformation['CONFIGJSON8'], 
        testdesc='Check for Event Information:(209) Display EPG') 
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSEventInformation['IMAGENAME9'])
        self.system.RunPictureJudgementProgram(TC.MYSEventInformation['IMAGENAME9'], TC.MYSEventInformation['CONFIGJSON9'], 
        testdesc='Check for Event Information:(209) Display EPG Desc') 
        self.remote.RCEPG(delay=2)

class MYSCodecInformation(DefaultTestCase):
    """
    1.3.1 - 1.3.5
    Check the video component and the audio component

    Steps:
        [1] Play out MYS_SIPSI_1a.ts
        [2] Set primary and secondary audio language to 'English' 
        [3] Using numerical keys, press '208' to enter service LCN 208 TV1_SD.
        [4] Access the banner and check information as in expectation. 
        [5] Repeat step [1]-[4] for LCN 209,210,211

    Expectation:
        [1] LCN 208 :
                    Flowers video shall be presented .
                    The English HE-AAC Stereo - Guitar Solo audio  shall be presented.
        [2] LCN 209 : Village video shall be presented.
        [3] LCN 210 : Park video shall be presented.
        [4] LCN 211 : Bridge video shall be presented.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_1a.ts)
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp()
        
        # Enter LCN 208
        self.brctfx.numeric_keys(208)
        self.brctfx.viewing_tvapp()
        videoname1 = 'LOGO_MYS_VCN_MYSCodecInformation_LCNCheck_208_video'
        testdescription1 = 'Flowers video shall be presented, The English HE-AAC Stereo - Guitar Solo audio  shall be presented.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCBanner(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # Enter LCN 209
        self.brctfx.numeric_keys(209)
        time.sleep(10)
        videoname2 = 'LOGO_MYS_VCN_MYSCodecInformation_LCNCheck_209_video'
        testdescription2 = 'Village video shall be presented.:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        self.remote.RCBanner(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))

        # Enter LCN 210
        self.brctfx.numeric_keys(210)
        time.sleep(10)
        videoname3 = 'LOGO_MYS_VCN_MYSCodecInformation_LCNCheck_210_video'
        testdescription3 = 'Park video shall be presented.:'
        self.capture.StartRecording(videoname3), time.sleep(5)
        self.remote.RCBanner(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))

        # Enter LCN 211
        self.brctfx.numeric_keys(211)
        time.sleep(10)
        videoname4 = 'LOGO_MYS_VCN_MYSCodecInformation_LCNCheck_211_video'
        testdescription4 = 'Bridge video shall be presented.:'
        self.capture.StartRecording(videoname4), time.sleep(5)
        self.remote.RCBanner(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname4,
                                                testdesc = testdescription4 +
                                                self.video_hlink_gen(videoname4))

class MYSCodecInformationAudioAlternate(DefaultTestCase):
    """
    1.3.6
    Play out ChID_voices_swp_ddp_DVB_h264_25fps.trp and perform receiver full scan.
    Enter Service Dolby Labs Test Stream

    Steps:
        [1] Play TS
        [2] Perform Full Scan Receiver

    Expectation:
        [1] Audio alternates between each channel should be presented. 
            Note: Audio presentation is optional.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        pass
        # Run TS ( ChID_voices_swp_ddp_DVB_h264_25fps.trp)
        # self.dektec1.Run(TC.TestCase4['TSCONFIGPATH'],TC.TestCase4['TSPATH'])

class MYSAudioSubsLanguage(DefaultTestCase):
    """
    1.4.1 - 1.4.11
    Check for audio and substitle language

    Steps:
        [1] Play out MYS_SIPSI_1a.ts and perform receiver full scan.
            Enter Service  TV1_SD
            Firstly, perform the following  setting : 
            - Enable Subtitles
            Note 1 : All subtitles presented are in English. 
            Note 2 : If subtitles do not display due to PTS-PCR difference, then subtitle tests can be considered a PASS. Please indicate in Remarks if this is the case, and also ensure to make self declaration in section 7.1 regarding the Display of Subtitles.


    Expectation:
        [1] Keyboard audio  shall be selectable when the audio selection is set to Bahasa Melayu (MSA).+E50:E59
            Bahasa Melayu subtitles,  "SIPSI Test. Subtitle 1, number…,  shall be selectable when the subtitle selection is set to Bahasa Melayu (MSA).
            Bell rings audio  shall be selectable when the audio selection is set to Chinese (ZHO).
            Chinese subtitles,  "SIPSI Test. Subtitle 2,  number…,  shall be selectable when the subtitle selection is set to Chinese (ZHO). 
            Drum Solo audio  shall be selectable when the audio selection is set to Tamil (TAM).
            Tamil subtitles,  SIPSI Test. Subtitle 3,  number…,  shall be selectable when the subtitle selection is set to Tamil (TAM). 
            Guitar Solo audio  shall be selectable when the audio selection is set to English.
            English subtitles, SIPSI Test. Subtitle 0,  number…,  shall be selectable when the subtitle selection is set to English. 
            Receiver shall present any of the following audio components when the audio selection is set to other languages besides Bahasa Melayu, English, Chinese and Tamil:
            English (ENG) - Guitar Solo
            Bahasa Melayu (MSA) - Keyboard
            Chinese (ZHO) - Bell rings
            Tamil (TAM) - Drum Solo
            Receiver shall present any of the following subtitle components when the subtitle selection is set to other languages besides Bahasa Melayu, English, Chinese and Tamil:

            English (ENG) Subtitles
            Bahasa Melayu (MSA) Subtitles
            Chinese (ZHO) Subtitles
            Tamil (TAM) Subtitles


    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        self.dektec1.Run('MYS_SIPSI_1a.xml','MYS_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(208)
        time.sleep(10)
        self.remote.RCAudioMenu(delay = 2)
        self.capture.CapturePhoto(TC.MYSAudioSubsLanguage['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSAudioSubsLanguage['IMAGENAME1'], TC.MYSAudioSubsLanguage['CONFIGJSON1'], 
        testdesc='Check for Audio and Subs Language: Open Audio Menu')
        self.remote.RCDown(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.MYSAudioSubsLanguage['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSAudioSubsLanguage['IMAGENAME2'], TC.MYSAudioSubsLanguage['CONFIGJSON2'], 
        testdesc='Check for Audio and Subs Language: All Audio Menu')
        self.remote.RCUp(delay = 2)
        
        videoname1 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_AudioCheck_BM_video'
        testdescription1 = 'Check for Audio Test (Keyboard BM).:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # Select Chinese audio
        self.remote.RCAudioMenu(delay = 2)
        videoname2 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_AudioCheck_ZHO_video'
        testdescription2 = 'Check for Audio Test (Bell ZHO).:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        self.remote.RCDown(delay = 2)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))
        
        # Select Tamil audio
        self.remote.RCAudioMenu(delay = 2)
        videoname3 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_AudioCheck_TAM_video'
        testdescription3 = 'Check for Audio Test (Drum Solo TAMIL).:'
        self.capture.StartRecording(videoname3), time.sleep(5)
        self.remote.RCDown(delay = 2)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))
        
        # Select English audio
        self.remote.RCAudioMenu(delay = 2)
        videoname4 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_AudioCheck_ENG_video'
        testdescription4 = 'Check for Audio Test (Guitar Solo ENG).:'
        self.capture.StartRecording(videoname4), time.sleep(5)
        self.remote.RCUp(repetition = 3, delay = 2)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname4,
                                                testdesc = testdescription4 +
                                                self.video_hlink_gen(videoname4))

        # Move from TV to SUBTITLE
        self.remote.RCMove(UIC.UI_DTV, UIC.UI_SUBTITLE, moreoption=[UIC.UIBASIC], delay=2)
        self.brctfx.viewing_tvapp()
        # Subtitle 
        self.remote.RCSubtitle(delay = 2)
        self.capture.CapturePhoto(TC.MYSAudioSubsLanguage['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSAudioSubsLanguage['IMAGENAME3'], TC.MYSAudioSubsLanguage['CONFIGJSON3'], 
        testdesc='Check for Audio and Subs Language: Open Substitle Menu')
        self.remote.RCDown(repetition = 2, delay = 2)
            
        videoname5 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_SubsCheck_BM_video'
        testdescription5 = 'Check for Subtitle BM.:'
        self.capture.StartRecording(videoname5), time.sleep(5)
        self.remote.RCSelect(delay = 2)
        self.remote.RCBanner(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname5,
                                                testdesc = testdescription5 +
                                                self.video_hlink_gen(videoname5))
        
        # Subtitle
        self.remote.RCSubtitle(delay = 2)
        self.remote.RCDown(repetition = 3, delay = 2)
            
        videoname6 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_SubsCheck_ZHO_video'
        testdescription6 = 'Check for Subtitle Chinese.:'
        self.capture.StartRecording(videoname6), time.sleep(5)
        self.remote.RCSelect(delay = 2)
        self.remote.RCBanner(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname6,
                                                testdesc = testdescription6 +
                                                self.video_hlink_gen(videoname6))
        
        # Subtitle
        self.remote.RCSubtitle(delay = 2)
        self.remote.RCDown(repetition = 4, delay = 2)
            
        videoname7 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_SubsCheck_TAM_video'
        testdescription7 = 'Check for Subtitle Tamil.:'
        self.capture.StartRecording(videoname7), time.sleep(5)
        self.remote.RCSelect(delay = 2)
        self.remote.RCBanner(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname7,
                                                testdesc = testdescription7 +
                                                self.video_hlink_gen(videoname7))
        
        # Subtitle
        self.remote.RCSubtitle(delay = 2)
        self.remote.RCDown(delay = 2)
            
        videoname8 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_SubsCheck_ENG_video'
        testdescription8 = 'Check for Subtitle English.:'
        self.capture.StartRecording(videoname8), time.sleep(5)
        self.remote.RCSelect(delay = 2)
        self.remote.RCBanner(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname8,
                                                testdesc = testdescription8 +
                                                self.video_hlink_gen(videoname8))

        # Enter LCN 209
        self.brctfx.numeric_keys(209)
        time.sleep(10)
        
        # Select audio
        self.remote.RCAudioMenu(delay = 2)
        # Start capturing photo (Audio menu)
        self.capture.CapturePhoto(TC.MYSAudioSubsLanguage['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSAudioSubsLanguage['IMAGENAME4'], TC.MYSAudioSubsLanguage['CONFIGJSON4'], 
        testdesc='Check for Audio and Subs Language: Open Audio LCN209 Menu')
        self.remote.RCDown(repetition = 3, delay = 2)

        videoname8 = 'LOGO_MYS_VCN_MYSAudioSubsLanguage_Audio_LCN209_video'
        testdescription8 = 'Check for Audio LCN209.:'
        self.capture.StartRecording(videoname8), time.sleep(5)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname8,
                                                testdesc = testdescription8 +
                                                self.video_hlink_gen(videoname8))

class MYSLCNV1Descriptors(DefaultTestCase):
    """
    2.1.1
    Test LCN V1 descriptors with valid PDS

    Steps:
        [1] Play out MYS_SIPSI_2.1a.ts. 
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 6 services shall be visible in the service list and shall be in ascending order as below:

            LCN  010       TV 1
            LCN  031       TV 4.1/TV 4.2
            LCN  561       Radio 9
            LCN  800++  TV 4.1/TV 4.2
            LCN  800++  TV 6
            LCN  800++  Service with no LCN

            Confirm that receiver is able to access each service normally via numerical keys and service list.

            Using numerical keys, press '102' to enter service LCN 102 Radio 8.
            This service is hidden and can only be selected using direct key entry.
            "Drum Solo" audio shall be presented. 

            Using numerical keys, press '031' to enter service LCN 031 TV 4.1/ or TV 4.2.
            "Bridge" video and 'Keyboard' audio shall be presented.

            Select 'Service with no LCN' service.
            LCN 800++  shall be assigned to this service.
            "Bridge" video and "Guitar Solo" audio shall be presented.
                    
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_2.1a)
        self.dektec1.Run('MYS_SIPSI_2.1a.xml','MYS_SIPSI_2.1a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSLCNV1Descriptors['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSLCNV1Descriptors['IMAGENAME1'], TC.MYSLCNV1Descriptors['CONFIGJSON1'], 
        testdesc='Check for LCN V1 Descriptor: Open EPG')
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.MYSLCNV1Descriptors['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSLCNV1Descriptors['IMAGENAME2'], TC.MYSLCNV1Descriptors['CONFIGJSON2'], 
        testdesc='Check for LCN V1 Descriptor: EPG Chl Check')
        self.remote.RCEPG(delay = 2)

        # Start Recording
        videoname1 = 'LOGO_MYS_VCN_MYSLCNV1Descriptors_LCNCheck_video'
        testdescription1 = 'Check for LCN Test V1 Descriptor.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [10,31,561,800,801,802,102]
        for x in range (7):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSLCNV2Descriptors(DefaultTestCase):
    """
    2.1.2
    Test LCN V2 descriptors with valid PDS

    Steps:
        [1] Play out stream  MYS_SIPSI_2.1b.ts  
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 6 services shall be visible in the service list and shall be in ascending order as below:
            LCN  005      TV 1
            LCN  055      TV 4.1
            LCN  166       Radio 9
            LCN  800++  TV 4.2
            LCN  800++  TV 6
            LCN  800++  Service with no LCN

            Service with LCN 300 is hidden and shall not appear in the service list. 
            Confirm that receiver is able to access each service normally via numerical keys. 

            Using numerical keys, press '300' to enter service LCN 300 Radio 8.
            This service is hidden and can only be selected using direct key entry.
            "Bell rings" audio shall be presented. 

            Using numerical keys, press '055' to enter service LCN 055 TV 4.1 or TV 4.2.
            "Bridge" video and "Keyboard" audio shall be presented.

            Select 'Service with no LCN' service.
            LCN 800++  shall be assigned to this service.
            "Bridge" video and "Guitar Solo" audio shall be presented.
        
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all']  
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_2.1b.ts)
        self.dektec1.Run('MYS_SIPSI_2.1b.xml','MYS_SIPSI_2.1b.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSLCNV2Descriptors['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSLCNV2Descriptors['IMAGENAME1'], TC.MYSLCNV2Descriptors['CONFIGJSON1'], 
        testdesc='Check for LCN V2 Descriptor: Open EPG')
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.MYSLCNV2Descriptors['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSLCNV2Descriptors['IMAGENAME2'], TC.MYSLCNV2Descriptors['CONFIGJSON2'], 
        testdesc='Check for LCN V2 Descriptor: EPG Chl Check')
        self.remote.RCEPG(delay = 2)

        # Start Recording
        videoname1 = 'LOGO_MYS_VCN_MYSLCNV2Descriptors_LCNCheck_video'
        testdescription1 = 'Check for LCN Test V2 Descriptor.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [5,55,166,800,801,802,300]
        for x in range (7):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSForeignService(DefaultTestCase):
    """
    2.2.1
    Check for foreign service with LCN800++

    Steps:
        [1] Play out stream  MYS_SIPSI_2.1b.ts and FGN_SIPSI_2.2.ts simultaneously and perform receiver's auto scan method
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 9 services shall be visible in the service list and shall be in ascending order as below for the Central Region channel list (ID : 0x0001)

            LCN  001  MY_TV 1
            LCN  005  MY_TV 15
            LCN  007  MY_TV 2
            LCN  033  MY_HDTV 4
            LCN  155  MYTV_10
            LCN  431  MY_Radio 6
            LCN  611  MY_TV 5
            LCN  701  MY_TV 7
            LCN  800++  MY_TV 8

            Confirm that receiver is able to access each service normally via numerical keys and service list.

            Note: Data type service is optional.
        
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_2.1b.ts)
        self.dektec1.Run('MYS_SIPSI_2.1b.xml','MYS_SIPSI_2.1b.ts')
        # Run TS2 (FGN_SIPSI_2.2.ts)
        self.dektec2.Run('FGN_SIPSI_2.2.xml','FGN_SIPSI_2.2.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSForeignService['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSForeignService['IMAGENAME1'], TC.MYSForeignService['CONFIGJSON1'], 
        testdesc='Check for Foreign Service: Open EPG')
        self.remote.RCDown(repetition=9, delay=1)
        self.capture.CapturePhoto(TC.MYSForeignService['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSForeignService['IMAGENAME2'], TC.MYSForeignService['CONFIGJSON2'], 
        testdesc='Check for Foreign Service: Check Channel in EPG')
        self.remote.RCDown(delay=1)
        self.capture.CapturePhoto(TC.MYSForeignService['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSForeignService['IMAGENAME3'], TC.MYSForeignService['CONFIGJSON3'], 
        testdesc='Check for Foreign Service: Down button 1 time EPG')
        self.remote.RCEPG(delay = 2)  

        videoname1 = 'LOGO_MYS_VCN_MYSForeignService_LCNCheck_video'
        testdescription1 = 'Check for LCN Foreign Language.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [5,55,166,800,801,802,803,804,805,806,300]
        for x in range (11):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # Stop dektec
        self.dektec2.StopVideo()

class MYSNoLCNDescriptor(DefaultTestCase):
    """
    2.3.1
    Check the No LCN Descriptor

    Steps:
        [1] Play out MYS_SIPSI_2.3.ts and FGN_SIPSI_2.3.ts simultaneously
            and perform receiver's auto scan method. 
        [2] Capture picture of the inital epg and make picture judgement
        [3] Record video for LCN Check

    Expectation:
        [1] Total of 12 services shall be visible in the service list and shall be an ascending order as below:

            LCN 001   TV 5
            LCN 002  TV 55_A
            LCN 003  Radio 5
            LCN 004  Radio7
            LCN 005  TV 55_B
            LCN 006  TV 132
            LCN 007  SI Television 100
            LCN 008  TV Service 101
            LCN 009  TV Service 102
            LCN 010  MI Television 201
            LCN 011  MI Television 202
            LCN 012  LL Television 300

            Confirm that receiver is able to access each service normally via numerical keys and service list.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_2.3.ts)
        self.dektec1.Run('MYS_SIPSI_2.3.xml','MYS_SIPSI_2.3.ts')
        # Run TS2 (FGN_SIPSI_2.3.ts)
        self.dektec2.Run('FGN_SIPSI_2.3.xml','FGN_SIPSI_2.3.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSNoLCNDescriptor['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSNoLCNDescriptor['IMAGENAME1'], TC.MYSNoLCNDescriptor['CONFIGJSON1'], 
        testdesc='Check for No LCN Descriptor: Open EPG')
        self.remote.RCDown(repetition=9, delay=1)
        self.capture.CapturePhoto(TC.MYSNoLCNDescriptor['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSNoLCNDescriptor['IMAGENAME2'], TC.MYSNoLCNDescriptor['CONFIGJSON2'], 
        testdesc='Check for No LCN Descriptor: Check Channel in EPG')
        self.remote.RCDown(delay=1)
        self.capture.CapturePhoto(TC.MYSNoLCNDescriptor['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSNoLCNDescriptor['IMAGENAME3'], TC.MYSNoLCNDescriptor['CONFIGJSON3'], 
        testdesc='Check for No LCN Descriptor: Down button 1 time EPG')
        self.remote.RCEPG(delay = 2) 

        videoname1 = 'LOGO_MYS_VCN_MYSNoLCNDescriptor_LCNCheck_video'
        testdescription1 = 'Check for No LCN Descriptor.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,3,4,5,6,7,8,9,10,11,12]
        for x in range (12):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSRegionalBroadcastManagement(DefaultTestCase):
    """
    2.4.1
    Check for regional broadcast management

    Steps:
        [1] Play out MYS_SIPSI_2.5.ts and perform receiver auto scan.
        [2] Select the channel list for Central Region (ID : 0x0001) in the  receiver's channel list menu.  
        [3] Record video to check the the LCN Central Region
        [4] Repeat step [1]-[3] for southern region

    Expectation:
        [1] Total of 9 services shall be visible in the service list and shall be in ascending order as below for the Central Region channel list (ID : 0x0001)

            LCN  001  MY_TV 1
            LCN  005  MY_TV 15
            LCN  007  MY_TV 2
            LCN  033  MY_HDTV 4
            LCN  155  MYTV_10
            LCN  431  MY_Radio 6
            LCN  611  MY_TV 5
            LCN  701  MY_TV 7
            LCN  800++  MY_TV 8

            Confirm that receiver is able to access each service normally via numerical keys and service list.

            Note: Data type service is optional.
        
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_2.4.ts)
        self.dektec1.Run('MYS_SIPSI_2.4.xml','MYS_SIPSI_2.4.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSRegionalBroadcastManagement['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSRegionalBroadcastManagement['IMAGENAME1'], TC.MYSNoLCNDescriptor['CONFIGJSON1'], 
        testdesc='Check for Regional Broadcast Mgnt: Open EPG')
        self.remote.RCDown(repetition=8, delay=1)
        self.capture.CapturePhoto(TC.MYSRegionalBroadcastManagement['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSRegionalBroadcastManagement['IMAGENAME2'], TC.MYSNoLCNDescriptor['CONFIGJSON2'], 
        testdesc='Check for Regional Broadcast Mgnt: Check Channel in EPG')
        self.remote.RCEPG(delay = 2) 

        videoname1 = 'LOGO_MYS_VCN_MYSRegionalBroadcastManagement_LCNCheck_video'
        testdescription1 = 'Check for LCN for Regional Brdcst Mgnt.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,5,7,33,155,431,611,701,800]
        for x in range (9):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(10)
        # Select Southern region
        self.brctfx.digital_auto_tuning(lcn_list=2)  
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSRegionalBroadcastManagement['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSRegionalBroadcastManagement['IMAGENAME3'], TC.MYSNoLCNDescriptor['CONFIGJSON3'], 
        testdesc='Check for Regional Broadcast Mgnt:LCN1 Open EPG')
        self.remote.RCDown(repetition=8, delay=2)
        self.capture.CapturePhoto(TC.MYSRegionalBroadcastManagement['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSRegionalBroadcastManagement['IMAGENAME4'], TC.MYSNoLCNDescriptor['CONFIGJSON4'], 
        testdesc='Check for Regional Broadcast Mgnt:LCN1 Check Channel in EPG')
        self.remote.RCEPG(delay = 2) 

        videoname2 = 'LOGO_MYS_VCN_MYSRegionalBroadcastManagement_LCNCheck_LCN1_video'
        testdescription2 = 'Check for LCN for Regional Brdcst Mgnt.:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        lcn = [2,6,10,36,105,437,617,770,800]
        for x in range (9):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))

class MYSServiceAddDelLCNCheck(DefaultTestCase): 
    """
    Do LCN Check for service addition and deletion testing

    Steps:
        [1] PLay TS MYS_SIPSI_3.1a.ts
        [2] Run Picture judgement for EPG check  
        [3] Record video to check the LCN is available or not 

    Expectation:
        A total of 4 services shall be presented as follows in ascending order:

        LCN 005 MY_TV Channel 1
        LCN 013 MY_ Radio Channel 5
        LCN 166 MY_TV Channel 11  
        LCN 180 MY_TV Channel 17  

        Confirm that receiver shall be able to access to each service normally via numerical keys and service list.
   
    Node Pre-requisite:
        [1] Dual Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.1a.ts)
        self.dektec1.Run('MYS_SIPSI_3.1a.xml','MYS_SIPSI_3.1a.ts') 
        
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelLCNCheck['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelLCNCheck['IMAGENAME1'], TC.MYSServiceAddDelLCNCheck['CONFIGJSON1'], 
        testdesc='Check for LCN based on MYS_SIPSI_3.1a: Open EPG')
        self.remote.RCEPG(delay=2)

        # LCN Input to check the LCN based on MYS_SIPSI_3.1a.ts
        videoname1 = 'LOGO_MYS_VCN_LCNCheck_31a_video'
        testdescription1 = 'Check for LCN based on MYS_SIPSI_3.1a.ts:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [5,13,166,180]
        for x in range (4):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1, 
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1)) 

class MYSServiceAddDelAddTS(DefaultTestCase):
    """
    3.1.2 & 3.1.3
    Stop the current TS, and add new ts in an interval time

    Steps:
        [1] Stop MYS_SIPSI_3.1a.ts and play out MYS_SIPSI_3.1a_addition.ts at the same frequency as before.
        [2] At interval 0::121,  same services shall be displayed in the service list as Ref. 3.1.1. (MYSServiceAddDelLCNCheck)

    Expectation:
        [1] Network update shall start within the interval 121::240.
        [2] Receiver shall automatically undergo network update and update the service list. 

        [3] A total of 6 services shall be presented in the service list as follows in ascending order:

            LCN 005 MY_TV Channel 1
            LCN 013 MY_ Radio Channel 5
            LCN 166 MY_TV Channel 11  
            LCN 180 MY_TV Channel 17  
            LCN 290 MY_Radio Channel 32
            LCN 351 MYS_TV Channel 106

        [4] Confirm that receiver shall be able to access to each service normally via numerical keys and service list. 

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.1a_addition.ts)
        self.dektec1.Run('MYS_SIPSI_3.1a_addition.xml','MYS_SIPSI_3.1a_addition.ts')
        self.brctfx.viewing_tvapp()
        # LCN 5
        self.brctfx.numeric_keys(5)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelAddTS['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelAddTS['IMAGENAME1'], TC.MYSServiceAddDelAddTS['CONFIGJSON1'], 
        testdesc='Check for LCN based on MYS_SIPSI_3.1a_addition.ts: Open EPG')
        self.remote.RCEPG(delay=2) 

        # LCN Input to check the LCN based on MYS_SIPSI_3.1a_addition.ts
        videoname1 = 'LOGO_MYS_VCN_LCNCheck_31a_Addition_video'
        testdescription1 = 'Check for LCN based on MYS_SIPSI_3.1a_addition.ts:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [13,166,180]
        for x in range (3):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        # LCN 5
        self.brctfx.numeric_keys(5)
        time.sleep(50)# Delay?? utk masuk saat 121
       
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelAddTS['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelAddTS['IMAGENAME2'], TC.MYSServiceAddDelAddTS['CONFIGJSON2'], 
        testdesc='Check for LCN based on MYS_SIPSI_3.1a_addition.ts: Open EPG')
        self.remote.RCDown(repetition = 5, delay = 2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelAddTS['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelAddTS['IMAGENAME3'], TC.MYSServiceAddDelAddTS['CONFIGJSON3'], 
        testdesc='Check for LCN based on MYS_SIPSI_3.1a_addition.ts: Downward 6 times')
        self.remote.RCEPG(delay=2)
        lcn = [5,13,166,180,290,351]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1, 
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1)) 

class MYSServiceAddDelLCNCheckAfterDel(DefaultTestCase): 
    """
    3.1.4
    Check LCN after TS Deletion 

    Steps:
        [1] Stop MYS_SIPSI_3.1a_addition.ts and play out MYS_SIPSI_3.1a.ts again.
        [2] Perform receiver auto scan.

    Expectation:
        [1] A total of 4 services shall be presented as follows in ascending order:

                LCN 005 MY_TV Channel 1
                LCN 013 MY_ Radio Channel 5
                LCN 166 MY_TV Channel 11  
                LCN 180 MY_TV Channel 17  

        [2] Confirm that receiver shall be able to access to each service normally via numerical keys and service list 

    Node Pre-requisite:
        [1] Dual Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.1a.ts)
        self.dektec1.Run('MYS_SIPSI_3.1a.xml','MYS_SIPSI_3.1a.ts')
        self.brctfx.viewing_tvapp()
        # LCN 5
        self.brctfx.numeric_keys(5)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelLCNCheckAfterDel['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelLCNCheckAfterDel['IMAGENAME1'], TC.MYSServiceAddDelLCNCheckAfterDel['CONFIGJSON1'], 
        testdesc='Check for LCN based on LCN 5: Open EPG')
        self.remote.RCEPG(delay=2) 

        videoname1 = 'LOGO_MYS_VCN_LCNCheck_AfterDEL_video'
        testdescription1 = 'Check for TS Del:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [5,13,166,180]
        for x in range (4):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))  

class MYSServiceAddDelTSDeletion(DefaultTestCase):
    """
    3.1.5 & 3.1.6
    Check for service deletion after an interval of time

    Steps:
        [1] Stop MYS_SIPSI_3.1a.ts and play out MYS_SIPSI_3.1a_deletion.ts at the same frequency as before.
        [2] Check the channel using video recording before and after the deletion 

    Expectation:
        [1] Network update shall start within the interval 121::240.
        [2] Receiver shall automatically undergo network update and update the service list. 

        [3] Confirm that 2 services are deleted from the service list and the remaining service presented in the service list are as follows in ascending order:

                LCN 005 MY_TV Channel 1
                LCN 013 MY_ Radio Channel 5

        [4] Confirm that receiver shall be able to access to each service normally via numerical keys and service list.
 
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.1a_deletion.ts)
        self.dektec1.Run('MYS_SIPSI_3.1a_deletion.xml','MYS_SIPSI_3.1a_deletion.ts')
        self.brctfx.viewing_tvapp() 
        # LCN 5
        self.brctfx.numeric_keys(5)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSServiceAddDelTSDeletion['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelTSDeletion['IMAGENAME1'], TC.MYSServiceAddDelTSDeletion['CONFIGJSON1'], 
        testdesc='Check for TS Deletion: Open EPG')
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_MYS_VCN_TSDeletion_video'
        testdescription1 = 'Check for TS Deletion:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [13,166,180]
        for x in range (3):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        # LCN 5
        self.brctfx.numeric_keys(5)
        time.sleep(50)# Delay?? utk masuk saat 121
        self.remote.RCEPG(delay=3)
        self.capture.CapturePhoto(TC.MYSServiceAddDelTSDeletion['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSServiceAddDelTSDeletion['IMAGENAME2'], TC.MYSServiceAddDelTSDeletion['CONFIGJSON2'], 
        testdesc='Check for TS Deletion: Open EPG after deletion')
        self.remote.RCEPG(delay=2)
        lcn = [5,13]
        for x in range (2):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSClashLCNResolutionTSMux(DefaultTestCase): 
    """
    3.2.1
    Play out 2 ts and check the LCN after auto scan

    Steps:
        [1] Play out MYS_SIPSI_3.2a.ts and MYS_SIPSI_3.2b.ts simultaneously and perform receiver auto scan method 
        [2] Capture picture of the epg
        [3] Record video for LCN checking

    Expectation:
        [1] Total of 9 services shall be visible in the service list and shall be an ascending order as below:

            LCN  100 Service_TV1_SD
            LCN  101 Service_TV2_SD
            LCN  102  Service_TV3_SD
            LCN  103  Service_Radio1
            LCN  104  Service_Radio2
            LCN  111 SD Service 1
            LCN  222 SD Service 1_muxB
            LCN  333 SD Service 2_muxB
            LCN  444 SD Service 2

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

            Using numerical keys, press '222'  to enter LCN 222 SD Service 1_muxB. 
            'Bridge' video and  'Bell Ring' audio shall be presented. 

            Commence following test from  LCN 222 SD Service 1_muxB.

    Node Pre-requisite:
        [1] Dual Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1','dektec2']

    def run(self):
        # Run TS (MYS_SIPSI_3.2a.ts)
        self.dektec1.Run('MYS_SIPSI_3.2a.xml','MYS_SIPSI_3.2a.ts')
        # Run TS (MYS_SIPSI_3.2b.ts)
        self.dektec2.Run('MYS_SIPSI_3.2b.xml','MYS_SIPSI_3.2b.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionTSMux['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionTSMux['IMAGENAME1'], TC.MYSClashLCNResolutionTSMux['CONFIGJSON1'], 
        testdesc='Check for clash lcn resolution ts mux: Open EPG')
        self.remote.RCDown(repetition = 8, delay = 2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionTSMux['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionTSMux['IMAGENAME2'], TC.MYSClashLCNResolutionTSMux['CONFIGJSON2'], 
        testdesc='Check for clash lcn resolution ts mux: Button Down')
        self.remote.RCEPG(delay=2) 

        videoname1 = 'LOGO_MYS_VCN_TSMux_32a_32b_video'
        testdescription1 = 'Check for TS Mux 3.2a and 3.2b:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,111,222,333,444]
        for x in range (9):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # LCN 222
        self.brctfx.numeric_keys(222) 

class MYSClashLCNResolutionASU(DefaultTestCase): 
    """
    3.2.2
    Mux 2 ts from power off on

    Steps:
        [1] Stop MYS_SIPSI_3.3a.ts. 
            Play out MYS_SIPSI_3.3a_mux.ts and MYS_SIPSI_3.3b_mux.ts simultaneously.

    Expectation:
        [1] Perform receiver method of network configuration update. 
            Ensure the following services shall be listed :

            LCN  100 Service_TV1_SD
            LCN  101 Service_TV2_SD
            LCN  102  Service_TV3_SD
            LCN  103  Service_Radio1
            LCN  104 Service_Radio2
            LCN  111 SD Service 1
            LCN  222  SD Service 1_muxB
            LCN  333 SD Service 2_muxB
            LCN  444 SD Service 2
            LCN 555 Service_Radio10
            LCN 666 Service_TV7_SD
            LCN 800++ SD_Service 2_muxA

            Using numerical keys, press '333', '555', and '666', and ensure the following components are available in the services :
            In LCN 333, 'Bell Ring' audio and  'Bridge' video shall be presented.
            In LCN 555, 'Keyboard' audio and 'Flowers' video shall be presented.
            In LCN 666,  'Keyboard' audio and 'Flowers' video shall be presented.
   
    Node Pre-requisite:
        [1] Dual Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1','dektec2']

    def run(self):
        # Run TS (MYS_SIPSI_3.2a_02.ts)
        self.dektec1.Run('MYS_SIPSI_3.2a_02.xml','MYS_SIPSI_3.2a_02.ts')
        # Run TS (MYS_SIPSI_3.2b_01.ts)
        self.dektec2.Run('MYS_SIPSI_3.2b_01.xml','MYS_SIPSI_3.2b_01.ts')
        
        self.remote.RCPower(delay=120)
        self.remote.RCPower(delay=10)

        # LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(10)

        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionASU['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionASU['IMAGENAME1'], TC.MYSClashLCNResolutionASU['CONFIGJSON1'], 
        testdesc='Check for MUX Addition: Open EPG')
        self.remote.RCDown(repetition=9, delay=1)         
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionASU['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionASU['IMAGENAME2'], TC.MYSClashLCNResolutionASU['CONFIGJSON2'], 
        testdesc='Check for MUX Addition: EPG Check CHL')
        self.remote.RCDown(delay = 2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionASU['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionASU['IMAGENAME3'], TC.MYSClashLCNResolutionASU['CONFIGJSON3'], 
        testdesc='Check for MUX Addition: Down Button 1 times')
        self.remote.RCEPG(delay = 2)

        videoname1 = 'LOGO_MYS_VCN_MYSClashLCNResolutionASU_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,111,222,333,444,555,666,800]
        for x in range (12):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # LCN 100
        self.brctfx.numeric_keys(100)
        
        self.dektec2.StopVideo()

class MYSClashLCNResolutionASUDiffMhz(DefaultTestCase):
    """
    3.2.3
    Mux 2 ts from power off on

    Steps:
        [1] Stop the streams and play out MYS_SIPSI_3.2a_02.ts and MYS_SIPSI_3.2b_02.ts 
            simultaneously at the same frequency as before.

    Expectation:
        [1] Perform receiver method of network configuration update. 
            Ensure that the following is displayed :

            LCN  100 Service_TV1_SD
            LCN  101 Service_TV2_SD
            LCN  102 Service_TV3_SD
            LCN  103 Service_Radio1
            LCN  104 Service_Radio2
            LCN  222 SD Service 1_muxB
            LCN  444 SD Service 2
            LCN 555 Service_Radio10
            LCN 666 Service_TV7_SD
            LCN 800++ SD_Service 2_muxA

            Ensure that the below services are removed :

            1. LCN  111 SD Service 1
            2. LCN  333 SD Service 2_muxB

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1','dektec2']

    def run(self):
        # Run TS (MYS_SIPSI_3.2a_02.ts) 474MHz
        self.dektec1.Run('MYS_SIPSI_3.2a_02.xml','MYS_SIPSI_3.2a_02.ts')
        # Run TS (MYS_SIPSI_3.2b_02.ts) 858MHz
        self.dektec2.Run('MYS_SIPSI_3.2b_02.ts','MYS_SIPSI_3.2b_02.ts')
        
        self.remote.RCPower(delay = 120)
        self.remote.RCPower(delay = 10)
        
        # LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(10)
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionASUDiffMhz['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionASUDiffMhz['IMAGENAME1'], TC.MYSClashLCNResolutionASUDiffMhz['CONFIGJSON1'], 
        testdesc='Check for MUX Addition Different MHz: Open EPG')
        self.remote.RCDown(repetition = 10, delay = 2)
        self.capture.CapturePhoto(TC.MYSClashLCNResolutionASUDiffMhz['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSClashLCNResolutionASUDiffMhz['IMAGENAME2'], TC.MYSClashLCNResolutionASUDiffMhz['CONFIGJSON2'], 
        testdesc='Check for MUX Addition Different MHz: EPG Check CHL')
        self.remote.RCEPG(delay = 2)
        
        videoname1 = 'LOGO_MYS_VCN_MYSClashLCNResolutionASUDiffMhz_LCNCheck_video'
        testdescription1 = 'Check for LCN Reso for Diff Mhz.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,222,444,555,666,800]
        for x in range (10):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        self.dektec2.StopVideo() 

class MYSMultiplexAddDelStaticAdd(DefaultTestCase):
    """
    3.3.1
    Multiplex addition and deletion, static addition

    Steps:
        [1] Static Multiplex Addition
        [2] Play out MYS_SIPSI_3.3a.ts and perform receiver auto scan. 
        [3] Capture image for initial EPG
        [4] Record video for lcn check

    Expectation:
        [1] A total of 6 services shall be presented as follows in ascending order:
            LCN 001 - TV1
            LCN 002 - TV2
            LCN 003 - TV3
            LCN 004 - TV4
            LCN 005 - TV5
            LCN 006 - Radio6


            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

            Using numerical keys, press '001'  to enter LCN 001 TV1. 
            'Flowers' video and  'Guitar Solo' audio shall be presented. 

            Commence following test from LCN001  TV1.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.3a.ts)
        self.dektec1.Run('MYS_SIPSI_3.3a.xml','MYS_SIPSI_3.3a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDelStaticAdd['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDelStaticAdd['IMAGENAME1'], TC.MYSMultiplexAddDelStaticAdd['CONFIGJSON1'], 
        testdesc='Check for Multiplex Add Del Static Add: Open EPG')
        self.remote.RCDown(repetition = 5, delay = 2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDelStaticAdd['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDelStaticAdd['IMAGENAME2'], TC.MYSMultiplexAddDelStaticAdd['CONFIGJSON2'], 
        testdesc='Check for Multiplex Add Del Static Add: EPG Chl Check')
        self.remote.RCEPG(delay = 2)
        
        videoname1 = 'LOGO_MYS_VCN_MYSMultiplexAddDelStaticAdd_LCNCheck_video'
        testdescription1 = 'Check for LCN Multiplex static addition.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,3,4,5,6]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # LCN 1
        self.brctfx.numeric_keys(1) 

class MYSMultiplexAddDelSimultaneous(DefaultTestCase):
    """
    3.3.2
    Stop MYS_SIPSI_3.3a.ts and play out MYS_SIPSI_3.3a_mux.ts and MYS_SIPSI_3.3b_mux.ts simultaneously.

    Steps:
        [1] Stop MYS_SIPSI_3.3a.ts and play out MYS_SIPSI_3.3a_mux.ts and MYS_SIPSI_3.3b_mux.ts simultaneously.
        [2] Capture image for epg
        [3] Make picture judgement for each item
        [4] Record video to do lcn check 

    Expectation:
        [1] Perform receiver method of network configuration update.
            (Note: Do not perform receiver autoscan.)

            A total of 10 services shall be presented as follows in ascending order:
            LCN 001 - TV1
            LCN 002 - TV2
            LCN 003 - TV3
            LCN 004 - TV4
            LCN 005 - TV5
            LCN 006 - Radio6
            LCN 100 - TV11
            LCN 200 - TV_12
            LCN 501 - TV_15
            LCN 502 - Radio 17

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

            Using numerical keys, press '001'  to enter LCN 001 TV1. 
            'Flowers' video and  'Guitar Solo' audio shall be presented. 

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1','dektec2']

    def run(self):
        # Run TS (MYS_SIPSI_3.3a_mux.ts)
        self.dektec1.Run('MYS_SIPSI_3.3a_mux.xml','MYS_SIPSI_3.3a_mux.ts')
        # Run TS (MYS_SIPSI_3.3b_mux.ts)
        self.dektec2.Run('MYS_SIPSI_3.3b_mux.xml','MYS_SIPSI_3.3b_mux.ts')
        
        self.remote.RCPower(delay = 120)
        self.remote.RCPower(delay = 10)
        
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDelSimultaneous['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDelSimultaneous['IMAGENAME1'], TC.MYSMultiplexAddDelSimultaneous['CONFIGJSON1'], 
        testdesc='Check for add mux simultaneous: Open EPG')
        self.remote.RCDown(repetition=10, delay=2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDelSimultaneous['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDelSimultaneous['IMAGENAME2'], TC.MYSMultiplexAddDelSimultaneous['CONFIGJSON2'], 
        testdesc='Check for add mux simultaneous: Check Channel in EPG')
        self.remote.RCEPG(delay = 2) 

        videoname1 = 'LOGO_MYS_VCN_MYSMultiplexAddDelSimultaneous_LCNCheck_video'
        testdescription1 = 'Check for LCN Simultaneous TS play.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,3,4,5,6,100,200,501,502]
        for x in range (10):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        self.dektec2.StopVideo()
        
        # LCN 1
        self.brctfx.numeric_keys(1)

class MYSMultiplexAddDel474Mhz(DefaultTestCase):
    """
    3.3.3
    Next, stop above streams and play out MYS_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan.

    Steps:
        [1] Next, stop above streams and play out MYS_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan.
        [2] Capture image for epg
        [3] Make picture judgement for each item
        [4] Record video to do lcn check 

    Expectation:
        [1]  A total of 6 services shall be presented as follows in ascending order:
            LCN001 - TV1
            LCN002 - TV2
            LCN 003 - TV3
            LCN 004 - TV4
            LCN 005 - TV5
            LCN 006 - Radio6

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.3a.ts) 474MHz
        self.dektec1.Run('MYS_SIPSI_3.3a.xml','MYS_SIPSI_3.3a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDel474Mhz['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDel474Mhz['IMAGENAME1'], TC.MYSMultiplexAddDel474Mhz['CONFIGJSON1'], 
        testdesc='Check for Mux 474MHz: Open EPG')
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDel474Mhz['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDel474Mhz['IMAGENAME2'], TC.MYSMultiplexAddDel474Mhz['CONFIGJSON2'], 
        testdesc='Check for Mux 474MHz: Check Channel in EPG')
        self.remote.RCEPG(delay = 2) 

        videoname1 = 'LOGO_MYS_VCN_MYSMultiplexAddDel474Mhz_LCNCheck_video'
        testdescription1 = 'Check for Mux 474MHz.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,3,4,5,6]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSMultiplexAddDel858Mhz(DefaultTestCase):
    """
    3.3.3
    Next, stop above streams and play out MYS_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan.

    Steps:
        [1] Next, stop above streams and play out MYS_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan.
        [2] Capture image for epg
        [3] Make picture judgement for each item
        [4] Record video to do lcn check 

    Expectation:
        [1]  A total of 6 services shall be presented as follows in ascending order:
            LCN001 - TV1
            LCN002 - TV2
            LCN 003 - TV3
            LCN 004 - TV4
            LCN 005 - TV5
            LCN 006 - Radio6

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.3a.ts) 858MHz
        self.dektec1.Run('MYS_SIPSI_3.3a.xml','MYS_SIPSI_3.3a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDel858Mhz['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDel858Mhz['IMAGENAME1'], TC.MYSMultiplexAddDel858Mhz['CONFIGJSON1'], 
        testdesc='Check for Mux 858MHz: Open EPG')
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.MYSMultiplexAddDel858Mhz['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSMultiplexAddDel858Mhz['IMAGENAME2'], TC.MYSMultiplexAddDel858Mhz['CONFIGJSON2'], 
        testdesc='Check for Mux 858MHz: Check Channel in EPG')
        self.remote.RCEPG(delay = 2) 

        videoname1 = 'LOGO_MYS_VCN_MYSMultiplexAddDel858MHz_LCNCheck_video'
        testdescription1 = 'Check for Mux 858MHz.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,3,4,5,6]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSServiceEventUpdateLCN120(DefaultTestCase):
    """
    3.4.1 
    Check for service and event update after an interval for LCN 120

    Steps:
        [1] Play out MYS_SIPSI_3.5.ts and perform receiver auto scan. 
        [2] Record video for service and event update  

    Expectation:
        [1] Using numerical keys, press '120' to enter LCN120 .

            At interval 0::60s, 'Village' video with  'keyboard' audio  shall be presented.
            Ensure no juddering or erraneous effects in components during presentation. 

            At interval 61::180s, audio and video shall stop. Receiver may optionally freeze the last image of the video during this interval. 

            Note: Receiver shall handle clean transitions into and out of the active and inactive states during the interval 60-61s.
        
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']
    
    def run(self):
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        # LCN 120
        self.brctfx.numeric_keys(120)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')

        videoname1 = 'LOGO_MYS_VCN_ServiceUpdate_LCN120_video'
        testdescription1 = 'Check for Service Update LCN 120:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        time.sleep(180)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1)) 

class MYSServiceEventUpdateLCN131(DefaultTestCase):
    """
    3.4.2
    Check for service and event update after an interval for LCN 131

    Steps:
        [1] Play out MYS_SIPSI_3.5.ts and perform receiver auto scan. 
        [2] Record video for service and event update  

    Expectation:
        [1] Using numerical keys, press '131' to enter LCN131  MYS_TV 200.

            At interval 0::60s, no components shall be presented.

            At interval 61::180s,  'Park' video with 'Bell rings' audio shall be presented.
            Ensure no juddering or erraneous effects in components during presentation. 

            Note: Receiver shall handle clean transitions into and out of the active and inactive states during the interval 60-61s.
        
    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        # LCN 131
        self.brctfx.numeric_keys(131)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')

        videoname1 = 'LOGO_MYS_VCN_ServiceUpdate_LCN131_video'
        testdescription1 = 'Check for Service Update LCN 131:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        time.sleep(180)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSServiceEventUpdateLCN555(DefaultTestCase):
    """
    3.3.3
    Check for service and event update after an interval for LCN 555

    Steps:
        [1] Play out MYS_SIPSI_3.5.ts and perform receiver auto scan. 
        [2] Record video for service and event update  

    Expectation:
        [1] Using numerical keys, press '555' to enter LCN555  TV 555. 
            Press'Info' key to view 'Now' and 'Next' event information at banner and optionally at other user interface.
            Ensure the event information are as in expectations below and take note of the changes of this information at interval 61s.

            At interval 0::60s,  present event information are as follows:
            Event Name : News at TV1
            Event Start/End Time: 9-April,  5:30 PM - 6:30 PM
            Event Description: News programme on air.
            Rating: Not defined

            At interval 61s, receiver shall detect version change in event p/f and event p/f information shall be updated accordingly.
            Present event information during  interval 61::180s shall be presented as follows:
            Event Name : Movie programme
            Event Start/End Time: 9-April, 6:30 PM - 8:00 PM
            Event Description: Movie programme on air.
            Rating: Not defined

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        # LCN 555
        self.brctfx.numeric_keys(555)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (MYS_SIPSI_3.5.ts)
        self.dektec1.Run('MYS_SIPSI_3.5.xml','MYS_SIPSI_3.5.ts')

        videoname1 = 'LOGO_MYS_VCN_ServiceUpdate_LCN555_video'
        testdescription1 = 'Check for Service Update LCN 555:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        for a in range(8):
            self.remote.RCBanner(delay = 3)
            self.remote.RCRight(delay = 2)
            self.remote.RCEPG(delay = 5)
            self.remote.RCSelect(repetition=2, delay=5)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSCharEventPF(DefaultTestCase): 
    """
    4.1.1-4.1.14
    Check for event pf for each lcn

    Steps:
        [1] Play out stream MYS_SIPSI_CHAR_4a.ts 
            and perform receiver auto scan method. 
            Enter each service.
        [2] Using numerical keys, press '100' to enter service LCN 100 Test 1 : Normal Encoding Character. 
            Access the banner and guide to view the present (now) event information.  
        [3] Capture image at the banner and make picture judgement
        [4] Record video for lcn check
        [5] Repeat steps [1]-[4] for LCN 101 and 102

    Expectation:
        [1] Ensure all services are populated correctly as in expectation. Ensure services are accessible via numerical keys. 
            Confirm correct service name and LCN numbering in each service 

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(5)
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME1'], TC.MYSCharEventPF['CONFIGJSON1'], 
        testdesc='Check for Character in event TS: Open EPG')
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_MYS_VCN_LCN_CHECK_CHAR_4a_video'
        testdescription1 = 'Check for LCN in Char 4a TS:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102]
        for x in range (3):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME2'], TC.MYSCharEventPF['CONFIGJSON2'], 
        testdesc='(LCN100) Check for Character in event TS: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME3'], TC.MYSCharEventPF['CONFIGJSON3'], 
        testdesc='(LCN100) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME4'], TC.MYSCharEventPF['CONFIGJSON4'], 
        testdesc='(LCN100) Check for Character in event TS: Display event infomation')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME5'], TC.MYSCharEventPF['CONFIGJSON5'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event ')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME6'], TC.MYSCharEventPF['CONFIGJSON6'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event infomation')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME7'], TC.MYSCharEventPF['CONFIGJSON7'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event infomation on banner') #TODO: Have burst check config
        
        # LCN 101
        self.brctfx.numeric_keys(101)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME8'], TC.MYSCharEventPF['CONFIGJSON8'], 
        testdesc='(LCN101) Check for Character in event TS: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME9'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME9'], TC.MYSCharEventPF['CONFIGJSON9'], 
        testdesc='(LCN101) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME10'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME10'], TC.MYSCharEventPF['CONFIGJSON10'], 
        testdesc='(LCN101) Check for Character in event TS: Display EPG Information')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME11'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME11'], TC.MYSCharEventPF['CONFIGJSON11'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME12'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME12'], TC.MYSCharEventPF['CONFIGJSON12'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next EPG Information')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME13'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME13'], TC.MYSCharEventPF['CONFIGJSON13'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next Banner')

        # LCN 102
        self.brctfx.numeric_keys(102)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME14'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME14'], TC.MYSCharEventPF['CONFIGJSON14'], 
        testdesc='(LCN102) Check for Character in event TS: Display Banner')
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)  
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME15'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME15'], TC.MYSCharEventPF['CONFIGJSON15'], 
        testdesc='(LCN102) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPF['IMAGENAME16'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPF['IMAGENAME16'], TC.MYSCharEventPF['CONFIGJSON16'], 
        testdesc='(LCN102) Check for Character in event TS: Display EPG Information')
        self.remote.RCEPG(delay=2)

class MYSCharEventSchedule(DefaultTestCase): 
    """
    4.2.1 - 4.2.13
    Check the event scheduling

    Steps:
        [1] Play TS MYS_SIPSI_CHAR_4a
        [2] Open EPG by the guide key
        [3] Capture image at EPG and make judgement for the character inside the banner 
        [4] Record video for the toogle button testing

    Expectation:
        [1] EPG is able to be presented when Guide key is pressed. 
        [2] 8 days of Event Schedule shall be presented.
            If less than 8 days of Event Schedule is accessed, this test shall fail. 
        [3] Event Name	"Event 3 : Characters Row A-B-C" 
            Short Event Description	"¡¢£€¥§¤‘“«←↑→↓°±²³×µ¶·÷’”»¼½¾¿"
            Extended Event Description	"ÀÁÂÃĀĂÄÅĄ"
          
        [4] Event Name	"Event 4 : Characters Row D-E"
            Short Event Description	"―¹®©™♪¬¦⅛⅜⅝⅞ΩÆÐᵃĦĲĿŁØŒ⁰ÞŦŊŉ"
            Extended Event Description	"Event information is not available."
          
        [5] Event Name	"Event 5 : Characters Row F"
            Short Event Description	"ĸæđðħıĳŀłøœßþŧŋ"
            Extended Event Description	"Event information is not available."

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts')
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(101)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME1'], TC.MYSCharEventSchedule['CONFIGJSON1'], 
        testdesc='Check for Event Schedule: Display EPG')

        # 4.2.5 - 4.2.13
        self.remote.RCRight(repetition = 4)
        time.sleep(2)
        # Start capturing photo (Event 3)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME2'], TC.MYSCharEventSchedule['CONFIGJSON2'], 
        testdesc='Check for Event Schedule: Display EPG Event 3')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME3'], TC.MYSCharEventSchedule['CONFIGJSON3'], 
        testdesc='Check for Event Schedule: Display EPG Information Event 3')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 6)
        time.sleep(2)
        # Start capturing photo (Event 4)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME4'], TC.MYSCharEventSchedule['CONFIGJSON4'], 
        testdesc='Check for Event Schedule: Display EPG Event 4')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME5'], TC.MYSCharEventSchedule['CONFIGJSON5'], 
        testdesc='Check for Event Schedule: Display EPG Information Event 4')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 8)
        time.sleep(2)
        # Start capturing photo (Event 5)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME6'], TC.MYSCharEventSchedule['CONFIGJSON6'], 
        testdesc='Check for Event Schedule: Display EPG Event 5')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventSchedule['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventSchedule['IMAGENAME7'], TC.MYSCharEventSchedule['CONFIGJSON7'], 
        testdesc='Check for Event Schedule: Display EPG Event 5')
        self.remote.RCEPG(delay=2)

        # 4.2.4
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4a.xml','MYS_SIPSI_CHAR_4a.ts'),time.sleep(3)
        videoname1 = 'LOGO_MYS_VCN_Button_Toggle_For_EPG_video'
        testdescription1 = 'Check for Button toggle in EPG:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCEPG(delay=2)
        self.remote.RCUp(delay=2)
        self.remote.RCDown(delay=2)
        self.remote.RCRight(repetition = 3, delay=2)
        self.remote.RCLeft(repetition = 2, delay=2)
        self.remote.RCEPG(delay=2)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class MYSCharEventPFHuffman(DefaultTestCase): 
    """
    4.3.1-4.3.14
    Check for event pf for each lcn to check huffman encoding

    Steps:
        [1] Play out stream MYS_SIPSI_CHAR_4b.ts 
            and perform receiver auto scan method. 
            Enter each service.
        [2] Using numerical keys, press '100' to enter service LCN 100 Test 1 : Normal Encoding Character. 
            Access the banner and guide to view the present (now) event information.  
        [3] Capture image at the banner and make picture judgement
        [4] Record video for lcn check
        [5] Repeat steps [1]-[4] for LCN 101 and 102

    Expectation:
        [1] Ensure all services are populated correctly as in expectation. Ensure services are accessible via numerical keys. 
            Confirm correct service name and LCN numbering in each service 

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(5)
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME1'], TC.MYSCharEventPFHuffman['CONFIGJSON1'], 
        testdesc='Check for Character in event TS Huffman: Open EPG')
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_MYS_VCN_LCN_CHECK_CHAR_4a_video'
        testdescription1 = 'Check for LCN in Char 4a TS:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102]
        for x in range (3):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,  
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME2'], TC.MYSCharEventPFHuffman['CONFIGJSON2'], 
        testdesc='(LCN100) Check for Character in event TS: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME3'], TC.MYSCharEventPFHuffman['CONFIGJSON3'], 
        testdesc='(LCN100) Check for Character in event TS Huffman: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME4'], TC.MYSCharEventPFHuffman['CONFIGJSON4'], 
        testdesc='(LCN100) Check for Character in event TS Huffman: Display event infomation')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME5'], TC.MYSCharEventPFHuffman['CONFIGJSON5'], 
        testdesc='(LCN100) Check for Character in event TS Huffman: Display next event ')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME6'], TC.MYSCharEventPFHuffman['CONFIGJSON6'], 
        testdesc='(LCN100) Check for Character in event TS Huffman: Display next event infomation')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME7'], TC.MYSCharEventPFHuffman['CONFIGJSON7'], 
        testdesc='(LCN100) Check for Character in event TS Huffman: Display next event infomation on banner') #TODO: Have burst check config
        
        # LCN 101
        self.brctfx.numeric_keys(101)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME8'], TC.MYSCharEventPFHuffman['CONFIGJSON8'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME9'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME9'], TC.MYSCharEventPFHuffman['CONFIGJSON9'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME10'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME10'], TC.MYSCharEventPFHuffman['CONFIGJSON10'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display EPG Information')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME11'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME11'], TC.MYSCharEventPFHuffman['CONFIGJSON11'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display Next EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME12'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME12'], TC.MYSCharEventPFHuffman['CONFIGJSON12'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display Next EPG Information')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME13'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME13'], TC.MYSCharEventPFHuffman['CONFIGJSON13'], 
        testdesc='(LCN101) Check for Character in event TS Huffman: Display Next Banner')

        # LCN 102
        self.brctfx.numeric_keys(102)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME14'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME14'], TC.MYSCharEventPFHuffman['CONFIGJSON14'], 
        testdesc='(LCN102) Check for Character in event TS Huffman: Display Banner')
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)  
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME15'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME15'], TC.MYSCharEventPFHuffman['CONFIGJSON15'], 
        testdesc='(LCN102) Check for Character in event TS Huffman: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.MYSCharEventPFHuffman['IMAGENAME16'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventPFHuffman['IMAGENAME16'], TC.MYSCharEventPFHuffman['CONFIGJSON16'], 
        testdesc='(LCN102) Check for Character in event TS Huffman: Display EPG Information')
        self.remote.RCEPG(delay=2)

class MYSCharEventScheduleHuffman(DefaultTestCase): 
    """
    4.4.1 - 4.2.7
    Check the event scheduling for huffman

    Steps:
        [1] Play TS MYS_SIPSI_CHAR_4b
        [2] Open EPG by the guide key
        [3] Capture image at EPG and make judgement for the character inside the banner 
        [4] Record video for the toogle button testing

    Expectation:
        [1] EPG is able to be presented when Guide key is pressed. 
        [2] 8 days of Event Schedule shall be presented.
            If less than 8 days of Event Schedule is accessed, this test shall fail. 
        [3] Event Name	"Event 3 : Huffman EPG 1" 
            Short Event Description	"Zebras have many black stripes. It is said that they come from a species of the African horse family. 
                                    This text should display in the EPG with Huffman Encoding implemented."
          
        [4] Event Name	"Event 4 : Huffman EPG 2"
            Short Event Description	"In 1987, statistics show that 43 percent of people in the world aged between 18 to 35 smoke 25 cigarettes per day.
                                     This text should display in the EPG with Huffman Encoding implemented."
              
        [5] Event Name	"Event 5 : Huffman EPG 3"
            Short Event Description	"The boy wore a red shirt. He was seen strolling in the zoo while feeding the flamingoes and ducklings.
                                    This text should display in the EPG with Huffman Encoding implemented."

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts')
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(101)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME1'], TC.MYSCharEventScheduleHuffman['CONFIGJSON1'], 
        testdesc='Check for Event Schedule Huffman: Display EPG')

        # 4.2.5 - 4.2.13
        self.remote.RCRight(repetition = 4)
        time.sleep(2)
        # Start capturing photo (Event 3)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME2'], TC.MYSCharEventScheduleHuffman['CONFIGJSON2'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Event 3')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME3'], TC.MYSCharEventScheduleHuffman['CONFIGJSON3'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Information Event 3')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 6)
        time.sleep(2)
        # Start capturing photo (Event 4)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME4'], TC.MYSCharEventScheduleHuffman['CONFIGJSON4'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Event 4')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME5'], TC.MYSCharEventScheduleHuffman['CONFIGJSON5'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Information Event 4')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4b.xml','MYS_SIPSI_CHAR_4b.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 8)
        time.sleep(2)
        # Start capturing photo (Event 5)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME6'], TC.MYSCharEventScheduleHuffman['CONFIGJSON6'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Event 5')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.MYSCharEventScheduleHuffman['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.MYSCharEventScheduleHuffman['IMAGENAME7'], TC.MYSCharEventScheduleHuffman['CONFIGJSON7'], 
        testdesc='Check for Event Schedule Huffman: Display EPG Event 5')
        self.remote.RCEPG(delay=2)

class MYSHuffmanMalay(DefaultTestCase): 
    """
    4.5.1 - 4.5.4
    Play out stream MYS_CHAR_4c.ts and perform receiver auto scan method. 
    Enter service.

    Steps:
        [1] Play TS MYS_SIPSI_CHAR_4c
        [2] Using numerical keys, press '100' to enter service LCN 100 Huffman Malaysia Service . 
        [3] Access the banner and guide to access the presnt (now) event information. 
        [4] Capture banner and epg image and run picture judgement

    Expectation:
        [1] Event Name	"Huffman Bahasa Malaysia"
        [2] Short Event Description	:Ikuti berita yang memaparkan perkembangan terkini dan
                                     semasa termasuk berita ekonomi dan kewangan. 
                                     Rancangan khas khusus untuk tontonan anda persembahan daripada TV6.
                                     Berhibur dengan kumpulan muzik tempatan dengan pilihan lagu-lagu.

            Note: Some truncation might occur.
            
        [3] Extended Event Description	Istimewa Bersama Zaidi Zainal yang menyampaikan lagu-lagu popularnya. 
                                        Saksikan Rentak Juara 2010 Konsert  Peringkat Akhir untuk hiburan
                                        semua hanya di TV6. Nikmati klip-klip video tempatan pilihan
                                        peminat yang terdiri daripada pelbagai kaum dan etnik.

            Note: Some truncation might occur.


    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA 
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4c.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4c.xml','MYS_SIPSI_CHAR_4c.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSHuffmanMalay['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanMalay['IMAGENAME1'], TC.MYSHuffmanMalay['CONFIGJSON1'], 
        testdesc='Check for LCN 100 Huffman Malaysia Service: Display Banner') #TODO: HAve burst check config
        self.dektec1.StopVideo(),time.sleep(3)
        self.dektec1.Run('MYS_SIPSI_CHAR_4c.xml','MYS_SIPSI_CHAR_4c.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSHuffmanMalay['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanMalay['IMAGENAME2'], TC.MYSHuffmanMalay['CONFIGJSON2'], 
        testdesc='Check for LCN 100 Huffman Malaysia Service: Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.MYSHuffmanMalay['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanMalay['IMAGENAME3'], TC.MYSHuffmanMalay['CONFIGJSON3'], 
        testdesc='Check for LCN 100 Huffman Malaysia Service: Display EPG Information')
        self.remote.RCEPG(delay=2) 

class MYSHuffmanESC(DefaultTestCase):
    """
    4.6.1-4.6.5
    Check the event Event names for huffman with ESC Character

    Steps:
        [1] Play out stream MYS_CHAR_4f.ts and perform receiver auto scan method. 
            Enter service.
        [2] Using numerical keys, press '100' to enter service LCN 100 Test 1 : Huffman Malaysia Service. 
        [3] Access the banner and guide to view the present (now)event information. 
        [4] Access the following events on the banner.
        [5] Capture image and make picture judgement 

    Expectation:
        [1] Event Name	"Huffman Bahasa Malaysia"
        [2] Short  Event Description	"RM10 adalah bersamaan dengan £2.05 atau ¥278.34"
        [3] Event Name	"Huffman English"
        [4] Short  Event Description	"RM10 adalah bersamaan dengan £2.05 atau ¥278.34"

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_CHAR_4f.ts)
        self.dektec1.Run('MYS_CHAR_4f.xml','MYS_CHAR_4f.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        # LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME1'], TC.MYSHuffmanESC['CONFIGJSON1'], 
        testdesc='Check for Huffman ESC Character: Display Banner')
        # stop dektec1
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (MYS_CHAR_4f.ts)
        self.dektec1.Run('MYS_CHAR_4f.xml','MYS_CHAR_4f.ts'),time.sleep(5)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME2'], TC.MYSHuffmanESC['CONFIGJSON2'], 
        testdesc='Check for Huffman ESC Character: Display EPG')
        self.remote.RCSelect(delay = 3)
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME3'], TC.MYSHuffmanESC['CONFIGJSON3'], 
        testdesc='Check for Huffman ESC Character: Event Information')
        self.remote.RCBack(delay = 2)
        self.remote.RCRight(delay = 2)
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME4'], TC.MYSHuffmanESC['CONFIGJSON4'], 
        testdesc='Check for Huffman ESC Character: Display EPG Next')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME5'], TC.MYSHuffmanESC['CONFIGJSON5'], 
        testdesc='Check for Huffman ESC Character: Display EI Next')
        self.remote.RCEPG(delay = 2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay = 2)
        # Start capturing photo
        self.capture.CapturePhoto(TC.MYSHuffmanESC['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.MYSHuffmanESC['IMAGENAME6'], TC.MYSHuffmanESC['CONFIGJSON6'], 
        testdesc='Check for Huffman ESC Character: Display Banner Next')

class MYSNoTableDefinition(DefaultTestCase): 
    """
    4.7.1 - 4.7.3
    Test for EPG with no table definition

    Steps:
        [1] Play out stream MYS_SIPSI_CHAR_4d.ts 
            and perform receiver auto scan method. 
        [2] Using numerical keys, press '100' to access LCN 100 Test 1 : No Character Table  
        [3] Capture image of the banner and epg  
        [4] Call Picture Judgement API 

    Expectation:
        [1] Event Name	"Event 1 : No Table Defined"
            Short Event Description:
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz.!#$%&'()*+,-./:;<=>?[]^_@{|}~ ¡¢£€¥§¤‘“«
            ←↑→↓°±²³×µ¶·÷’”»¼½¾¿ÀÁÂÃĀĂÄÅĄ¹®©™♪¬¦⅛⅝⅞ΩÆÐᵃĲĿŁØŒ⁰ÞŦŊŉĸæđðħıĳŀłøœßþŧŋ"
 
    Node Pre-requisite:
        [1] Dual Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_CHAR_4d.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4d.xml','MYS_SIPSI_CHAR_4d.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSNoTableDefinition['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSNoTableDefinition['IMAGENAME1'], TC.MYSNoTableDefinition['CONFIGJSON1'], 
        testdesc='Check for No table definition: Display Banner') #TODO: Burst
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (MYS_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('MYS_SIPSI_CHAR_4d.xml','MYS_SIPSI_CHAR_4d.ts')    
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.MYSNoTableDefinition['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSNoTableDefinition['IMAGENAME2'], TC.MYSNoTableDefinition['CONFIGJSON2'], 
        testdesc='Check for No table definition: Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.MYSNoTableDefinition['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSNoTableDefinition['IMAGENAME3'], TC.MYSNoTableDefinition['CONFIGJSON3'], 
        testdesc='Check for No table definition: Display EPG Information')
        self.remote.RCEPG(delay=2)

class MYSAFDTest(DefaultTestCase):
    """
    5.1.1
    Test for AFD

    Steps:
        [1] Play out stream MYS_SIPSI_AFD.ts and perform receiver auto scan method
            Note: Configure the receiver screen setting to display the video as coded frame.
        [2] Capture image of the banner inside the AFD test
        [3] Call Picture Judgement API 

    Expectation:
        [1] A set of screen is required to pass this test, refer checksheet 

    Node Pre-requisite:
        [1] One Dektec 
        [2] No-network 

    SW Pre-requisite:
        [1] Software must be PA
    """
    def __init__(self, **optional):
        self.test_case_dependent_on = None 
        self.supported_projects = ['all'] 
        self.supported_regions = [CN.STR_PA] 
        self.supported_country = ['all'] 
        self.supported_categories = None 
        self.required_hws = ['dektec1']

    def run(self):
        # Run TS (MYS_SIPSI_AFD.ts)
        self.dektec1.Run('MYS_SIPSI_AFD.xml','MYS_SIPSI_AFD.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay = 2)
         
        self.capture.CapturePhoto(TC.MYSAFDTest['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.MYSAFDTest['IMAGENAME1'], TC.MYSAFDTest['CONFIGJSON1'], 
        testdesc='Check for MYS AFD Test: Open EPG')
    
        self.remote.RCEPG(delay = 2)
        self.remote.RCMove(UIC.UI_DTV, UIC.UI_HSWIDEMODE, moreoption=[UIC.UIAUTO], delay=2)
        self.remote.RCMove(UIC.UI_HSWIDEMODE, UIC.UI_HS43DEFAULT, moreoption=[UIC.UINORMAL], delay=2)
        self.brctfx.viewing_tvapp()

        # LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSAFDTest['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.MYSAFDTest['IMAGENAME2'], TC.MYSAFDTest['CONFIGJSON2'], 
        testdesc='(LCN 100) Check for MYS AFD Test: Display Banner')
        # LCN 200
        self.brctfx.numeric_keys(200)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSAFDTest['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.MYSAFDTest['IMAGENAME3'], TC.MYSAFDTest['CONFIGJSON3'], 
        testdesc='(LCN 200) Check for MYS AFD Test: Display Banner')
        # LCN 300
        self.brctfx.numeric_keys(300)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.MYSAFDTest['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.MYSAFDTest['IMAGENAME4'], TC.MYSAFDTest['CONFIGJSON4'], 
        testdesc='(LCN 300) Check for MYS AFD Test: Display Banner')


###----------- Test Case Classes Ends -------------###


###----------- Script Execution -------------###
if STATION_INFO['env'] == 'dev':
    TestExecution(DefaultTestCase).main()
