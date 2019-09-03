from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ggh01_M125_Toa01a01_M12_Tobbtautau'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'HIG-RunIIFall18wmLHEGS-02803_1_cfg.py'
config.JobType.numCores = 4
config.JobType.inputFiles = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/ggh01_M125_Toa01a01_MXX_Tobbtautau/ggh01_M125_Toa01a01_M12_Tobbtautau/v1/ggh01_M125_Toa01a01_M12_Tobbtautau_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz']

config.Data.outputPrimaryDataset = 'HIG-RunIIFall18wmLHEGS-02803'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/ade/'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_ggh01_M125_Toa01a01_M12_Tobbtautau'

config.Site.storageSite = 'T2_IN_TIFR'
