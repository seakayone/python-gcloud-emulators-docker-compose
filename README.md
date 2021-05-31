# Setup project

Create virtual environment and install dependencies.

# Testing Python code running on host with emulators started locally or with docker

## Starting the emulators on the host

```console
gcloud beta emulators bigtable start &
$(gcloud beta emulators bigtable env-init)
python gcloud-emulators-docker-python/main.py  

BIGTABLE_EMULATOR_HOST: localhost:8086
Ensuring the some-table table exists.
Creating the some-table table.
Creating column family cf1 with Max Version GC rule...
Deleting the some-table table.
```

## Starting the emulator with docker

```console
docker run -p8086:8086 gcr.io/google.com/cloudsdktool/cloud-sdk:emulators gcloud beta emulators bigtable start --host-port=0.0.0.0:8086
export BIGTABLE_EMULATOR_HOST=127.0.0.1:8086
python gcloud-emulators-docker-python/main.py

// output from emulator container
Executing: /google-cloud-sdk/platform/bigtable-emulator/cbtemulator --host=0.0.0.0 --port=8086
[bigtable] Cloud Bigtable emulator running on [::]:8086

// output from Python process
BIGTABLE_EMULATOR_HOST: 127.0.0.1:8086
Ensuring the some-table table exists.
Creating the some-table table.
Creating column family cf1 with Max Version GC rule...
Deleting the some-table table.
```

# Testing code Python code running in docker container with emulators started with docker

Starting the emulators as docker container:

```console
docker compose up                                                                                                                                                                        gcloud-emulators-docker-python/git/main !+

[+] Running 2/0
 ⠿ Container gcloud-emulators-docker-python_bigtable_1   Created                                                                                                                                                                                                  0.0s
 ⠿ Container gcloud-emulators-docker-python_pythonapp_1  Created                                                                                                                                                                                                  0.0s
Attaching to bigtable_1, pythonapp_1

bigtable_1   | Executing: /google-cloud-sdk/platform/bigtable-emulator/cbtemulator --host=0.0.0.0 --port=8086
bigtable_1   | [bigtable] Cloud Bigtable emulator running on [::]:8086

pythonapp_1  | BIGTABLE_EMULATOR_HOST: bigtable:8086
pythonapp_1  | Ensuring the some-table table exists.
pythonapp_1  | Creating the some-table table.
pythonapp_1  | Creating column family cf1 with Max Version GC rule...
pythonapp_1  | Traceback (most recent call last):
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/grpc_helpers.py", line 67, in error_remapped_callable
pythonapp_1  |     return callable_(*args, **kwargs)
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/grpc/_channel.py", line 946, in __call__
pythonapp_1  |     return _end_unary_response_blocking(state, call, False, None)
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/grpc/_channel.py", line 849, in _end_unary_response_blocking
pythonapp_1  |     raise _InactiveRpcError(state)
pythonapp_1  | grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
pythonapp_1  |  status = StatusCode.UNAVAILABLE
pythonapp_1  |  details = "failed to connect to all addresses"
pythonapp_1  |  debug_error_string = "{"created":"@1622112486.781421900","description":"Failed to pick subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":3008,"referenced_errors":[{"created":"@1622112471.707069600","description":"failed to connect to all addresses","file":"src/core/ext/filters/client_channel/lb_policy/pick_first/pick_first.cc","file_line":397,"grpc_status":14}]}"
pythonapp_1  | >
pythonapp_1  |
pythonapp_1  | The above exception was the direct cause of the following exception:
pythonapp_1  |
pythonapp_1  | Traceback (most recent call last):
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/retry.py", line 188, in retry_target
pythonapp_1  |     return target()
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/grpc_helpers.py", line 69, in error_remapped_callable
pythonapp_1  |     six.raise_from(exceptions.from_grpc_error(exc), exc)
pythonapp_1  |   File "<string>", line 3, in raise_from
pythonapp_1  | google.api_core.exceptions.ServiceUnavailable: 503 failed to connect to all addresses
pythonapp_1  |
pythonapp_1  | The above exception was the direct cause of the following exception:
pythonapp_1  |
pythonapp_1  | Traceback (most recent call last):
pythonapp_1  |   File "/app/main.py", line 35, in <module>
pythonapp_1  |     main()
pythonapp_1  |   File "/app/main.py", line 25, in main
pythonapp_1  |     if not table.exists():
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/cloud/bigtable/table.py", line 415, in exists
pythonapp_1  |     table_client.get_table(request={"name": self.name, "view": VIEW_NAME_ONLY})
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/cloud/bigtable_admin_v2/services/bigtable_table_admin/client.py", line 828, in get_table
pythonapp_1  |     response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/gapic_v1/method.py", line 145, in __call__
pythonapp_1  |     return wrapped_func(*args, **kwargs)
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/retry.py", line 285, in retry_wrapped_func
pythonapp_1  |     return retry_target(
pythonapp_1  |   File "/usr/local/lib/python3.9/site-packages/google/api_core/retry.py", line 203, in retry_target
pythonapp_1  |     six.raise_from(
pythonapp_1  |   File "<string>", line 3, in raise_from
pythonapp_1  | google.api_core.exceptions.RetryError: Deadline of 60.0s exceeded while calling functools.partial(<function _wrap_unary_errors.<locals>.error_remapped_callable at 0x7f07f9d65af0>, name: "projects/some-project-id/instances/some-instance-id/tables/some-table"
pythonapp_1  | view: NAME_ONLY
pythonapp_1  | , metadata=[('x-goog-request-params', 'name=projects/some-project-id/instances/some-instance-id/tables/some-table'), ('x-goog-api-client', 'gl-python/3.9.5 grpc/1.38.0 gax/1.28.0')]), last exception: 503 failed to connect to all addresses
pythonapp_1 exited with code 1
```
