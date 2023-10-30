from django.utils import timezone

from celery.app import shared_task
from data.providers import fetch_data

from seekers.contrib.sma import SMASeekerPrototype
from seekers.contrib.test_seeker import TestSeekerPrototype


@shared_task(name='initiate_run')
def initiate_run(data):
    from seekers.models import Event, Run

    run_id = data['run_id']
    run = Run.objects.get(id=run_id)

    run.status = Run.STATUSES['IN_PROGRESS']
    run.start = timezone.now()
    run.save()

    seeker_prototype = None

    # Fetch Seeker prototype
    if run.seeker.prototype == 'test':
        seeker_prototype = TestSeekerPrototype
    elif run.seeker.prototype == 'sma':
        seeker_prototype = SMASeekerPrototype
    else:
        raise Exception(f'Unknown seeker prototype {run.seeker.prototype}')

    prototype = seeker_prototype()

    # Fetch data
    data = fetch_data(run.from_timestamp, run.to_timestamp)

    results = prototype.process()

    if 'events' in results:
        for event in results['events']:
            Event.objects.create(run=run, timestamp=event['timestamp'], message=event['message'])

    run.status = Run.STATUSES['COMPLETED']
    run.end = timezone.now()
    run.save()
