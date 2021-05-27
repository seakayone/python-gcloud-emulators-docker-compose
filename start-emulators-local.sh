#!/usr/bin/env bash
set -euxo pipefail

gcloud beta emulators bigtable start
gcloud beta emulators pubsub start --project=emulator-test
