---
title: "How to collect DU usage data with in-cluster objectstore (Ceph)"
visible: true
slug: "how-to-collect-du-usage-data-with-in-cluster-objectstore-ceph"
---

This section explains how to collect Document Understanding (DU) usage data when using in-cluster objectstore (Ceph).

Take the following steps:

1. Before running the DU collector script, make sure to update the following values:
   * `<REGISTRY>`:
     + Use `localhost:30071` for offline deployments.
     + Use `registry.uipath.com` for online deployments.
     + Use your external registry URL for private registries.
   * `<TAG>`: Open `versions.json` and locate the `sf-k8-utils-rhel` image tag. Use this tag to replace `<TAG>` in the script.
2. Run the DU usage collector script after updating the values, as follows:
   ```
   NAMESPACE="rook-ceph"
   POD_NAME="du-usage-collector"
   SECRET_NAME="ceph-object-store-secret"
   LOCAL_TAR="du-usage.tar.gz"
   MOUNTED_SECRET_PATH="/rook-secret"
   TARGET_PATH="aistorage/org-00000000-0000-0000-0000-000000000001/tenant-00000000-0000-0000-0000-000000000001"
   BUCKET_NAME="ai-storage"
   IMAGE="<REGISTRY>/uipath/sf-k8-utils-rhel:<TAG>"

   echo "[*] Removing pod $POD_NAME in namespace $NAMESPACE..."
   kubectl delete pod "$POD_NAME" -n "$NAMESPACE" --ignore-not-found=true

   echo "[*] Creating pod $POD_NAME in namespace $NAMESPACE..."
   kubectl apply -n "$NAMESPACE" -f - <<EOF
   apiVersion: v1
   kind: Pod
   metadata:
     name: $POD_NAME
     namespace: $NAMESPACE
   spec:
     restartPolicy: Never
     containers:
     - name: sleep
       image: $IMAGE
       command: ["bash", "-c", "echo 'Main container started, sleeping...'; sleep 3600"]
       volumeMounts:
       - name: output
         mountPath: /output
     initContainers:
     - name: du-usage-collector
       image: $IMAGE
       command: ["/bin/bash", "-c"]
       args:
         - |
           set -euo pipefail
           echo "[*] Extracting Ceph secret values..."
           ACCESS_KEY=\$(cat $MOUNTED_SECRET_PATH/OBJECT_STORAGE_ACCESSKEY)
           SECRET_KEY=\$(cat $MOUNTED_SECRET_PATH/OBJECT_STORAGE_SECRETKEY)
           HOST=\$(cat $MOUNTED_SECRET_PATH/OBJECT_STORAGE_INTERNAL_SERVICE)
           PORT=\$(cat $MOUNTED_SECRET_PATH/OBJECT_STORAGE_PORT)
           export AWS_ACCESS_KEY_ID=\$ACCESS_KEY
           export AWS_SECRET_ACCESS_KEY=\$SECRET_KEY
           echo "[*] Syncing from s3://$BUCKET_NAME/$TARGET_PATH ..."
           mkdir -p /tmp/download
           s3cmd sync s3://$BUCKET_NAME/$TARGET_PATH/ /tmp/download/ \
             --host=\$HOST:\$PORT --host-bucket= --no-ssl --no-check-certificate
           echo "[*] Creating archive..."
           mkdir -p /output
           tar -czf /output/du-usage.tar.gz -C /tmp/download .
           echo "[✔] Archive ready at /output/du-usage.tar.gz"
       volumeMounts:
       - name: rook-secret
         mountPath: $MOUNTED_SECRET_PATH
         readOnly: true
       - name: output
         mountPath: /output
     volumes:
     - name: rook-secret
       secret:
         secretName: $SECRET_NAME
         optional: false
     - name: output
       emptyDir: {}
   EOF

   echo "[*] Waiting for pod to be Running..."
   for i in {1..30}; do
     phase=$(kubectl get pod "$POD_NAME" -n "$NAMESPACE" -o jsonpath="{.status.phase}")
     if [[ "$phase" == "Running" ]]; then
       echo "Pod is Running."
       break
     fi
     echo "[$i] Still waiting..."
     sleep 5
   done

   echo -e "\nArchive will be saved as: $LOCAL_TAR\n\n"
   echo "[*] Copying archive from pod to local..."
   kubectl cp "$NAMESPACE/$POD_NAME:/output/du-usage.tar.gz" "$LOCAL_TAR"
   ```
3. After retrieving the archive, delete the pod:
   ```
   kubectl delete pod "$POD_NAME" -n "$NAMESPACE"
   ```

The `du-usage.tar.gz` file contains the DU usage data.