#!/usr/bin/env python3
#!/usr/bin/env python3
import aws_cdk as core

from cdk_app.cdk_app_stack import HelloCdkStack

app = core.App()
HelloCdkStack(app, "CdkTestAppCICDContainer")
app.synth()

