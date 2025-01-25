from is3_python_sdk.config import config_model
from is3_python_sdk.custom.execute import Execute
from is3_python_sdk.data_query.is3_python_api import iS3PythonApi
from is3_python_sdk.domain.data_dto import DataEntity
from is3_python_sdk.is3_kafka.kafka_execute import KafkaProcessor


class iS3PythonCore:
    def __init__(self, config: config_model):
        self.config = config

    def startPlugin(self, execute: Execute):
        processor = KafkaProcessor(self.config.uniquePluginCode, self.config.headers, self.config.kafkaUrl)
        processor.processor(execute)

    def create_data_entity(self, plugin_data_config, pre_node_data):
        # 输入数据
        dataDto = DataEntity(
            preData={"data": pre_node_data},
            pluginDataConfig=plugin_data_config,
            taskInstanceId=1111,
            taskId=1,
            nodeId=1,
            customInstanceCode=1,
            logId=1,
            serverName=self.config.uniquePluginCode,
            headers=self.config.headers,
            prjId=self.config.prjId,
            tenantId=1,
            bootstrapServers=self.config.kafkaUrl,
        )
        return dataDto
