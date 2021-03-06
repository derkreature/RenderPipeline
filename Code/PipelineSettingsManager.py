
from SettingsManager import SettingsManager

class PipelineSettingsManager(SettingsManager):

    """ This class is a subclass of the SettingsManager and
    stores the settings (and their defaults) used by RenderPipeline. """

    def __init__(self):
        """ Constructs a new PipelineSettingsManager. Remember to call
        loadFromFile to load actual settings instead of the defaults. """
        SettingsManager.__init__(self, "PipelineSettings")

    def _addDefaultSettings(self):
        """ Internal method which populates the settings array with defaults
        and the internal type of settings (like int, bool, ...) """

        # [General]
        self._addSetting("preventMultipleInstances", bool, False)

        # [Antialiasing]
        self._addSetting("antialiasingTechnique", str, "SMAA")
        self._addSetting("smaaQuality", str, "Low")
        self._addSetting("jitterAmount", float, 1.0)

        # [Lighting]
        self._addSetting("computePatchSizeX", int, 32)
        self._addSetting("computePatchSizeY", int, 32)
        self._addSetting("minMaxDepthAccuracy", int, 3)
        self._addSetting("defaultReflectionCubemap", str, "Default-0/#.png")
        self._addSetting("ambientCubemapSamples", int, 16)
        self._addSetting("colorLookupTable", str, "Default.png")
        self._addSetting("enableSSLR", bool, True)
        self._addSetting("cubemapAntialiasingFactor", float, 5.0)
        self._addSetting("useAdaptiveBrightness", bool, True)
        self._addSetting("targetExposure", float, 0.8)
        self._addSetting("brightnessAdaptionSpeed", float, 1.0)
        self._addSetting("globalAmbientFactor", float, 1.0)

        # [Scattering]
        self._addSetting("enableScattering", bool, False)
        self._addSetting("useSkyboxScattering", bool, True)
        self._addSetting("useSkyboxClouds", bool, True)

        # [Occlusion]
        self._addSetting("occlusionTechnique", str, "None")
        self._addSetting("occlusionRadius", float, 1.0)
        self._addSetting("occlusionStrength", float, 1.0)
        self._addSetting("occlusionSampleCount", int, 16)
        self._addSetting("useTemporalOcclusion", bool, True)
        self._addSetting("useLowQualityBlur", bool, False)
        
        # [Shadows]
        self._addSetting("renderShadows", bool, True)
        self._addSetting("shadowAtlasSize", int, 8192)
        self._addSetting("shadowCascadeBorderPercentage", float, 0.1)       
        self._addSetting("maxShadowUpdatesPerFrame", int, 2)
        self._addSetting("numPCFSamples", int, 64)
        self._addSetting("usePCSS", bool, True)
        self._addSetting("numPCSSSearchSamples", int, 32)
        self._addSetting("numPCSSFilterSamples", int, 64)
        self._addSetting("useHardwarePCF", bool, False)
        self._addSetting("alwaysUpdateAllShadows", bool, False)

        # [Transparency]
        self._addSetting("useTransparency", bool, True)
        self._addSetting("maxTransparencyLayers", int, 10)
        self._addSetting("maxTransparencyRange", float, 100.0)
        self._addSetting("transparencyBatchSize", int, 200)

        # [Motion blur]
        self._addSetting("motionBlurEnabled", bool, True)
        self._addSetting("motionBlurSamples", int, 8)
        self._addSetting("motionBlurFactor", float, 1.0)

        # [Global Illumination]
        self._addSetting("enableGlobalIllumination", bool, False)

        # [Debugging]
        self._addSetting("displayOnscreenDebugger", bool, False)
        self._addSetting("displayDebugStats", bool, True)
        self._addSetting("pipelineOutputLevel", str, "debug")
