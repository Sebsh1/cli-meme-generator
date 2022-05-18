from PIL import ImageEnhance

# Inspired by r/deepfriedmemes, Currently missing consecutive JPEG compressions
def deepfry(img, factor=3):
    enhancer = ImageEnhance.Brightness(img)
    enhanced_image = enhancer.enhance(factor)

    enhancer = ImageEnhance.Sharpness(enhanced_image)
    enhanced_image = enhancer.enhance(factor)

    enhancer = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = enhancer.enhance(factor)

    return enhanced_image