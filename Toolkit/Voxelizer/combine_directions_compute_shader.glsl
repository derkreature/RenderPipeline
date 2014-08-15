#version 430

layout (local_size_x = 8, local_size_y = 8, local_size_z = 8) in;


uniform sampler2D directionX;
uniform sampler2D directionY;
uniform sampler2D directionZ;

uniform writeonly image2D destination;
uniform int gridSize;

ivec2 convertCoord(ivec3 coord) {
    return coord.xy + ivec2(coord.z * gridSize, 0);
}

void main() {
    ivec3 texelCoords = ivec3(gl_GlobalInvocationID.xyz);


    float factorX = texelFetch(directionX, convertCoord(texelCoords.yzx), 0).x;
    float factorY = texelFetch(directionY, convertCoord(texelCoords.xzy), 0).x;
    float factorZ = texelFetch(directionZ, convertCoord(texelCoords.xyz), 0).x;

    float result = (factorX + factorY + factorZ) > 0.5 ? 1.0 : 0.0;
    imageStore(destination, convertCoord(texelCoords.xyz), vec4(result,result,result, 1));
}