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
from testscript.broadcast import logo_uae_sipsi_config as TC

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
                        'TestCase1': UAEDigitalTuningLCNCheck,
                        'TestCase2': UAEDigitalEventInformation,
                        'TestCase3': UAECodecInformation,
                        'TestCase4': UAEAudSubtitle,
                        'TestCase5': UAEParentalLock,
                        'TestCase6': UAEBroadcastMixedAudio,
                        'TestCase7': UAELCNV1Descriptors,
                        'TestCase8': UAELCNZeroDescriptors,
                        'TestCase9': UAEAddDelLCNCheck,
                        'TestCase10': UAEAddDelAddService,
                        'TestCase11': UAEAddDelNormalService,
                        'TestCase12': UAEAddDelDeleteService,
                        'TestCase13': UAEClashLCNSimultaneous,
                        'TestCase14': UAEClashLCNMuxInitial,
                        'TestCase15': UAEClashLCNMuxAfter,
                        'TestCase16': UAEMuxAddDelInitial,
                        'TestCase17': UAEMuxAddDelSimultaneous,
                        'TestCase18': UAEMuxAddDelChlDel474,
                        'TestCase19': UAEMuxAddDelChlDel858,
                        'TestCase20': UAEServiceLCNUpdate,
                        'TestCase21': UAEServiceEventUpdate120,
                        'TestCase22': UAEServiceEventUpdate131,
                        'TestCase23': UAEServiceEventUpdate555,
                        'TestCase24': UAECharEventPF,
                        'TestCase25': UAECharEventSchedule,
                        'TestCase26': UAENoTableDefinition,
                        'TestCase27': UAELatinTable1,
                        'TestCase28': UAELatinTable2,
                        'TestCase29': UAEAFDTest
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
                    self.brctfx.return_to_ootb_condition(country=UIC.UI_FGCC)
            try:
                self.ac_netswitch.off()
            except:
                self.SYS_LOG.debug('No network found')


###----------- Test Case Classes Starts -------------###

class UAEDigitalTuningLCNCheck(DefaultTestCase): 
    """
    Playout digital tuning and perform lcn check

    Steps:
            1) Perform factory data reset, country selection: UAE(GCC)
            2) Play out UAE_SIPSI_1a.ts and perform receiver full scan.
            3) Enter each service and ensure that all of them are accessible via numerical keys. 
            4) Confirm the correct service name and LCN numbering in each service. 
            5) Check the clock information.
            6) Capture image banner for each channel.

    Expectation:
        [1] Observe the Service Name and LCN Numbering for each service in the service list and ensure that they are correctly
            arranged in an ascending order.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1'] 
        self.tc_timeout=60

    def run(self):      
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.brctfx.digital_auto_tuning() 
        self.brctfx.viewing_tvapp(pincode=TC.Init['SETUPPIN'])

        # Enter LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME1'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON1'], 
        testdesc='Check for service name and LCN: LCN100')

        # Enter LCN 101
        self.brctfx.numeric_keys(101)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME2'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON2'], 
        testdesc='Check for service name and LCN: LCN101')
                
        # Enter LCN 102
        self.brctfx.numeric_keys(102)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME3'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON3'], 
        testdesc='Check for service name and LCN: LCN102')
        
        # Enter LCN 103
        self.brctfx.numeric_keys(103)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME4'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON4'], 
        testdesc='Check for service name and LCN: LCN103')
                
        # Enter LCN 104
        self.brctfx.numeric_keys(104)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME5'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON5'], 
        testdesc='Check for service name and LCN: LCN104')
                
        # Enter LCN 105
        self.brctfx.numeric_keys(105)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME6'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON6'], 
        testdesc='Check for service name and LCN: LCN105')
                
        # Enter LCN 107
        self.brctfx.numeric_keys(107)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalTuningLCNCheck['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalTuningLCNCheck['IMAGENAME7'], TC.UAEDigitalTuningLCNCheck['CONFIGJSON7'], 
        testdesc='Check for service name and LCN: LCN106')

        # Enter LCN 100        
        videoname = 'LOGO_UAE_VCN_CheckEPG_video'
        testdescription = 'Check for EPG after LCN input:'
        self.capture.StartRecording(videoname), time.sleep(5)
        self.remote.RCEPG(delay=2)
        self.remote.RCDown(delay=2)
        self.remote.RCEPG(delay=2)
        self.remote.RCChannelUp(delay=3)
        self.remote.RCChannelDown(delay=3) 
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname,
                                                testdesc = testdescription +
                                                self.video_hlink_gen(videoname))

class UAEDigitalEventInformation(DefaultTestCase): 
    """
    Playout digital tuning and perform lcn check

    Steps:
            1) Play out UAE_SIPSI_1a.ts
            2) Enter LCN 100, then access banner, EPG and event description of now and next program.
            3) Enter LCN 101, then access banner, EPG and event description of now program.
            4) Enter LCN 102, then access banner, EPG and event description of now program.
            5) Enter LCN 103, then access banner, EPG and event description of now program.
            6) Enter LCN 104, then access banner, EPG and event description of now program.

    Expectation:
        [1] Observe the details of each service is as expected.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp() 

        # Enter LCN 100
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner() 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME1'], TC.UAEDigitalEventInformation['CONFIGJSON1'], 
        testdesc='Check for event description: banner initial')

        self.dektec1.StopVideo(),time.sleep(2)
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME2'], TC.UAEDigitalEventInformation['CONFIGJSON2'], 
        testdesc='Check for event description: EPG initial')

        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME3'], TC.UAEDigitalEventInformation['CONFIGJSON3'], 
        testdesc='Check for event description: EPG Select')
    
        self.remote.RCBack(delay=2)
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME4'], TC.UAEDigitalEventInformation['CONFIGJSON4'], 
        testdesc='Check for event description: EPG Next event')
        
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME5'], TC.UAEDigitalEventInformation['CONFIGJSON5'], 
        testdesc='Check for event description: EPG Select next event')
        
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2) 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME6'], TC.UAEDigitalEventInformation['CONFIGJSON6'], 
        testdesc='Check for event description: Banner next button')

        # Enter LCN 101
        self.brctfx.numeric_keys(101)
        self.brctfx.display_banner() 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME7'], TC.UAEDigitalEventInformation['CONFIGJSON7'], 
        testdesc='Check for event description: LCN101 Banner')
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME8'], TC.UAEDigitalEventInformation['CONFIGJSON8'], 
        testdesc='Check for event description: LCN101 EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME9'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME9'], TC.UAEDigitalEventInformation['CONFIGJSON9'], 
        testdesc='Check for event description: LCN101 Event Description')
        self.remote.RCEPG(delay=2)

        # Enter LCN 102
        self.brctfx.numeric_keys(102)
        self.brctfx.display_banner() 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME10'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME10'], TC.UAEDigitalEventInformation['CONFIGJSON10'], 
        testdesc='Check for event description: LCN102 Banner')
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME11'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME11'], TC.UAEDigitalEventInformation['CONFIGJSON11'], 
        testdesc='Check for event description: LCN102 EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME12'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME12'], TC.UAEDigitalEventInformation['CONFIGJSON12'], 
        testdesc='Check for event description: LCN102 Event Description')
        self.remote.RCEPG(delay=2)

        # Enter LCN 103
        self.brctfx.numeric_keys(103)
        self.brctfx.display_banner() 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME13'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME13'], TC.UAEDigitalEventInformation['CONFIGJSON13'], 
        testdesc='Check for event description: LCN103 Banner')
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME14'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME14'], TC.UAEDigitalEventInformation['CONFIGJSON14'], 
        testdesc='Check for event description: LCN103 EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME15'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME15'], TC.UAEDigitalEventInformation['CONFIGJSON15'], 
        testdesc='Check for event description: LCN103 Event Description')
        self.remote.RCEPG(delay=2)

        # Enter LCN 104
        self.brctfx.numeric_keys(104)
        self.brctfx.display_banner() 
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME16'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME16'], TC.UAEDigitalEventInformation['CONFIGJSON16'], 
        testdesc='Check for event description: LCN104 Banner')
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME17'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME17'], TC.UAEDigitalEventInformation['CONFIGJSON17'], 
        testdesc='Check for event description: LCN104 EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAEDigitalEventInformation['IMAGENAME18'])
        self.system.RunPictureJudgementProgram(TC.UAEDigitalEventInformation['IMAGENAME18'], TC.UAEDigitalEventInformation['CONFIGJSON18'], 
        testdesc='Check for event description: LCN104 Event Description')
        self.remote.RCEPG(delay=2)

class UAECodecInformation(DefaultTestCase):
    """
    Docstring for the Test Case # Change here for TC summary

    Steps:
            1) Play out UAE_SIPSI_1a.ts.
            2) Press '101' to enter service LCN 101 Service_TV2. Check video and audio component of that service.
            3) Press 100' to enter service LCN 100 Service_TV1. Check video component of that service.
            4) Play out UAE_SIPSI_1b.ts and perform receiver full scan.
            5) Press '100' to enter service LCN 100 Service_TV1. Check video and audio component of that service.
            6) Press 101' to enter service LCN 101 Service_TV2. Check video and audio component of that service.
            7) Play out UAE_SIPSI_1c.ts and perform receiver full scan.
            8) Press '100' to enter service LCN 100 Service_TV_HD1. Check video component of that service.
            9) Press 101' to enter service LCN 101 Service_TV_HD2. Check video component of that service.

    Expectation:
        [1] Observe the video and audio component of each service is as expected.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_1a)
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp()

        # Enter LCN 101        
        videoname1 = 'LOGO_UAE_VCN_VidAudComp_TS1a_LCN101_video'
        testdescription1 = '(TS1a) Check for Component of Audio and Video LCN101:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.brctfx.numeric_keys(101)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # Enter LCN 100        
        videoname2 = 'LOGO_UAE_VCN_VidAudComp_TS1a_LCN100_video'
        testdescription2 = '(TS1a) Check for Component of Audio and Video LCN100:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        self.brctfx.numeric_keys(100)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))

        # Run TS (UAE_SIPSI_1b)
        self.dektec1.Run('UAE_SIPSI_1b.xml','UAE_SIPSI_1b.ts')
        self.brctfx.digital_auto_tuning()

        # Enter LCN 100        
        videoname3 = 'LOGO_UAE_VCN_VidAudComp_TS1b_LCN100_video'
        testdescription3 = '(TS1b) Check for Component of Audio and Video LCN100:'
        self.capture.StartRecording(videoname3), time.sleep(5)
        self.brctfx.numeric_keys(101)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))
        
        # Enter LCN 101        
        videoname4 = 'LOGO_UAE_VCN_VidAudComp_TS1b_LCN101_video'
        testdescription4 = '(TS1b) Check for Component of Audio and Video LCN101:'
        self.capture.StartRecording(videoname4), time.sleep(5)
        self.brctfx.numeric_keys(100)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname4,
                                                testdesc = testdescription4 +
                                                self.video_hlink_gen(videoname4))

        # Run TS (UAE_SIPSI_1c)
        self.dektec1.Run('UAE_SIPSI_1c.xml','UAE_SIPSI_1c.ts')
        self.brctfx.digital_auto_tuning()

        # Enter LCN 100        
        videoname5 = 'LOGO_UAE_VCN_VidAudComp_TS1c_LCN100_video'
        testdescription5 = '(TS1c) Check for Component of Audio and Video LCN100:'
        self.capture.StartRecording(videoname5), time.sleep(5)
        self.brctfx.numeric_keys(101)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname5,
                                                testdesc = testdescription5 +
                                                self.video_hlink_gen(videoname5))
        
        # Enter LCN 101        
        videoname6 = 'LOGO_UAE_VCN_VidAudComp_TS1c_LCN101_video'
        testdescription6 = '(TS1c) Check for Component of Audio and Video LCN101:'
        self.capture.StartRecording(videoname6), time.sleep(5)
        self.brctfx.numeric_keys(100)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname6,
                                                testdesc = testdescription6 +
                                                self.video_hlink_gen(videoname6))

         # Run TS (UAE_SIPSI_1d.ts)
        self.dektec1.Run('UAE_SIPSI_1d.xml','UAE_SIPSI_1d.ts')
        self.brctfx.digital_auto_tuning()

        # Enter LCN 104
        videoname7 = 'LOGO_UAE_VCN_VidAudComp_TS1d_LCN104_video'
        testdescription7 = '(TS1d) Check for Component of Audio and Video LCN101:'
        self.capture.StartRecording(videoname7), time.sleep(5)
        self.brctfx.numeric_keys(104)
        time.sleep(30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname7,
                                                testdesc = testdescription7 +
                                                self.video_hlink_gen(videoname7))

class UAEAudSubtitle(DefaultTestCase):
    """
    Check for ENG and ARABIC Audio and subtitle with exchanging primary language
    and secondary language

    Steps:
            1) Play out UAE_SIPSI_1a.ts and perform receiver full scan. Set Audio Description to 'Off' (by default audio description is off). Enable Subtitles.
            2) Enter Service LCN 100 Service_TV1. 
            3) Access audio menu and select English audio.
            4) Access subtitle menu and select English subtitle.
            5) Access audio menu and select Arabic audio.
            6) Access subtitle menu and select Arabic subtitle.

    Expectation:
        [1] Observe the subtitle and audio component is as expected.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None  
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_1a.ts)
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')

        self.brctfx.digital_auto_tuning()
        self.remote.RCMove(UIC.UI_DIGITALAUTOTUNING, UIC.UI_SUBTITLE, moreoption = [UIC.UION], delay=2 )
        self.brctfx.viewing_tvapp()

        # Enter LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(5)
    
        # Start Recording 
        videoname1 = 'LOGO_UAE_VCN_AudSubtitle_Keyboard_Audio_LCN100_video'
        testdescription1 = 'Check for Keyboard audio shall be selectable when the audio selection is set to English.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCAudioMenu(delay = 2)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        
        videoname2 = 'LOGO_UAE_VCN_AudSubtitle_ENG_SUBS_LCN100_video'
        testdescription2 = 'Check for English subtitles, SIPSI Test. Subtitle 0, number…, shall be selectable when the subtitle selection is set to English.:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        self.remote.RCSubtitle(delay = 2)
        self.remote.RCDown(delay=2)
        self.remote.RCSelect(delay=15)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))

        # Enter LCN 102
        self.brctfx.numeric_keys(102)
        time.sleep(5)

        # Start Recording 
        videoname3 = 'LOGO_UAE_VCN_AudSubtitle_Drum_Audio_LCN102_video'
        testdescription3 = 'Check for Drum solo audio :'
        self.capture.StartRecording(videoname3), time.sleep(5)
        self.remote.RCAudioMenu(repetition=2, delay=2)
        self.remote.RCSelect(delay = 30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))
        
        videoname4 = 'LOGO_UAE_VCN_AudSubtitle_ENG_SUBS_LCN102_video'
        testdescription4 = 'Check for English (Eng) Hearing Impaired subtitles, SIPSI Test. Subtitle 0, number…, shall be selectable when the subtitle selection is set to English.:'
        self.capture.StartRecording(videoname4), time.sleep(5)
        self.remote.RCSubtitle(delay=2)
        self.remote.RCDown(delay=2)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname4,
                                                testdesc = testdescription4 +
                                                self.video_hlink_gen(videoname4))

        self.remote.RCMove(UIC.UI_DTV, UIC.UI_DAUDIODESCRIPTION, moreoption = [UIC.UION], delay=2 )
        self.brctfx.viewing_tvapp()

        # Start Recording 
        videoname5 = 'LOGO_UAE_VCN_AudSubtitle_GuitarBell_Mix_Audio_LCN102_video'
        testdescription5 = 'Check for Guitar Solo audio mixed with Bell Ring audio shall be manually selectable -Arabic (ARA) :'
        self.capture.StartRecording(videoname5), time.sleep(5)
        self.remote.RCAudioMenu(repetition=2, delay=2)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname5,
                                                testdesc = testdescription5 +
                                                self.video_hlink_gen(videoname5))

        videoname6 = 'LOGO_UAE_VCN_AudSubtitle_ARABIC_SUBS_LCN102_video'
        testdescription6 = 'Check for Arabic Hearing Impaired  subtitles,SIPSI Test. Subtitle 1, number… shall be manually selectable - Arabic (ARA). :'
        self.capture.StartRecording(videoname6), time.sleep(5)
        self.remote.RCSubtitle(delay=2)
        self.remote.RCDown(repetition=2, delay=1)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname6,
                                                testdesc = testdescription6 +
                                                self.video_hlink_gen(videoname6))

        self.remote.RCMove(UIC.UI_DTV, UIC.UI_DAUDIODESCRIPTION, moreoption = [UIC.UIOFF], delay=2)
        self.remote.RCMove(UIC.UI_DAUDIODESCRIPTION, UIC.UI_DAPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIENGLISH], delay=2)
        self.remote.RCMove(UIC.UI_DAPRIMARYPREFEREDLANGUAGE, UIC.UI_DASECONDARYPREFEREDLANGUAGE, moreoption = [UIC.UIARABIC], delay=2)
        self.remote.RCMove(UIC.UI_DASECONDARYPREFEREDLANGUAGE, UIC.UI_SPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIENGLISH], delay=2)         
        self.remote.RCMove(UIC.UI_SPRIMARYPREFEREDLANGUAGE, UIC.UI_SSECONDARYPREFEREDLANGUAGE, moreoption = [UIC.UIARABIC], delay=2)
        self.brctfx.viewing_tvapp()

        # Start Recording 
        videoname7 = '(1.4.7)LOGO_UAE_VCN_AudSubtitle_DrumSolo_Audio_video'
        testdescription7 = 'Check for The English - Drum Solo audio  shall be presented.:'
        self.capture.StartRecording(videoname7), time.sleep(5)
        self.remote.RCAudioMenu(delay=2)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname7,
                                                testdesc = testdescription7 +
                                                self.video_hlink_gen(videoname7))

        videoname8 = '(1.4.8)LOGO_UAE_VCN_AudSubtitle_ENG_SUBS_video'
        testdescription8 = 'Check for English subtitles,SIPSI Test. Subtitle 0, number…, subtitles shall be presented.:'
        self.capture.StartRecording(videoname8), time.sleep(5)
        self.remote.RCSubtitle(delay=2)
        self.remote.RCDown(delay=1)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname8,
                                                testdesc = testdescription8 +
                                                self.video_hlink_gen(videoname8))

        self.remote.RCMove(UIC.UI_DTV, UIC.UI_DAPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIGERMAN], delay=2)        
        self.remote.RCMove(UIC.UI_DAPRIMARYPREFEREDLANGUAGE, UIC.UI_DASECONDARYPREFEREDLANGUAGE, moreoption = [UIC.UIARABIC], delay=2)  
        self.remote.RCMove(UIC.UI_DASECONDARYPREFEREDLANGUAGE, UIC.UI_SPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIGERMAN], delay=2)         
        self.remote.RCMove(UIC.UI_SPRIMARYPREFEREDLANGUAGE, UIC.UI_SSECONDARYPREFEREDLANGUAGE, moreoption = [UIC.UIARABIC], delay=2)         
        self.brctfx.viewing_tvapp()

        # Start Recording
        videoname9 = '(1.4.9)LOGO_UAE_VCN_AudSubtitle_GuitarSolo_Audio_video'
        testdescription9 = 'The Arabic - Guitar Solo audio shall be presented.:'
        self.capture.StartRecording(videoname9), time.sleep(5)
        self.remote.RCAudioMenu(delay=2)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname9,
                                                testdesc = testdescription9 +
                                                self.video_hlink_gen(videoname9))


        videoname10 = '(1.4.10)LOGO_UAE_VCN_AudSubtitle_ARABIC_SUBS_video'
        testdescription10 = 'Check for Arabic,SIPSI Test. Subtitle 1, number…, subtitles shall be presented.:'
        self.capture.StartRecording(videoname10), time.sleep(5)
        self.remote.RCSubtitle(delay=2)
        self.remote.RCDown(delay=1)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname10,
                                                testdesc = testdescription10 +
                                                self.video_hlink_gen(videoname10))

        self.remote.RCMove(UIC.UI_DTV, UIC.UI_DAPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIENGLISH], delay=2)
        self.remote.RCMove(UIC.UI_DAPRIMARYPREFEREDLANGUAGE, UIC.UI_DASECONDARYPREFEREDLANGUAGE, moreoption = [UIC.UIENGLISH], delay=2)
        self.remote.RCMove(UIC.UI_DASECONDARYPREFEREDLANGUAGE, UIC.UI_SPRIMARYPREFEREDLANGUAGE, moreoption = [UIC.UIENGLISH], delay=2)
        self.remote.RCMove(UIC.UI_SPRIMARYPREFEREDLANGUAGE,UIC.UI_SSECONDARYPREFEREDLANGUAGE , moreoption = [UIC.UIENGLISH], delay=2)
        self.brctfx.viewing_tvapp()

class UAEParentalLock(DefaultTestCase):
    """
    Check for UAE Parental Lock

    Steps:
            1) Play out UAE_SIPSI_1a.ts and perform receiver full scan.
               Disable the parental rating function.
            2) Set Parental Rating to 9. 
            3) Set Parental Rating to 11.
            4) Set Parental Rating to 15.
            5) Set Parental Rating to 18.

    Expectation:
        [1] Observe the blocked channel with the parental lock

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_1a.ts)
        self.dektec1.Run('UAE_SIPSI_1a.xml','UAE_SIPSI_1a.ts')
        self.brctfx.viewing_tvapp(), time.sleep(3)
                
        # No Parental Lock
        self.brctfx.numeric_keys(100)
        time.sleep(5)
        
        # Start Recording
        videoname1 = 'LOGO_UAE_VCN_ParentalLock_LCNCheck_All_Channel_Viewable_video'
        testdescription1 = 'Check for all programs in all services shall be viewable.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        time.sleep(10)
        self.remote.RCUp(repetition= 6,  delay=10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # PR9
        self.brctfx.numeric_keys(100)
        time.sleep(5)
        
        self.remote.RCMove(UIC.UI_DTV, UIC.UI_PARENTALONOFF, moreoption=[UIC.UION], pincode=TC.Init['SETUPPIN'])
        self.remote.RCMove(UIC.UI_PARENTALONOFF, UIC.UI_PR9, moreoption=[UIC.UIBLOCKED], pincode=TC.Init['SETUPPIN'])
        self.brctfx.viewing_tvapp()
        
        # Start Recording
        videoname2 = 'LOGO_UAE_VCN_ParentalLock_LCNCheck_PR9_video'
        testdescription2 = 'Check for All programs in all services shall be blocked while Service_TV1, Service_Radio 1 and Service_TV6 shall be viewable.:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        time.sleep(10)
        self.remote.RCChannelUp(repetition=6, delay=10)
        self.remote.RCUp(repetition=6, delay=10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))

        # PR11
        self.brctfx.numeric_keys(100)
        time.sleep(5)
        
        self.remote.RCMove(UIC.UI_DTV , UIC.UI_NONE , moreoption=[UIC.UIBLOCKED], pincode=TC.Init['SETUPPIN'], delay=2)
        self.remote.RCMove(UIC.UI_NONE , UIC.UI_PR11 , moreoption=[UIC.UIBLOCKED], delay=2)
        self.brctfx.viewing_tvapp()
        
        # Start Recording
        videoname3 = 'LOGO_UAE_VCN_ParentalLock_LCNCheck_PR11_video'
        testdescription3 = 'Check for all programs in all services shall be blocked while Service_TV1, Service_TV2, Service_Radio 1 and Service_TV6 are viewable.:'
        self.capture.StartRecording(videoname3), time.sleep(5)
        time.sleep(10)
        self.remote.RCUp(repetition= 6,  delay=10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))

        # PR 15
        self.brctfx.numeric_keys(100)
        time.sleep(5)
        
        self.remote.RCMove(UIC.UI_DTV , UIC.UI_NONE, moreoption=[UIC.UIBLOCKED], pincode=TC.Init['SETUPPIN'], delay=2)
        self.remote.RCMove(UIC.UI_NONE , UIC.UI_PR15 , moreoption=[UIC.UIBLOCKED])
        self.brctfx.viewing_tvapp()
        
        # Start Recording
        videoname4 = 'LOGO_UAE_VCN_ParentalLock_LCNCheck_PR15_video'
        testdescription4 = 'Check for all programs in all services shall be blocked while Service_TV1,  Service_TV2,  Service_TV3, Service_Radio 1 and Service_TV6 are viewable.:'
        self.capture.StartRecording(videoname4), time.sleep(5)
        time.sleep(10)
        self.remote.RCUp(repetition= 6,  delay=10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname4,
                                                testdesc = testdescription4 +
                                                self.video_hlink_gen(videoname4))

        # PR 18
        self.brctfx.numeric_keys(100)
        time.sleep(5)
        
        self.remote.RCMove(UIC.UI_DTV , UIC.UI_NONE , moreoption=[UIC.UIBLOCKED], pincode=TC.Init['SETUPPIN'])
        self.remote.RCMove(UIC.UI_NONE , UIC.UI_PR18 , moreoption=[UIC.UIBLOCKED])
        self.brctfx.viewing_tvapp()
        
        # Start Recording
        videoname5 = 'LOGO_UAE_VCN_ParentalLock_LCNCheck_PR18_video'
        testdescription5 = 'Check for All programs in all services shall be viewable except for Service_TV5.:'
        self.capture.StartRecording(videoname5), time.sleep(5)
        time.sleep(10)
        self.remote.RCUp(repetition= 6,  delay=10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname5,
                                                testdesc = testdescription5 +
                                                self.video_hlink_gen(videoname5))
    
        self.remote.RCMove(UIC.UI_DTV , UIC.UI_NONE , moreoption=[UIC.UIBLOCKED], pincode=TC.Init['SETUPPIN'])        
        self.brctfx.viewing_tvapp()

class UAEBroadcastMixedAudio(DefaultTestCase):
    """
    Check for UAE Parental Lock

    Steps:
            1) Play out UAE_SIPSI_1e.ts and perform receiver full scan.

            2) Enter Service LCN 002 UAE_TV2_SD.

            3) Firstly, perform the following settings : 
                - Set Audio Description to 'ON'
                - Enable Subtitles

            Note: All subtitles are presented in english.

    Expectation:
        [1] Created by writer-editor Stan Lee and writer-artist Steve Ditko.
        [2] Arabic subtitles,SIPSI Test. Subtitle 2, number…, shall be presented when
            the subtitle selection is set to Arabic (ARA).
        [3] "Birds" main Arabic (ARA) audio shall be selectable when the audio button (such as "Audio" button ) on the remote control is pressed.
        [4] "Bell Ring" Broadcast Mixed Arabic (ARA) audio shall be selectable when the audio button(such as "Audio" button ) on the remote control is subsequenly pressed.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_1e.ts)
        self.dektec1.Run('UAE_SIPSI_1e.xml','UAE_SIPSI_1e.ts')
        self.brctfx.digital_auto_tuning()

        self.remote.RCMove(UIC.UI_HSDIGITALAUTOTUNING , UIC.UI_HSDAUDIODESCRIPTION , moreoption=[UIC.UIOFF], delay=2)
        self.brctfx.viewing_tvapp()
        
        # Start Recording
        videoname1 = 'LOGO_UAE_VCN_BroadcastMixedAudio_SelectAudio_video'
        testdescription1 = 'Check for Created by writer-editor Stan Lee and writer-artist Steve Ditko.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        self.remote.RCAudioMenu(delay=2)
        self.remote.RCSelect(delay=30)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        videoname2 = 'LOGO_UAE_VCN_BroadcastMixedAudio_ArabicSubtitle_video'
        testdescription2 = 'Check for Arabic subtitles,SIPSI Test. Subtitle 2, number…, shall be presented when the subtitle selection is set to Arabic (ARA).:'
        self.capture.StartRecording(videoname2), time.sleep(5)
        self.remote.RCSubtitle(delay=2)
        self.remote.RCDown(delay=1)
        self.remote.RCSelect(delay=1)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname2,
                                                testdesc = testdescription2 +
                                                self.video_hlink_gen(videoname2))
        
        # Start Recording
        videoname3 = 'LOGO_UAE_VCN_BroadcastMixedAudio_ArabicAudio_video'
        testdescription3 = 'Check for Bell Ring Broadcast Mixed Arabic (ARA) audio shall be selectable when the audio button(such as Audio button ) on the remote control is subsequenly pressed.:'
        self.capture.StartRecording(videoname3), time.sleep(5)
        self.remote.RCAudioMenu(repetition =2, delay=2)
        self.remote.RCSelect(delay=15)
        self.remote.RCAudioMenu(repetition =2, delay=2)
        self.remote.RCSelect(delay=15)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname3,
                                                testdesc = testdescription3 +
                                                self.video_hlink_gen(videoname3))

class UAELCNV1Descriptors(DefaultTestCase):
    """
    Check for LCN V1 Descdriptors

    Steps:
        [1] Play out UAE_SIPSI_2.1a.ts and perform receiver auto scan. 
        [2] Check LCN
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 6 services shall be visible in the service list and shall be in ascending order as below:

            LCN  005       Channel 1
            LCN  017       Channel 2 / Channel 6
            LCN  102       Radio 3
            LCN 590        Radio 4
            LCN  800++  Channel 2 / Channel 6
            LCN  800++  Channel 7

            Service with LCN 600 is hidden and shall not appear in the service list. 
            Confirm that receiver is able to access each service normally via numerical keys. 

            Using numerical keys, press '600' to enter service LCN 600 Channel 5.
            This service is hidden and can only be selected using direct key entry.
            'Village' video and 'Keyboard' audio shall be presented.

            Using numerical keys, press '017' to enter service LCN 017 Channel 2 / Channel 6.
            'Village' video and 'Keyboard' audio shall be presented.

            Select 'Channel 7' service.
            LCN 800++  shall be assigned to this service.
            'Village' video and 'Guitar Solo' audio shall be presented.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_2.1a)
        self.dektec1.Run('UAE_SIPSI_2.1a.xml','UAE_SIPSI_2.1a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()

        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAELCNV1Descriptors['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAELCNV1Descriptors['IMAGENAME1'], TC.UAELCNV1Descriptors['CONFIGJSON1'], 
        testdesc='Check for LCN V1 Descriptor: Open EPG')
         
        self.remote.RCDown(delay=2)
        self.capture.CapturePhoto(TC.UAELCNV1Descriptors['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAELCNV1Descriptors['IMAGENAME2'], TC.UAELCNV1Descriptors['CONFIGJSON2'], 
        testdesc='Check for LCN V1 Descriptor: Down button')
         
        self.remote.RCEPG(delay=2)

        # Start Recording
        videoname1 = 'LOGO_UAE_VCN_UAELCNV1Descriptors_LCNCheck_video'
        testdescription1 = 'Check for LCN Test.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [5,17,102,590,800,801,600]
        for x in range (7):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAELCNZeroDescriptors(DefaultTestCase):
    """
    Check for LCN Zero Descdriptors

    Steps:
        [1] Play out UAE_SIPSI_2.1a.ts and perform receiver auto scan. 
        [2] Check LCN
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 5 services shall be visible in the service list and shall be in ascending order as below:

            LCN  017       Channel 2 / Channel 6
            LCN  102       Radio 3
            LCN 590        Radio 4
            LCN  800++  Channel 2 / Channel 6
            LCN  800++  Channel 7

            LCN zero (0) are not listed in the channel list.

            Using numerical keys, press '0' to enter service LCN 0 Channel 1  and TV will display 'This programme number is not available.' message.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_2.1b)
        self.dektec1.Run('UAE_SIPSI_2.1b.xml','UAE_SIPSI_2.1b.ts')

        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
         
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAELCNZeroDescriptors['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAELCNZeroDescriptors['IMAGENAME1'], TC.UAELCNZeroDescriptors['CONFIGJSON1'], 
        testdesc='Check for LCN Zero Descriptor: Open EPG')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAELCNZeroDescriptors_LCNCheck_video'
        testdescription1 = 'Check for LCN Test Zero.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [17,102,590,800,801,0]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEAddDelLCNCheck(DefaultTestCase):
    """
    Check for LCN to prepare for Service addition and deletion

    Steps:
        [1] Play out UAE_SIPSI_3.1a.ts and perform receiver auto scan. 
        [2] Check LCN
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] A total of 4 services shall be presented as follows in ascending order:

        LCN 001 Service TV1
        LCN 002 Service TV2
        LCN 010 SD TV 10
        LCN 200 Standard Definition TV200

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.1a.ts)
        self.dektec1.Run('UAE_SIPSI_3.1a.xml','UAE_SIPSI_3.1a.ts')

        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
         
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEAddDelLCNCheck['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelLCNCheck['IMAGENAME1'], TC.UAEAddDelLCNCheck['CONFIGJSON1'], 
        testdesc='Check for LCN to prepare for service addition and deletion: Open EPG')
         
        self.remote.RCEPG(delay=2)
        
        videoname1 = 'LOGO_UAE_VCN_UAEAddDelLCNCheck_LCNCheck_video'
        testdescription1 = 'Check for LCN to prepare for service addition and deletion:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,10,200]
        for x in range (4):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEAddDelAddService(DefaultTestCase):
    """
    Stop the current TS and playout the addition TS in an Interval of time

    Steps:
        [1] Stop UAE_SIPSI_3.1a.ts and play out UAE_SIPSI_3.1a_addition.ts at the same frequency as before. 
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Network update shall start within the interval 121::240.
            Receiver shall automatically undergo network update and update the service list. 

            A total of 7 services shall be presented in the service list as follows in ascending order:

            LCN 001 Service TV1
            LCN 002 Service TV2
            LCN 010 SD TV 10
            LCN 200 Standard Definition TV200
            LCN 311 Service 311
            LCN 400 Service Television 400
            LCN 550 Radio Service 550

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.1a_addition.ts)
        self.dektec1.Run('UAE_SIPSI_3.1a_addition.xml','UAE_SIPSI_3.1a_addition.ts')
        self.brctfx.viewing_tvapp(), time.sleep(5)
        
        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(10)
        
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEAddDelAddService['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelAddService['IMAGENAME1'], TC.UAEAddDelAddService['CONFIGJSON1'], 
        testdesc='Check for LCN Addition: Open EPG')
             
        self.remote.RCEPG(delay=2)
        
        videoname1 = 'LOGO_UAE_VCN_UAEAddDelAddService_LCNAddition_video'
        testdescription1 = 'Check for LCN Addition:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(50)# Delay?? utk masuk saat 121
        self.remote.RCEPG(delay=3)
        self.capture.CapturePhoto(TC.UAEAddDelAddService['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelAddService['IMAGENAME2'], TC.UAEAddDelAddService['CONFIGJSON3'], 
        testdesc='Check for LCN Addition: Open EPG After delay')
         
        self.remote.RCDown(repetition=6, delay=1)
        self.capture.CapturePhoto(TC.UAEAddDelAddService['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelAddService['IMAGENAME3'], TC.UAEAddDelAddService['CONFIGJSON3'], 
        testdesc='Check for LCN Addition: Down button 6 times')
         
        self.remote.RCEPG(delay=2)
        
        lcn = [1,2,10,200,311,400,550]
        for x in range (7):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEAddDelNormalService(DefaultTestCase):
    """
    Stop the addition TS and playout the TS in an Interval of time to make the current ts is normal

    Steps:
        [1] UAE_SIPSI_3.1a_addition.ts and play out UAE_SIPSI_3.1a.ts again. 
        [2] Perform receiver auto scan.
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] A total of 4 services shall be presented as follows in ascending order:

            LCN 001 Service TV1
            LCN 002 Service TV2
            LCN 010 SD TV 10
            LCN 200 Standard Definition TV004

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.1a.ts)
        self.dektec1.Run('UAE_SIPSI_3.1a.xml','UAE_SIPSI_3.1a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        
        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(10)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEAddDelNormalService['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelNormalService['IMAGENAME1'], TC.UAEAddDelNormalService['CONFIGJSON1'], 
        testdesc='Check for LCN Normal Service: Open EPG')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEAddDelNormalService_LCNCheck_video'
        testdescription1 = 'Check for LCN Normal Service:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [1,2,10,200]
        for x in range (4):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEAddDelDeleteService(DefaultTestCase):
    """
    Stop UAE_SIPSI_3.1a.ts and play out UAE_SIPSI_3.1a_deletion.ts at the same frequency as before.

    Steps:
        [1] Stop UAE_SIPSI_3.1a.ts and play out UAE_SIPSI_3.1a_deletion.ts at the same frequency as before. 
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Network update shall start within the interval 121::240.
            Receiver shall automatically undergo network update and update the service list. 

            Confirm that 2 services are deleted from the service list and the remaining service presented in the service list are as follows in ascending order:

            LCN 010 SD TV 10
            LCN 200 Standard Definition TV200

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.1a_deletion.ts)
        self.dektec1.Run('UAE_SIPSI_3.1a_deletion.xml','UAE_SIPSI_3.1a_deletion.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()

        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(10)
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEAddDelDeleteService['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelDeleteService['IMAGENAME1'], TC.UAEAddDelDeleteService['CONFIGJSON1'], 
        testdesc='Check for LCN Deletion: Open EPG')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEAddDelDeleteService_LCNCheck_video'
        testdescription1 = 'Check for LCN after deletion.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [2,10,200]
        
        for x in range (3):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        
        # LCN 1
        self.brctfx.numeric_keys(1)
        time.sleep(55)# Delay?? utk masuk saat 121
        
        self.remote.RCEPG(delay=3)
        self.capture.CapturePhoto(TC.UAEAddDelDeleteService['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEAddDelDeleteService['IMAGENAME2'], TC.UAEAddDelDeleteService['CONFIGJSON2'], 
        testdesc='Check for LCN Deletion: Open EPG After interval')
         
        self.remote.RCEPG(delay=2)
        
        lcn = [10,200]
        
        for x in range (2):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEClashLCNSimultaneous(DefaultTestCase):
    """
    Play out UAE_SIPSI_3.2a.ts and UAE_SIPSI_3.2b.ts simultaneously and perform receiver auto scan method. 

    Steps:
        [1] Play out UAE_SIPSI_3.2a.ts and UAE_SIPSI_3.2b.ts simultaneously  
        [2] Perform receiver auto scan method.
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Total of 9 services shall be visible in the service list and shall be an ascending order as below:

            LCN  100 Service_TV1_SD
            LCN  101 Service_TV2_SD
            LCN  102  Service_TV3_SD
            LCN  103  Service_Radio1
            LCN  104 Service_Radio2
            LCN  111 SD Service 1
            LCN  222 SD Service 1_muxB
            LCN  333 SD Service 2_muxB
            LCN  444 Radio_Service 2

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.2a.ts)
        self.dektec1.Run('UAE_SIPSI_3.2a.xml','UAE_SIPSI_3.2a.ts')
        # Run TS (UAE_SIPSI_3.2b.ts)
        self.dektec2.Run('UAE_SIPSI_3.2b.xml','UAE_SIPSI_3.2b.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()

        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEClashLCNSimultaneous['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNSimultaneous['IMAGENAME1'], TC.UAEClashLCNSimultaneous['CONFIGJSON1'], 
        testdesc='Check for LCN Clash Simultineous: Open EPG')
         
        self.remote.RCDown(repetition=8, delay=1)
        self.capture.CapturePhoto(TC.UAEClashLCNSimultaneous['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNSimultaneous['IMAGENAME2'], TC.UAEClashLCNSimultaneous['CONFIGJSON2'], 
        testdesc='Check for LCN Clash Simultineous: Down 8 times')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEClashLCNSimultaneous_LCNCheck_video'
        testdescription1 = 'Check for LCN For Clash LCN Simultaneous.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,111,222,333,444]
        for x in range (9):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(10)

class UAEClashLCNMuxInitial(DefaultTestCase):
    """
    Stop the streams and play out UAE_SIPSI_3.2a_02.ts and UAE_SIPSI_3.2b_01.ts simultaneously at the same frequency as before.

    Set the power of multiplex to be such that UAE_SIPSI_3.2b_01.ts > UAE_SIPSI_3.2a_02.ts


    Steps:
        [1] Playout ts
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

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
            LCN  444 Radio_Service 2
            LCN 555 Service_Radio10
            LCN 666 Service_TV7_SD
            LCN 800++ SD_Service 2_muxA

            Using numerical keys, press  '333', '555', and '666', and ensure the following components are available in the services :
            In LCN 333, 'Village' video and 'Bell Ring' audio shall be presented.
            In LCN 555, 'Flowers' video and 'Keyboard' audio shall be presented.
            In LCN 666,  'Flowers' video and 'Keyboard' audio shall be presented.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.2a_02.ts) 474MHz
        self.dektec1.Run('UAE_SIPSI_3.2a_02.xml','UAE_SIPSI_3.2a_02.ts')
        # Run TS (UAE_SIPSI_3.2b_01.ts) 858MHz
        self.dektec2.Run('UAE_SIPSI_3.2b_01.xml','UAE_SIPSI_3.2b_01.ts')

        # ASU
        self.remote.RCPower(delay=120)
        self.remote.RCPower(delay=10)
                
        # LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(10)
        
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEClashLCNMuxInitial['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNMuxInitial['IMAGENAME1'], TC.UAEClashLCNMuxInitial['CONFIGJSON1'], 
        testdesc='Check for LCN Mux Initial: Open EPG')
         
        self.remote.RCDown(repetition=9, delay=1)
        self.capture.CapturePhoto(TC.UAEClashLCNMuxInitial['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNMuxInitial['IMAGENAME2'], TC.UAEClashLCNMuxInitial['CONFIGJSON2'], 
        testdesc='Check for LCN Mux Initial: CHL check in EPG')
         
        self.remote.RCDown(delay=1)
        self.capture.CapturePhoto(TC.UAEClashLCNMuxInitial['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNMuxInitial['IMAGENAME3'], TC.UAEClashLCNMuxInitial['CONFIGJSON3'], 
        testdesc='Check for LCN Mux Initial: Down button 1 time')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEClashLCNMuxInitial_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux Initial.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,111,222,333,444,555,666,800]
        for x in range (12):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
        # Stop dektec
        self.dektec2.StopVideo(),time.sleep(2)

class UAEClashLCNMuxAfter(DefaultTestCase):
    """
    Stop the streams and play out UAE_SIPSI_3.2a_02.ts and UAE_SIPSI_3.2b_02.ts simultaneously at the same frequency as before.

    Steps:
        [1] Stop the streams and play out UAE_SIPSI_3.2a_02.ts and UAE_SIPSI_3.2b_02.ts simultaneously at the same frequency as before. 
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Perform receiver method of network configuration update.
            Ensure the following services shall be listed :

            LCN  100 Service_TV1_SD
            LCN  101 Service_TV2_SD
            LCN  102  Service_TV3_SD
            LCN  103  Service_Radio1
            LCN  104 Service_Radio2
            LCN  222  SD Service 1_muxB
            LCN  444 Radio_Service 2
            LCN 555 Service_Radio10
            LCN 666 Service_TV7_SD
            LCN 800++ SD_Service 2_muxA

            Ensure that the below services are removed :

            1. SD Service 1
            2. SD Service 2_muxB 
        
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.2a_02.ts) 474MHz
        self.dektec1.Run('UAE_SIPSI_3.2a_02.xml','UAE_SIPSI_3.2a_02.ts')
        # Run TS (UAE_SIPSI_3.2b_02.ts) 858MHz
        self.dektec2.Run('UAE_SIPSI_3.2b_02.xml','UAE_SIPSI_3.2b_02.ts')

        # ASU
        self.remote.RCPower(delay=120)
        self.remote.RCPower(delay=10)
        
        # LCN 100
        self.brctfx.numeric_keys(100)
        time.sleep(10)
        
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEClashLCNMuxAfter['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNMuxAfter['IMAGENAME1'], TC.UAEClashLCNMuxAfter['CONFIGJSON1'], 
        testdesc='Check for LCN Clash After: Open EPG')
        self.remote.RCDown(repetition=10, delay=1)
        self.capture.CapturePhoto(TC.UAEClashLCNMuxAfter['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEClashLCNMuxAfter['IMAGENAME2'], TC.UAEClashLCNMuxAfter['CONFIGJSON2'], 
        testdesc='Check for LCN Clash After: Check CHL in EPG')
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEClashLCNMuxAfter_LCNCheck_video'
        testdescription1 = 'Check for LCN Clash after.:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,222,444,555,666,800]
        for x in range (10):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEMuxAddDelInitial(DefaultTestCase):
    """
    Play out UAE_SIPSI_3.3a.ts and perform receiver auto scan. 

    Steps:
        [1] Play out UAE_SIPSI_3.3a.ts and perform receiver auto scan.  
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] A total of 6 services shall be presented as follows in ascending order:
            LCN 100 - TV1
            LCN 101 - TV2
            LCN 102 - TV3
            LCN 103- TV4
            LCN 104 - TV5
            LCN 105 - Radio_1

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

            Using numerical keys, press '100'  to enter LCN 100 TV1. 
            'Village' video and  'Keyboard' audio shall be presented. 

            Commence following test from LCN 100 TV1.
        
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.3a.ts)
        self.dektec1.Run('UAE_SIPSI_3.3a.xml','UAE_SIPSI_3.3a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
         
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEMuxAddDelInitial['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelInitial['IMAGENAME1'], TC.UAEMuxAddDelInitial['CONFIGJSON1'], 
        testdesc='Check for Mux Add and Del Initial: Open EPG')
        
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.UAEMuxAddDelInitial['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelInitial['IMAGENAME2'], TC.UAEMuxAddDelInitial['CONFIGJSON2'], 
        testdesc='Check for Mux Add and Del Initial: Check chl in EPG')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEMuxAddDelInitial_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux Add and Del Initial CHL:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,105]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        # LCN 1
        self.brctfx.numeric_keys(100)

class UAEMuxAddDelSimultaneous(DefaultTestCase):
    """
    Stop UAE_SIPSI_3.3a.ts and play out UAE_SIPSI_3.3a_mux.ts  and UAE_SIPSI_3.3b_mux.ts  simultaneously at the same frequency as before.

    Steps:
        [1] Stop UAE_SIPSI_3.3a.ts and play out UAE_SIPSI_3.3a_mux.ts  and UAE_SIPSI_3.3b_mux.ts  simultaneously at the same frequency as before.
        [2] Do not perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Perform receiver method of network configuration update.
            (Note: Do not perform receiver autoscan.)

            A total of 10 services shall be presented as follows in ascending order:
            LCN100 - TV1
            LCN 101 - TV2
            LCN 102 - TV3
            LCN 103 - TV4
            LCN 104 - TV5
            LCN 105 - Radio_1
            LCN 200 - TV10
            LCN 201 - TV11
            LCN 202 - TV12
            LCN 203 - Radio_4

            Confirm that receiver shall be able to access to each service normally via numerical keys and service list.

            Using numerical keys, press '100'  to enter LCN 100 TV1. 
            'Village' video and  'Keyboard' audio shall be presented. 

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1','dektec2']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.3a_mux.ts)
        self.dektec1.Run('UAE_SIPSI_3.3a_mux.xml','UAE_SIPSI_3.3a_mux.ts')
        # Run TS (UAE_SIPSI_3.3b_mux.ts)
        self.dektec2.Run('UAE_SIPSI_3.3b_mux.xml','UAE_SIPSI_3.3b_mux.ts')

        #ASU
        self.remote.RCPower(delay=120)
        self.remote.RCPower(delay=10)
                
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEMuxAddDelSimultaneous['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelSimultaneous['IMAGENAME1'], TC.UAEMuxAddDelSimultaneous['CONFIGJSON1'], 
        testdesc='Check for LCN Mux Add and Del Simultaneous TS: Open EPG')
         
        self.remote.RCDown(repetition=9, delay=1)
        self.capture.CapturePhoto(TC.UAEMuxAddDelSimultaneous['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelSimultaneous['IMAGENAME2'], TC.UAEMuxAddDelSimultaneous['CONFIGJSON2'], 
        testdesc='Check for LCN Mux Add and Del Simultaneous TS: Check CHL EPG')
         
        self.remote.RCEPG(delay=2)
        
        videoname1 = 'LOGO_UAE_VCN_UAEMuxAddDelSimultaneous_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux Simultaneos:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,105,200,201,202,203]
        for x in range (10):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

        self.dektec2.StopVideo(),time.sleep(2)
        
        # LCN 100
        self.brctfx.numeric_keys(100)

class UAEMuxAddDelChlDel474(DefaultTestCase):
    """
    Multiplex Deletion/Addition
    Next, stop above streams and play out UAE_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan.

    Steps:
        [1] stop above streams and play out UAE_SIPSI_3.3a.ts at frequency 474 MHz and perform auto scan. 
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] A  total of 6 services shall be presented as follows in ascending order:

            LCN 100 - TV1
            LCN 101 - TV2
            LCN 102 - TV3
            LCN 103- TV4
            LCN 104 - TV5
            LCN 105 - Radio_1

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.3a_474MHz.ts) 474MHz
        self.dektec1.Run('UAE_SIPSI_3.3a_474MHz.xml','UAE_SIPSI_3.3a_474MHz.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
         
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEMuxAddDelChlDel474['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelChlDel474['IMAGENAME1'], TC.UAEMuxAddDelChlDel474['CONFIGJSON1'], 
        testdesc='Check for LCN Mux Chl deletion 474 MHz: Open EPG')
         
        self.remote.RCDown(repetition=5, delay=1)
        self.capture.CapturePhoto(TC.UAEMuxAddDelChlDel474['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelChlDel474['IMAGENAME2'], TC.UAEMuxAddDelChlDel474['CONFIGJSON2'], 
        testdesc='Check for LCN Mux Chl deletion 474 MHz: Check Channel EPG')
         
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_UAEMuxAddDelChlDel474_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux Chl Deletion 474 MHz:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,105]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEMuxAddDelChlDel858(DefaultTestCase):
    """
    Stop UAE_SIPSI_3.3a.ts and change the frequency to 858 MHz.Perform receiver method of service update.


    Steps:
        [1] Stop UAE_SIPSI_3.3a.ts and change the frequency to 858 MHz.Perform receiver method of service update.
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] All the 6 services as previous service list shall be presented.

            LCN 100 - TV1
            LCN 101 - TV2
            LCN 102 - TV3
            LCN 103- TV4
            LCN 104 - TV5
            LCN 105 - Radio_1

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.3a_858MHz.ts) 858MHz
        self.dektec1.Run('UAE_SIPSI_3.3a_858MHz.xml','UAE_SIPSI_3.3a_858MHz.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
         
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEMuxAddDelChlDel858['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelChlDel858['IMAGENAME1'], TC.UAEMuxAddDelChlDel858['CONFIGJSON1'], 
        testdesc='Check for LCN Mux Deletion 858MHz: Open EPG')
        
        self.remote.RCDown(repetition=5 , delay=1 )
        self.capture.CapturePhoto(TC.UAEMuxAddDelChlDel858['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEMuxAddDelChlDel858['IMAGENAME2'], TC.UAEMuxAddDelChlDel858['CONFIGJSON2'], 
        testdesc='Check for LCN Mux Deletion 858MHz: Check CHL EPG')
         
        self.remote.RCEPG(delay=2)    

        videoname1 = 'LOGO_UAE_VCN_UAEMuxAddDelChlDel858_LCNCheck_video'
        testdescription1 = 'Check for LCN Mux CHL deletion 858MHz:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [100,101,102,103,104,105]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEServiceLCNUpdate(DefaultTestCase):
    """
    Update the service name and LCN after an interval

    Steps:
        [1] Play out UAE_SIPSI_3.4.ts 
        [2] Perform receiver auto scan 
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] At interval 0::60s,  A total of 2 services shall be presented in the service list as follows in ascending order:

            LCN 110 - Channel 110
            LCN 120 - TV 120
        
        [2] At interval  61s, receiver shall detect NIT/SDT version change information and service list shall be updated accordingly.

            LCN 100 - Channel 100
            LCN 120 - TV 120

            Confirm that the LCN and Service Name is updated at banner and optionally at other user interface

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.4.ts) 
        self.dektec1.Run('UAE_SIPSI_3.4.xml','UAE_SIPSI_3.4.ts')

        # Stop dektec2
        self.dektec1.StopVideo(),time.sleep(2)
        self.dektec1.Run('UAE_SIPSI_3.4.xml','UAE_SIPSI_3.4.ts')

        videoname1 = 'LOGO_UAE_VCN_UAEServiceLCNUpdate_LCNCheck_video'
        testdescription1 = 'Check for LCN and service after LCN Update:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        lcn = [17,102,590,800,801,0]
        for x in range (6):
            self.brctfx.numeric_keys(lcn[x])
            time.sleep(10)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))
        
class UAEServiceEventUpdate120(DefaultTestCase):
    """
    Check for service and event update after an interval of time

    Steps:
        [1] Play out UAE_SIPSI_3.5.ts 
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] At interval 0::60s, 'Village' video with  'Keyboard' audio  shall be presented.
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts'),time.sleep(10)
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        # LCN 120
        self.brctfx.numeric_keys(120)
        time.sleep(10)
         
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts')

        videoname1 = 'LOGO_UAE_VCN_UAEServiceEventUpdate120_LCNCheck_video'
        testdescription1 = 'Check for Service and event update LCN120:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        time.sleep(180)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))

class UAEServiceEventUpdate131(DefaultTestCase):
    """
    Check for service and event update after an interval of time

    Steps:
        [1] Play out UAE_SIPSI_3.5.ts 
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Using numerical keys, press '131' to enter LCN131  TV Service 131.

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts'),time.sleep(10)
        self.brctfx.viewing_tvapp()
        # LCN 131
        self.brctfx.numeric_keys(131)
        time.sleep(10)
         
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts')

        videoname1 = 'LOGO_UAE_VCN_UAEServiceEventUpdate131_LCNCheck_video'
        testdescription1 = 'Check for Service and event update LCN131:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        time.sleep(180)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))      

class UAEServiceEventUpdate555(DefaultTestCase):
    """
    Check for service and event update after an interval of time

    Steps:
        [1] Play out UAE_SIPSI_3.5.ts 
        [2] Perform auto scan
        [3] Make picture judgement for initial epg
        [4] Record video to do lcn check 

    Expectation:
        [1] Using numerical keys, press '555' to enter LCN555 Channel 266. 
        Press'Info' key to view 'Now' and 'Next' event information at banner and optionally at other user interface.
        Ensure the event information are as in expectations below and take note of the changes of this information at interval 61s.

        At interval 0::60s,  present event information are as follows:
        Event Name : News at TV1
        Event Start/End Time: 9 April,  1:30 PM - 2:30 PM
        Event Description: News programme on air.
        Rating: Not defined

        At interval 61s, receiver shall detect version change in event p/f and event p/f information shall be updated accordingly.
        Present event information during  interval 61::180s shall be presented as follows:
        Event Name : Movie programme
        Event Start/End Time: 9 April, 2:30 PM - 4:00 PM
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts'),time.sleep(10)
        self.brctfx.viewing_tvapp()
        # LCN 555
        self.brctfx.numeric_keys(555)
        time.sleep(10)
         
        self.dektec1.StopVideo(),time.sleep(2)
        # Run TS (UAE_SIPSI_3.5.ts)
        self.dektec1.Run('UAE_SIPSI_3.5.xml','UAE_SIPSI_3.5.ts')

        videoname1 = 'LOGO_UAE_VCN_UAEServiceEventUpdate555_LCNCheck_video'
        testdescription1 = 'Check for Service and event update LCN555:'
        self.capture.StartRecording(videoname1), time.sleep(5)
        for a in range(8):
            self.brctfx.display_banner()
            self.remote.RCRight(delay = 2)
            self.remote.RCEPG(delay=5)
            self.remote.RCSelect(repetition=2, delay=5)
        self.capture.StopRecording()
        self.system.run_auto_video_judgement(videoname1,
                                                testdesc = testdescription1 +
                                                self.video_hlink_gen(videoname1))      

class UAECharEventPF(DefaultTestCase): 
    """
    Check for event pf for each lcn

    Steps:
        [1] Play out stream UAE_SIPSI_CHAR_4a.ts 
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(5)
        self.remote.RCEPG(delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME1'], TC.UAECharEventPF['CONFIGJSON1'], 
        testdesc='Check for Character in event TS: Open EPG')
        self.remote.RCEPG(delay=2)

        videoname1 = 'LOGO_UAE_VCN_LCN_CHECK_CHAR_4a_video'
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
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME2'], TC.UAECharEventPF['CONFIGJSON2'], 
        testdesc='(LCN100) Check for Character in event TS: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME3'], TC.UAECharEventPF['CONFIGJSON3'], 
        testdesc='(LCN100) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME4'], TC.UAECharEventPF['CONFIGJSON4'], 
        testdesc='(LCN100) Check for Character in event TS: Display event infomation')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME5'], TC.UAECharEventPF['CONFIGJSON5'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event ')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME6'], TC.UAECharEventPF['CONFIGJSON6'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event infomation')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME7'], TC.UAECharEventPF['CONFIGJSON7'], 
        testdesc='(LCN100) Check for Character in event TS: Display next event infomation on banner') #TODO: Have burst check config

        # LCN 101
        self.brctfx.numeric_keys(101)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME8'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME8'], TC.UAECharEventPF['CONFIGJSON8'], 
        testdesc='(LCN101) Check for Character in event TS: Display banner') #TODO: Have burst check config
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME9'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME9'], TC.UAECharEventPF['CONFIGJSON9'], 
        testdesc='(LCN101) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME10'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME10'], TC.UAECharEventPF['CONFIGJSON10'], 
        testdesc='(LCN101) Check for Character in event TS: Display EPG Information')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 2, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME11'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME11'], TC.UAECharEventPF['CONFIGJSON11'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next EPG')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME12'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME12'], TC.UAECharEventPF['CONFIGJSON12'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next EPG Information')
        self.remote.RCEPG(delay=2)
        self.brctfx.display_banner()
        self.remote.RCRight(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME13'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME13'], TC.UAECharEventPF['CONFIGJSON13'], 
        testdesc='(LCN101) Check for Character in event TS: Display Next Banner')

        # LCN 102
        self.brctfx.numeric_keys(102)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME14'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME14'], TC.UAECharEventPF['CONFIGJSON14'], 
        testdesc='(LCN102) Check for Character in event TS: Display Banner')
        self.dektec1.StopVideo(),time.sleep(5)  
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)  
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME15'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME15'], TC.UAECharEventPF['CONFIGJSON15'], 
        testdesc='(LCN102) Check for Character in event TS: Display EPG')
        self.remote.RCSelect(delay=3)
        self.capture.CapturePhoto(TC.UAECharEventPF['IMAGENAME16'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventPF['IMAGENAME16'], TC.UAECharEventPF['CONFIGJSON16'], 
        testdesc='(LCN102) Check for Character in event TS: Display EPG Information')
        self.remote.RCEPG(delay=2)

class UAECharEventSchedule(DefaultTestCase): 
    """
    Check the event scheduling

    Steps:
        [1] Play TS UAE_SIPSI_CHAR_4a
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts')
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(101)
        time.sleep(10)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME1'], TC.UAECharEventSchedule['CONFIGJSON1'], 
        testdesc='Check for Event Schedule: Display EPG')

        # 4.2.5 - 4.2.13
        self.remote.RCRight(repetition = 4)
        time.sleep(2)
        # Start capturing photo (Event 3)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME2'], TC.UAECharEventSchedule['CONFIGJSON2'], 
        testdesc='Check for Event Schedule: Display EPG Event 3')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME3'], TC.UAECharEventSchedule['CONFIGJSON3'], 
        testdesc='Check for Event Schedule: Display EPG Information Event 3')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 6)
        time.sleep(2)
        # Start capturing photo (Event 4)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME4'], TC.UAECharEventSchedule['CONFIGJSON4'], 
        testdesc='Check for Event Schedule: Display EPG Event 4')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME5'], TC.UAECharEventSchedule['CONFIGJSON5'], 
        testdesc='Check for Event Schedule: Display EPG Information Event 4')
        self.remote.RCEPG(delay=2)
        self.dektec1.StopVideo(),time.sleep(5)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.remote.RCRight(repetition = 8)
        time.sleep(2)
        # Start capturing photo (Event 5)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME6'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME6'], TC.UAECharEventSchedule['CONFIGJSON6'], 
        testdesc='Check for Event Schedule: Display EPG Event 5')
        self.remote.RCSelect(delay=2)
        self.capture.CapturePhoto(TC.UAECharEventSchedule['IMAGENAME7'])
        self.system.RunPictureJudgementProgram(TC.UAECharEventSchedule['IMAGENAME7'], TC.UAECharEventSchedule['CONFIGJSON7'], 
        testdesc='Check for Event Schedule: Display EPG Event 5')
        self.remote.RCEPG(delay=2)

        # 4.2.4
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (UAE_SIPSI_CHAR_4a.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4a.xml','UAE_SIPSI_CHAR_4a.ts'),time.sleep(3)
        videoname1 = 'LOGO_UAE_VCN_Button_Toggle_For_EPG_video'
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

class UAENoTableDefinition(DefaultTestCase): 
    """
    Test for EPG with no table definition

    Steps:
        [1] Play out stream UAE_SIPSI_CHAR_4b.ts 
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4b.xml','UAE_SIPSI_CHAR_4b.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAENoTableDefinition['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAENoTableDefinition['IMAGENAME1'], TC.UAENoTableDefinition['CONFIGJSON1'], 
        testdesc='Check for No table definition: Display Banner') #TODO: Burst
        self.dektec1.StopVideo(),time.sleep(3)
        # Run TS (UAE_SIPSI_CHAR_4b.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4b.xml','UAE_SIPSI_CHAR_4b.ts')    
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAENoTableDefinition['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAENoTableDefinition['IMAGENAME2'], TC.UAENoTableDefinition['CONFIGJSON2'], 
        testdesc='Check for No table definition: Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.UAENoTableDefinition['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAENoTableDefinition['IMAGENAME3'], TC.UAENoTableDefinition['CONFIGJSON3'], 
        testdesc='Check for No table definition: Display EPG Information')
        self.remote.RCEPG(delay=2)

class UAELatinTable1(DefaultTestCase): 
    """
    Play ts and enter epg to check Test 1 : Character Table 05 (ISO-8859-9).

    Steps:
        [1] Play TS UAE_SIPSI_CHAR_4c
        [2] Using numerical keys, press '100' to enter service LCN 100 Test 1 : Character Table 05 (ISO-8859-9). 
        [3] Access the banner and guide to access the presnt (now) event information. 
        [4] Capture banner and epg image and run picture judgement

    Expectation:
        [1] Short Event Description	
        " !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~ 
        ¡¢£¤¥§¨©×«¬®¯°±²³´µ¶·¸¹»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏĞÑÒÓÔÕÖ×ØÙÚÛÜİŞßàáâãåæçèéêëìíîïğñòóôõö÷øùúûüışÿ"

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_CHAR_4c.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4c.xml','UAE_SIPSI_CHAR_4c.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME1'], TC.UAELatinTable['CONFIGJSON1'], 
        testdesc='Check for Latin Table 05 - ISO-8859-9: Display Banner') #TODO: HAve burst check config
        self.dektec1.StopVideo(),time.sleep(3)
        self.dektec1.Run('UAE_SIPSI_CHAR_4c.xml','UAE_SIPSI_CHAR_4c.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME2'], TC.UAELatinTable['CONFIGJSON2'], 
        testdesc='Check for Latin Table 05 - ISO-8859-9: Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME3'], TC.UAELatinTable['CONFIGJSON3'], 
        testdesc='Check for Latin Table 05 - ISO-8859-9: Display EPG Information')
        self.remote.RCEPG(delay=2)

class UAELatinTable2(DefaultTestCase): 
    """
    Play ts and enter epg to check Test 1 : Character Table 02 (ISO-8859-6).

    Steps:
        [1] Play TS UAE_SIPSI_CHAR_4d
        [2] Using numerical keys, press '100' to enter service LCN 100 Test 1 : Character Table 05 (ISO-8859-9). 
        [3] Access the banner and guide to access the presnt (now) event information. 
        [4] Capture banner and epg image and run picture judgement

    Expectation:
        [1] Short Event Description	
        " !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~ 
        ¡¢£¤¥§¨©×«¬®¯°±²³´µ¶·¸¹»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏĞÑÒÓÔÕÖ×ØÙÚÛÜİŞßàáâãåæçèéêëìíîïğñòóôõö÷øùúûüışÿ"

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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_CHAR_4d.ts)
        self.dektec1.Run('UAE_SIPSI_CHAR_4d.xml','UAE_SIPSI_CHAR_4d.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.brctfx.numeric_keys(100)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME1'], TC.UAELatinTable['CONFIGJSON1'], 
        testdesc='Check for Latin Table 02 - ISO-8859-6: Display Banner') #TODO: HAve burst check config
        self.dektec1.StopVideo(),time.sleep(3)
        self.dektec1.Run('UAE_SIPSI_CHAR_4d.xml','UAE_SIPSI_CHAR_4d.ts'),time.sleep(3)
        self.remote.RCEPG(repetition = 3, delay = 2)
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME2'], TC.UAELatinTable['CONFIGJSON2'], 
        testdesc='Check for Latin Table 02 - ISO-8859-6: Display EPG')
        self.remote.RCSelect(delay = 2)
        self.capture.CapturePhoto(TC.UAELatinTable['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAELatinTable['IMAGENAME3'], TC.UAELatinTable['CONFIGJSON3'], 
        testdesc='Check for Latin Table 02 - ISO-8859-6: Display EPG Information')
        self.remote.RCEPG(delay=2)

class UAEAFDTest(DefaultTestCase): 
    """
    Test for AFD

    Steps:
        [1] Play out stream UAE_SIPSI_AFD.ts and perform receiver auto scan method
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
        self.supported_country = [CN.STR_UAE]
        self.supported_categories = None 
        self.required_hws = ['dektec1']
        self.tc_timeout=60

    def run(self):
        # Run TS (UAE_SIPSI_AFD.ts)
        self.dektec1.Run('UAE_SIPSI_AFD.xml','UAE_SIPSI_AFD.ts')
        self.brctfx.digital_auto_tuning()
        self.brctfx.viewing_tvapp()
        self.remote.RCEPG(delay=2)
        self.capture.CapturePhoto(TC.UAEAFDTest['IMAGENAME1'])
        self.system.RunPictureJudgementProgram(TC.UAEAFDTest['IMAGENAME1'], TC.UAEAFDTest['CONFIGJSON1'], 
        testdesc='Check for AFD Test: Display EPG')
        self.remote.RCEPG(delay=2)
        self.remote.RCMove(UIC.UI_DTV, UIC.UI_HSWIDEMODE, moreoption=[UIC.UIAUTO], delay=2)
        self.remote.RCMove(UIC.UI_HSWIDEMODE, UIC.UI_HS43DEFAULT, moreoption=[UIC.UINORMAL], delay=2)
        self.brctfx.viewing_tvapp()
        
        self.brctfx.numeric_keys(1)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEAFDTest['IMAGENAME2'])
        self.system.RunPictureJudgementProgram(TC.UAEAFDTest['IMAGENAME2'], TC.UAEAFDTest['CONFIGJSON2'], 
        testdesc='Check for AFD Test: LCN 1') # Have burst check config
        
        self.brctfx.numeric_keys(2)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEAFDTest['IMAGENAME3'])
        self.system.RunPictureJudgementProgram(TC.UAEAFDTest['IMAGENAME3'], TC.UAEAFDTest['CONFIGJSON3'], 
        testdesc='Check for AFD Test: LCN 2') # Have burst check config
        
        self.brctfx.numeric_keys(3)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEAFDTest['IMAGENAME4'])
        self.system.RunPictureJudgementProgram(TC.UAEAFDTest['IMAGENAME4'], TC.UAEAFDTest['CONFIGJSON4'], 
        testdesc='Check for AFD Test: LCN 3') # Have burst check config
        
        self.brctfx.numeric_keys(4)
        self.brctfx.display_banner()
        self.capture.CapturePhoto(TC.UAEAFDTest['IMAGENAME5'])
        self.system.RunPictureJudgementProgram(TC.UAEAFDTest['IMAGENAME5'], TC.UAEAFDTest['CONFIGJSON5'], 
        testdesc='Check for AFD Test: LCN 4') # Have burst check config

###----------- Test Case Classes Ends -------------###


###----------- Script Execution -------------###
if STATION_INFO['env'] == 'dev':
    TestExecution(DefaultTestCase).main()