import os
# Common variables for SCons script

base ='#/src'

pathBoost   = os.environ["BOOST_DIR"];
pathSdl     = os.environ["SDL2_DIR"];
pathGlm     = os.environ["GLM_DIR"];
pathBullet  = os.environ["BULLET_DIR"];
pathCxxTest = os.environ["CXXTEST"];

lSDL      = ['SDL2']
lSDLimage = ['SDL2_image']
lSDLmixer = ['SDL2_mixer']
lSDLttf   = ['SDL2_ttf']
lBullet   = ['BulletCollision', 'BulletDynamics', 'LinearMath']
lGL       = ['GL', 'GLU']
lFlite    = ['flite_voice_list',
             'flite_cmu_us_awb',
             'flite_cmu_us_rms',
             'flite_usenglish',
             'flite_cmulex',
             'flite']
lNoise    = ['noise']
lPolyVox  = ['PolyVoxCore', 'PolyVoxUtil']
lOther    = ['m', 'dl', 'rt']
lAll  = (lSDL + lSDLimage + lSDLmixer + lSDLttf +
         lBullet + lGL +
         lFlite + lNoise + lPolyVox +
         lOther)

libpaths = ['#/lib/',
            pathSdl    + '/lib',
            pathBullet + '/lib']

# Macros definitions
macroDefinitions = [
   'USING_SDL',            # Should always be set in SDL projects.
#   'LOGGING_DISABLED',    # Disables all logging
#   'LOG2STREAM_DISABLED', # Disables logging to stream
#   'LOG2FILE_DISABLED',   # Disables logging to file
   'LOG_SDL_EVENTS_VERBOSELY'
]

gccWarningLevel = [
   '-Wall', '-Wextra', '-Wcast-align', '-Wcast-qual',
   '-Wconversion', '-Wdisabled-optimization', #'-Weffc++',
   '-Wfloat-equal', '-Wformat=2', '-Wimport', '-Winit-self',
   '-Winline', '-Winvalid-pch', '-Wlong-long',
   '-Wmissing-format-attribute', '-Wmissing-include-dirs',
   '-Wmissing-noreturn', '-Wpacked', '-Wpointer-arith',
   '-Wredundant-decls', '-Wshadow', '-Wstack-protector',
   '-Wstrict-aliasing=2', '-Wunreachable-code',
   '-Wunused',
   '-Wvariadic-macros', '-Wwrite-strings', '-pedantic',
   '-pedantic-errors', '-Woverloaded-virtual',
   '-Wswitch-enum', '-Werror'
   # # Clang unsupported flags.
   # '-fpermissive',
   # -Wunsafe-loop-optimizations'
]

# CPPFLAGS
####################
cppflags = ['-O0', '-g', '-gdwarf-2']
#cppflags = ['-O3']
cppflags.extend(['-fno-strict-aliasing',
                 '-std=c++11',
                 '-D_REENTRANT',
                 '-DGLM_FORCE_RADIANS'])
cppflags.extend(['-isystem', pathBoost  + '/include',
                 '-isystem', pathSdl    + '/include/',
                 '-isystem', pathGlm,
                 '-isystem', 'external/',
                 '-isystem', pathCxxTest,
                 '-isystem', 'external/polyvox/library/PolyVoxCore/include',
                 '-isystem', pathBullet + '/include/bullet'])
cppflags.extend(gccWarningLevel)
for macro in macroDefinitions:
   cppflags.append('-D' + macro)
if 'CPPFLAGS' in os.environ:
   cppflags.extend(os.environ['CPPFLAGS'].split())

# LINKFLAGS
####################
linkflags = []
if 'LDFLAGS' in os.environ:
   linkflags.extend(os.environ['LDFLAGS'].split())


sourcepaths = [
   base,
   '../external/',
   '../external/polyvox/library/PolyVoxCore/include/',
   '../external/polyvox/library/PolyVoxUtil/include/',
   pathBoost  + '/include',
   pathGlm,
   pathBullet + '/include/bullet/',
   pathCxxTest,
   pathSdl    + "/include/"]
