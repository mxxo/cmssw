#ifndef HcalSimAlgos_HcalDigitizerTraits_h
#define HcalSimAlgos_HcalDigitizerTraits_h
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "SimCalorimetry/HcalSimAlgos/interface/HcalElectronicsSim.h"

class HBHEDigitizerTraits {
  typedef HBHEDigiCollection DigiCollection;
  typedef HBHEDataFrame Digi;
  typedef HcalElectronicsSim ElectronicsSim;
};


class HODigitizerTraits {
  typedef HODigiCollection DigiCollection;
  typedef HODataFrame Digi;
  typedef HcalElectronicsSim ElectronicsSim;
};


class HFDigitizerTraits {
  typedef HFDigiCollection DigiCollection;
  typedef HFDataFrame Digi;
  typedef HcalElectronicsSim ElectronicsSim;
};

#endif

