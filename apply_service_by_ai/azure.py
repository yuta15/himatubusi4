from .resource import Field, ResourceSpec, simulated
from .validation import integer, one_of, storage_account_name, text


RESOURCES = {
    "STORAGE_ACCOUNT": ResourceSpec(
        fields={
            "account_name": Field(storage_account_name),
            "location": Field(text),
            "replication": Field(one_of("LRS", "GRS")),
        },
        execute=simulated("Simulated storage account creation: {account_name}"),
    ),
    "VIRTUAL_MACHINE": ResourceSpec(
        fields={"name": Field(text), "size": Field(text), "disk_size_gb": Field(integer(1, 1024))},
        execute=simulated("Simulated virtual machine creation: {name}"),
    ),
    "AZURE_FUNCTIONS": ResourceSpec(
        fields={
            "name": Field(text),
            "runtime": Field(one_of("python", "node", "dotnet")),
            "storage_account": Field(text),
        },
        execute=simulated("Simulated function app creation: {name}"),
    ),
    "APP_SERVICE": ResourceSpec(
        fields={
            "name": Field(text),
            "plan_name": Field(text),
            "runtime": Field(one_of("python", "node", "dotnet")),
        },
        execute=simulated("Simulated web app creation: {name}"),
    ),
    "COSMOS_DB": ResourceSpec(
        fields={
            "account_name": Field(text),
            "database_name": Field(text),
            "throughput": Field(integer(400, 10000, step=100)),
        },
        execute=simulated("Simulated Cosmos DB creation: {database_name}"),
    ),
}
