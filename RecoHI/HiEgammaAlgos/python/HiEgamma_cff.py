import FWCore.ParameterSet.Config as cms

# clustering sequence
from RecoHI.HiEgammaAlgos.HiIslandClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.hybridClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.multi5x5ClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.multi5x5PreshowerClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.preshowerClusteringSequence_cff import *
from RecoHI.HiEgammaAlgos.HiIsolationCommonParameters_cff import *
from RecoEcal.EgammaClusterProducers.particleFlowSuperClusterECAL_cfi import *

particleFlowSuperClusterECAL.regressionConfig.vertexCollection = 'hiSelectedVertex'

hiEcalClusteringTask = cms.Task(islandClusteringTask,hybridClusteringTask,multi5x5ClusteringTask,multi5x5PreshowerClusteringTask,preshowerClusteringTask,particleFlowSuperClusterECAL)
hiEcalClusteringSequence = cms.Sequence(hiEcalClusteringTask)


# reco photon producer
from RecoEgamma.EgammaPhotonProducers.photonSequence_cff import *

# use island for the moment
photonCore.scHybridBarrelProducer = "correctedIslandBarrelSuperClusters"
photonCore.scIslandEndcapProducer = "correctedIslandEndcapSuperClusters"
photonCore.minSCEt    = 8.0
photons.minSCEtBarrel = 5.0
photons.minSCEtEndcap = 15.0
photons.minR9Barrel   = 10.  #0.94
photons.minR9Endcap   = 10.  #0.95
photons.maxHoverEEndcap = 0.5   #0.5
photons.maxHoverEBarrel = 0.99  #0.5
photons.primaryVertexProducer = 'hiSelectedVertex' # replace the primary vertex
photons.isolationSumsCalculatorSet.trackProducer = isolationInputParameters.track    # cms.InputTag("highPurityTracks")

from RecoHI.HiEgammaAlgos.photonIsolationHIProducer_cfi import photonIsolationHIProducer
hiPhotonTask = cms.Task(photonTask,photonIsolationHIProducer)
hiPhotonSequence = cms.Sequence(hiPhotonTask)

# HI Ecal reconstruction
hiEcalClustersTask = cms.Task(hiEcalClusteringTask)
hiEcalClusters = cms.Sequence(hiEcalClustersTask)
hiEgammaTask = cms.Task(hiPhotonTask)
hiEgammaSequence = cms.Sequence(hiEgammaTask)

# HI Spike Clean Sequence
import RecoHI.HiEgammaAlgos.hiSpikeCleaner_cfi
hiSpikeCleanedSC = RecoHI.HiEgammaAlgos.hiSpikeCleaner_cfi.hiSpikeCleaner.clone()
cleanPhotonCore = photonCore.clone(
    scHybridBarrelProducer = "hiSpikeCleanedSC"
)
cleanPhotons = photons.clone(
    photonCoreProducer = cms.InputTag("cleanPhotonCore")
)

hiPhotonCleaningTask = cms.Task(hiSpikeCleanedSC,
                                cleanPhotonCore,
                                cleanPhotons)
hiPhotonCleaningSequence = cms.Sequence(hiPhotonCleaningTask)
