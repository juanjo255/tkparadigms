## Freely Moving
## FT ##
FTstage0 = {'experimenter':'jenny', 'outcomeMode':'sides_direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage1 = {'experimenter':'jenny', 'outcomeMode':'direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage2 = {'experimenter':'jenny', 'outcomeMode':'on_next_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0.0,'automationMode':'increase_delay', 'targetMaxIntensity':60}

FTstage3 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage4 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage5 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage6 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}


FTBiasCorr = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'antibiasMode':'repeat_mistake', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

leftBias = {'timeWaterValveL':0.025}

rightBias = {'timeWaterValveR':0.025}

# bili animals
bili052 = {'subject':'bili052', **FTstage4}
bili053 = {'subject':'bili053', **FTstage3}
bili054 = {'subject':'bili054', **FTstage3}
bili055 = {'subject':'bili055', **FTBiasCorr}
bili056 = {'subject':'bili056', **FTstage4}
bili057 = {'subject':'bili057', **FTstage4}
bili058 = {'subject':'bili058', **FTstage3}
bili059 = {'subject':'bili059', **FTstage3}
bili060 = {'subject':'bili060', **FTstage3}


## Headfixed
headfix_habituation = {'rewardSideMode':'toggle'}

febeSpectralStage1 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'water_after_sound', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage2 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'lick_on_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStageBiasCorrect = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage3 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage4 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage5 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage6 = {'experimenter':'gabriel', 'relevantFeature':'spectral', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}


febe013 = {'subject':'febe013', **febeSpectralStage3}
febe019 = {'subject':'febe019', **febeSpectralStage4}
febe020 = {'subject':'febe020', **febeSpectralStage5}
febe007 = {'subject':'febe007', **febeSpectralStage4}
febe012 = {'subject':'febe012', **febeSpectralStageBiasCorrect}
