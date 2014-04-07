LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := main

JNI_PATH := ../android/jni
SDL_PATH := $(JNI_PATH)/SDL
SDL_IMAGE_PATH := $(JNI_PATH)/SDL_image
SDL_MIXER_PATH := $(JNI_PATH)/SDL_mixer

LOCAL_C_INCLUDES := $(LOCAL_PATH)/$(SDL_PATH)/include \
	$(LOCAL_PATH)/$(SDL_IMAGE_PATH) \
	$(LOCAL_PATH)/$(SDL_MIXER_PATH) \
	$(BULLETDIR)/include/bullet \
	$(GLMDIR)

# Add your application source files here...
LOCAL_SRC_FILES := $(SDL_PATH)/src/main/android/SDL_android_main.c \
	$(shell find $(JNI_PATH)/src/ -name "*.cpp")

# Alternative way to wildcard-include files.
#	$(wildcard $(JNI_PATH)/src/*.cpp)

# To view variables use:
# $(warning $(LOCAL_SRC_FILES))

LOCAL_SHARED_LIBRARIES := SDL2 SDL2_image SDL2_mixer bullet
LOCAL_STATIC_LIBRARIES := cpufeatures

LOCAL_LDLIBS := -lGLESv1_CM -lGLESv2 -llog
LOCAL_CFLAGS := -fno-strict-aliasing -D_REENTRANT -DGLM_FORCE_RADIANS
LOCAL_CFLAGS += -isystem $(GLMDIR)
LOCAL_CPPFLAGS += -fexceptions -frtti -std=c++11

include $(BUILD_SHARED_LIBRARY)

$(call import-module,android/cpufeatures)
