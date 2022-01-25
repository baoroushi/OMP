from django.db.models.signals import pre_delete
from django.dispatch import receiver

from db_models.models import Service, MainInstallHistory, \
    ExecutionRecord, UpgradeHistory, RollbackHistory


@receiver(pre_delete, sender=Service)
def update_execution_record(sender, instance, *args, **kwargs):
    # models.SET_NULL --> models.SET() ?
    filter_keys = {
        MainInstallHistory: "detailinstallhistory__service",
        UpgradeHistory: "upgradedetail__service",
        RollbackHistory: "rollbackdetail__upgrade__service"
    }
    for model_cls, filter_key in filter_keys.items():
        history = model_cls.objects.filter(**{filter_key: instance}).first()
        if not history:
            continue
        execution_record = ExecutionRecord.objects.filter(
            module=history.__class__.__name__,
            module_id=history.id
        ).first()
        if not execution_record:
            continue
        execution_record.count = history.operate_count([instance.id])
        execution_record.save()
