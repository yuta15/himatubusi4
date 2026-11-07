from . import (
    storage_account,
    virtual_machine,
    azure_functions,
    app_service,
    cosmos_db,
    key_vault,
    container_registry,
    service_bus,
)


RESOURCES = {
    "STORAGE_ACCOUNT": storage_account.SPEC,
    "VIRTUAL_MACHINE": virtual_machine.SPEC,
    "AZURE_FUNCTIONS": azure_functions.SPEC,
    "APP_SERVICE": app_service.SPEC,
    "COSMOS_DB": cosmos_db.SPEC,
    "KEY_VAULT": key_vault.SPEC,
    "CONTAINER_REGISTRY": container_registry.SPEC,
    "SERVICE_BUS": service_bus.SPEC,
}

__all__ = ["RESOURCES"]
