import os

from google.auth.credentials import AnonymousCredentials
from google.cloud import bigtable
from google.cloud.bigtable import column_family


def main(
    project_id="some-project-id", instance_id="some-instance-id", table_id="some-table"
):
    print("BIGTABLE_EMULATOR_HOST: " + os.environ["BIGTABLE_EMULATOR_HOST"])
    client = bigtable.Client(
        project=project_id, credentials=AnonymousCredentials(), admin=True
    )
    instance = client.instance(instance_id)
    print("Ensuring the {} table exists.".format(table_id))

    print("Creating the {} table.".format(table_id))
    table = instance.table(table_id)

    print("Creating column family cf1 with Max Version GC rule...")
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    column_family_id = "cf1"
    column_families = {column_family_id: max_versions_rule}
    if not table.exists():
        table.create(column_families=column_families)
    else:
        print("Table {} already exists.".format(table_id))

    print("Deleting the {} table.".format(table_id))
    table.delete()


if __name__ == "__main__":
    main()
