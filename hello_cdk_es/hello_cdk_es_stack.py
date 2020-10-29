from aws_cdk import (
    core,
    aws_elasticsearch as aes,
)


class HelloCdkEsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ctx_es = self.node.try_get_context("es")
        es_version = ctx_es["version"]

        sourceIp = self.node.try_get_context("sourceIp")
        if sourceIp == None:
            sourceIp = "127.0.0.1"

        region = core.Aws.REGION
        account_id = core.Aws.ACCOUNT_ID

        self.elastic_domain = aes.CfnDomain(
            self,
            id="HelloCdkEs",
            access_policies={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": [
                                "*"
                            ]
                        },
                        "Action": [
                            "es:*"
                        ],
                        "Resource": "*",
                        "Condition": {
                            "IpAddress": {
                                'aws:SourceIp': sourceIp,
                            },
                        },
                    },
                ]
            },
            domain_name="hello-cdk-es",
            ebs_options={
                "ebsEnabled": True,
                "volumeSize": 10,
                "volumeType": "gp2",
            },
            elasticsearch_cluster_config={
                "instanceCount": 1,
                "instanceType": "t2.small.elasticsearch",
            },
            elasticsearch_version=es_version,
            encryption_at_rest_options={
                "enabled": False,
            },
            node_to_node_encryption_options={
                "enabled": False,
            },
            snapshot_options={
                "automated_snapshot_start_hour": 0
            },
        )
