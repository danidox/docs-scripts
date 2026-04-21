---
title: "Allocating GPU resources for Document Understanding modern projects"
visible: true
slug: "allocating-gpu-resources-for-document-understanding-modern-projects"
---

For optimal performance, allocating the appropriate number of GPU resources is vital. You allocate GPU resources through ArgoCD, which contains specific parameters that correspond to each service. By adjusting these parameters, you can control the distribution of GPU resources as per the needs of each service.

Each service listed in the capacity calculator has a corresponding ArgoCD parameter as follows:

* **OCR replicas** corresponds to the `du-ocr-saas.replicaCount` parameter.
* **Custom model training replicas** corresponds to the `du-training-ssde.replicas` parameter.
* **Custom model replicas** corresponds to the `du-aimodelhost-2404.replicas` parameter.
* **OOB model replicas** corresponds to the `du-ssde-saas.replicaCount` parameter.

Before allocating of GPU resources to each service, use the capacity calculator to determine the appropriate number of GPUs that should be allocated to each service. The output is based on your specific needs and will serve as a guide when updating the parameters in ArgoCD.

For more information, check the [UiPath Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning) page.
:::note
For Document Understanding modern projects, the minimum recommended GPU is NVIDIA T4.
:::

1. Open ArgoCD.
2. Select the **documentunderstanding** application.
3. Select **Details** to open the Details menu.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/497375)
4. Select the **Parameters** tab.
5. Select **Edit** so you can edit the parameter values.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/497383)
6. Search for the parameters that need to be edited and allocate the needed number of GPUs.

Each service listed in the capacity calculator has its corresponding ArgoCD parameter as follows:
   * **OCR replicas** corresponds to the `du-ocr-saas.replicaCount` parameter.
   * **Custom model training replicas** corresponds to the `du-training-ssde.replicas` parameter.
   * **Custom model replicas** corresponds to the `du-aimodelhost-2404.replicas` parameter.
   * **OOB model replicas** corresponds to the `du-ssde-saas.replicaCount` parameter.
7. Select **Save**.