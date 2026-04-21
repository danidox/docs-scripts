---
title: "Migrating from Automation Suite on EKS/AKS to Automation Suite on OpenShift"
visible: true
slug: "migrating-from-automation-suite-on-eksaks-to-automation-suite-on-openshift"
---

You can migrate from Automation Suite deployed on EKS/AKS to Automation Suite on OpenShift. To do that, you must move your Kubernetes resources and, if applicable, migrate your data and Insights.

## Step 1: Migrating Kubernetes resources

To migrate your Kubernetes resources from EKS/AKS to OpenShift, take the following steps:

1. Export your Kubernetes resources from the EKS/AKS cluster:
   ```
   uipathctl cluster migration export ~/Downloads/aksinput.json --output-dir ~/Migrate --kubeconfig ~/Downloads/akskubeconfig --log-level debug
   ```
2. Update the values for `namespace`, `resourceVersion`, and `uid` in the file generated in the output directory. Make sure to replace &lt;uipath&gt; with the namespace you plan to use.
   ```
   sed -i '' 's/namespace: uipath/namespace: <uipath>/g' source-cluster-223902721
   sed -i '' 's/namespace: airflow/namespace: <uipath>/g' source-cluster-223902721
   sed -i '' '/  resourceVersion:/d' source-cluster-223902721
   sed -i '' '/  uid:/d' source-cluster-223902721
   ```
3. Create the manifests in the target cluster using its kubeconfigr:
   ```
   kubectl apply -f source-cluster-223902721 --namespace=<namespace>
   ```
4. After completing the data and Insights migration ([Step 2](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-from-automation-suite-on-eksaks-to-automation-suite-on-openshift#step-2%3A-migrating-data) and [Step 3](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-from-automation-suite-on-eksaks-to-automation-suite-on-openshift#step-3%3A-migrating-insights)), complete the Automation Suite installation on the target cluster, by running the following command:
   ```
   uipathctl manifest apply input-target.json --kubeconfig kubeconfig.target --versions versions-target.json
   ```

## Step 2: Migrating data

To migrate your data from Automation Suite on EKS/AKS to Automation Suite on OpenShift, take the following steps:

1. Copy all the data from the source objectstore to the destination objectstore. Skip this step if you plan to use the same objectstore in the target cluster.
2. Copy the SQL data from the source SQL server to the target SQL server. Skip this step if you plan to use the same SQL server in the target cluster.

## Step 3: Migrating Insights

### About the Insights migration

To migrate Insights, you must migrate the following PVCs:

* `insights-looker-lookerdir-pvc` (PVC size: 500Mi)
* `insights-looker-datadir-pvc` (PVC size: 10Gi)

### How to migrate Insights

To migrate the Insights PVCs, take the following steps:

1. Create the external storage secret by running one of the following commands.
   * If you use S3-compatible storage, run the following command:
     ```
     kubectl create secret -n <namespace> generic export-externalobjects-secret \
     --from-literal=ACCESSKEY=<accesskey> \
     --from-literal=SECRETKEY=<secretkey> \
     --from-literal=REGION=<region> \
     --from-literal=FQDN=<fqdn> \
     --from-literal=BUCKET=<bucket> \
     --from-literal=USE_INSTANCE_PROFILE=<use_instance_profile> \
     --from-literal=CREATE_BUCKET=<create_bucket> \
     --from-literal=STORAGE_TYPE=s3 \
     --from-literal=PORT=<port>
     ```
   * If you use AWS S3 storage, run the following command:
     ```
     kubectl create secret -n <namespace> generic export-externalobjects-secret \ 
     --from-literal=ACCOUNTKEY=<accountkey> \
     --from-literal=ACCOUNTNAME=<accountname> \
     --from-literal=CLIENT_ID=<client_id> \
     --from-literal=AZURE_FQDN_SUFFIX=<fqdn> \
     --from-literal=BUCKET=<bucket> \
     --from-literal=USE_MANAGED_IDENTITY=<use_managed_profile> \
     --from-literal=CREATE_CONTAINER=<create_container> \
     --from-literal=STORAGE_TYPE=azure \
     --from-literal=USE_WORKLOAD_IDENTITY=<use_workload_identity>
     ```
2. Create the `insights-looker-lookerdir-pvc` PVC:
   ```
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     labels:
       app.kubernetes.io/component: insightslooker
       app.kubernetes.io/instance: insights
       app.kubernetes.io/part-by: cloud-rpa
       argocd.argoproj.io/instance: insights
     name: insights-looker-lookerdir-pvc
     namespace: <namespace>
   spec:
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
         storage: 500Mi
     storageClassName: <storage-class-name>
   ```
3. Create the RBAC:
   ```
   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: migration-sa
     namespace: <uipath>
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: migration-role
     namespace: <namespace>
   rules:
     - apiGroups: [""]
       resources: ["configmaps", "secrets"]
       verbs: ["get", "list", "watch", "create", "patch"]

   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: migration-rolebinding
     namespace: <namespace>
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: migration-role
   subjects:
     - kind: ServiceAccount
       name: migration-sa
       namespace: <namespace>
   ```
4. Create the pod for migrating `insights-looker-lookerdir-pvc`:
   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: inbound-migrator
     namespace: <namespace>
   spec:
     containers:
     - command:
       - /uipathcore
       - data
       - migrate
       - --source-secret 
       - export-externalobjects-secret
       - --source-path
       - insights/mnt/lookerfiles
       - --destination-path
       - /mnt/lookerfiles
       - --namespace
       - <namespace>
       - --log-level
       - debug
       image: sfbrdevhelmweacr.azurecr.io/uipath/uipathcore:2.2510.0
       imagePullPolicy: IfNotPresent
       name: pvc-migrator
       securityContext:
         allowPrivilegeEscalation: false
         capabilities:
           drop:
           - ALL
           - MKNOD
         runAsNonRoot: true
       volumeMounts:
       - mountPath: /mnt/lookerfiles
         name: insights-looker-lookerdir
     serviceAccountName: migration-sa
     imagePullSecrets:
     - name: uipathpullsecret
     securityContext:
       runAsNonRoot: true
     volumes:
     - name: insights-looker-lookerdir
       persistentVolumeClaim:
         claimName: insights-looker-lookerdir-pvc
   ```
5. Create the `insights-looker-datadir-pvc` PVC:
   ```
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     labels:
       app.kubernetes.io/component: insightslooker
       app.kubernetes.io/instance: insights
       app.kubernetes.io/part-by: cloud-rpa
       argocd.argoproj.io/instance: insights
     name: insights-looker-datadir-pvc
     namespace: <namespace>
   spec:
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
         storage: 10Gi
     storageClassName: <storage-class-name>
   ```
6. Create the pod for migrating `insights-looker-datadir-pvc`:
   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: inbound-migrator-data
     namespace: <namespace>
   spec:
     containers:
     - command:
       - /uipathcore
       - data
       - migrate
       - --source-secret 
       - export-externalobjects-secret
       - --source-path
       - insights/app/workdir
       - --destination-path
       - /mnt/lookerfiles
       - --namespace
       - <namespace>
       - --log-level
       - debug
       image: sfbrdevhelmweacr.azurecr.io/uipath/uipathcore:2.2510.0
       imagePullPolicy: IfNotPresent
       name: pvc-migrator
       securityContext:
         allowPrivilegeEscalation: false
         capabilities:
           drop:
           - ALL
           - MKNOD
         runAsNonRoot: true
       volumeMounts:
       - mountPath: /mnt/lookerfiles
         name: insights-looker-datadir
     serviceAccountName: migration-sa
     imagePullSecrets:
     - name: uipathpullsecret
     securityContext:
       runAsUser: 1000700000
       runAsNonRoot: true
     volumes:
     - name: insights-looker-datadir
       persistentVolumeClaim:
         claimName: insights-looker-datadir-pvc
   ```
7. Delete the service account, role, and rolebinding previously created in step 3:
   ```
   kubectl -n <namespace> delete sa migration-sa
   kubectl -n <namespace> delete role migration-role
   kubectl -n <namespace> delete rolebinding migration-rolebinding
   ```