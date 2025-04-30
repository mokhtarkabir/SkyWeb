from django.core.cache import cache
from .models import CarouselSlide
def carousel_slides(request):
    slides = cache.get('carousel_slides')
    if not slides:
        slides = list(CarouselSlide.objects.all())
        cache.set('carousel_slides', slides, 3600)  # Cache for 1 hour
    return {'carouselData': slides}