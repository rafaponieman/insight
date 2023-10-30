from celery.app import shared_task

from seekers.contrib.test_seeker import TestSeekerPrototype


@shared_task(name='initiate_run')
def initiate_run(data):
    from seekers.models import Event, Run

    run_id = data['run_id']
    run = Run.objects.get(id=run_id)

    run.status = Run.STATUSES['IN_PROGRESS']
    run.save()

    seeker_prototype = None

    if run.seeker.prototype == 'test':
        seeker_prototype = TestSeekerPrototype
    else:
        raise Exception(f'Unknown seeker prototype {run.seeker.prototype}')

    prototype = seeker_prototype()
    print('pre')
    results = prototype.process()

    if 'events' in results:
        for event in results['events']:
            Event.objects.create(run=run, timestamp=event['timestamp'], message=event['message'])
    print('post')

    run.status = Run.STATUSES['COMPLETED']
    run.save()
