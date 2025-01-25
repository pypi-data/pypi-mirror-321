class ConfigModel:
    def __init__(self, configJSON):
        try:
            self.serverUrl = configJSON["server"]["serverUrl"]
            self.kafkaUrl = configJSON["server"]["kafkaUrl"]
            self.prjId = configJSON["key"]["prjId"]
            self.xAccessKey = configJSON["key"]["xAccessKey"]
            self.xSecretKey = configJSON["key"]["xSecretKey"]
            self.pluginCode = configJSON["plugin"]["pluginCode"]
            self.pluginVersion = configJSON["plugin"]["pluginVersion"]
            self.taskFlowCode = configJSON["task"]["taskFlowCode"]
        except KeyError as e:
            raise KeyError(f"Missing required configuration key: {e}")

        self.uniquePluginCode = self.pluginCode + "-" + self.pluginVersion.replace(".", "-")

        self.headers = {
            'Content-Type': 'application/json',
            'X-Access-Key': self.xAccessKey,
            'X-Secret-Key': self.xSecretKey
        }
