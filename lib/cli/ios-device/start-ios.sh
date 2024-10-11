#!/bin/bash
stf ios-device \
    --serial ios-device \
    --device-name "ios device" \
    --host localhost \
    --screen-port 7409 \
    --mjpeg-port 9100 \
    --provider local-provider \
    --public-ip localhost \
    --screen-ws-url-pattern "ws://localhost:7409" \
    --storage-url http://localhost:7100/ \
    --connect-sub tcp://127.0.0.1:7114 \
    --connect-push tcp://127.0.0.1:7116 \
    --connect-app-dealer tcp://127.0.0.1:7112 \
    --connect-dev-dealer tcp://127.0.0.1:7115 \
    --wda-host 127.0.0.1 \
    --wda-port 8100
