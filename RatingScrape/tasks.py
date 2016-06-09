from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from urllib.request import urlopen
from .models import RatingStars
import json

from datetime import datetime

logger = get_task_logger(__name__)


# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def get_ios_ratings_periodic():
    logger.info("Start task")

    #Logic here
    app_id = 419267350
    target_url = "https://itunes.apple.com/lookup?id=" + str(app_id) + "&country=jp"
    content = urlopen(target_url).read().decode('utf8')
    content_data = json.loads(content)

    RatingStars.objects.create(
        star_number=content_data['results'][0]['averageUserRatingForCurrentVersion'],
        title=content_data['results'][0]['trackName'],
        text="Other text",
    )

    #Logging
    name = "scraper_example"

