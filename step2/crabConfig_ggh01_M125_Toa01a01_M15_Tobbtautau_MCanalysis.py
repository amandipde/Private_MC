from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ggh01_M125_Toa01a01_M15_Tobbtautau_AOD'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'HIG-RunIIAutumn18DRPremix-01706_2_cfg.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 9999
config.Data.inputDataset = '/HIG-RunIIFall18wmLHEGS-02803/ade-CRAB3_ggh01_M125_Tobbtautau_M15_Tomumutautau_RAWSIMv1-5aa1749307f00d6302ec929df355f761/USER'
config.Data.inputDBS = 'phys03'


config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 5
#NJOBS =1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.JobType.sendExternalFolder = True
config.Data.outLFNDirBase = '/store/user/ade/'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_ggh01_M125_Tobbtautau_M15_Tomumutautau_AOD'
#config.Data.ignoreLocality = True

config.Site.storageSite = 'T2_IN_TIFR'
#config.Site.whitelist = ['T2_US_MIT','T2_US_Nebraska','T3_TW_NCU','T2_DE_DESY','T2_CH_CERN','T2_BE_IIHE']
#config.Site.blacklist = ['T2_US_Florida']
