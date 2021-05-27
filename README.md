# Setup project

Create virtual environment and install dependencies.

# Testing code running with emulators started locally

Starting the emulators manually:

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

# Testing code running with emulators started with docker compose

Starting the emulators as docker container:

```console
docker-compose up &
export BIGTABLE_EMULATOR_HOST=localhost:8086
python gcloud-emulators-docker-python/main.py  

// output from docker compose
[+] Running 1/0
 ⠿ Container gcloud-emulators-docker-python_bigtable_1  Created                                                                                        0.1s
Attaching to bigtable_1
bigtable_1  | Executing: /google-cloud-sdk/platform/bigtable-emulator/cbtemulator --host=localhost --port=8086
bigtable_1  | [bigtable] Cloud Bigtable emulator running on 127.0.0.1:8086

// output from python process
BIGTABLE_EMULATOR_HOST127.0.0.1:8086
Ensuring the some-table table exists.
Creating the some-table table.
Creating column family cf1 with Max Version GC rule...
Traceback (most recent call last):
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/grpc_helpers.py", line 67, in error_remapped_callable
    return callable_(*args, **kwargs)
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/grpc/_channel.py", line 946, in __call__
    return _end_unary_response_blocking(state, call, False, None)
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/grpc/_channel.py", line 849, in _end_unary_response_blocking
    raise _InactiveRpcError(state)
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
	status = StatusCode.UNAVAILABLE
	details = "failed to connect to all addresses"
	debug_error_string = "{"created":"@1622107536.009954000","description":"Failed to pick subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":3009,"referenced_errors":[{"created":"@1622107521.031831000","description":"failed to connect to all addresses","file":"src/core/ext/filters/client_channel/lb_policy/pick_first/pick_first.cc","file_line":398,"grpc_status":14}]}"
>

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/retry.py", line 188, in retry_target
    return target()
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/grpc_helpers.py", line 69, in error_remapped_callable
    six.raise_from(exceptions.from_grpc_error(exc), exc)
  File "<string>", line 3, in raise_from
google.api_core.exceptions.ServiceUnavailable: 503 failed to connect to all addresses

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/kleinboelting/git/one-platform-rtl/gcloud-emulators-docker-python/gcloud-emulators-docker-python/main.py", line 35, in <module>
    main()
  File "/Users/kleinboelting/git/one-platform-rtl/gcloud-emulators-docker-python/gcloud-emulators-docker-python/main.py", line 25, in main
    if not table.exists():
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/cloud/bigtable/table.py", line 415, in exists
    table_client.get_table(request={"name": self.name, "view": VIEW_NAME_ONLY})
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/cloud/bigtable_admin_v2/services/bigtable_table_admin/client.py", line 828, in get_table
    response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/gapic_v1/method.py", line 145, in __call__
    return wrapped_func(*args, **kwargs)
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/retry.py", line 285, in retry_wrapped_func
    return retry_target(
  File "/Users/kleinboelting/.virtualenvs/gcloud-emulators-docker-python/lib/python3.8/site-packages/google/api_core/retry.py", line 203, in retry_target
    six.raise_from(
  File "<string>", line 3, in raise_from
google.api_core.exceptions.RetryError: Deadline of 60.0s exceeded while calling functools.partial(<function _wrap_unary_errors.<locals>.error_remapped_callable at 0x10926a3a0>, name: "projects/some-project-id/instances/some-instance-id/tables/some-table"
view: NAME_ONLY
, metadata=[('x-goog-request-params', 'name=projects/some-project-id/instances/some-instance-id/tables/some-table'), ('x-goog-api-client', 'gl-python/3.8.9 grpc/1.38.0 gax/1.28.0')]), last exception: 503 failed to connect to all addresses

Process finished with exit code 1

```
