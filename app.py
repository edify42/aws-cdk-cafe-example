#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import aws_iam as iam

from cdk_workshop.coffee_listing_app import CoffeeListingAppStack


app = cdk.App()
CoffeeListingAppStack(app, "CakeListingAppStack",
    synth_commands=[
      "aws codeartifact login --tool pip --repository cdkadvancedlab --domain cdkadvancedlab",
      "npm ci",
      "pip install -r requirements.txt",
      "npx cdk synth",
    ],
    code_build_policies=[
      iam.PolicyStatement(
        effect=iam.Effect.ALLOW,
        actions=["codeartifact:*"],
        resources=["*"],
      ),
      iam.PolicyStatement(
        effect=iam.Effect.ALLOW,
        actions=["sts:*"],
        resources=["*"],
      ),
    ]
)

app.synth()
