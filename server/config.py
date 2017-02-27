from datetime import timedelta

# ================== Server Config ==================
# celery config
task_serializer = 'json'
CELERYD_CONCURRENCY=1

# celery beats config
beat_schedule = {

    'start_spiders'   : {
            'task'    : 'start_spiders',   
            'schedule': timedelta(seconds=100)
    }, 
}

# ===================================================
