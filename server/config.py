from datetime import timedelta

# ================== Server Config ==================
# celery config
task_serializer = 'json'

# celery beats config
beat_schedule = {

    'start_spiders'   : {
            'task'    : 'start_spiders',   
            'schedule': timedelta(seconds=100)
    }, 
}

# ip spider config
ip_use = 50

# ================== Client Config ==================
# redis config

