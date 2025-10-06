from CRABClient.UserUtilities import config

username='yehe'
lumi_mask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions25/Cert_Collisions2025_391658_397032_Golden.json'
output_dataset_tag = 'jetMET24I'
input_dataset = '/JetMET0/Run2025C-PromptReco-v1/AOD'
pset_name = 'nano.py'
output_files = ['nano.root']
file_output_path = f'/store/group/dpg_trigger/comm_trigger/L1Trigger/{username}/JECs2025/'
config = config()

# General settings
config.General.requestName = output_dataset_tag 
config.General.transferLogs = True
config.General.transferOutputs = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = pset_name
config.JobType.outputFiles = output_files
config.JobType.maxMemoryMB = 2500 #4500

# Data settings
config.Data.inputDataset = input_dataset
config.Data.inputDBS = 'global'

config.Data.useParent = True
config.Data.partialDataset = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 #10

config.Data.allowNonValidInputDataset = True

config.Data.outputDatasetTag = output_dataset_tag
config.Data.outLFNDirBase = file_output_path

config.Data.lumiMask = lumi_mask
config.Site.storageSite = 'T2_CH_CERN'
