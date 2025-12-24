#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib/core';
import { ToDoInfraStack } from '../lib/to-do-infra-stack';

const app = new cdk.App();
new ToDoInfraStack(app, "ToDoInfraStack", {
  env: { account: "492267599260", region: "us-east-1" },
});
