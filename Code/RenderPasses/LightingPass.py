
from panda3d.core import NodePath, Shader, LVecBase2i, Texture, GeomEnums, Vec3
from panda3d.core import Camera, OrthographicLens, CullFaceAttrib, DepthTestAttrib
from panda3d.core import SamplerState, Vec4

from ..Globals import Globals
from ..RenderPass import RenderPass
from ..RenderTarget import RenderTarget
from Code.MemoryMonitor import MemoryMonitor

class LightingPass(RenderPass):

    """ This is the main lighting pass, it combines the inpupts of almost all
    features to create a combined image. It handles the lighting, shadows and
    ambient factors. It also computes the scattering based on the precomputed
    scattering model if specified """

    def __init__(self):
        RenderPass.__init__(self)

    def getID(self):
        return "LightingPass"

    def getRequiredInputs(self):
        return {

            # Deferred target
            "data0": "DeferredScenePass.data0",
            "data1": "DeferredScenePass.data1",
            "data2": "DeferredScenePass.data2",
            "data3": "DeferredScenePass.data3",
            "depth": "DeferredScenePass.depth",

            # GI and occlusion
            "giDiffuseTex": ["GlobalIlluminationPass.diffuseResult", "Variables.emptyTextureWhite"],
            "giReflectionTex": ["GlobalIlluminationPass.specularResult", "Variables.emptyTextureWhite"],
            "occlusionTex": ["OcclusionBlurPass.blurResult", "Variables.emptyTextureWhite"],


            # "lastFramePosition": "Variables.emptyTextureWhite", #TODO
            # "lastFrameOcclusion": "Variables.emptyTextureWhite", #TODO

            # Dynamic exposure
            "dynamicExposureTex": ["Variables.dynamicExposureTex", "Variables.null"],

            # Scattering
            "scatteringTex": ["ScatteringPass.resultTex", "Variables.emptyTextureWhite"],

            # Default environment
            "fallbackCubemap": "Variables.defaultEnvironmentCubemap",
            "fallbackCubemapMipmaps": "Variables.defaultEnvironmentCubemapMipmaps",

            # Precomputed unshadowed lights
            "unshadowedLightsTex": ["UnshadowedLightsPass.resultTex"],

            # Precomputed unshadowed lights
            "shadowedLightsTex": ["ShadowedLightsPass.resultTex"],

            # Volumetric lighting
            "volumetricLightingTex": ["VolumetricLightingPass.resultTex", "Variables.emptyTextureWhite"],

            # Scene data
            "noiseTexture": "Variables.noise4x4",
            "cameraPosition": "Variables.cameraPosition",
            "mainCam": "Variables.mainCam",
            "mainRender": "Variables.mainRender"
        }

    def create(self):
        # Not much to be done here, most is done in the shader
        self.target = RenderTarget("LightingPass")
        self.target.addColorTexture()
        self.target.setColorBits(16)
        self.target.prepareOffscreenBuffer()

    def setShaders(self):
        shader = Shader.load(Shader.SLGLSL, 
            "Shader/DefaultPostProcess.vertex",
            "Shader/LightingPass.fragment")
        self.target.setShader(shader)

        return [shader]

    def getOutputs(self):
        return {
            "LightingPass.resultTex": lambda: self.target.getColorTexture(),
        }

