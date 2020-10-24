#!/usr/bin/env python3

from aws_cdk import core

from hello_cdk_es.hello_cdk_es_stack import HelloCdkEsStack


app = core.App()
HelloCdkEsStack(app, "hello-cdk-es")

app.synth()
