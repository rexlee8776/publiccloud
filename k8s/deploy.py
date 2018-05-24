from os import path

import yaml
import json

from kubernetes import client, config


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.spec.template.spec.containers[0].image = "nginx:1.9.1"
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def main():
    # config.load_kube_config(config_file=consts.K8S_CONF_FILE)
    config.load_kube_config()
    extensions_v1beta1 = client.ExtensionsV1beta1Api()
    with open('yardstick_bkp.yaml', 'r') as f:
        obj = yaml.load(f)
    print json.dumps(obj, indent=2)
    deployment = obj

    create_deployment(extensions_v1beta1, deployment)
    # time.sleep(6


if __name__ == '__main__':
    main()
